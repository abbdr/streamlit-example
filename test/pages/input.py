import streamlit as st

if 'input' not in st.session_state:
    st.session_state['input'] = 0
  
st.session_state['input'] = st.text_input('')
query = st.session_state['input']

if st.button('Save Filters'):
        st.session_state['input'] = query

if st.button('Clear page Filters'):
        st.session_state['input'] = 0 # or default value

'query : ',query
