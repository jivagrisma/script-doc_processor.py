#!/bin/bash

# Colores para mensajes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}Iniciando instalación de Doc Processor...${NC}"
echo -e "${YELLOW}Sistema de procesamiento de documentación para mejorar las capacidades de modelos LLM${NC}"

# Verificar permisos de ejecución
if [ ! -x "$(command -v chmod)" ]; then
    echo "Error: chmod no está disponible. Verifica los permisos del sistema."
    exit 1
fi

# Crear estructura de directorios
echo -e "${GREEN}Creando estructura de directorios...${NC}"
mkdir -p doc_py
mkdir -p chroma_db
mkdir -p test_docs

# Verificar Docker
if ! command -v docker &> /dev/null; then
    echo "Docker no está instalado. Por favor, instala Docker primero."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose no está instalado. Por favor, instala Docker Compose primero."
    exit 1
fi

# Asegurar permisos de ejecución
echo -e "${GREEN}Configurando permisos...${NC}"
chmod +x doc_processor.py
chmod +x query_docs.py
chmod +x smart_docs.py

# Construir imagen Docker
echo -e "${GREEN}Construyendo imagen Docker...${NC}"
docker-compose build

# Verificar instalación
echo -e "${GREEN}Verificando instalación...${NC}"
docker-compose run --rm doc-processor --help

echo -e "${BLUE}Instalación completada.${NC}"
echo -e "${GREEN}Puedes comenzar a usar Doc Processor con los siguientes comandos:${NC}"
echo
echo "1. Procesar documentación:"
echo "docker-compose run --rm doc-processor --path /ruta/a/tus/documentos"
echo
echo "2. Realizar consultas:"
echo "docker-compose run --rm query"
echo
echo "3. Utilizar funciones avanzadas:"
echo "docker-compose run --rm smart --help"
echo
echo -e "${YELLOW}Ejemplos de uso:${NC}"
echo
echo "1. Procesar documentación nueva:"
echo "docker-compose run --rm doc-processor --path doc_py/nueva_documentacion"
echo
echo "2. Consulta interactiva:"
echo "docker-compose run --rm query"
echo
echo "3. Consulta específica:"
echo "docker-compose run --rm query --search \"¿Cómo implementar esta funcionalidad?\""
echo
echo -e "${BLUE}Nota: El sistema está diseñado para procesar cualquier documentación en formato txt${NC}"
echo -e "${BLUE}y proporcionar contexto actualizado a modelos LLM a través de Cline.${NC}"
