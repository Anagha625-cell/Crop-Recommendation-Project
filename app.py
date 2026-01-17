import streamlit as st
import joblib
import numpy as np

st.title("🌾 AI-Based Crop Recommendation")

model = joblib.load("model/crop_model.pkl")

st.header("Enter Soil & Weather Data")

N = st.number_input("Nitrogen (N)", min_value=0, max_value=200)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=200)
K = st.number_input("Potassium (K)", min_value=0, max_value=200)
temp = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0)
humid = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0)
rain = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0)

if st.button("Recommend Crop"):
    features = np.array([[N,P,K,temp,humid,ph,rain]])
    crop = model.predict(features)[0]
    st.success(f"🌾 Recommended Crop: {crop}")
