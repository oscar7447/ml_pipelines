from loan_model.base.connectors.abstract_versionist import AbstractVersionist
import os
import pandas as pd
import pickle

class LocalVersionist(AbstractVersionist):
    """
    This class acts as a model versionist for the local environment.
    It provides methods to save and load models, artifacts, and metrics
    for a specific version of the model.

    Attributes:
        path (str): The base path where the version-specific directories will be created.
        version (str): The version of the model.

    Methods:
        __init__(self, path: str, version: str): Initializes the LocalVersionist object.
        save_model(self, model): Saves the model to the version-specific directory.
        load_model(self): Loads the model from the version-specific directory.
        save_artifacts(self, artifacts): Saves the artifacts to the version-specific directory.
        load_artifacts(self): Loads the artifacts from the version-specific directory.
        save_metrics(self, metrics: pd.DataFrame): Saves the metrics to the version-specific directory.
        _save(self, obj, path): Helper method to save an object to a given path.
        _load(self, path): Helper method to load an object from a given path.
    """
    
    def __init__(self, path:str, version:str):
        self.path = path + "/" + version



    def save_model(self, model):

        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self._save(model, self.path + "/model.pkl")

    def load_model(self):
        return self._load(self.path + "/model.pkl")
    
    def save_artifacts(self, artifacts):
        artifacts_path = self.path + "/artifacts"
        os.makedirs(artifacts_path)
        for name, value in artifacts.items():
            tmp_path = artifacts_path + "/" + name
            self._save(value, tmp_path)

    def load_artifacts(self):
        artifacts_path = self.path + "/artifacts"

        return self._load_folder(artifacts_path)
    
    def save_metrics(self, metrics:pd.DataFrame):
        os.makedirs(self.path + "/metrics")

        metrics.to_csv(self.path + "/metrics/metrics.csv")

    def _save(self, obj, path):

        with open(path, 'wb') as f:
            pickle.dump(obj, f)
    def _load(self, path):

        with open(path, 'rb') as f:
            loaded_object = pickle.load(f)
        return loaded_object
    
    def _load_folder(self, path):
        all_objects = {}
        for name in os.listdir(path):
            with open(os.path.join(path, name), 'rb') as f:
                # Read content of file
                loaded_object = pickle.load(f)
                all_objects = {name:loaded_object}
        

        return all_objects