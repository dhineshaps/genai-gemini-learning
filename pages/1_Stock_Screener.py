import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plot
from urllib.request import urlopen, Request
import traceback
from PIL import Image


im = Image.open('the-fet-quest.jpg')
st.set_page_config(page_title="Stock_Data", page_icon = im,layout="wide")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
      new_title = '<p style="font-family:fantasy; color:#DAA520; font-size: 32px;">Stock Screener  📈</p>'
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
st.sidebar.image("the-fet-quest.jpg")
st.header(":violet[Know About Your Stock:]",anchor=False)

market_cap = 0.0
cmp = 0.0
PE = 0.0
BV = 0.0
sector = " "
industry = " "
PB_Ratio= 0.0

df = pd.read_csv('/mount/src/genai-gemini-learning/stock_list.csv')  #data is taken from NSE
col_one_list = df['Symbol'].tolist()

SCRIP = st.selectbox(
   "Enter the Stock Symbol",
   col_one_list,
   index=None,
   placeholder="ITC",
) 


def table_extraction(soup, section_id, class_name):
    section_extract = soup.find('section',{'id': section_id})
    table_extract = section_extract.find('table',{'class': class_name})

    col_headers = []
    for header in table_extract.find_all('th'):
        col_headers.append(  header.text or 'Type')

    table_df = pd.DataFrame(columns = col_headers)

    for row_element in table_extract.find_all('tr')[1:]:
            row_data = row_element.find_all('td')
            row = [tr.text.strip() for tr in row_data]
            length = len(table_df)
            table_df.loc[length] = row 

    table_df=table_df.replace('\+','',regex=True)
    table_df=table_df.replace('\%','',regex=True)
    table_df=table_df.replace('\,','',regex=True)        
    return table_df,col_headers

def promoter_holdings():
     promoter_holding,Headers = table_extraction(soup,'shareholding','data-table')
     promoter_holding.drop(promoter_holding.tail(1).index,inplace=True)
     sharehold_last_qtr = Headers[-1]
     print(sharehold_last_qtr)
     promoter_holding[sharehold_last_qtr] = promoter_holding[sharehold_last_qtr].astype(float)
     df1 = promoter_holding[['Type', sharehold_last_qtr]]    
     return df1,sharehold_last_qtr

def sales_nums():
     table_df,qtrs = table_extraction(soup,'quarters','data-table')
     df2 = table_df.loc[[0]]
     row_list = df2.loc[[0]].values.flatten().tolist()
     heads =qtrs[1:]
     num_row = [float(i) for i in row_list[1:]]   
     return num_row,qtrs

def eps_nums():
     table_df,qtrs = table_extraction(soup,'quarters','data-table')
     df3 = table_df.loc[[10]]
     print("I am here")
     row_list = df3.loc[[10]].values.flatten().tolist()
     heads =qtrs[1:]
     print(heads)   #print headers - quater
     num_row = [float(i) for i in row_list[1:]]
     print(num_row)
     return num_row, qtrs

def output_display(pr_hld,qtr,sales,qtrs,eps,qtrss):
    c1, c2, c3 = st.columns(3)
    with c1:
         st.write(f':orange[Current Market price -] {cmp} Rs')
         st.write(f':orange[Market Capitilization -] {market_cap} Cr')
    with c2:
        st.write(f':orange[P/E -] {PE}')
        st.write(f':orange[Book Value -] {BV}')
    with c3:
        st.write(f':orange[P/B ratio -] {PB_Ratio}')
        st.write(f':orange[Sector -] {sector.strip()}')
        #st.write(f'Industry : {industry.strip()}')
    c4, c5 = st.columns(2)

    with c4:
        st.write(':blue[Share Holding Pattern]')
        x = pr_hld['Type']
        y = pr_hld[qtr]
        fig, ax = plot.subplots(figsize=(12,3.5))
        ax.stem(x, y)
        plot.xlabel("Type of Shareholders")
        plot.ylabel("in %")
        st.pyplot(fig)
        st.info("Higher the Promoter Holding, Higher the Trust in the Company by Owners, however some exception are there" )
    with c5:        
        st.write(':blue[Quaterly Sales or Revenue of the company]')
        x1 = sales
        y1 = qtrs[1:]
        fig2, ax2= plot.subplots(figsize=(12,3.5))
        x1 =  qtrs[1:]
        y1 = sales
        ax2.stem(x1, y1)
        plot.xlabel("Quaters")
        plot.ylabel("Sales | Revenue in Rs. crores")
        st.pyplot(fig2)
        st.info("Increaing Sales or Revenue is Good Sign")

    c7, c8 = st.columns(2)
    
    with c7:
        st.write(':blue[Earning Per Share]')
        fig3, ax3= plot.subplots(figsize=(12,3.5))
        x2 =  qtrss[1:]
        y2 = eps
        ax3.stem(x2, y2)
        plot.xlabel("Quaters")
        plot.ylabel("EPS in Rs.")
        st.pyplot(fig3)
        st.info("Increaing in EPS is good sign")

if(SCRIP):
       link = f'https://www.screener.in/company/{SCRIP}'
       hdr = {'User-Agent':'Mozilla/5.0'}
       req = Request(link,headers=hdr)
try:
      page=urlopen(req)
      soup = BeautifulSoup(page)
      pr_hld,qtr= promoter_holdings()
      sales,qtrs = sales_nums()
      eps,qtrss= eps_nums()
      #print(pr_hld)
      #print("Quater is "+qtr)
      #print(sales)
      div_html = soup.find('div',{'class': 'company-ratios'})
      ul_html = div_html.find('ul',{'id': 'top-ratios'})
      for li in ul_html.find_all("li"):
         name_span = li.find('span',{'class':'name'})
         if 'Market Cap' in name_span.text: 
               num_span = li.find('span',{'class':'number'})
               num_span = num_span.text.replace(',', '')
               market_cap = float(num_span) if (num_span != '') else 0.0
         if ' Current Price' in name_span.text: 
               num_span = li.find('span',{'class':'number'})
               num_span = num_span.text.replace(',', '')
               cmp = float(num_span) if (num_span != '') else 0.0
         if ' Stock P/E' in name_span.text: 
               num_span = li.find('span',{'class':'number'})
               num_span = num_span.text.replace(',', '')
               PE = float(num_span) if (num_span != '') else 0.0
         if ' Book Value' in name_span.text: 
               num_span = li.find('span',{'class':'number'})
               num_span = num_span.text.replace(',', '')
               BV = float(num_span) if (num_span != '') else 0.0
      PB_Ratio = (round(cmp/BV,2))

      div_html1 = soup.find('div',{'class': 'flex flex-space-between'})
      ul_html1 = div_html1.find('p')
      for idx, x in enumerate (ul_html1):
        if(idx == 1):
            for i in x:
                sector = i
        if(idx == 5):
            for i in x:
                industry = i 
      output_display(pr_hld,qtr,sales,qtrs,eps,qtrss)
except Exception:
      traceback.print_exc()
      print(f'EXCEPTION THROWN: UNABLE TO FETCH DATA FOR {SCRIP}')

st.info("Watch out this space for more updates")