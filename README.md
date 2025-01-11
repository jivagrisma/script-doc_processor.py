# Script Doc Processor

Solución para procesar y consultar grandes volúmenes de documentos de texto utilizando ChromaDB como base de datos vectorial. Diseñado específicamente para trabajar con Claude Sonnet 3.5v2 a través de la extensión Cline en VS Code.

## Características

- Procesamiento de documentos de texto en chunks manejables
- Almacenamiento vectorial usando ChromaDB
- Consultas semánticas sobre la documentación procesada
- Integración con Cline para desarrollo asistido

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/jivagrisma/script-doc_processor.py.git
cd script-doc_processor.py
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso con Cline

### 1. Procesar Documentación

Primero, procesa los documentos que servirán como contexto:

```bash
python3 smart_docs.py --path ruta/a/documentos --reset
```

Ejemplo:
```bash
python3 smart_docs.py --path doc_py/fastapi-fastapi_p36 --reset
```

Este comando:
- Procesa todos los archivos en el directorio especificado
- Divide los documentos en chunks manejables
- Almacena los chunks en ChromaDB
- Prepara el contenido para consultas

### 2. Realizar Consultas

Para obtener información estructurada, usa el siguiente formato de consulta:

```bash
python3 smart_docs.py --query "Basándote en la documentación de [tecnología], muestra paso a paso cómo [objetivo específico], incluyendo:
1) [primer aspecto]
2) [segundo aspecto]
3) [tercer aspecto]"
```

Ejemplo de consulta para desarrollo:
```bash
python3 smart_docs.py --query "Basándote en la documentación de FastAPI, muestra paso a paso cómo crear una API con autenticación, incluyendo:
1) Importaciones y configuración inicial
2) Definición de modelos y esquemas
3) Implementación de rutas y autenticación"
```

### 3. Resultados

El script devolverá:
- Fragmentos relevantes de la documentación
- Porcentaje de relevancia para cada fragmento
- Fuente exacta de la información
- Fecha de procesamiento del contenido

### 4. Uso con Cline

1. Procesa la documentación relevante para tu proyecto
2. Realiza una consulta específica sobre lo que necesitas implementar
3. Usa la respuesta como contexto en Cline para:
   - Generar código nuevo
   - Modificar código existente
   - Implementar funcionalidades
   - Resolver problemas específicos

## Ejemplos de Uso

### Ejemplo 1: Consulta sobre Implementación

```bash
python3 smart_docs.py --query "Basándote en la documentación de FastAPI, muestra cómo implementar autenticación OAuth2 con JWT, incluyendo:
1) Configuración de dependencias
2) Manejo de tokens
3) Protección de rutas"
```

### Ejemplo 2: Consulta sobre Arquitectura

```bash
python3 smart_docs.py --query "Basándote en la documentación de FastAPI, explica la estructura recomendada para una API, incluyendo:
1) Organización de directorios
2) Separación de responsabilidades
3) Manejo de configuraciones"
```

## Estructura de Archivos

```
script-doc_processor/
├── smart_docs.py     # Script principal
├── requirements.txt  # Dependencias
└── README.md        # Documentación
```

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
