import chromadb
from chromadb.config import Settings
from typing import List, Dict
import json

def query_documents(query: str, n_results: int = 10, doc_type: str = None) -> List[Dict]:
    """
    Consulta los documentos más relevantes basados en una pregunta
    
    Args:
        query: La pregunta o consulta
        n_results: Número de resultados a devolver
        doc_type: Filtrar por tipo de documento ('python', 'fastapi', o None para todos)
    """
    client = chromadb.PersistentClient(
        path="./chroma_db"
    )
    
    collection = client.get_collection("documents")
    
    # Preparar el filtro si se especifica un tipo de documento
    where = {"doc_type": doc_type} if doc_type else None
    
    # Expandir la consulta para mejorar los resultados
    expanded_query = f"{query} FastAPI Python version requirements compatibility dependencies installation setup"
    
    results = collection.query(
        query_texts=[expanded_query],
        n_results=n_results * 2,  # Obtener más resultados para filtrar después
        where=where,
        include=["documents", "metadatas", "distances"]
    )
    
    # Ordenar resultados por distancia (menor distancia = más relevante)
    sorted_results = []
    for doc, meta, dist in zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    ):
        relevance = 100 * (1 - dist)  # Convertir distancia a porcentaje de relevancia
        
        # Dar más peso a documentos que mencionan versiones de Python y FastAPI
        content_lower = doc.lower()
        if 'python' in content_lower and any(v in content_lower for v in ['version', 'compatible', 'requires']):
            relevance *= 1.5
        if 'fastapi' in content_lower and any(v in content_lower for v in ['version', 'compatible', 'requires']):
            relevance *= 1.5
        
        sorted_results.append({
            "document": doc,
            "metadata": meta,
            "distance": dist,
            "relevance": relevance
        })
    
    # Ordenar por relevancia y tipo de documento (priorizar FastAPI)
    sorted_results.sort(key=lambda x: (
        0 if x['metadata']['doc_type'] == 'fastapi' else 1,  # Priorizar FastAPI
        -x['relevance']  # Luego por relevancia (mayor primero)
    ))
    
    # Tomar solo los n_results más relevantes
    return sorted_results[:n_results]

def format_result(result: Dict, max_length: int = 1000) -> str:
    """
    Formatea un resultado para su presentación
    """
    metadata = result['metadata']
    content = result['document']
    
    # Preparar el encabezado con la información del documento
    header = [
        f"Archivo: {metadata.get('source', 'N/A')}",
        f"Directorio: {metadata.get('directory', 'N/A')}",
        f"Tipo: {metadata.get('doc_type', 'N/A').upper()}",
        f"Versión: {metadata.get('version', 'N/A')}",
        f"Relevancia: {result['relevance']:.2f}%",
        f"Palabras clave: {metadata.get('keywords', 'N/A')}"
    ]
    
    # Resaltar menciones de versiones de Python y FastAPI
    content = content.replace('Python', '\033[1mPython\033[0m')
    content = content.replace('FastAPI', '\033[1mFastAPI\033[0m')
    for v in range(2, 4):
        for d in range(10):
            version = f"{v}.{d}"
            content = content.replace(version, f"\033[1m{version}\033[0m")
    
    # Preparar el contenido, truncando si es necesario
    if len(content) > max_length:
        content = content[:max_length] + "..."
    
    # Combinar todo en un formato legible
    return "\n".join([
        "\n".join(header),
        "\nContenido relevante:",
        content,
        "\n" + "="*80
    ])

if __name__ == "__main__":
    try:
        print("\nSistema de Consulta de Documentación")
        print("===================================")
        print("Este sistema permite buscar en la documentación de Python y FastAPI.")
        print("Puedes hacer preguntas naturales sobre cualquier tema de la documentación.")
        print("\nEjemplos de preguntas:")
        print("- ¿Cuáles son los requisitos mínimos para instalar FastAPI?")
        print("- ¿Qué versiones de Python son compatibles?")
        print("- ¿Cómo se implementa el manejo de errores en FastAPI?")
        
        # Permitir filtrar por tipo de documento
        print("\nTipos de documentación disponibles:")
        print("1. Todos")
        print("2. Solo Python")
        print("3. Solo FastAPI")
        
        tipo = input("\nSelecciona el tipo de documentación (1-3): ").strip()
        doc_type = {
            "1": None,
            "2": "python",
            "3": "fastapi"
        }.get(tipo)
        
        query = input("\nIngresa tu pregunta: ")
        results = query_documents(query, doc_type=doc_type)
        
        if not results:
            print("\nNo se encontraron resultados para tu consulta.")
            print("Intenta reformular tu pregunta o usar términos diferentes.")
        else:
            print("\nResultados encontrados:")
            for i, result in enumerate(results, 1):
                print(f"\n--- Resultado {i} ---")
                print(format_result(result))
            
            print("\nNota: Los resultados se muestran ordenados por relevancia.")
            print("Un porcentaje de relevancia más alto indica una mejor coincidencia con tu pregunta.")
            print("Los documentos de FastAPI tienen prioridad cuando son relevantes para la consulta.")
            
    except ValueError as e:
        print(f"\nError: {str(e)}")
        print("Asegúrate de ejecutar primero doc_processor.py para procesar los documentos.")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")
        print("Detalles:", str(e.__dict__))
