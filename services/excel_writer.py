# services/excel_writer.py

import pandas as pd
from typing import Dict, Any


class ExcelWriterService:
    """
    Servicio estándar para escritura de archivos Excel
    con hojas: Records, Pagination y Status.
    """

    SHEET_RECORDS = "Records"
    SHEET_PAGINATION = "Pagination"
    SHEET_STATUS = "Status"

    @staticmethod
    def write_response_to_excel(response: Dict[str, Any], output_path: str) -> None:
        """
        Escribe la respuesta estándar en un archivo Excel.
        """

        records = response.get("records", [])
        pagination = response.get("pagination", {})
        status = response.get("status", {})

        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:

            # Hoja Records
            df_records = pd.DataFrame(records)
            df_records.to_excel(writer, sheet_name=ExcelWriterService.SHEET_RECORDS, index=False)

            # Hoja Pagination
            df_pagination = pd.DataFrame([pagination])
            df_pagination.to_excel(writer, sheet_name=ExcelWriterService.SHEET_PAGINATION, index=False)

            # Hoja Status
            df_status = pd.DataFrame([status])
            df_status.to_excel(writer, sheet_name=ExcelWriterService.SHEET_STATUS, index=False)
