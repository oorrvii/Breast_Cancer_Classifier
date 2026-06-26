# 🎗️ Breast Cancer Tumor Classifier

A machine learning web app that classifies breast tumors as **Benign** or **Malignant** based on cytology features from a Fine Needle Aspirate (FNA).

🔗 **Live Demo:** [breastcancerclassifier-z2j9ti8kzusqgtgxvqqd8f.streamlit.app](https://breastcancerclassifier-z2j9ti8kzusqgtgxvqqd8f.streamlit.app/)

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Algorithm | Logistic Regression |
| Accuracy | 96.70% |
| Standard Deviation | ± 1.97% |
| Validation | 10-Fold Cross Validation |

---

## 🔬 Features Used

The model uses 9 cytology features extracted from FNA samples:

1. Clump Thickness
2. Uniformity of Cell Size
3. Uniformity of Cell Shape
4. Marginal Adhesion
5. Single Epithelial Cell Size
6. Bare Nuclei
7. Bland Chromatin
8. Normal Nucleoli
9. Mitoses

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn** — Logistic Regression, Cross Validation
- **Streamlit** — Web app deployment
- **NumPy / Pandas** — Data handling
- **Pickle** — Model serialization

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/breast-cancer-classifier.git
cd breast-cancer-classifier

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📁 Project Structure

```
breast-cancer-classifier/
├── app.py               # Streamlit web app
├── classifier.pkl       # Trained Logistic Regression model
├── requirements.txt     # Dependencies
└── README.md
```

---

## 📌 How It Works

1. User inputs 9 tumor feature values via sliders
2. Features are passed to the trained Logistic Regression model
3. Model predicts **Benign (2)** or **Malignant (4)**
4. Result is displayed with a color-coded card

---

## ⚠️ Disclaimer

This tool is built for **educational purposes only** and is not a substitute for professional medical diagnosis. Always consult a qualified healthcare provider.

---

## 👩‍💻 Author

Built by **Oorvi** as part of an ML learning journey.
