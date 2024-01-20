import streamlit as st

st.set_page_config(layout="wide")

st.set_page_config(page_title="Gemini AI")

st.header("The FET Quest")

st.write('Welcome to the blog')

with st.sidebar:
    st.title("Menu")
    #pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)