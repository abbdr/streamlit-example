import streamlit as st

def proc():
    st.write(st.session_state.text_key)

st.text_area('enter text', on_change=proc, key='text_key')
