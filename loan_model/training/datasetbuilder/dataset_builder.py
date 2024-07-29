import pandas as pd
from sklearn.impute import SimpleImputer
from loan_model.training.datasetbuilder.abstract_dataset_builder import AbstractDatasetBuilder


class DatasetBuilder(AbstractDatasetBuilder):
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.dataset_signature = ['Age', 'Annual_Income', 'Credit_Score', 'Loan_Amount', 'Number_of_Open_Accounts', 'Loan_Duration_Years', 'Had_Past_Default']

    def build(self) -> pd.DataFrame:

        # Handling null values
        imputer = SimpleImputer(fill_value=0)
        df_imputed = self.dataset .copy()
        df_imputed[['Age', 'Annual_Income', 
                    'Credit_Score', 'Loan_Amount', 
                    'Number_of_Open_Accounts']] = imputer.fit_transform(
                        self.dataset[['Age', 'Annual_Income', 'Credit_Score', 'Loan_Amount', 'Number_of_Open_Accounts']])

        # Splitting the data into features and target
        X = df_imputed.drop('Loan_Approval', axis=1)
        y = df_imputed['Loan_Approval']

        try:
            X = X[self.dataset_signature]
        except KeyError as e:
            raise KeyError(f"Dataset is missing required columns: {e}")
        
        
        return X, y, imputer