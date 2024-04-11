import streamlit as st
import pandas as pd

if 'dataku' in st.session_state:
  clean_data = st.session_state['dataku']
  clean_data

