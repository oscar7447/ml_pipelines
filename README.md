# Machine Learning Engineering Assignment

This assignment is expected to be completed by a Machine Learning Engineer within 3-4 hours.

### Assignment:

Your teammate Mike gave you a Machine Learning Model that needs to be deployed, examine the model.py file. 
Your task is to add the necessary components to get this model to production, 
this model is crucial for the company's success, so it should be available receive and predict data upon request.
This model should work for any cloud provider. Also this is the model v1 of a series of versions to be deployed.
(Optional): you can come up with a better model pipeline if you think the one provided is not suitable for this case.

Add all the necessary files, code, docs, to improve this repository and make this model ready to be shipped.

Note: You can reach out to us through email at marcos.soto@qubika.com or anibal.jasin@qubika.com but since
you could be working off hours we suggest you can write down questions and assumptions you came across
and what decision you take e.g. “I’m gonna assume this project should have X because of Y” or 
“I would ask about if there is some ACL for this model, so I would assume X”.

Some general considerations and guidance:

- It is expected that you include files, code, documentation, and any other resources you find useful in the new repository you create.
- A fully production-ready model deployed in the cloud is not required.
- You are not expected to spend money on cloud services, ensuring everything works locally is sufficient.
- It is acceptable if some aspects are not fully functional, our goal is to understand your approach to this problem.
- In case you don’t finish the assignment, you can add what other things you would do in the README.md.


---------------------------------------------------------------------------
version=0.0.3


# Solution

# Machine Learning Engineer Test Documentation

This documentation provides an overview of the task for developing a machine learning API using FastAPI, with endpoints for inference on single data points and batch data, as well as a training endpoint. The test also includes implementing a local model versioning system. Below, you'll find detailed instructions and guidelines for each component.

## Project Structure

```
qubika_test/
│
├── files/
│   ├── model_version/       # versioning tool folder
       ├──  version_id/
         ├── artifacts/
         ├── metrics/
         ├── model.pkl
│   ├── dataset.csv        # data for training and inference testing
 loan model/
│   ├── base     # base code shared by the pipelines
│   ├── inference      # Inference pipeline results
│   └── training         # Training pipelines

├── requirements.txt     # List of dependencies
├── README.md            # Project README file
└── Dockerfile           # Dockerfile for containerization
└── main.py           # Fast api main file

```

## FastAPI Endpoints

### 1. **Single Data Point Inference Endpoint**

**Endpoint**: `/predict`

**Method**: `POST`

**Description**: Takes a single data point as input and returns the model's prediction.

**Request Body**:
- JSON object with the features required by the model.

**Response**:
- JSON object containing the prediction and the version of the model used.

**Example**:

```json
POST /predict
{
  "feature1": value1,
  "feature2": value2,
  ...
}
```

Response:
```json
{
  "prediction": 123,
  "model_version": "v1"
}
```

### 2. **Batch Inference Endpoint**

**Endpoint**: `/predict_batch`

**Method**: `POST`

**Description**: Takes a batch of data points and returns predictions for each.

**Request Body**:
- JSON array of objects, where each object represents a data point with the same structure as required by the single data point endpoint.

**Response**:
- JSON object containing an array of predictions and the model version used.

**Example**:

```json
POST /predict_batch
[
  {"feature1": value1, "feature2": value2, ...},
  {"feature1": value3, "feature2": value4, ...},
  ...
]
```

Response:
```json
{
  "predictions": [123, 456, ...],
  "model_version": "v1"
}
```

### 3. **Training Endpoint**

**Endpoint**: `/train`

**Method**: `POST`

**Description**: Initiates a training process using the provided data. The new model version is saved locally with an incremented version number.

**Request Body**:
- Optional JSON object specifying training parameters such as number of epochs, learning rate, etc. If not provided, defaults are used.

**Response**:
- JSON object containing a message about the status of the training process and the new model version.

**Example**:

```json
POST /train
{
  "epochs": 10,
  "learning_rate": 0.001
}
```

Response:
```json
{
  "message": "Training completed successfully.",
  "new_model_version": "v2"
}
```

## Model Versioning

### Loading Models
- Models are stored in the `models/` directory with filenames indicating their versions (e.g., `model_v1.pkl`, `model_v2.pkl`).
- The latest version is loaded by default, but specific versions can be loaded if required.

### Saving Models
- After training, the new model is saved with an incremented version number, e.g., if the latest version is `model_v1.pkl`, the new model is saved as `model_v2.pkl`.

## Testing

- Unit tests are provided in the `tests/` directory. These tests cover various aspects of the API, including single and batch inference and model training.
- To run the tests, use a testing framework like `pytest`.

## Dependencies

- All required dependencies are listed in the `requirements.txt` file. To install them, use:

```bash
pip install -r requirements.txt
```

## Running the Application

To start the FastAPI server locally, navigate to the project directory and run:

```bash
uvicorn app.main:app --reload
```

## Docker

A `Dockerfile` is provided for containerizing the application. To build the Docker image, use:

```bash
docker build -t ml_api .
```

To run the Docker container:

```bash
docker run -p 8000:8000 ml_api
```

This documentation serves as a guide for setting up and testing the machine learning API. For any additional questions or issues, please refer to the README file or contact the project maintainer.