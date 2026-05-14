"""
Model loading and prediction logic.

The model must be loaded ONCE at module level, NOT inside the predict function.
"""

import joblib
import numpy as np 
import pandas as pd

# TODO 1: Load your serialized churn model from data/model.joblib
model = joblib.load("data/rf_model.pkl")
transformer = joblib.load("data/column_transformer.pkl")

sample = pd.DataFrame([{
        "CreditScore": 619,
        "Geography": "France",
        "Gender": "Female",
        "Age": 42,
        "Tenure": 2,
        "Balance": 0.0,
        "NumOfProducts": 1,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 101348.9
    }])

def predict_churn(features: list[float]) -> int:
    """
    Takes a list of feature values and returns a churn prediction (0 or 1).
    """
    X_transformed = transformer.transform(features)
    prediction = model.predict(X_transformed)

    return int(prediction[0])

if __name__ == "__main__":
    # TODO 3: Replace with sample features that match your model
    print(f"Input:      {sample}")
    print(f"Prediction: {predict_churn(sample)}")
