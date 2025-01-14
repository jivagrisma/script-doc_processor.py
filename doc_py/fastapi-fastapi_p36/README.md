# FastAPI Documentation

FastAPI es un framework web moderno y rápido para construir APIs con Python 3.7+ basado en estándares Python.

## Requisitos del Sistema

### Versiones de Python Compatibles

FastAPI requiere Python 3.7 o superior. Las versiones recomendadas son:

- Python 3.7 (soporte mínimo)
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11 (recomendado para mejor rendimiento)
- Python 3.12 (última versión estable)

La versión más recomendable para usar FastAPI es Python 3.11, ya que ofrece mejoras significativas de rendimiento y todas las características modernas de Python que FastAPI aprovecha.

### Dependencias Principales

- Starlette para las funcionalidades web
- Pydantic para la validación de datos
- Uvicorn como servidor ASGI
- Python 3.7+ (CPython y PyPy)

## Instalación

```bash
pip install fastapi[all]
```

Para una instalación mínima:

```bash
pip install fastapi uvicorn
