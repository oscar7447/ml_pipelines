from abc import ABC, abstractmethod
from typing import Tuple
import pandas as pd


class AbstractDatasetBuilder(ABC):
    @abstractmethod
    def build(self, dataset: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, any]:
        pass