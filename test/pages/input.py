import streamlit as st

st.session_state.query = st.chat_input('ketik query')
query = st.session_state.query
'query : ',query
