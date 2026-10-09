"""Evaluate the saved model on the held-out test split and save plots."""
import os

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score,
                             classification_report, confusion_matrix)
from sklearn.model_selection import train_test_split

from config import (MODEL_PATH, PREPROCESSED_DATA_PATH, RANDOM_STATE, RESULTS_DIR,
                    TARGET_COLUMN, TEST_SIZE)


def main() -> None:
    model = joblib.load(MODEL_PATH)
    data = pd.read_csv(PREPROCESSED_DATA_PATH)
    X = data.drop(TARGET_COLUMN, axis=1)
    y = data[TARGET_COLUMN]
    # Same split as training, so the test set was never seen by the model.
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification report:\n", classification_report(y_test, y_pred))

    os.makedirs(RESULTS_DIR, exist_ok=True)
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap=plt.cm.Blues)
    plt.title("Confusion matrix")
    plt.savefig(os.path.join(RESULTS_DIR, "confusion_matrix.png"), bbox_inches="tight")
    plt.close()

    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.title("ROC curve")
    plt.savefig(os.path.join(RESULTS_DIR, "roc_curve.png"), bbox_inches="tight")
    plt.close()
    print(f"Plots saved to {RESULTS_DIR}")


if __name__ == "__main__":
    main()
