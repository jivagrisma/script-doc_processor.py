from typing import Dict, List, Optional
import nltk
import spacy
from loguru import logger
from pathlib import Path
from datetime import datetime
import re
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import lru_cache
from ..config import OPTIMIZATION_SETTINGS, PATTERNS

class TextProcessor:
    """
    Procesador de texto optimizado con procesamiento paralelo y caché.
    """
    def __init__(self):
        try:
            # Cargar spaCy con componentes optimizados
            self.nlp = spacy.load(
                OPTIMIZATION_SETTINGS["spacy_model"],
                disable=OPTIMIZATION_SETTINGS["spacy_disabled_components"]
            )
            # Agregar el componente sentencizer
            if 'sentencizer' not in self.nlp.pipe_names:
                self.nlp.add_pipe('sentencizer')
                
            self.stop_words = set(nltk.corpus.stopwords.words('english'))
            
            # Usar patrones precompilados
            self.section_pattern = PATTERNS["section_split"]
            self.sentence_pattern = PATTERNS["sentence_split"]
            self.whitespace_pattern = PATTERNS["whitespace_cleanup"]
            
            # Configuración de procesamiento
            self.chunk_size = OPTIMIZATION_SETTINGS["chunk_size"]
            self.overlap_size = OPTIMIZATION_SETTINGS["overlap_size"]
            self.batch_size = OPTIMIZATION_SETTINGS["batch_size"]
            self.max_workers = OPTIMIZATION_SETTINGS["max_workers"]
            
        except Exception as e:
            logger.error(f"Error inicializando TextProcessor: {e}")
            raise

    def process_batch(self, files: List[Dict]) -> List[Dict]:
        """
        Procesa un lote de archivos en paralelo.
        """
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self.process_file, [f["path"] for f in files]))
        return [r for r in results if r is not None]

    def process_file(self, file_path: str) -> Optional[Dict]:
        """
        Procesa un archivo individual con optimizaciones.
        """
        try:
            path = Path(file_path)
            with path.open('r', encoding='utf-8') as f:
                content = f.read()

            # Limpiar contenido
            content = self.whitespace_pattern.sub(' ', content)
            
            # Extraer metadatos básicos
            metadata = {
                "filename": path.name,
                "created_at": datetime.now().isoformat(),
                "file_size": path.stat().st_size,
                "path": str(path)
            }

            # Procesar contenido en paralelo
            processed_content = self.process_content(content)
            
            return {
                "metadata": metadata,
                **processed_content
            }

        except Exception as e:
            logger.error(f"Error procesando archivo {file_path}: {e}")
            return None

    def process_content(self, text: str) -> Dict:
        """
        Procesa el contenido con paralelización.
        """
        try:
            with ThreadPoolExecutor(max_workers=3) as executor:
                # Ejecutar tareas en paralelo
                future_sections = executor.submit(self._split_into_sections, text)
                future_doc = executor.submit(self.nlp, text)
                
                # Esperar resultados
                doc = future_doc.result()
                sections = future_sections.result()
                
                # Procesar resultados en paralelo
                future_entities = executor.submit(self._extract_entities, doc)
                future_keywords = executor.submit(self._extract_keywords, doc)
                future_summary = executor.submit(self._generate_summary, doc)
                
                return {
                    "sections": sections,
                    "entities": future_entities.result(),
                    "keywords": future_keywords.result(),
                    "summary": future_summary.result()
                }
        except Exception as e:
            logger.error(f"Error procesando contenido: {e}")
            # Devolver un resultado vacío pero válido
            return {
                "sections": [],
                "entities": {},
                "keywords": [],
                "summary": ""
            }

    @lru_cache(maxsize=1000)
    def _split_into_sections(self, text: str) -> List[Dict]:
        """
        Divide el texto en secciones con caché.
        """
        try:
            paragraphs = [p.strip() for p in self.section_pattern.split(text) if p.strip()]
            sections = []

            for i, para in enumerate(paragraphs):
                sentences = [s.strip() for s in self.sentence_pattern.split(para) if s.strip()]
                if not sentences and para.strip():
                    sentences = [para.strip()]
                
                section = {
                    "id": i,
                    "content": para,
                    "sentences": sentences,
                    "length": len(para),
                    "sentence_count": len(sentences)
                }
                sections.append(section)

            return sections
        except Exception as e:
            logger.error(f"Error dividiendo en secciones: {e}")
            return []

    def _extract_entities(self, doc) -> Dict[str, List[str]]:
        """
        Extrae entidades nombradas optimizado.
        """
        try:
            entities = {}
            for ent in doc.ents:
                if ent.label_ not in entities:
                    entities[ent.label_] = []
                if ent.text not in entities[ent.label_]:
                    entities[ent.label_].append(ent.text)
            return entities
        except Exception as e:
            logger.error(f"Error extrayendo entidades: {e}")
            return {}

    def _extract_keywords(self, doc) -> List[str]:
        """
        Extrae palabras clave optimizado.
        """
        try:
            return sorted(list({
                token.text.lower() for token in doc
                if not token.is_stop and 
                   not token.is_punct and 
                   token.is_alpha and
                   len(token.text) > 2 and
                   token.text.lower() not in self.stop_words
            }))
        except Exception as e:
            logger.error(f"Error extrayendo keywords: {e}")
            return []

    def _generate_summary(self, doc) -> str:
        """
        Genera resumen optimizado.
        """
        try:
            sentences = [sent.text.strip() for sent in doc.sents]
            return " ".join(sentences[:min(3, len(sentences))])
        except Exception as e:
            logger.error(f"Error generando resumen: {e}")
            return ""

    def create_chunks(self, sections: List[Dict]) -> List[Dict]:
        """
        Crea chunks optimizados con solapamiento inteligente.
        """
        try:
            chunks = []
            current_chunk = ""
            current_metadata = {
                "sections": [],
                "entities": set(),
                "keywords": set()
            }

            for section in sections:
                potential_size = len(current_chunk) + len(section["content"])

                if potential_size > self.chunk_size and current_chunk:
                    # Guardar chunk actual
                    chunks.append(self._create_chunk_with_metadata(current_chunk, current_metadata))
                    
                    # Iniciar nuevo chunk con solapamiento
                    overlap_text = current_chunk[-self.overlap_size:] if self.overlap_size > 0 else ""
                    current_chunk = overlap_text + section["content"]
                    current_metadata = {
                        "sections": [section["id"]],
                        "entities": set(),
                        "keywords": set()
                    }
                else:
                    if current_chunk:
                        current_chunk += "\n\n"
                    current_chunk += section["content"]
                    current_metadata["sections"].append(section["id"])

            # Agregar último chunk
            if current_chunk:
                chunks.append(self._create_chunk_with_metadata(current_chunk, current_metadata))

            return chunks
        except Exception as e:
            logger.error(f"Error creando chunks: {e}")
            return []

    def _create_chunk_with_metadata(self, content: str, metadata: Dict) -> Dict:
        """
        Crea un chunk con metadatos optimizados.
        """
        try:
            return {
                "content": content.strip(),
                "metadata": {
                    "sections": list(metadata["sections"]),
                    "entities": list(metadata["entities"]),
                    "keywords": list(metadata["keywords"]),
                    "length": len(content),
                    "chunk_hash": hash(content)  # Para identificación única
                }
            }
        except Exception as e:
            logger.error(f"Error creando chunk con metadatos: {e}")
            return {
                "content": "",
                "metadata": {
                    "sections": [],
                    "entities": [],
                    "keywords": [],
                    "length": 0,
                    "chunk_hash": 0
                }
            }
