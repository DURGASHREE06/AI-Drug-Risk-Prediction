from database import save_prediction
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load model and feature columns
model = joblib.load("../models/drug_risk_model.pkl")
features = joblib.load("../models/feature_columns.pkl")
print("Features used by model:")
print(features)
print("Total:", len(features))


class UserInput(BaseModel):
    Age: float
    Nscore: float
    Escore: float
    Oscore: float
    Ascore: float
    Cscore: float
    Impulsive: float
    SS: float


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/predict")
def predict(data: UserInput):

    # Create empty sample with all required features
    sample = {c: 0 for c in features}

    # Fill user inputs
    sample["Age"] = data.Age
    sample["Nscore"] = data.Nscore
    sample["Escore"] = data.Escore
    sample["Oscore"] = data.Oscore
    sample["Ascore"] = data.Ascore
    sample["Cscore"] = data.Cscore
    sample["Impulsive"] = data.Impulsive
    sample["SS"] = data.SS

    # Convert to DataFrame
    df = pd.DataFrame([sample])

    # Prediction
    pred = int(model.predict(df)[0])

    # Probability
    prob = float(model.predict_proba(df)[0][1])

    # Save to database
    save_prediction(
        data.Age,
        data.Nscore,
        data.Escore,
        data.Oscore,
        data.Ascore,
        data.Cscore,
        data.Impulsive,
        data.SS,
        pred,
        prob
    )

    return {
        "prediction": pred,
        "risk_probability": prob
    }