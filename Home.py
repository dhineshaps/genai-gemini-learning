import streamlit as st
from PIL import Image
im = Image.open('the-fet-quest.jpg')
st.set_page_config(page_title="Home", page_icon = im,layout="wide")

#st.sidebar.image("the-fet-quest.jpg",use_column_width=True)

left_co, cent_co,last_co = st.columns(3)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.title("The FET Quest")

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


st.write('The FET Quest is committed to simplifying Finance and creating value for our esteemed clients in making their investment decisions.')

st.write("You don't have to be brilliant, only a little bit wiser than the other guys, on average, for a long, long, time.")

st.write('Investment instruments continue to bewilder individuals with their financial jargon, we are envisioned to untangle it by Integrating it with technology and making life simple.')

st.write('we are working on services that include financial Valuation of the equity markets and AI-powered Annual Report Analyser of the company which saves huge time in evaluating the cos.')

st.write('Many more yet to come - Passionate to keep things Simple.')