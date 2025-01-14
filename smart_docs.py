#!/usr/bin/env python3
from typing import Dict, List, Optional
import argparse
from pathlib import Path
from loguru import logger
import sys
from concurrent.futures import ThreadPoolExecutor
import time

from src.processors.text_processor import TextProcessor
from src.storage.vector_store import VectorStore
from src.utils.file_handler import FileHandler
from src.utils.initialize_nltk import download_nltk_resources
from src.config import OPTIMIZATION_SETTINGS

class SmartDocs:
    """
    Procesador inteligente de documentación con optimizaciones de rendimiento.
    """
    def __init__(self):
        self.setup_logging()
        self.initialize_resources()
        self.file_handler = FileHandler()
        self.text_processor = TextProcessor()
        self.vector_store = VectorStore()
        self.batch_size = OPTIMIZATION_SETTINGS["batch_size"]

    def setup_logging(self):
        """
        Configura el sistema de logging.
        """
        logger.remove()
        logger.add(
            sys.stderr,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            level="INFO"
        )

    def initialize_resources(self):
        """
        Inicializa recursos necesarios.
        """
        try:
            logger.info("Inicializando recursos NLTK...")
            download_nltk_resources()
        except Exception as e:
            logger.error(f"Error inicializando recursos: {e}")
            raise

    def process_directory(self, directory: str, reset: bool = False) -> None:
        """
        Procesa todos los archivos en un directorio con optimizaciones.
        """
        try:
            start_time = time.time()
            
            # Crear/obtener colección
            collection = self.vector_store.create_or_get_collection(reset=reset)
            
            # Escanear directorio
            files = self.file_handler.scan_directory(directory)
            total_files = len(files)
            logger.info(f"Encontrados {total_files} archivos para procesar")

            # Procesar archivos en lotes
            for i in range(0, total_files, self.batch_size):
                batch = files[i:i + self.batch_size]
                batch_start = time.time()
                
                logger.info(f"Procesando lote {i//self.batch_size + 1}/{(total_files + self.batch_size - 1)//self.batch_size}")
                
                # Procesar lote
                processed_files = self.text_processor.process_batch(batch)
                
                # Almacenar resultados
                for processed_file in processed_files:
                    if processed_file:
                        chunks = self.text_processor.create_chunks(processed_file["sections"])
                        self.vector_store.add_documents(
                            collection=collection,
                            chunks=chunks,
                            source_metadata=processed_file["metadata"]
                        )
                
                batch_time = time.time() - batch_start
                logger.info(f"Lote procesado en {batch_time:.2f} segundos")

            # Mostrar estadísticas
            stats = self.vector_store.get_collection_stats(collection)
            total_time = time.time() - start_time
            
            logger.info(f"Procesamiento completado en {total_time:.2f} segundos!")
            logger.info(f"Estadísticas finales: {stats}")

        except Exception as e:
            logger.error(f"Error en el procesamiento: {e}")
            raise

    def query(self, query_text: str, n_results: int = 5) -> Dict:
        """
        Realiza una consulta optimizada sobre la documentación procesada.
        """
        try:
            start_time = time.time()
            collection = self.vector_store.create_or_get_collection()
            
            # Realizar consulta
            results = self.vector_store.query_documents(
                collection=collection,
                query_text=query_text,
                n_results=n_results
            )
            
            # Formatear resultados para Cline
            formatted_results = self._format_results_for_cline(results)
            
            query_time = time.time() - start_time
            logger.info(f"Consulta completada en {query_time:.2f} segundos")
            
            return formatted_results

        except Exception as e:
            logger.error(f"Error en la consulta: {e}")
            raise

    def _format_results_for_cline(self, results: Dict) -> Dict:
        """
        Formatea los resultados para ser utilizados por Cline.
        """
        formatted_results = {
            "query": results["query"],
            "results": []
        }

        for result in results["results"]:
            # Formatear cada resultado individual
            formatted_result = {
                "content": result["content"],
                "relevance": f"{result['relevance_score']*100:.2f}%",
                "source": result["metadata"].get("filename", "Unknown"),
                "context": {
                    "section": result["metadata"].get("sections", []),
                    "keywords": result["metadata"].get("keywords", []),
                    "summary": result["metadata"].get("summary", "")
                }
            }
            formatted_results["results"].append(formatted_result)

        return formatted_results

def main():
    parser = argparse.ArgumentParser(description="Procesador inteligente de documentación")
    parser.add_argument("--path", help="Ruta al directorio de documentos")
    parser.add_argument("--query", help="Consulta a realizar")
    parser.add_argument("--reset", action="store_true", help="Resetear la base de datos")
    parser.add_argument("--results", type=int, default=5, help="Número de resultados a mostrar")
    
    args = parser.parse_args()
    processor = SmartDocs()

    try:
        if args.path:
            processor.process_directory(args.path, args.reset)
        
        if args.query:
            results = processor.query(args.query, args.results)
            print("\nResultados encontrados:")
            print("-" * 80)
            
            for result in results["results"]:
                print(f"\nRelevancia: {result['relevance']}")
                print(f"Fuente: {result['source']}")
                if result['context']['summary']:
                    print(f"Resumen: {result['context']['summary']}")
                print(f"Contenido:\n{result['content']}")
                print("-" * 80)

    except Exception as e:
        logger.error(f"Error en la ejecución: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
