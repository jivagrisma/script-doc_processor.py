from typing import Dict, List, Optional, Any
import chromadb
from chromadb.config import Settings
from loguru import logger
from datetime import datetime, timedelta
import json
from collections import OrderedDict
from ..config import OPTIMIZATION_SETTINGS

class QueryCache:
    """
    Caché LRU (Least Recently Used) para consultas.
    """
    def __init__(self, max_size: int = 1000, ttl: int = 300):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.ttl = ttl

    def get(self, key: str) -> Optional[Dict]:
        if key in self.cache:
            value, timestamp = self.cache[key]
            if datetime.now() - timestamp < timedelta(seconds=self.ttl):
                # Mover el item al final (más recientemente usado)
                self.cache.move_to_end(key)
                return value
            else:
                # Expirado
                del self.cache[key]
        return None

    def set(self, key: str, value: Dict):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = (value, datetime.now())
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)

class VectorStore:
    """
    Gestiona el almacenamiento y recuperación de documentos usando ChromaDB con optimizaciones.
    """
    def __init__(self, persist_directory: str = "chroma_db"):
        try:
            # Configurar ChromaDB con optimizaciones
            self.client = chromadb.PersistentClient(
                path=persist_directory,
                settings=Settings(**OPTIMIZATION_SETTINGS["chroma_settings"])
            )
            
            # Inicializar caché
            self.query_cache = QueryCache(
                max_size=OPTIMIZATION_SETTINGS["max_cache_size"],
                ttl=OPTIMIZATION_SETTINGS["cache_ttl"]
            )
            
            logger.info(f"ChromaDB inicializado en {persist_directory}")
        except Exception as e:
            logger.error(f"Error inicializando ChromaDB: {e}")
            raise

    def create_or_get_collection(self, name: str = "docs", reset: bool = False) -> chromadb.Collection:
        """
        Crea o recupera una colección de documentos con optimizaciones.
        """
        try:
            if reset:
                try:
                    self.client.delete_collection(name)
                    logger.info(f"Colección {name} eliminada")
                except:
                    pass

            collection = self.client.get_or_create_collection(
                name=name,
                metadata={"hnsw:space": "cosine"}  # Optimización para búsqueda de similitud
            )
            
            logger.info(f"Colección {name} lista para usar")
            return collection

        except Exception as e:
            logger.error(f"Error con la colección {name}: {e}")
            raise

    def _prepare_metadata(self, metadata: Dict) -> Dict:
        """
        Prepara los metadatos para ChromaDB asegurando tipos de datos compatibles.
        """
        processed = {}
        for key, value in metadata.items():
            if isinstance(value, (str, int, float, bool)):
                processed[key] = value
            elif isinstance(value, (list, set)):
                processed[key] = json.dumps(list(value))
            elif isinstance(value, dict):
                processed[key] = json.dumps(value)
            else:
                processed[key] = str(value)
        return processed

    def add_documents(self, 
                     collection: chromadb.Collection,
                     chunks: List[Dict],
                     source_metadata: Dict) -> None:
        """
        Agrega documentos procesados a la colección con optimizaciones.
        """
        try:
            # Preparar datos en lotes
            batch_size = OPTIMIZATION_SETTINGS["batch_size"]
            source_metadata = self._prepare_metadata(source_metadata)

            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]
                
                documents = []
                metadatas = []
                ids = []

                for j, chunk in enumerate(batch):
                    chunk_id = i + j
                    # Procesar metadatos del chunk
                    chunk_metadata = self._prepare_metadata(chunk["metadata"])
                    
                    # Combinar metadatos
                    combined_metadata = {
                        **source_metadata,
                        **chunk_metadata,
                        "chunk_id": chunk_id,
                        "batch_id": i // batch_size,
                        "timestamp": datetime.now().isoformat()
                    }

                    documents.append(chunk["content"])
                    metadatas.append(combined_metadata)
                    ids.append(f"{source_metadata['filename']}_{chunk_id}")

                # Agregar lote a ChromaDB
                collection.add(
                    documents=documents,
                    metadatas=metadatas,
                    ids=ids
                )
            
            logger.info(f"Agregados {len(chunks)} chunks a la colección")

        except Exception as e:
            logger.error(f"Error agregando documentos: {e}")
            raise

    def query_documents(self, 
                       collection: chromadb.Collection,
                       query_text: str,
                       n_results: int = 5,
                       metadata_filter: Optional[Dict] = None) -> Dict:
        """
        Realiza una consulta optimizada en la colección de documentos.
        """
        try:
            # Verificar caché
            cache_key = f"{query_text}:{n_results}:{json.dumps(metadata_filter or {})}"
            cached_result = self.query_cache.get(cache_key)
            if cached_result:
                logger.info("Resultados recuperados de caché")
                return cached_result

            # Realizar búsqueda
            results = collection.query(
                query_texts=[query_text],
                n_results=n_results,
                where=metadata_filter,
                include=["documents", "metadatas", "distances"]
            )

            # Procesar resultados
            processed_results = []
            for i in range(len(results['documents'][0])):
                # Procesar metadatos
                metadata = {}
                for key, value in results['metadatas'][0][i].items():
                    try:
                        if isinstance(value, str) and (value.startswith('[') or value.startswith('{')):
                            metadata[key] = json.loads(value)
                        else:
                            metadata[key] = value
                    except:
                        metadata[key] = value

                processed_results.append({
                    "content": results['documents'][0][i],
                    "metadata": metadata,
                    "relevance_score": 1 - results['distances'][0][i]
                })

            # Ordenar por relevancia
            processed_results.sort(key=lambda x: x['relevance_score'], reverse=True)

            result = {
                "query": query_text,
                "results": processed_results,
                "total_results": len(processed_results)
            }

            # Guardar en caché
            self.query_cache.set(cache_key, result)

            return result

        except Exception as e:
            logger.error(f"Error en la consulta: {e}")
            raise

    def get_collection_stats(self, collection: chromadb.Collection) -> Dict:
        """
        Obtiene estadísticas de la colección.
        """
        try:
            count = collection.count()
            return {
                "total_documents": count,
                "collection_name": collection.name,
                "last_updated": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error obteniendo estadísticas: {e}")
            raise
