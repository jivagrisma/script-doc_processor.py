# Script Doc Processor

Solución para procesar y consultar grandes volúmenes de documentos de texto utilizando ChromaDB como base de datos vectorial. Diseñado específicamente para trabajar con Claude Sonnet 3.5v2 a través de la extensión Cline en VS Code.

## Características

- Procesamiento de documentos de texto en chunks manejables
- Almacenamiento vectorial usando ChromaDB
- Consultas semánticas sobre la documentación procesada
- Integración con Cline para desarrollo asistido
- Soporte para Docker

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

3. Usar el procesador de documentos:
```bash
# Procesar documentación
docker-compose run --rm doc-processor --path docs/mi_proyecto --reset

# Realizar consultas
docker-compose run --rm doc-processor --query "tu consulta aquí"
```

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

## Estructura de Proyecto Recomendada

```
proyecto/
├── docs/                    # Documentación del proyecto
│   ├── nextjs_2025/        # Documentación específica (ej: Next.js 2025)
│   │   ├── parte_1.txt
│   │   └── parte_2.txt
│   └── otros_docs/         # Otra documentación relevante
├── smart_docs.py           # Script principal
├── requirements.txt        # Dependencias
├── .gitignore             # Configuración de git
└── chroma_db/             # Base de datos vectorial (auto-generada)
```

## Uso con Cline

### 1. Procesar Documentación

```bash
# Con Docker:
docker-compose run --rm doc-processor --path docs/nextjs_2025 --reset

# Sin Docker:
python3 smart_docs.py --path docs/nextjs_2025 --reset
```

### 2. Realizar Consultas Estructuradas

```bash
# Con Docker:
docker-compose run --rm doc-processor --query "Basándote en la documentación de [tecnología], muestra paso a paso cómo [objetivo específico], incluyendo:
1) [primer aspecto]
2) [segundo aspecto]
3) [tercer aspecto]"

# Sin Docker:
python3 smart_docs.py --query "..."
```

### 3. Ejemplo de Consulta

```bash
docker-compose run --rm doc-processor --query "Basándote en la documentación de Next.js 2025, explica cómo implementar:
1) Configuración inicial del proyecto
2) Manejo de rutas y páginas
3) Integración con APIs"
```

## Mejores Prácticas

### 1. Organización de Documentación

- Dividir documentación en archivos manejables
- Usar nombres descriptivos y numerados
- Mantener una estructura consistente por tecnología/tema
- Incluir versión en nombre de directorio

### 2. Control de Versiones

- Documentar fecha y versión de la documentación
- Mantener documentación antigua en directorios separados
- Usar --reset al cambiar significativamente el contexto

### 3. Uso con Docker

- Los volúmenes persisten entre ejecuciones
- La documentación se monta en /app/docs
- La base de datos ChromaDB se monta en /app/chroma_db
- Usar --rm para limpiar contenedores después de cada uso

### 4. Mantenimiento

- Limpiar chroma_db/ periódicamente
- Hacer respaldo de documentos importantes
- Actualizar la imagen Docker cuando haya cambios en requirements.txt

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
