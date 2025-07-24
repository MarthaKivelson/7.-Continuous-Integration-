import streamlit as st

st.title("Not so Simple calculator")
st.write("Enter a number")

n = st.number_input("Enter an integer")

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"Square of {n} is {square}")
st.write(f"cube of {n} is {cube}")
st.write(f"Fifth power of {n} is {fifth_power}")