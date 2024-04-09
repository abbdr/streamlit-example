import streamlit as st

if 'input' not in st.session_state:
    st.session_state['input'] = 0
  
st.session_state['input'] = st.text_input('')
query = st.session_state['input']

'query : ',query
