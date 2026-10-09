"""Download the UCI Phishing Websites dataset (id 327) and save it as a CSV.

The dataset has 30 URL/domain/HTML features encoded as -1, 0 or 1 and a
`Result` column: -1 = phishing, 1 = legitimate.
"""
import os

import pandas as pd
from ucimlrepo import fetch_ucirepo

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(DATA_DIR, "phishing_dataset.csv")


def main() -> None:
    dataset = fetch_ucirepo(id=327)
    features = dataset.data.features
    target = dataset.data.targets.rename(columns=lambda _: "Result")
    df = pd.concat([features, target], axis=1)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} rows x {df.shape[1]} columns to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
