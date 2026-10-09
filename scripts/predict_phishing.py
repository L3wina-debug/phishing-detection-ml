"""Load the trained model and classify one website from its feature vector."""
import joblib
import pandas as pd

from config import MODEL_PATH, PHISHING_LABEL

_model = None


def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


def feature_names() -> list:
    """Feature names, in the order the model expects them."""
    return list(load_model().feature_names_in_)


def predict_phishing(features: dict) -> str:
    """Return "Phishing" or "Legitimate" for a dict {feature_name: -1|0|1}."""
    model = load_model()
    row = pd.DataFrame([features], columns=model.feature_names_in_)
    prediction = model.predict(row)[0]
    return "Phishing" if prediction == PHISHING_LABEL else "Legitimate"
