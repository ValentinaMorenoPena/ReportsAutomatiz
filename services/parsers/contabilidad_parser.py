import pandas as pd


class ContabilidadParser:
    """
    Parser específico para el JSON de la API de Contabilidad.
    Convierte el JSON en DataFrames listos para Excel.
    """

    def __init__(self, json_data: dict):
        self.json_data = json_data

    def parse_records(self) -> pd.DataFrame:
        """
        Extrae los registros principales de valorización
        """
        records = self.json_data.get("body", {}).get("records", [])
        return pd.DataFrame(records)

    def parse_debitos(self) -> pd.DataFrame:
        """
        Extrae débitos desde los records (si aplica)
        """
        records = self.parse_records()

        if records.empty or "debitCredit" not in records.columns:
            return pd.DataFrame()

        return records[records["debitCredit"] == "DB"]

    def parse_creditos(self) -> pd.DataFrame:
        """
        Extrae créditos desde los records (si aplica)
        """
        records = self.parse_records()

        if records.empty or "debitCredit" not in records.columns:
            return pd.DataFrame()

        return records[records["debitCredit"] == "CR"]

    def parse_pagination(self) -> pd.DataFrame:
        pagination = self.json_data.get("header", {}).get("pagination", {})
        return pd.DataFrame([pagination]) if pagination else pd.DataFrame()

    def parse_audit(self) -> pd.DataFrame:
        audit = self.json_data.get("header", {}).get("audit", {})
        return pd.DataFrame([audit]) if audit else pd.DataFrame()

    def parse_status(self) -> pd.DataFrame:
        status = self.json_data.get("header", {}).get("status", {})
        return pd.json_normalize(status) if status else pd.DataFrame()
