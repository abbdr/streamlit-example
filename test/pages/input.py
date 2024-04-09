import streamlit as st

query = ''
def callback(string):
    query = string

input_text = st.text_area("Enter a text", key="input_text", on_change=callback)

'query : ',query
