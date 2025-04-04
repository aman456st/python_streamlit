import streamlit as st

st.title("Registration Form")

name = st.text_input("Enter Your Name:")
age = st.text_input("Enter Your Age:")
college_name = st.text_input("Your College Name:")
date = st.date_input("Enter the Date:")

st.button("Submit")
