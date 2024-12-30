import streamlit as st

# Adding a title
st.title('Hello, Streamlit!')

# Adding some text
st.write("Welcome to Streamlit. This is an example app.")

# You can add interactive widgets
number = st.slider('Pick a number', 0, 100)
st.write(f'You selected {number}')
