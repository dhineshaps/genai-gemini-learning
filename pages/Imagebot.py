import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image

im = Image.open('the-fet-quest.jpg')
st.set_page_config(page_title="Chatbot", page_icon = im,layout="wide")
st.header("The FET Quest - Image Bot")


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
st.sidebar.image("the-fet-quest.jpg")
load_dotenv() ##loading all the environment variables

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro-vision")  #for image - gemini pro

def get_gemini_response(input,image):

    if input != "":
        
          response = model.generate_content([input,image])
    else:
         
          response = model.generate_content(image)

    return response.text

input = st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

#when submit is clicked

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is ")
    st.write(response)