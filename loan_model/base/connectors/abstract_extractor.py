import pandas as pd
from abc import ABC, abstractmethod


class AbstractExtractor(ABC):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    @abstractmethod
    def extract(self) -> pd.DataFrame:
        pass