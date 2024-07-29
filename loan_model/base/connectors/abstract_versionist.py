from abc import ABC, abstractmethod

class AbstractVersionist(ABC):
    
    @abstractmethod
    def save_model(self, model, version):
        pass

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def save_artifacts(self, artifacts, version):
        pass

    @abstractmethod
    def load_artifacts(self):
        pass

    @abstractmethod
    def save_metrics(self, metrics:str):
        pass



