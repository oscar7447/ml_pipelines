import unittest
from unittest.mock import MagicMock
import pandas as pd
from loan_model.inference.predictor.predictor import LoanApprovalPredictor
from loan_model.training.training.trainer import Trainer
class TestLoanApprovalPredictor(unittest.TestCase):

    def setUp(self):
        self.versionist_mock = MagicMock()
        self.dataset_builder_mock = MagicMock()
        self.dataset = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
        self.model_version = '1.0'
        self.predictor = LoanApprovalPredictor(self.versionist_mock, 
                                               self.dataset_builder_mock, 
                                               self.dataset, 
                                               self.model_version)

    def test_load_model(self):
        self.versionist_mock.load_model.return_value = 'model_mock'
        self.versionist_mock.load_artifacts.return_value = {'imputer': 'imputer_mock'}
        self.predictor._load_model()
        self.assertEqual(self.predictor.model, 'model_mock')
        self.assertEqual(self.predictor.artifacts, {'imputer': 'imputer_mock'})

    def test_predict(self):
        self.predictor.model = MagicMock()
        self.predictor.artifacts = {'imputer': 'imputer_mock'}
        self.dataset_builder_mock.build.return_value = self.dataset
        self.predictor.predict()
        self.predictor.model.predict.assert_called_once()



class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.mock_versionist = MagicMock()
        self.mock_dataset_builder = MagicMock()
        self.mock_extractor = MagicMock()
        self.trainer = Trainer(self.mock_versionist, self.mock_dataset_builder, self.mock_extractor)

    def test_train(self):
        # Setup mock returns
        self.dataset = pd.DataFrame(columns={'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
        self.mock_extractor.extract.return_value = self.dataset
        self.mock_dataset_builder.build.return_value = (self.dataset["feature1"], self.dataset["feature2"], 'imputer')
        self.mock_versionist.save_model.return_value = None
        self.mock_versionist.save_artifacts.return_value = None
        self.mock_versionist.save_metrics.return_value = None

        # Execute the train method
        self.trainer.train(model_name="test")

        # Assertions to ensure methods were called
        self.mock_versionist.save_model.assert_called_once()
        self.mock_versionist.save_metrics.assert_called_once()
if __name__ == '__main__':
    unittest.main()