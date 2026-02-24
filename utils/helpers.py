import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

def load_json_file(path: str | Path) -> list:
    """
    Carga un archivo JSON y retorna su contenido como lista
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"No existe el archivo: {file_path}")

    with file_path.open(encoding="utf-8") as f:
        return json.load(f)

def generate_timestamped_filename(base_name: str, directory: str, extension: str = "xlsx") -> str:
    """
    Genera un nombre de archivo con fecha y hora de ejecución.

    Ejemplo:
    contabilidad 17-02-2025 14-40.xlsx
    """

    timestamp = datetime.now().strftime("%d-%m-%Y %H-%M")
    filename = f"{base_name} {timestamp}.{extension}"

    return os.path.join(directory, filename)

def build_pagination(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Construye la estructura estándar de paginación.
    """
    total_records = len(records)

    return {
        "totalRecords": total_records,
        "pageSize": total_records,
        "totalPages": 1,
        "currentPage": 1,
        "generatedAt": datetime.utcnow().isoformat()
    }


def build_status(success: bool = True, message: str = "Proceso ejecutado correctamente") -> Dict[str, Any]:
    """
    Construye la estructura estándar de estado.
    """
    return {
        "code": 200 if success else 500,
        "success": success,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }


def build_standard_response(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Construye la respuesta completa estándar para cualquier servicio.
    """
    return {
        "records": records,
        "pagination": build_pagination(records),
        "status": build_status(True)
    }


def build_error_response(error: Exception) -> Dict[str, Any]:
    """
    Construye estructura estándar en caso de error.
    """
    return {
        "records": [],
        "pagination": build_pagination([]),
        "status": build_status(False, str(error))
    }


def delete_input_file(path: str | Path) -> None:
    """
    Elimina el archivo de input después de procesamiento exitoso.
    """
    file_path = Path(path)

    if file_path.exists():
        file_path.unlink()
        print(f"🗑️ Archivo eliminado: {file_path}")