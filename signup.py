# pages/signup.py

import streamlit as st
import pandas as pd

def signup():
    st.title("Signup Page")
    
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Signup"):
        if password == confirm_password:
            # Save user
            user_data = pd.DataFrame([[username, password]], columns=["Username", "Password"])
            
            try:
                existing_data = pd.read_csv('users.csv')
                updated_data = pd.concat([existing_data, user_data])
                updated_data.to_csv('users.csv', index=False)
            except FileNotFoundError:
                user_data.to_csv('users.csv', index=False)
            
            st.success("Account created successfully! Please login now.")
        else:
            st.error("Passwords do not match!")