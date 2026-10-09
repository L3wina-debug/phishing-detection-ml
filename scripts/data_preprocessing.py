"""Load the raw dataset, check missing values, encode categorical columns."""
import os

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from config import PREPROCESSED_DATA_PATH, RAW_DATA_PATH


def main() -> None:
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(
            f"File not found: {RAW_DATA_PATH}. Run `python data/download_dataset.py` first."
        )

    data = pd.read_csv(RAW_DATA_PATH)
    print(data.head())
    print("Missing values per column:\n", data.isnull().sum())

    # The UCI features are already numeric (-1/0/1); this keeps the step safe
    # if a text column is ever added.
    encoder = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == "object":
            data[column] = encoder.fit_transform(data[column])

    data.to_csv(PREPROCESSED_DATA_PATH, index=False)
    print(f"Preprocessed data saved to: {PREPROCESSED_DATA_PATH}")


if __name__ == "__main__":
    main()
