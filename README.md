# 📧 Spam Detection Web App

![Spam Detection](https://img.shields.io/badge/Streamlit-Deployed-brightgreen) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Project Overview

This is a **Spam Detection Web Application** built with **Python**, **scikit-learn**, and **Streamlit**. It classifies messages as **Spam** or **Not Spam** using a **Logistic Regression model** trained on SMS data with TfidfVectorizer for feature extraction.

---

## ✨ **Features**

- 🔍 Real-time spam detection for user input
- ✅ Clean, interactive, and attractive Streamlit UI
- 📊 Uses TfidfVectorizer for text feature extraction
- 🤖 Logistic Regression model for classification
- 🌐 Deployed on Streamlit Cloud for public access

---

## 🛠️ **Technologies Used**

- Python
- scikit-learn
- pandas
- Streamlit
- pickle (for model serialization)

---

## 📂 **Project Structure**

├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md


---


---

## 💻 **Setup Instructions**

Follow these steps to run the app locally:

1. **Clone the repository**

-bash

git clone https://github.com/budhdev04/spam-detection-app.git

cd spam-detection-app

2. **Install dependencies**

pip install -r requirements.txt


3. **Run the Streamlit app**

streamlit run app.py

4. The app will open at http://localhost:8501 in your browser.
