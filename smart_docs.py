import os
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional, Any, Tuple
import json
import re
from dataclasses import dataclass
from tqdm import tqdm
import argparse
import time

@dataclass
class DocumentChunk:
    content: str
    metadata: Dict[str, Any]
    chunk_id: int
    total_chunks: int

class SmartDocumentManager:
    def __init__(self, persist_directory: str = "./chroma_db", reset: bool = False):
        """
        Inicializa el gestor de documentos con ChromaDB
        """
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        
        settings = Settings(
            anonymized_telemetry=False,
            allow_reset=True,
            is_persistent=True
        )
        
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=settings
        )
        
        # Configuración de chunks
        self.max_chunk_size = 4000  # Caracteres por chunk
        self.overlap = 200  # Solapamiento entre chunks para mantener contexto
        
        # Obtener o crear colección
        self.collection = self.get_or_create_collection(reset)

    def get_or_create_collection(self, reset: bool = False):
        """
        Obtiene la colección existente o crea una nueva
        """
        collection_name = "smart_docs"
        
        if reset:
            try:
                self.client.delete_collection(collection_name)
                time.sleep(1)  # Dar tiempo para que se complete la eliminación
            except Exception as e:
                print(f"Error al eliminar colección: {str(e)}")
        
        try:
            return self.client.get_collection(collection_name)
        except:
            try:
                return self.client.create_collection(
                    name=collection_name,
                    metadata={"hnsw:space": "cosine"}
                )
            except Exception as e:
                print(f"Error al crear colección: {str(e)}")
                # Si todo falla, crear una colección con nombre único
                return self.client.create_collection(
                    name=f"{collection_name}_{os.urandom(4).hex()}",
                    metadata={"hnsw:space": "cosine"}
                )

    def preprocess_content(self, content: str) -> str:
        """
        Preprocesa el contenido del documento
        """
        # Eliminar múltiples espacios en blanco y saltos de línea
        content = re.sub(r'\s+', ' ', content)
        return content.strip()

    def chunk_document(self, content: str, metadata: Dict) -> List[DocumentChunk]:
        """
        Divide un documento en chunks más pequeños con solapamiento
        """
        content = self.preprocess_content(content)
        chunks = []
        
        # Dividir en chunks con solapamiento
        start = 0
        chunk_id = 0
        while start < len(content):
            # Calcular el final del chunk actual
            end = start + self.max_chunk_size
            
            # Si no es el último chunk, ajustar para no cortar palabras
            if end < len(content):
                # Buscar el último espacio dentro del solapamiento
                last_space = content.rfind(' ', end - self.overlap, end)
                if last_space != -1:
                    end = last_space
            
            # Crear el chunk
            chunk_content = content[start:end].strip()
            if chunk_content:
                chunks.append(DocumentChunk(
                    content=chunk_content,
                    metadata={
                        **metadata,
                        "chunk_id": chunk_id,
                        "start_char": start,
                        "end_char": end
                    },
                    chunk_id=chunk_id,
                    total_chunks=0  # Se actualizará después
                ))
            
            # Mover el inicio al siguiente chunk, considerando el solapamiento
            start = end - self.overlap if end < len(content) else len(content)
            chunk_id += 1
        
        # Actualizar el total de chunks en cada chunk
        total_chunks = len(chunks)
        for chunk in chunks:
            chunk.total_chunks = total_chunks
            chunk.metadata["total_chunks"] = total_chunks
        
        return chunks

    def process_file(self, file_path: str) -> List[DocumentChunk]:
        """
        Procesa un archivo y lo divide en chunks
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Extraer información de versión del path
                path_parts = file_path.split(os.sep)
                version = "latest"
                for part in path_parts:
                    if part.startswith('v') and any(c.isdigit() for c in part):
                        version = part
                    elif "latest" in part.lower():
                        version = "latest"
                
                # Metadata enriquecida
                metadata = {
                    "source": os.path.basename(file_path),
                    "directory": os.path.basename(os.path.dirname(file_path)),
                    "file_path": file_path,
                    "version": version,
                    "processed_date": time.strftime("%Y-%m-%d"),
                    "is_latest": "latest" in version.lower(),
                }
                
                # Dividir en chunks
                return self.chunk_document(content, metadata)
                
        except Exception as e:
            print(f"Error procesando {file_path}: {str(e)}")
            return []

    def process_directory(self, directory_path: str, recursive: bool = True) -> None:
        """
        Procesa todos los archivos .txt en un directorio usando batch processing
        """
        def get_files(dir_path):
            if recursive:
                for root, _, files in os.walk(dir_path):
                    for file in files:
                        if file.endswith('.txt'):
                            yield os.path.join(root, file)
            else:
                for file in os.listdir(dir_path):
                    if file.endswith('.txt'):
                        yield os.path.join(dir_path, file)
        
        files = list(get_files(directory_path))
        total_chunks = 0
        batch_size = 10  # Tamaño del batch muy reducido para evitar problemas de memoria
        
        # Acumuladores para batch processing
        all_documents = []
        all_metadatas = []
        all_ids = []
        
        with tqdm(total=len(files), desc="Procesando archivos") as pbar:
            for file_path in files:
                try:
                    chunks = self.process_file(file_path)
                    
                    if chunks:
                        # Preparar datos para el batch
                        documents = [chunk.content for chunk in chunks]
                        metadatas = [chunk.metadata for chunk in chunks]
                        file_name = os.path.basename(file_path)
                        ids = [f"doc_{os.path.splitext(file_name)[0]}_chunk_{chunk.chunk_id}" for chunk in chunks]
                        
                        # Acumular resultados
                        all_documents.extend(documents)
                        all_metadatas.extend(metadatas)
                        all_ids.extend(ids)
                        
                        # Si alcanzamos el tamaño del batch, insertar en ChromaDB
                        if len(all_documents) >= batch_size:
                            try:
                                # Añadir documentos en grupos más pequeños
                                for i in range(0, len(all_documents), 5):
                                    end = min(i + 5, len(all_documents))
                                    self.collection.add(
                                        documents=all_documents[i:end],
                                        metadatas=all_metadatas[i:end],
                                        ids=all_ids[i:end]
                                    )
                                    total_chunks += end - i
                                    time.sleep(0.1)  # Pequeña pausa para evitar sobrecarga
                                    
                                # Limpiar acumuladores
                                all_documents = []
                                all_metadatas = []
                                all_ids = []
                                
                            except Exception as e:
                                print(f"Error al añadir batch a ChromaDB: {str(e)}")
                    
                    pbar.update(1)
                    
                except Exception as e:
                    print(f"Error procesando {file_path}: {str(e)}")
                    pbar.update(1)
        
        # Insertar el último batch si quedan documentos
        if all_documents:
            try:
                # Añadir documentos en grupos más pequeños
                for i in range(0, len(all_documents), 5):
                    end = min(i + 5, len(all_documents))
                    self.collection.add(
                        documents=all_documents[i:end],
                        metadatas=all_metadatas[i:end],
                        ids=all_ids[i:end]
                    )
                    total_chunks += end - i
                    time.sleep(0.1)  # Pequeña pausa para evitar sobrecarga
            except Exception as e:
                print(f"Error al añadir último batch a ChromaDB: {str(e)}")
        
        print(f"\nTotal de chunks procesados: {total_chunks}")

    def query_documents(self, 
                       query: str, 
                       n_results: int = 5, 
                       max_chars: int = 8000000) -> Dict:
        """
        Consulta los documentos más relevantes
        """
        try:
            # Realizar la consulta
            results = self.collection.query(
                query_texts=[query],
                n_results=n_results * 2,  # Obtener más resultados para filtrar después
                include=["documents", "metadatas", "distances"]
            )
            
            if not results['documents'][0]:
                return {"error": "No se encontraron resultados"}
            
            # Procesar resultados
            processed_results = []
            total_chars = 0
            
            for doc, meta, dist in zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
            ):
                # Verificar límite de caracteres
                if total_chars + len(doc) > max_chars:
                    break
                
                relevance = (1 - dist) * 100
                processed_results.append({
                    "content": doc,
                    "metadata": meta,
                    "relevance": relevance
                })
                total_chars += len(doc)
            
            # Ordenar por relevancia
            processed_results.sort(key=lambda x: x['relevance'], reverse=True)
            
            return {
                "results": processed_results,
                "stats": {
                    "total_chars": total_chars,
                    "max_chars": max_chars,
                    "results_count": len(processed_results),
                    "truncated": total_chars >= max_chars
                }
            }
            
        except Exception as e:
            return {"error": f"Error en la consulta: {str(e)}"}

def process_path(manager: SmartDocumentManager, path: str, recursive: bool = True) -> None:
    """
    Procesa un archivo o directorio
    """
    if os.path.isfile(path):
        if path.endswith('.txt'):
            print(f"\nProcesando archivo: {path}")
            chunks = manager.process_file(path)
            if chunks:
                documents = [chunk.content for chunk in chunks]
                metadatas = [chunk.metadata for chunk in chunks]
                ids = [f"doc_{os.path.splitext(os.path.basename(path))[0]}_chunk_{chunk.chunk_id}" for chunk in chunks]
                
                # Añadir documentos en grupos pequeños
                total_chunks = 0
                for i in range(0, len(documents), 5):
                    end = min(i + 5, len(documents))
                    try:
                        manager.collection.add(
                            documents=documents[i:end],
                            metadatas=metadatas[i:end],
                            ids=ids[i:end]
                        )
                        total_chunks += end - i
                        time.sleep(0.1)  # Pequeña pausa para evitar sobrecarga
                    except Exception as e:
                        print(f"Error al añadir chunks a ChromaDB: {str(e)}")
                
                print(f"\nTotal de chunks procesados: {total_chunks}")
        else:
            print(f"\nIgnorando archivo no txt: {path}")
    elif os.path.isdir(path):
        print(f"\nProcesando directorio: {path}")
        manager.process_directory(path, recursive)
        print("\nProcesamiento completado!")
    else:
        print(f"\nNo se encontró el archivo o directorio: {path}")

def main():
    parser = argparse.ArgumentParser(description='Procesa documentos de texto y permite consultas semánticas')
    parser.add_argument('--path', type=str, help='Archivo o directorio a procesar', required=True)
    parser.add_argument('--recursive', action='store_true', help='Procesar subdirectorios recursivamente')
    parser.add_argument('--query', type=str, help='Consulta a realizar (opcional)')
    parser.add_argument('--reset', action='store_true', help='Resetear la base de datos')
    args = parser.parse_args()

    manager = SmartDocumentManager(reset=args.reset)
    
    if os.path.exists(args.path):
        process_path(manager, args.path, args.recursive)
        
        if args.query:
            print(f"\nRealizando consulta: {args.query}")
            results = manager.query_documents(args.query)
            
            if "error" in results:
                print(f"\nError: {results['error']}")
            else:
                print("\nResultados encontrados:")
                print("-" * 80)
                
                for r in results["results"]:
                    print(f"\nRelevancia: {r['relevance']:.2f}%")
                    print(f"Fuente: {r['metadata']['source']} (versión: {r['metadata']['version']})")
                    print(f"Fecha de procesamiento: {r['metadata']['processed_date']}")
                    print(f"Contenido:\n{r['content']}\n")
                    print("-" * 80)
                
                print(f"\nEstadísticas:")
                print(f"Total de caracteres: {results['stats']['total_chars']}")
                print(f"Resultados encontrados: {results['stats']['results_count']}")
    else:
        print(f"\nNo se encontró el directorio: {args.path}")

if __name__ == "__main__":
    main()
