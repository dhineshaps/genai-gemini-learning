from nsepython import *
import json 
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

st.set_page_config(page_title="The FET Image")

st.header("The FET Quest - Image Bot")


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



n50 = nse_get_index_quote("nifty 50").get('last')
n50change = nse_get_index_quote("nifty 50").get('percChange') + "%"

nbank = nse_get_index_quote("NIFTY BANK").get('last')
nbankchange = nse_get_index_quote("NIFTY BANK").get('percChange') + "%"

nIT = nse_get_index_quote("NIFTY IT").get('last')
nITchange = nse_get_index_quote("NIFTY IT").get('percChange') + "%"
col1,col2,col3= st.columns(3)

col1.metric(label="Nitfy 50", value=n50,delta=n50change)
col2.metric(label="Nitfy Bank", value=nbank,delta=nbankchange)
col3.metric(label="Nitfy IT", value=nIT,delta=nITchange)

colnames = ['Investment Scheme', 'Interest Rate','Benefits', 'Lock-in Period', 'Minimum Investment','Maximum Investment']

df = pd.read_csv('/mount/src/genai-gemini-learning/investment_int_rates.csv', names=colnames)

AgGrid(df)