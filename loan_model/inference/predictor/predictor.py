import pandas as pd
from loan_model.inference.datasetbuilder.abstract_dataset_builder import AbstractDatasetBuilder
from loan_model.base.connectors.abstract_versionist import AbstractVersionist

class LoanApprovalPredictor:

    def __init__(self, versionist:AbstractVersionist, 
                 dataset_builder:AbstractDatasetBuilder,
                 dataset:pd.DataFrame,
                 model_version:str):
        self.versionist = versionist
        self.dataset_builder = dataset_builder
        self.dataset = dataset
        self.model_version = model_version
        self.model = None
        self.artifacts = None


    def predict(self):
        self._load_model()
        X = self.dataset.copy()
        imputer = self.artifacts.get("imputer")
        X = self.dataset_builder.build(X, imputer)
        return self.model.predict(X)

    def _load_model(self):
        self.model = self.versionist.load_model()
        self.artifacts = self.versionist.load_artifacts()
