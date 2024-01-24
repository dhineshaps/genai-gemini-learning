from nsepython import *
import json 
import streamlit as st

n50 = nse_get_index_quote("nifty 50").get('last')
st.write(n50)