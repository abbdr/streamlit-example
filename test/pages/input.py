import streamlit as st

if 'input' not in st.session_state:
    st.session_state['input'] = 0
  

query = st.text_input('')
st.session_state['input'] = query
query = st.session_state['input']

'query : ',query
