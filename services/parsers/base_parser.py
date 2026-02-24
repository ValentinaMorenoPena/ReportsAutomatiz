from abc import ABC, abstractmethod

import pandas as pd


class BaseParser(ABC):
    """
    Contrato que todos los parsers de APIs deben cumplir.
    """

    @abstractmethod
    def parse_records(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def parse_pagination(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def parse_audit(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def parse_status(self) -> pd.DataFrame:
        pass
