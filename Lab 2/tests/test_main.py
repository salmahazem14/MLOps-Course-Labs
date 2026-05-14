import pytest

from app.model_utils import predict_churn
from main import app
from litestar.testing import TestClient


# ---------------------------------------------------------------------------
# Function Tests
# ---------------------------------------------------------------------------

# TODO 1: direct model test
def test_predict_churn_basic():
    sample = [
        619,
        "France",
        "Female",
        42,
        2,
        0.0,
        1,
        1,
        1,
        101348.9
    ]

    result = predict_churn(sample)

    assert result in [0, 1]


# TODO 2: edge case test
def test_predict_churn_edge_case():
    sample = [
        0,
        "France",
        "Male",
        0,
        0,
        0.0,
        0,
        0,
        0,
        0.0
    ]

    result = predict_churn(sample)

    assert result in [0, 1]


# ---------------------------------------------------------------------------
# Endpoint Tests
# ---------------------------------------------------------------------------

# TODO 3: POST /predict
def test_predict_endpoint():
    payload = {
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
    }

    with TestClient(app=app) as client:
        response = client.post("/predict", json=payload)

    assert response.status_code == 201
    assert "prediction" in response.json()


# TODO 4: GET /health
def test_health_endpoint():
    with TestClient(app=app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


# TODO 5: GET /
def test_home_endpoint():
    with TestClient(app=app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()


# TODO 6: invalid input test
def test_invalid_input():
    payload = {
        "CreditScore": "invalid", 
        "Geography": "France"
    }

    with TestClient(app=app) as client:
        response = client.post("/predict", json=payload)

    assert response.status_code == 400