import streamlit as st
import numpy as np
import pandas as pd

## Title of Application
st.title("Hello Streamlit")

## Display a simple text 
st.write("This is a simple text")

## Create a simple dataframe 

df = pd.DataFrame({
    'first column': [1, 2, 3, 4, 5],
    'second column': [10, 20, 30, 40, 50]
})

st.write("Here is the DataFrame")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)