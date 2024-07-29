from loan_model.training.training.enums import Models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

class TrainerFactory:
    @staticmethod
    def get_model(model:Models, **kwargs):
        model_instance = None
        if model==Models.LOGISTIC_CLASSIFIER:
            model_instance = LogisticRegression(**kwargs)
        elif model==Models.RANDOM_FOREST_CLASSIFIER:
            model_instance = RandomForestClassifier(**kwargs)
        return model_instance