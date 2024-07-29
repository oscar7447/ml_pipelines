import pandas as pd
from sklearn.impute import SimpleImputer
from loan_model.inference.datasetbuilder.abstract_dataset_builder import AbstractDatasetBuilder


class DatasetBuilder(AbstractDatasetBuilder):

    def __init__(self) -> None:
        self.dataset_signature = ['Age', 'Annual_Income', 'Credit_Score', 'Loan_Amount', 'Number_of_Open_Accounts', 'Loan_Duration_Years', 'Had_Past_Default']
    def build(self, dataset:pd.DataFrame, 
              imputer:SimpleImputer) -> pd.DataFrame:

        # Handling null values
        df_imputed = dataset .copy()
        df_imputed[['Age', 'Annual_Income', 
                    'Credit_Score', 'Loan_Amount', 
                    'Number_of_Open_Accounts']] = imputer.transform(
                        dataset[['Age', 'Annual_Income', 'Credit_Score', 'Loan_Amount', 'Number_of_Open_Accounts']])
        try:
            df_imputed = df_imputed[self.dataset_signature]
        except KeyError as e:
            raise KeyError(f"Dataset is missing required columns: {e}")
        
        
        return df_imputed