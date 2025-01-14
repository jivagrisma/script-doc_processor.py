# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Crear directorios necesarios
RUN mkdir -p /app/chroma_db /app/doc_py

# Establecer variables de entorno
ENV PYTHONPATH=/app
ENV CHROMA_DB_DIR=/app/chroma_db

# Comando por defecto (puede ser sobreescrito)
CMD ["python3", "doc_processor.py"]
