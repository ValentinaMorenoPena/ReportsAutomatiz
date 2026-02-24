# services/valorizacion.py

from services.json_loader import JsonLoader
from services.excel_writer import ExcelWriterService
from utils.helpers import build_error_response


class ValorizacionService:

    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def process(self) -> None:
        try:
            # 1️⃣ Cargar JSON completo
            raw_data = JsonLoader.load(self.input_path)

            # 2️⃣ Extraer records correctamente
            records = (
                raw_data.get("body", {})
                .get("records", [])
            )

            # 3️⃣ Extraer paginación real
            header_pagination = (
                raw_data.get("header", {})
                .get("pagination", {})
            )

            pagination = {
                "page": header_pagination.get("page"),
                "size": header_pagination.get("size"),
                "count": header_pagination.get("count"),
                "total": header_pagination.get("total"),
            }

            # 4️⃣ Extraer status real
            header_status = (
                raw_data.get("header", {})
                .get("status", {})
            )

            status = {
                "httpCode": header_status.get("HTTP_CODE"),
                "httpMessage": header_status.get("HTTP_MESSAGE"),
                "result": header_status.get("result"),
                "description": header_status.get("description"),
                "message": header_status.get("message"),
            }

            # 5️⃣ Construir respuesta
            response = {
                "records": records,
                "pagination": pagination,
                "status": status
            }

            # 6️⃣ Escribir Excel
            ExcelWriterService.write_response_to_excel(
                response,
                self.output_path
            )

        except Exception as e:
            error_response = build_error_response(e)
            ExcelWriterService.write_response_to_excel(
                error_response,
                self.output_path
            )