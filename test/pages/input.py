import streamlit as st

query = ''
def proc():
    query = st.cache.text_key
    st.write(st.cache.text_key)

st.text_area('enter text', on_change=proc, key='text_key')
query
