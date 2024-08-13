import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name = st.text_input("Enter Your Name:")
if name:
    st.write(f"Hello My Name is, {name}.")

age = st.slider("Select Your Age:", 0,100,50)
st.write(f"Your Age is {age}.")

options = ["Python", "Java", "C++", "Javascript"]
choice = st.selectbox("Choose Your Favorite Language:", options)
st.write(f"You Selected {choice}.")

data = {
    "Name":["John", "Jane", "Jake", "Jill"],
    "Age": [28, 25, 35,40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV File", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

st.link_button("Udemy", "https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/lecture/44450096#content")
