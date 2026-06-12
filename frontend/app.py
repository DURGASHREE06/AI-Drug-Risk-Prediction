import streamlit as st
import requests
import plotly.graph_objects as go
import sqlite3
import pandas as pd

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Drug Risk Classification",
    page_icon="🧠",
    layout="wide"
)

# ==========================
# LOAD CSS
# ==========================

try:
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ==========================
# HEADER
# ==========================

st.markdown("""
<div class='hero'>
<h1 class='main-title'>
🧠 AI Drug Risk Classification System
</h1>

<p class='subtitle'>
Machine Learning • Deep Learning • Explainable AI
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

menu = st.sidebar.radio(
    "📌 Navigation",
    [
        "Dashboard",
        "Predict",
        "History",
        "About"
    ]
)

# ==========================================================
# DASHBOARD PAGE
# ==========================================================

if menu == "Dashboard":

    st.title("📊 Project Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Model",
            "XGBoost"
        )

    with col2:
        st.metric(
            "Backend",
            "FastAPI"
        )

    with col3:
        st.metric(
            "Database",
            "SQLite"
        )

    with col4:
        st.metric(
            "Status",
            "Active"
        )

    st.markdown("---")

    st.subheader("🎯 Project Objective")

    st.info("""
This system predicts the likelihood of illicit drug usage using
Machine Learning, Deep Learning and Explainable AI techniques.

Features:

• Drug Risk Prediction

• FastAPI Backend

• SQLite Database Storage

• Explainable AI (SHAP)

• Streamlit Dashboard
""")

# ==========================================================
# PREDICTION PAGE
# ==========================================================

elif menu == "Predict":

    st.title("🤖 Drug Risk Prediction")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            value=0.0
        )

        nscore = st.number_input(
            "Nscore",
            value=0.0
        )

        escore = st.number_input(
            "Escore",
            value=0.0
        )

        oscore = st.number_input(
            "Oscore",
            value=0.0
        )

    with col2:

        ascore = st.number_input(
            "Ascore",
            value=0.0
        )

        cscore = st.number_input(
            "Cscore",
            value=0.0
        )

        impulsive = st.number_input(
            "Impulsive",
            value=0.0
        )

        ss = st.number_input(
            "SS",
            value=0.0
        )

    st.markdown("")

    if st.button("🚀 Predict Risk"):

        payload = {
            "Age": age,
            "Nscore": nscore,
            "Escore": escore,
            "Oscore": oscore,
            "Ascore": ascore,
            "Cscore": cscore,
            "Impulsive": impulsive,
            "SS": ss
        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload
            )

            result = response.json()

            prediction = result["prediction"]
            probability = result["risk_probability"]

            st.markdown("---")

            if prediction == 1:
                st.error("⚠️ HIGH RISK")
            else:
                st.success("✅ LOW RISK")

            st.metric(
                "Risk Probability",
                f"{probability * 100:.2f}%"
            )

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=probability * 100,
                    title={"text": "Drug Risk Score"},
                    gauge={
                        "axis": {"range": [0, 100]}
                    }
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        except Exception as e:
            st.error(f"API Error: {e}")

# ==========================================================
# HISTORY PAGE
# ==========================================================

elif menu == "History":

    st.title("📜 Prediction History")

    try:

        conn = sqlite3.connect(
            "../database/predictions.db"
        )

        df = pd.read_sql(
            "SELECT * FROM predictions ORDER BY id DESC",
            conn
        )

        st.dataframe(
            df,
            use_container_width=True,
            height=500
        )

        conn.close()

    except Exception as e:
        st.error(f"Database Error: {e}")

# ==========================================================
# ABOUT PAGE
# ==========================================================

elif menu == "About":

    st.title("ℹ️ About Project")

    st.markdown("""
## AI Drug Risk Classification System

### Technologies Used

✅ Python

✅ XGBoost

✅ Deep Learning (PyTorch)

✅ FastAPI

✅ Streamlit

✅ SQLite

✅ SHAP Explainability

---

### System Architecture

User

⬇

Streamlit Frontend

⬇

FastAPI Backend

⬇

XGBoost / Deep Learning Model

⬇

SQLite Database

---

### Key Features

• Drug Risk Prediction

• Explainable AI

• REST API Integration

• Prediction History

• Interactive Dashboard

• Database Storage
""")