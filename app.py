import streamlit as st
st.title("MY FIRST CLOUD APP")
st.write("Streamlit cloud application ")
st.write("Hello")
number1 = st.slider("Pick a number", 0, 100)
number2 = st.slider("Pick another number", 0, 100)
x = number1 + number2
y = number1 - number2
st.title("SUM :",x)
st.title("DIFFERENCE :",y)
