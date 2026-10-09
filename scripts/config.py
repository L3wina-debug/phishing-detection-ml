"""Shared paths and constants for the phishing detection pipeline."""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
MODELS_DIR = os.path.join(ROOT_DIR, "models")
RESULTS_DIR = os.path.join(ROOT_DIR, "results")

RAW_DATA_PATH = os.path.join(DATA_DIR, "phishing_dataset.csv")
PREPROCESSED_DATA_PATH = os.path.join(DATA_DIR, "preprocessed_data.csv")
MODEL_PATH = os.path.join(MODELS_DIR, "phishing_model.pkl")

TARGET_COLUMN = "Result"
PHISHING_LABEL = -1  # UCI encoding: -1 = phishing, 1 = legitimate
TEST_SIZE = 0.2
RANDOM_STATE = 42
