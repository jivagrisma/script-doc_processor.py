# Smart Documents Processor

Este script permite procesar documentos de texto que exceden el límite de tokens/bytes de Claude (9,854,598 > 9,000,000) para que puedan ser utilizados como contexto actualizado por el modelo. Esto significa que el modelo podrá utilizar información más reciente que la incluida en su entrenamiento original.

## Uso con Documentación Actualizada

El sistema está diseñado específicamente para permitir que el modelo use documentación nueva/actualizada como contexto para sus respuestas:

1. **Documentación Nueva**: Cuando tienes documentación más reciente que el entrenamiento del modelo (por ejemplo, documentación de FastAPI 2025), puedes:
   - Convertir la documentación a archivos .txt
   - Procesarla con este script
   - El modelo usará esta información actualizada en sus respuestas

2. **Versionamiento**: 
   - Puedes mantener diferentes versiones de documentación en diferentes directorios
   - Usar el flag --reset para actualizar la base de datos cuando hay nueva documentación
   - Los metadatos incluyen información sobre la fuente y versión

3. **Contexto Dinámico**:
   - El modelo combinará su conocimiento base con la información nueva
   - Priorizará la información de los documentos procesados sobre su entrenamiento original
   - Puede referenciar específicamente las partes relevantes de la nueva documentación

## Características

- Divide documentos grandes en chunks más pequeños (4000 caracteres)
- Usa solapamiento (200 caracteres) para mantener el contexto entre chunks
- Almacena los chunks en ChromaDB (una base de datos vectorial)
- Permite consultas inteligentes que devuelven solo los chunks más relevantes
- Procesa documentos de forma recursiva en directorios
- Soporta procesamiento por lotes para mejor rendimiento
- Maneja errores y reintentos automáticamente

## Instalación

```bash
# Instalar dependencias
pip install chromadb numpy pandas
```

## Uso

### Procesar documentos

```bash
# Procesar un archivo
python smart_docs.py --path ruta/al/archivo.txt

# Procesar un directorio recursivamente
python smart_docs.py --path ruta/al/directorio --recursive

# Resetear la base de datos antes de procesar
python smart_docs.py --path ruta/al/directorio --reset
```

### Realizar consultas

```bash
# Procesar y consultar en un solo paso
python smart_docs.py --path ruta/al/directorio --query "¿Cuál es la pregunta?"

# Solo consultar (usando documentos ya procesados)
python smart_docs.py --query "¿Cuál es la pregunta?"
```

## Ejemplos

1. Procesar documentación de FastAPI:
```bash
python smart_docs.py --path doc_py/fastapi-fastapi_p36 --recursive
```

2. Consultar sobre características de FastAPI:
```bash
python smart_docs.py --query "¿Cuáles son las características principales de FastAPI?"
```

## Estructura de Archivos

```
.
├── smart_docs.py     # Script principal
├── chroma_db/        # Base de datos vectorial (creada automáticamente)
└── doc_py/          # Directorio de ejemplo con documentos
```

## Cómo Funciona

1. **Procesamiento de Documentos**:
   - Lee archivos de texto
   - Divide en chunks de 4000 caracteres
   - Mantiene 200 caracteres de solapamiento entre chunks
   - Almacena en ChromaDB con metadatos

2. **Consultas**:
   - Vectoriza la consulta
   - Encuentra chunks relevantes
   - Ordena por relevancia
   - Devuelve resultados con metadatos

3. **Batch Processing**:
   - Procesa documentos en lotes
   - Maneja errores automáticamente
   - Reintentos configurables

## Limitaciones y Consideraciones

- Solo procesa archivos de texto (.txt)
- Requiere suficiente memoria RAM para vectorización
- La calidad de las respuestas depende de la consulta
- El modelo combina la información nueva con su conocimiento base
- Es importante mantener la documentación actualizada y bien estructurada
- Se recomienda organizar la documentación por versiones/temas

## Mejores Prácticas

1. **Organización de Documentación**:
   ```
   doc_py/
   ├── framework_v1/          # Versión 1 de la documentación
   │   ├── intro.txt
   │   └── api.txt
   ├── framework_v2/          # Versión 2 de la documentación
   │   ├── intro.txt
   │   └── api.txt
   └── latest/               # Última versión
       ├── intro.txt
       └── api.txt
   ```

2. **Actualización de Contexto**:
   ```bash
   # Limpiar base de datos y procesar nueva documentación
   python smart_docs.py --path doc_py/latest --reset --recursive
   ```

3. **Consultas Específicas**:
   ```bash
   # Especificar que queremos información de la última versión
   python smart_docs.py --query "En la última versión, ¿cómo se implementa X?"
   ```

4. **Mantenimiento**:
   - Actualizar la documentación regularmente
   - Mantener un formato consistente
   - Documentar cambios importantes
   - Verificar la calidad de las respuestas

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crea un Pull Request
