import streamlit as st

with 'query' not in st.session_state:
  st.session_state.query = st.chat_input('ketik query')
query = st.session_state.query
'query : ',query
