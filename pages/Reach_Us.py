import streamlit as st
from PIL import Image
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.buy_me_a_coffee import button

im = Image.open('the-fet-quest.jpg')
st.set_page_config(page_title="Home", page_icon = im,layout="wide")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
#    st.title("The FET Quest")
      new_title = '<p style="font-family:fantasy; color:#DAA520; font-size: 42px;">The FET Quest</p>'
      st.markdown(new_title, unsafe_allow_html=True)

left_co1, cent_co1,last_co1= st.columns(3)
with cent_co1:
#    st.title("The FET Quest")
      new_title = '<h6 style="font-family:cursive; color:#DAA520; font-size: 15px;">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Embracing the Financial Literacy</h6>'
      st.markdown(new_title, unsafe_allow_html=True)

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
st.write("Thanks for Visting us, we are happy to hear from you !")

st.info("This is model site, we are not recommending any investment instrments or stocks , please do your own research based on the data available here")

new_title = '<p style="font-family:fantasy; color:#DAA520; font-size: 22px;">FAQs</p>'
st.markdown(new_title, unsafe_allow_html=True)

with st.expander(":mailbox: Reach Us"):
      st.write("Feel Free to write to us :e-mail: daps.investments@gmail.com")
with st.expander("Describe About The FET Quest ?"):
      st.write("The FET Quest is the Educational and Technology subsidiary of :green[DAPS Investments].")
with st.expander("Whether The FET Quest is Registered ?"):
      st.write("We are genuine however this is a Model Technical Portfolio Site, we are not registered under any Sections Indian Companies Act for now.")
with st.expander("What Benefits The FET Quest can Provide ?"):
      st.write("We offer the First layer of advisory and solutions to your doubts on Financial doubts in Primary and Secondary Markets, Bonds and other Investment Instruments.")

button(username="fake-username", text="blog",floating=False, width=221)