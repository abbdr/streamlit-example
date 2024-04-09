import streamlit as st


@st.cache_data
def input():
    data = st.text_input('')
    return data
    
query = input()

if st.button('reset'):
    query = 0

'query : ',query
