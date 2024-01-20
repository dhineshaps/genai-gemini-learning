import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv() ##loading all the environment variables

#genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) #locally

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])


## FUNCTION TO LOAD Gemini Pro model and get response

model = genai.GenerativeModel("gemini-pro")  #for text - gemini pro

def get_gemini_response(question):

    response = model.generate_content(question)
   
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM |Application")

input = st.text_input("Input: ",key="input")

submit = st.button("Ask the question")

#when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)