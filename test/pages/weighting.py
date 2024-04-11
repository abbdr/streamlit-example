import streamlit as st
import pandas as pd

if 'input_user' in st.session_state:
  from pages.training import data
  
  data

