import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

from PIL import Image
im = Image.open('the-fet-quest.jpg')
st.set_page_config(page_title="Chatbot", page_icon = im,layout="wide")

st.header("Chatbot")

footer="""<style>
#MainMenu {visibility: hidden; }
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

input = st.text_input("Input: ",key="input")

submit = st.button("Ask the question")

#when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)