from smart_docs import SmartDocumentManager

def main():
    manager = SmartDocumentManager()
    
    # Realizar la consulta
    query = "¿Cuáles son las características principales de FastAPI?"
    results = manager.query_documents(query, n_results=3)
    
    # Mostrar resultados
    print("\nResultados de la consulta:")
    print("-" * 80)
    
    if 'results' in results:
        for r in results['results']:
            print(f"\nRelevancia: {r['relevance']:.2f}%")
            print(f"Fuente: {r['metadata']['source']}")
            print(f"Contenido:\n{r['content']}\n")
            print("-" * 80)
        
        print(f"\nEstadísticas:")
        print(f"Total de caracteres: {results['stats']['total_chars']}")
        print(f"Resultados encontrados: {results['stats']['results_count']}")
    else:
        print("No se encontraron resultados")

if __name__ == "__main__":
    main()
