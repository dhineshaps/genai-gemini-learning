import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv() ##loading all the environment variables

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro-vision")  #for image - gemini pro

def get_gemini_response(input,image):

    if input != "":
        
          response = model.generate_content([input,image])
    else:
         
          response = model.generate_content(image)

    return response.text

st.set_page_config(page_title="The FET Image")

st.header("The FET Quest - Image Bot")

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