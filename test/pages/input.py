import streamlit as st

input_user = st.text_input("Masukkan teks Anda di sini:")
if st.button("Simpan"):
    st.session_state['input_user'] = input_user
    st.success("Input berhasil disimpan!")

