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

## Instalación y Uso en Nuevos Proyectos

El sistema está diseñado para ser fácilmente integrado en cualquier proyecto que necesite proporcionar contexto actualizado a Cline. La instalación se realiza a través de Docker para garantizar consistencia y facilidad de uso.

### Prerrequisitos

- Docker instalado en el sistema
- Docker Compose instalado
- Git para clonar el repositorio

### Instalación en un Nuevo Proyecto

1. Clonar el repositorio dentro de tu proyecto:
```bash
git clone https://github.com/jivagrisma/script-doc_processor.py.git docs-processor
cd docs-processor
```

2. Ejecutar el script de instalación automático:
```bash
chmod +x install.sh
./install.sh
```

El script de instalación realiza automáticamente:
- Verificación de prerrequisitos (Docker y Docker Compose)
- Creación de la estructura de directorios necesaria
- Configuración de permisos
- Construcción de la imagen Docker
- Creación de la configuración local
- Configuración del volumen persistente para ChromaDB

### Estructura Docker

El proyecto utiliza Docker Compose para definir tres servicios principales:

1. **doc-processor**: Servicio para procesar documentación
   ```bash
   docker-compose run --rm doc-processor --path /ruta/a/tu/documentacion
   ```

2. **query**: Servicio para realizar consultas
   ```bash
   docker-compose run --rm query
   ```

3. **smart-docs**: Servicio para funcionalidades adicionales
   ```bash
   docker-compose run --rm smart-docs
   ```

Cada servicio está configurado con:
- Volúmenes persistentes para datos
- Variables de entorno preconfiguradas
- Aislamiento de dependencias
- Gestión automática de recursos

### Ejemplo de Uso en un Nuevo Proyecto

Por ejemplo, para un proyecto como "app_bancolombia":

1. Dentro del proyecto, clonar el repositorio:
```bash
cd app_bancolombia
git clone https://github.com/jivagrisma/script-doc_processor.py.git docs-processor
```

2. Instalar el sistema:
```bash
cd docs-processor
./install.sh
```

3. Colocar documentación en formato txt:
```bash
# Ejemplo: documentación de Next.js 2025
cp /ruta/documentacion/next2025/*.txt doc_py/
```

4. Procesar la documentación:
```bash
docker-compose run --rm doc-processor --path doc_py
```

5. Realizar consultas a través de Cline:
```bash
docker-compose run --rm query
```

### Ventajas de la Dockerización

1. **Portabilidad**
   - Funciona de manera consistente en cualquier sistema
   - No requiere configuración adicional del entorno

2. **Aislamiento**
   - Las dependencias no interfieren con otros proyectos
   - Cada instancia es independiente

3. **Mantenibilidad**
   - Actualizaciones simplificadas
   - Gestión centralizada de dependencias

4. **Escalabilidad**
   - Fácil de replicar en múltiples proyectos
   - Configuración consistente en todos los ambientes

### Instalación Local (Alternativa)

Si prefieres no usar Docker, puedes realizar una instalación local:

```bash
git clone https://github.com/jivagrisma/script-doc_processor.py.git
cd script-doc_processor.py
pip install -r requirements.txt
```

**Nota**: La instalación con Docker es la opción recomendada para evitar problemas de compatibilidad y dependencias.

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
