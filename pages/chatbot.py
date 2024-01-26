import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ By The FET Quest<a style='display: block; text-align: center</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

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