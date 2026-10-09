# Phishing Website Detection with Machine Learning

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Random%20Forest-F7931E?logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-data-150458?logo=pandas&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Topic](https://img.shields.io/badge/Topic-AI%20for%20Cybersecurity-6242ff)

A machine-learning classifier that flags **phishing websites** from 30 URL, domain and page features, with a small **Tkinter** desktop interface to test a website's feature profile.

> Personal project at the intersection of **AI and cybersecurity**, 2025. It applies the supervised learning I studied in the Master in AI & Cybersecurity to a real security problem.

## How it works

```text
UCI Phishing Websites (11k sites, 30 features)
        │  data/download_dataset.py
        ▼
phishing_dataset.csv ──► data_preprocessing.py ──► preprocessed_data.csv
                                                        │
                                   model_training.py (Random Forest, stratified 80/20 split)
                                                        ▼
                                                models/phishing_model.pkl
                                     ┌──────────────────┴──────────────────┐
                          model_evaluation.py                          gui.py
            accuracy, confusion matrix, classification          enter 30 features,
            report, ROC curve → results/                         get a prediction
```

**Dataset:** [UCI Phishing Websites](https://archive.ics.uci.edu/dataset/327/phishing+websites) (Mohammad, Thabtah & McCluskey). Each feature (e.g. `having_IP_Address`, `URL_Length`, `SSLfinal_State`, `age_of_domain`) is encoded as `1` (legitimate), `0` (suspicious) or `-1` (phishing). The label `Result` is `-1` for phishing and `1` for legitimate.

## Tech stack

Python · pandas · scikit-learn (`RandomForestClassifier`, `train_test_split`, metrics displays) · joblib · matplotlib · Tkinter · ucimlrepo

## Installation

```bash
git clone https://github.com/L3wina-debug/phishing-detection-ml.git
cd phishing-detection-ml
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python data/download_dataset.py        # 1. download the dataset → data/phishing_dataset.csv
cd scripts
python data_preprocessing.py           # 2. check missing values, encode → preprocessed_data.csv
python model_training.py               # 3. train the Random Forest → models/phishing_model.pkl
python model_evaluation.py             # 4. metrics in the console, plots in results/
python gui.py                          # 5. desktop interface
```

Use the model from Python:

```python
from predict_phishing import feature_names, predict_phishing

features = {name: 1 for name in feature_names()}   # every feature "legitimate"
features["having_IP_Address"] = -1                  # the URL uses a raw IP address
print(predict_phishing(features))                   # "Phishing" or "Legitimate"
```

## Results

Run `model_evaluation.py` to print the accuracy, confusion matrix and classification report, and to save `results/confusion_matrix.png` and `results/roc_curve.png`. Results are not committed, so the numbers you see are the ones your run produces.

## Known limitations

- The GUI takes the 30 encoded features, not a raw URL. A feature extractor (URL parsing, WHOIS age, SSL check) would be the next step.
- The dataset dates from 2012–2015. Modern phishing techniques may need fresher data.

## What I learned

- **Framing a security problem as classification:** choosing features that reflect attacker behavior (IP in URL, short domain age, missing SSL) and checking class balance.
- **Building a reproducible ML pipeline:** separate download, preprocessing, training and evaluation steps with shared configuration and a fixed random seed.
- **Evaluating honestly:** keeping a held-out test set, reading the confusion matrix rather than accuracy alone, and plotting the ROC curve.
- **Shipping a usable tool:** saving the model with joblib and wrapping it in a Tkinter interface.

## Author

**Mahmoud El Aaouadi**, Master's student in AI & Cybersecurity. [Portfolio](https://mahmoud-elaaouadi.netlify.app) · [LinkedIn](https://www.linkedin.com/in/mahmoud-elaaouadi-7b3087416)

## License

[MIT](LICENSE)
