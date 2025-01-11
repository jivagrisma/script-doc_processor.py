FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos necesarios
COPY requirements.txt .
COPY smart_docs.py .
COPY .gitignore .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorio para documentación
RUN mkdir -p docs

# Volumen para persistir la base de datos y documentos
VOLUME ["/app/docs", "/app/chroma_db"]

# Comando por defecto
ENTRYPOINT ["python3", "smart_docs.py"]
