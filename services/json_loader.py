# services/json_loader.py

import json
from typing import Any


class JsonLoader:
    """
    Servicio responsable de cargar archivos JSON
    y garantizar que siempre retorne un diccionario.
    """

    @staticmethod
    def load(file_path: str) -> Any:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                # ✅ Si viene doble serializado (string)
                if isinstance(data, str):
                    data = json.loads(data)

                return data

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {str(e)}")
