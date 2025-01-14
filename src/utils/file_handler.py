from typing import List, Dict, Optional
from pathlib import Path
import magic
from loguru import logger
import os

class FileHandler:
    """
    Maneja operaciones de sistema de archivos y validación de archivos.
    """
    def __init__(self):
        self.mime = magic.Magic(mime=True)
        self.supported_types = {
            'text/plain': '.txt',
            'text/markdown': '.md',
            'text/x-python': '.py',
            'application/json': '.json'
        }

    def scan_directory(self, 
                      directory: str, 
                      recursive: bool = True) -> List[Dict]:
        """
        Escanea un directorio en busca de archivos de texto soportados.
        """
        try:
            path = Path(directory)
            if not path.exists():
                raise FileNotFoundError(f"Directorio no encontrado: {directory}")

            files_info = []
            pattern = "**/*" if recursive else "*"

            for file_path in path.glob(pattern):
                if file_path.is_file():
                    file_info = self.get_file_info(file_path)
                    if file_info:
                        files_info.append(file_info)

            logger.info(f"Encontrados {len(files_info)} archivos válidos en {directory}")
            return files_info

        except Exception as e:
            logger.error(f"Error escaneando directorio {directory}: {e}")
            raise

    def get_file_info(self, file_path: Path) -> Optional[Dict]:
        """
        Obtiene información detallada de un archivo.
        """
        try:
            # Detectar tipo MIME
            mime_type = self.mime.from_file(str(file_path))
            
            # Verificar si es un tipo soportado
            if mime_type not in self.supported_types:
                logger.debug(f"Tipo no soportado {mime_type} para {file_path}")
                return None

            # Obtener estadísticas del archivo
            stats = file_path.stat()
            
            return {
                "path": str(file_path),
                "name": file_path.name,
                "extension": file_path.suffix,
                "mime_type": mime_type,
                "size": stats.st_size,
                "modified": stats.st_mtime,
                "created": stats.st_ctime,
                "relative_path": str(file_path.relative_to(file_path.parent.parent))
            }

        except Exception as e:
            logger.warning(f"Error procesando archivo {file_path}: {e}")
            return None

    def read_file(self, file_path: str) -> str:
        """
        Lee el contenido de un archivo de forma segura.
        """
        try:
            path = Path(file_path)
            
            # Verificar existencia
            if not path.exists():
                raise FileNotFoundError(f"Archivo no encontrado: {file_path}")

            # Verificar tipo
            mime_type = self.mime.from_file(str(path))
            if mime_type not in self.supported_types:
                raise ValueError(f"Tipo de archivo no soportado: {mime_type}")

            # Leer contenido
            with path.open('r', encoding='utf-8') as f:
                content = f.read()

            logger.debug(f"Archivo leído exitosamente: {file_path}")
            return content

        except Exception as e:
            logger.error(f"Error leyendo archivo {file_path}: {e}")
            raise

    def create_directory_structure(self, base_path: str) -> Dict[str, str]:
        """
        Crea la estructura de directorios necesaria.
        """
        try:
            paths = {
                "base": base_path,
                "docs": os.path.join(base_path, "docs"),
                "processed": os.path.join(base_path, "processed"),
                "chroma_db": os.path.join(base_path, "chroma_db")
            }

            for path in paths.values():
                Path(path).mkdir(parents=True, exist_ok=True)
                logger.debug(f"Directorio creado/verificado: {path}")

            return paths

        except Exception as e:
            logger.error(f"Error creando estructura de directorios: {e}")
            raise

    def get_file_metadata(self, file_path: str) -> Dict:
        """
        Obtiene metadatos extendidos de un archivo.
        """
        try:
            path = Path(file_path)
            stats = path.stat()
            
            return {
                "filename": path.name,
                "extension": path.suffix,
                "path": str(path),
                "size": stats.st_size,
                "created": stats.st_ctime,
                "modified": stats.st_mtime,
                "is_symlink": path.is_symlink(),
                "parent_dir": str(path.parent),
                "absolute_path": str(path.absolute())
            }

        except Exception as e:
            logger.error(f"Error obteniendo metadatos de {file_path}: {e}")
            raise
