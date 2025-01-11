#!/bin/bash

# Colores para mensajes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Iniciando instalación de Doc Processor...${NC}"

# Crear estructura de directorios
echo -e "${GREEN}Creando estructura de directorios...${NC}"
mkdir -p docs
mkdir -p chroma_db

# Verificar Docker
if ! command -v docker &> /dev/null; then
    echo "Docker no está instalado. Por favor, instala Docker primero."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose no está instalado. Por favor, instala Docker Compose primero."
    exit 1
fi

# Construir imagen Docker
echo -e "${GREEN}Construyendo imagen Docker...${NC}"
docker-compose build

# Verificar instalación
echo -e "${GREEN}Verificando instalación...${NC}"
docker-compose run --rm doc-processor --help

echo -e "${BLUE}Instalación completada.${NC}"
echo -e "${GREEN}Puedes comenzar a usar Doc Processor con:${NC}"
echo "docker-compose run --rm doc-processor [comandos]"
echo
echo "Ejemplos:"
echo "1. Procesar documentación:"
echo "docker-compose run --rm doc-processor --path docs/mi_proyecto --reset"
echo
echo "2. Realizar consulta:"
echo "docker-compose run --rm doc-processor --query \"tu consulta aquí\""
