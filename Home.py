import streamlit as st
from PIL import Image
im = Image.open('the-fet-quest.jpg')
st.set_page_config(page_title="Home", page_icon = im,layout="wide")

st.image("fet-quest-front-bluw.PNG")

st.header("The FET Quest")

st.write('Welcome to the blog')

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