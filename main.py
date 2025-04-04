import streamlit as st

st.title("Registration Form")

name = st.text_input("Enter Your Name:")
age = st.text_input("Enter Your Age:")
college_name = st.text_input("Your College Name:")
date = st.date_input("Enter the Date:")

if st.button("Submit"):
    
    st.success("Registration Successful!")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("College Name:", college_name)
    st.write("Date:", date)
