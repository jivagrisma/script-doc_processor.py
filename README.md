# Script Doc Processor

Sistema de procesamiento y consulta de documentación diseñado para mejorar las capacidades de modelos LLM (como Claude) proporcionándoles contexto actualizado a través de documentación en formato txt. El sistema utiliza ChromaDB como base de datos vectorial para almacenar y recuperar eficientemente la información relevante.

## Propósito Principal

El objetivo principal de este sistema es permitir que los modelos LLM, específicamente Claude a través de la extensión Cline en VS Code, tengan acceso a información actualizada y contextual para tomar decisiones más precisas. Esto se logra mediante:

1. Procesamiento de cualquier documentación en formato txt
2. Almacenamiento eficiente en una base de datos vectorial
3. Recuperación contextual basada en similitud semántica
4. Integración seamless con Cline para consultas en tiempo real

## Scripts Principales

El proyecto cuenta con tres scripts principales:

1. **doc_processor.py**: Script principal para procesar documentación
   - Procesa cualquier archivo txt independiente de su contenido o temática
   - Extrae metadatos automáticamente
   - Detecta tipos de documentos y versiones
   - Genera embeddings para búsqueda semántica

2. **query_docs.py**: Script para realizar consultas
   - Búsqueda semántica en toda la documentación procesada
   - Filtrado por tipo de documento
   - Ranking de relevancia
   - Resaltado de coincidencias

3. **smart_docs.py**: Script con funcionalidades adicionales
   - Procesamiento avanzado de texto
   - Utilidades de manipulación de documentos
   - Funciones auxiliares

## Características

- **Flexibilidad en el Procesamiento**: 
  - Acepta cualquier documentación en formato txt
  - No está limitado a un tipo específico de contenido
  - Adaptable a diferentes estructuras y formatos de documentación

- **Procesamiento Inteligente**:
  - División automática en chunks manejables
  - Extracción de metadatos relevantes
  - Detección automática de tipos de documento
  - Identificación de versiones cuando están disponibles

- **Almacenamiento Eficiente**:
  - Uso de ChromaDB como base de datos vectorial
  - Optimización para búsquedas semánticas
  - Persistencia de datos entre sesiones

- **Integración con Cline**:
  - Proporciona contexto actualizado a Claude
  - Mejora la precisión de las respuestas
  - Permite decisiones basadas en documentación actual

## Estructura del Proyecto

```
proyecto/
├── src/                    # Código fuente principal
│   ├── processors/        # Procesamiento de documentos
│   ├── storage/          # Gestión de almacenamiento
│   └── utils/           # Utilidades generales
├── doc_py/              # Directorio para documentación
├── doc_processor.py     # Script principal
├── query_docs.py        # Script de consultas
└── smart_docs.py        # Funcionalidades adicionales
```

## Instalación

### Opción 1: Usando Docker (Recomendado)

1. Clonar el repositorio:
```bash
git clone https://github.com/jivagrisma/script-doc_processor.py.git
cd script-doc_processor.py
```

2. Ejecutar script de instalación:
```bash
chmod +x install.sh
./install.sh
```

El script de instalación:
- Verifica las dependencias necesarias
- Crea la estructura de directorios
- Construye la imagen Docker
- Configura los permisos necesarios

### Opción 2: Instalación Local

1. Clonar el repositorio:
```bash
git clone https://github.com/jivagrisma/script-doc_processor.py.git
cd script-doc_processor.py
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### 1. Procesamiento de Nueva Documentación

```bash
# Con Docker
docker-compose run --rm doc-processor --path /ruta/a/tu/documentacion

# Sin Docker
python3 doc_processor.py --path /ruta/a/tu/documentacion
```

### 2. Consultas sobre la Documentación

```bash
# Con Docker
docker-compose run --rm query

# Sin Docker
python3 query_docs.py
```

## Ejemplos de Uso

### 1. Procesar Nueva Documentación

```bash
# Procesar documentación de un proyecto
docker-compose run --rm doc-processor --path doc_py/nueva_documentacion

# Procesar múltiples archivos
python3 doc_processor.py --path /ruta/a/tus/archivos/txt
```

### 2. Realizar Consultas

```bash
# Consulta interactiva
docker-compose run --rm query

# Consulta específica
python3 query_docs.py --search "¿Cómo implementar esta funcionalidad?"
```

## Mejores Prácticas

### 1. Organización de Documentación

- Dividir documentación extensa en archivos manejables
- Usar nombres descriptivos
- Mantener una estructura consistente
- Incluir información de versiones cuando sea relevante

### 2. Mantenimiento

- Actualizar la documentación regularmente
- Limpiar la base de datos vectorial periódicamente
- Hacer respaldos de documentación importante

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request
