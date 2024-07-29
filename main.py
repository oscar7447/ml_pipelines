from fastapi import (
    FastAPI,
    status,
    Depends,
    HTTPException,
    BackgroundTasks,
    Request,
)
import numpy as np
from typing import Dict, Any
from loan_model.training.application.trainer_application_service import TrainerApplicationService
from loan_model.inference.application.predictor_application_service import PredictorApplicationService, PredictorApplicationBatchService
from loan_model.training.training.enums import Models
app = FastAPI(title="Qubika Test",description="Model training and inference pipelines")

 
@app.post("/train")
def train_model(model_name:Models, 
                model_parameters:Dict[str, Any],
    dataset_path = "./files/dataset.csv"):
    service = TrainerApplicationService(dataset_path=dataset_path)
    model_version, model = service.train(model_name, **model_parameters)
    return {"model_version": model_version,
            "model_params":str(model.get_params()),
            "model_name":str(model)}

@app.get("/predict")
def inference(age: int, 
              annual_income: int, 
              credit_score: int, 
              loan_amount: int, 
              number_of_open_accounts: int, 
              loan_duration_years: int, 
              had_past_default: bool, 
              model_version: str= "7e42b3e1-f234-4ede-ae81-85c116b8f1f9"):
    service = PredictorApplicationService()
    prediction = service.predict(model_version, 
                                age, 
                                annual_income, 
                                credit_score, 
                                loan_amount, 
                                number_of_open_accounts, 
                                loan_duration_years, 
                                had_past_default)
    results = np.where(prediction==1, "Approved", "Rejected")
    response = {"prediction": results[0]}
    return response

@app.get("/predict_batch")
def batch_inference(model_version:str = "7e42b3e1-f234-4ede-ae81-85c116b8f1f9",
                    path: str = "./files/dataset.csv"):
    service = PredictorApplicationBatchService(path)
    prediction = service.predict(model_version)
    print(prediction)
    response = {"prediction": str(prediction)}
    return response



@app.get("/health")
def health_check():
    return {"status": "healthy"}

