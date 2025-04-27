# pages/login.py

import streamlit as st
import pandas as pd

def login():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        try:
            users = pd.read_csv('users.csv')
            if username in users['Username'].values:
                user_pass = users[users['Username'] == username]['Password'].values[0]
                if password == user_pass:
                    st.success("Login Successful!")
                    st.session_state['logged_in'] = True
                else:
                    st.error("Incorrect Password.")
            else:
                st.error("Username not found.")
        except FileNotFoundError:
            st.error("No users found. Please Signup first.")