from loan_model.inference.datasetbuilder.dataset_builder import DatasetBuilder
from loan_model.inference.predictor.predictor import LoanApprovalPredictor
from loan_model.base.connectors.local_extractor import LocalExtractor
from loan_model.base.connectors.local_versionist import LocalVersionist
import pandas as pd

class PredictorApplicationBatchService:
        
        def __init__(self, path: str):
            self.extractor = LocalExtractor(path)
            self.dataset = self.extractor.extract()
            self.dataset_builder = DatasetBuilder()
            
        def predict(self, model_version = "7e42b3e1-f234-4ede-ae81-85c116b8f1f9"):
            versionist = LocalVersionist("./files/model_versions", model_version)
            predictor = LoanApprovalPredictor(versionist, self.dataset_builder, self.dataset, model_version)
            return predictor.predict()
        

class PredictorApplicationService:
        
        def __init__(self):

            self.dataset_builder = DatasetBuilder()
            version = "7e42b3e1-f234-4ede-ae81-85c116b8f1f9"
            self.versionist = LocalVersionist("./files/model_versions", version)
            
        def predict(self, model_version, 
                    age, annual_income, 
                    credit_score, 
                    loan_amount, 
                    number_of_open_accounts, 
                    loan_duration_years, 
                    had_past_default):
            
            dataset = {'Age': [age], 
                       'Annual_Income': [annual_income], 
                       'Credit_Score': [credit_score], 
                       'Loan_Amount': [loan_amount], 
                       'Number_of_Open_Accounts': [number_of_open_accounts], 
                       'Loan_Duration_Years': [loan_duration_years], 
                       'Had_Past_Default': [had_past_default]}
            dataset = pd.DataFrame(dataset)
            self.predictor = LoanApprovalPredictor(self.versionist, self.dataset_builder, dataset, model_version)

            return self.predictor.predict()
if __name__ == "__main__":
    service = PredictorApplicationService()
    print(service.predict())
    