import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# CSS Styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #74ebd5, #ACB6E5);
        padding: 20px;
        border-radius: 10px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subheader
st.title("📧 Spam Detection Web App")
st.subheader("🔍 Check if a message is Spam or Not Spam instantly")

# Sidebar
st.sidebar.title("About")
st.sidebar.info("""
This app uses Logistic Regression trained on SMS spam data to classify messages.
""")

# Input area
user_input = st.text_area("✏️ Enter your message here:")

# Prediction
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to check.")
    else:
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)
        result = "🚫 Spam" if prediction[0] == 0 else "✅ Not Spam"
        st.success(f"Prediction: **{result}**")

# Footer
st.markdown("""
<hr>
<p style='text-align: center;'>
    Developed by <b>Budhdev Kumar</b> | 🌐 <a href='https://https://github.com/budhdev04'>GitHub</a>
</p>
""", unsafe_allow_html=True)
