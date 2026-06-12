The Drug Risk Prediction System is a machine learning-based web application designed to predict the risk level associated with drug usage based on psychological and personality traits.
It helps in early identification of potential drug risk behavior using data-driven insights.

The system is built using a trained ML model and deployed via an API using FastAPI and can be integrated with a frontend like Streamlit or web dashboards.

🎯 Problem Statement

Drug abuse risk detection is often subjective and dependent on manual assessment.
This project aims to:

Automate risk prediction
Reduce human bias
Assist early intervention strategies
🧠 Machine Learning Approach
Model: Trained classification model (e.g., Random Forest / Logistic Regression / SVM)
Library: scikit-learn
Input Features:
Age
Nscore (Neuroticism)
Escore (Extraversion)
Oscore (Openness)
Ascore (Agreeableness)
Cscore (Conscientiousness)
Output:
Risk Category (Low / Medium / High)

🏗️ Project Architecture
User Input
   ↓
Frontend (Streamlit / UI)
   ↓
FastAPI Backend
   ↓
ML Model (.pkl file)
   ↓
Prediction Output
   ↓
Result Display

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/Drug-Risk-Prediction.git
cd Drug-Risk-Prediction
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
🚀 Run the Project
▶️ Start FastAPI Backend
cd backend
uvicorn main:app --reload
▶️ Run Streamlit Frontend (if used)
cd frontend
streamlit run app.py
📊 Example API Endpoint
POST /predict
Input JSON:
{
  "Age": 25,
  "Nscore": 0.5,
  "Escore": 0.2,
  "Oscore": 0.7,
  "Ascore": 0.4,
  "Cscore": 0.6
}
Output:
{
  "risk_level": "High"
}
🧪 Features
ML-based risk prediction
REST API using FastAPI
Easy frontend integration
Scalable architecture
Real-time predictions
📌 Future Improvements
Add deep learning model
Improve dataset size and diversity
Deploy on cloud (AWS / Render / Azure)
Add user authentication
Improve UI dashboard
👨‍💻 Tech Stack
Python
FastAPI
Streamlit
scikit-learn
Pandas, NumPy
Joblib
