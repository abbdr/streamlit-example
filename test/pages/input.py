import streamlit as st

query = ''
def proc():
    query = st.session_state.text_key
    # st.write(st.session_state.text_key)

st.text_area('enter text', on_change=proc, key='text_key')
query
