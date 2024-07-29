import pandas as pd
from loan_model.base.connectors.abstract_extractor import AbstractExtractor

class LocalExtractor(AbstractExtractor):
    def __init__(self, path: str):
        self.path = path

    def extract(self) -> pd.DataFrame:
        return pd.read_csv(self.path)