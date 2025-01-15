import os
import chromadb
from chromadb.config import Settings
from typing import List, Dict
import json
import re

class DocumentProcessor:
    def __init__(self, persist_directory: str = "./chroma_db"):
        """
        Inicializa el procesador de documentos con ChromaDB
        """
        # Asegurarse de que el directorio de persistencia existe
        os.makedirs(persist_directory, exist_ok=True)
        
        # Eliminar la colección existente si existe
        self.client = chromadb.PersistentClient(
            path=persist_directory
        )
        try:
            self.client.delete_collection("documents")
        except:
            pass
        
        # Crear una nueva colección
        self.collection = self.client.create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )

    def preprocess_content(self, content: str) -> str:
        """
        Preprocesa el contenido del documento para mejorar la calidad de los embeddings
        """
        # Eliminar múltiples espacios en blanco y saltos de línea
        content = re.sub(r'\s+', ' ', content)
        
        # Eliminar caracteres especiales manteniendo la estructura
        content = re.sub(r'[^\w\s\.\,\;\:\-\(\)\[\]\{\}\'\"\`\/]', '', content)
        
        # Normalizar espacios alrededor de puntuación
        content = re.sub(r'\s*([,\.\;\:\-])\s*', r'\1 ', content)
        
        return content.strip()

    def extract_metadata(self, file_path: str, content: str) -> Dict:
        """
        Extrae metadatos adicionales del contenido y el nombre del archivo
        """
        file_name = os.path.basename(file_path)
        directory = os.path.basename(os.path.dirname(file_path))
        
        # Detectar el tipo de documento basado en el contenido y el directorio
        content_lower = content.lower()
        directory_lower = directory.lower()
        
        # Determinar el tipo de documento
        doc_type = "unknown"
        if "fastapi" in content_lower or "fastapi" in directory_lower:
            doc_type = "fastapi"
        elif "python" in content_lower or "python" in directory_lower:
            doc_type = "python"
        
        # Extraer versión si está presente en el contenido
        version = "unknown"
        version_match = re.search(r'Python\s+(\d+\.\d+(?:\.\d+)?)', content)
        if version_match:
            version = version_match.group(1)
        
        # Extraer palabras clave relevantes
        keywords = set()
        if doc_type == "fastapi":
            keywords.update([
                "web", "api", "rest", "async", "fastapi", "framework",
                "http", "json", "openapi", "swagger", "pydantic"
            ])
        if doc_type == "python":
            keywords.update([
                "programming", "language", "runtime", "python",
                "interpreter", "package", "module"
            ])
        
        # Convertir keywords a string
        keywords_str = ", ".join(sorted(keywords)) if keywords else ""
        
        return {
            "source": file_name,
            "directory": directory,
            "doc_type": doc_type,
            "version": version,
            "keywords": keywords_str,
            "file_path": file_path
        }

    def process_directory(self, directory_path: str, batch_size: int = 5) -> None:
        """
        Procesa todos los archivos .txt y .md en un directorio y los almacena en ChromaDB
        """
        files = sorted([
            f for f in os.listdir(directory_path) 
            if f.endswith('.txt') or f.endswith('.md')
        ])
        total_processed = 0
        
        for i in range(0, len(files), batch_size):
            batch_files = files[i:i + batch_size]
            documents = []
            metadatas = []
            ids = []
            
            for file_name in batch_files:
                file_path = os.path.join(directory_path, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        # Preprocesar contenido
                        processed_content = self.preprocess_content(content)
                        doc_id = f"doc_{os.path.splitext(file_name)[0]}"
                        
                        # Extraer metadatos
                        metadata = self.extract_metadata(file_path, content)
                        
                        documents.append(processed_content)
                        metadatas.append(metadata)
                        ids.append(doc_id)
                        
                except Exception as e:
                    print(f"Error procesando {file_path}: {str(e)}")
            
            if documents:
                try:
                    self.collection.add(
                        documents=documents,
                        metadatas=metadatas,
                        ids=ids
                    )
                    total_processed += len(documents)
                    print(f"Procesado lote de {len(documents)} documentos")
                except Exception as e:
                    print(f"Error al añadir documentos a ChromaDB: {str(e)}")
        
        print(f"Total documentos procesados en {directory_path}: {total_processed}")

    def get_collection_stats(self) -> Dict:
        """
        Obtiene estadísticas de la colección
        """
        total_docs = self.collection.count()
        doc_types = {}
        versions = {}
        keywords = set()
        
        # Contar documentos por tipo y versión
        results = self.collection.get()
        for metadata in results['metadatas']:
            doc_type = metadata.get('doc_type', 'unknown')
            version = metadata.get('version', 'unknown')
            kw = metadata.get('keywords', '').split(', ')
            
            doc_types[doc_type] = doc_types.get(doc_type, 0) + 1
            versions[version] = versions.get(version, 0) + 1
            keywords.update(k for k in kw if k)
        
        return {
            "total_documents": total_docs,
            "collection_name": self.collection.name,
            "document_types": doc_types,
            "versions": versions,
            "keywords": sorted(list(keywords))
        }

if __name__ == "__main__":
    import argparse
    
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Procesa documentos y los almacena en ChromaDB')
    parser.add_argument('--path', type=str, help='Ruta al directorio que contiene los documentos a procesar')
    parser.add_argument('--batch-size', type=int, default=5, help='Tamaño del lote para procesamiento (default: 5)')
    args = parser.parse_args()

    if not args.path:
        print("Error: Debe especificar una ruta con --path")
        exit(1)

    if not os.path.exists(args.path):
        print(f"Error: La ruta {args.path} no existe")
        exit(1)

    # Inicializar el procesador
    processor = DocumentProcessor()
    total_docs = 0
    
    # Si la ruta es un directorio, procesar sus subdirectorios
    if os.path.isdir(args.path):
        print(f"\nProcesando directorio principal: {args.path}")
        # Primero procesar archivos en el directorio raíz
        processor.process_directory(args.path, args.batch_size)
        
        # Luego procesar subdirectorios
        for subdir in os.listdir(args.path):
            subdir_path = os.path.join(args.path, subdir)
            if os.path.isdir(subdir_path):
                print(f"\nProcesando subdirectorio: {subdir}")
                processor.process_directory(subdir_path, args.batch_size)
    
    # Mostrar estadísticas
    stats = processor.get_collection_stats()
    print("\nEstadísticas de la colección:")
    print(json.dumps(stats, indent=2))
