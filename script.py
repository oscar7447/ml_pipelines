import uuid
from loan_model.base.connectors.local_extractor import LocalExtractor
from loan_model.training.datasetbuilder.dataset_builder import DatasetBuilder
from loan_model.training.training.trainer import Trainer
from loan_model.base.connectors.local_versionist import LocalVersionist
from loan_model.training.training.enums import Models

class TrainerApplicationService:

    def __init__(self, dataset_path:str):
        self.extractor = LocalExtractor(dataset_path)
        dataset = self.extractor.extract()
        self.dataset_builder = DatasetBuilder(dataset)
        self.version = str(uuid.uuid4())
        self.versionist = LocalVersionist("./files/model_versions", self.version)
        self.trainer = Trainer(self.versionist, self.dataset_builder, self.extractor)



    def train(self, model_name, **kwargs):
        model = self.trainer.train(model_name, **kwargs)
        print(f"Model trained with version: {self.version}")
        return self.version, model

if __name__ == "__main__":
    dataset_path = "./files/dataset.csv"
    service = TrainerApplicationService(dataset_path=dataset_path)
    model_parameters = {"max_depth":10}
    model_version, model = service.train(Models.RANDOM_FOREST_CLASSIFIER, **model_parameters)
    print(1)
