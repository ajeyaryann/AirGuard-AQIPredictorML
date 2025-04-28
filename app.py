# app.py

import streamlit as st
import pickle
import pandas as pd
import gdown

import signup as signup_page
import login as login_page

file_id = '1rdTvIw7qMroBYYvqfEpKJFx2ot38ZmHa'
url = f'https://drive.google.com/uc?id = {file_id}'

output = 'air_quality_dataset.csv'
gdown.download(url, output, quiet=False)

df = pd.read_csv(output)

file_id = '18TLIGR6hMN7jpB33rRJPC6rJ35fs5slZ'
url = f'https://drive.google.com/uc?id = {file_id}'

users_output = 'users.csv'
gdown.download(url, output, quiet=False)

df = pd.read_csv(users_output)


# Load ML model
with open('models/air_quality_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Navigation
menu = st.sidebar.selectbox("Menu", ["Login", "Signup", "Predict AQI"])

if menu == "Signup":
    signup_page.signup()

elif menu == "Login":
    login_page.login()

elif menu == "Predict AQI":
    if st.session_state['logged_in']:
        st.title("AirGuard: Air Quality Predictor")

        # Updated input fields based on your features
        pm25 = st.number_input("PM2.5 (µg/m³)")
        pm10 = st.number_input("PM10 (µg/m³)")
        no = st.number_input("NO (ppb)")
        no2 = st.number_input("NO2 (ppb)")
        nox = st.number_input("NOx (ppb)")
        nh3 = st.number_input("NH3 (ppb)")
        co = st.number_input("CO (ppm)")
        so2 = st.number_input("SO2 (ppb)")
        o3 = st.number_input("O3 (ppb)")
        benzene = st.number_input("Benzene (ppb)")
        toluene = st.number_input("Toluene (ppb)")
        xylene = st.number_input("Xylene (ppb)")

        if st.button("Predict AQI"):
            # Features in correct order
            features = [[pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene]]
            prediction = model.predict(features)[0]
            st.success(f"Predicted AQI: {prediction:.2f}")

            # Health Advice
            if prediction <= 50:
                st.info("Air quality is Good. Enjoy your day!")
            elif prediction <= 100:
                st.warning("Air quality is Moderate. Sensitive groups take care.")
            else:
                st.error("Poor air quality. Minimize outdoor activities.")
    else:
        st.warning("Please login to access predictions.")
