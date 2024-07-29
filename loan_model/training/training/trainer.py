import pandas as pd
from loan_model.base.connectors.abstract_versionist import AbstractVersionist
from loan_model.training.datasetbuilder.abstract_dataset_builder import AbstractDatasetBuilder
from loan_model.base.connectors.abstract_extractor import AbstractExtractor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


class Trainer:
    def __init__(
        self, 
        versionist:AbstractVersionist,
        dataset_builder:AbstractDatasetBuilder,
        extractor:AbstractExtractor
        ):
        
        self.versionist = versionist
        self.dataset_builder = dataset_builder
        self.extractor = extractor

    def train(self):
        self.dataset = self.extractor.extract()
        X, y, imputer = self.dataset_builder.build()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

        self.model = self._train_model(X_train, y_train)
        metrics = self._metrics(X_test, y_test)
        artifacts = {"imputer":imputer}
        self.versionist.save_model(self.model)
        self.versionist.save_artifacts(artifacts)
        self.versionist.save_metrics(metrics)
        
    def _train_model(self, X, y):

        # Training the Logistic Regression model
        model = LogisticRegression()
        model.fit(X, y)
        return model

    def _metrics(self, X_test, y_test):

        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        return pd.DataFrame({'accuracy':  [accuracy], 'f1': [f1]})