from typing import Dict, Any

OPTIMIZATION_SETTINGS: Dict[str, Any] = {
    # Configuración de chunks
    "chunk_size": 4000,
    "overlap_size": 200,
    
    # Configuración de procesamiento por lotes
    "batch_size": 10,
    "max_workers": 4,
    
    # Configuración de caché
    "cache_ttl": 300,  # 5 minutos
    "max_cache_size": 1000,  # Número máximo de entradas en caché
    
    # Configuración de vectores
    "vector_size": 384,
    
    # Configuración de spaCy
    "spacy_model": "en_core_web_sm",
    "spacy_disabled_components": ["parser", "ner"],
    
    # Configuración de ChromaDB
    "chroma_settings": {
        "anonymized_telemetry": False,
        "allow_reset": True,
        "is_persistent": True
    }
}

# Patrones de regex precompilados
import re

PATTERNS = {
    "section_split": re.compile(r'\n\s*\n'),
    "sentence_split": re.compile(r'(?<=[.!?])\s+'),
    "whitespace_cleanup": re.compile(r'\s+')
}
