from nsepython import *
import json 
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

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