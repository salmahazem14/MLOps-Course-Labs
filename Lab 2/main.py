"""
Churn Prediction API

Run with:
    litestar --app main:app run --reload
Then open:
    http://localhost:8000/schema/swagger
"""

import pandas as pd
from litestar import Litestar, get, post
from pydantic import BaseModel

from app.logger_setup import setup_logging
from app.model_utils import predict_churn

logger = setup_logging()


# ---------------------------------------------------------------------------
# Request Schema
# ---------------------------------------------------------------------------

class ChurnRequest(BaseModel):
    CreditScore: float
    Geography : str
    Gender : str
    Age : int
    Tenure : int 
    Balance : float
    NumOfProducts : int
    HasCrCard : int
    IsActiveMember : int
    EstimatedSalary : float


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

# TODO 2: Create a GET endpoint at "/" that returns a welcome message
#         Log that the home endpoint was accessed

@get('/')
async def home() -> dict:
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to the Churn Prediction API!"}

# TODO 3: Create a GET endpoint at "/health" that returns {"status": "healthy"}
@get('/health')
async def health() -> dict: 
    return {"status": "healthy"}

# TODO 4: Create a POST endpoint at "/predict" that:
#         - Accepts a ChurnRequest as the data parameter
#         - Extracts features into a list
#         - Calls predict_churn(features)
#         - Returns the prediction
#         - Logs the input features and the prediction result

@post('/predict')
async def predict(data: ChurnRequest) -> dict:
    sample = pd.DataFrame([data.model_dump()])

    logger.info(f"Received sample: {sample.to_dict(orient='records')}")
    prediction = predict_churn(sample)
    logger.info(f"Prediction result: {prediction}")
    return {"prediction": prediction}


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

# TODO 5: Register your endpoint functions in the list below
app = Litestar(
    route_handlers=[home, health, predict],
)
