import nltk
from loguru import logger

def download_nltk_resources():
    """
    Descarga los recursos necesarios de NLTK.
    """
    resources = [
        'punkt',
        'stopwords',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words'
    ]

    for resource in resources:
        try:
            nltk.download(resource, quiet=True)
            logger.info(f"Recurso NLTK '{resource}' descargado correctamente")
        except Exception as e:
            logger.error(f"Error descargando recurso NLTK '{resource}': {e}")
            raise

if __name__ == "__main__":
    download_nltk_resources()
