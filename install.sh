#!/bin/bash

# Colores para mensajes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}Iniciando instalación del Script Doc Processor...${NC}"

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Docker no está instalado. Por favor, instale Docker primero.${NC}"
    exit 1
fi

# Verificar si Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}Docker Compose no está instalado. Por favor, instale Docker Compose primero.${NC}"
    exit 1
fi

# Crear estructura de directorios
echo -e "${BLUE}Creando estructura de directorios...${NC}"
mkdir -p doc_py chroma_db

# Establecer permisos
echo -e "${BLUE}Configurando permisos...${NC}"
chmod +x doc_processor.py query_docs.py smart_docs.py

# Construir imagen Docker
echo -e "${BLUE}Construyendo imagen Docker...${NC}"
docker-compose build

# Verificar si la construcción fue exitosa
if [ $? -eq 0 ]; then
    echo -e "${GREEN}¡Instalación completada con éxito!${NC}"
    echo -e "\nPara procesar documentación:"
    echo -e "${BLUE}docker-compose run --rm doc-processor --path /ruta/a/tu/documentacion${NC}"
    echo -e "\nPara realizar consultas:"
    echo -e "${BLUE}docker-compose run --rm query${NC}"
    echo -e "\nPara usar funcionalidades adicionales:"
    echo -e "${BLUE}docker-compose run --rm smart-docs${NC}"
else
    echo -e "${RED}Error durante la instalación${NC}"
    exit 1
fi

# Crear archivo de configuración local si no existe
if [ ! -f config.local.yml ]; then
    echo -e "${BLUE}Creando archivo de configuración local...${NC}"
    cat > config.local.yml << EOL
chroma_db:
  path: /app/chroma_db
doc_directories:
  - /app/doc_py
EOL
fi

# Instrucciones para nuevo proyecto
echo -e "\n${GREEN}Instrucciones para usar en un nuevo proyecto:${NC}"
echo -e "1. Clone este repositorio en su proyecto:"
echo -e "${BLUE}git clone https://github.com/jivagrisma/script-doc_processor.py.git docs-processor${NC}"
echo -e "2. Entre al directorio:"
echo -e "${BLUE}cd docs-processor${NC}"
echo -e "3. Ejecute el script de instalación:"
echo -e "${BLUE}./install.sh${NC}"
echo -e "4. Coloque sus archivos .txt en el directorio 'doc_py/'"
echo -e "5. Procese la documentación:"
echo -e "${BLUE}docker-compose run --rm doc-processor --path doc_py${NC}"
echo -e "6. Realice consultas:"
echo -e "${BLUE}docker-compose run --rm query${NC}"

echo -e "\n${GREEN}El sistema está listo para usar.${NC}"
