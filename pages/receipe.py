import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import numpy as np


total_slurry_needed = 52
pump_out = 0.084
displacement_fluid = 112.8
displacing_mud = 11
old_mud = 10
toc = 3937
tvd = 5167
fc = 5078
od = 5.5
csd = 5156
well_name = "BK#32"
date = "11-06-2023"
md = 5167
client = "xxxxx"
excess_cement = "cccc"
dead_vol = 2
#total_slurry_needed = st.session_state['total_slurry_need'] 
#pump_out = st.session_state['pump_out']
#displacement_fluid = st.session_state['displacement_fluid']
#displacing_mud = st.session_state['displacing_mud']
#old_mud = st.session_state['old_mud']
#toc = st.session_state['toc']
#tvd = st.session_state['tvd']
#fc = st.session_state['fc']
#od = st.session_state['od']
#csd = st.session_state['csd']
#excess_cement = st.session_state['excess_cement']
#client = st.session_state['client']
#well_name = st.session_state['well_name']
#date = st.session_state['date']
#dead_vol = st.session_state['dead_vol']

for key in st.session_state.keys():
  del st.session_state[key]

with st.container():
  st.title("CEMENTING - DETAILS")
  st.header("TOTAL VOLUME OF SLURRY NEEDED - "+str(total_slurry_needed))
  cement_den = st.number_input("CEMENT DENSITY (PPG) - ",min_value=1) 
  cementyld = st.number_input("CEMENT YIELD (CF-SK) - ",min_value=0.1)  
  cement_sk = (total_slurry_needed/(cementyld*0.178))         
  preflush = st.number_input("PRE-FLUSH VOL (bbls) - ",min_value=1)
  woc = st.number_input("PLANNED WOC (HRS)- ",min_value=1)
  st.header("CEMENT-RECEIPE")
  col1,col2,col3 = st.columns(3)
  with col1:
    name1 = st.text_input("RECEIPE NAME - ",key=1)
    name2 = st.text_input("RECEIPE NAME - ",key=2)
    name3 = st.text_input("RECEIPE NAME - ",key=3)
    name4 = st.text_input("RECEIPE NAME - ",key=4)
    name5 = st.text_input("RECEIPE NAME - ",key=5)
            
  with col2:
    bowc1 = st.number_input("BWOC PERCENTAGE - ",key=6)
    bowc2 = st.number_input("BWOC PERCENTAGE - ",key=7)
    bowc3 = st.number_input("BWOC PERCENTAGE - ",key=8)
    bowc4 = st.number_input("BWOC PERCENTAGE - ",key=9)
    bowc5 = st.number_input("BWOC PERCENTAGE - ",key=10)
         
  with col3:
    galsk1 = st.number_input("GAL/SACK - ",key=11)
    galsk2 = st.number_input("GAL/SACK - ",key=12)
    galsk3 = st.number_input("GAL/SACK - ",key=13)
    galsk4 = st.number_input("GAL/SACK - ",key=14)
    galsk5 = st.number_input("GAL/SACK - ",key=15)

df = pd.DataFrame()
df['receipe_name'] = [name1,name2,name3,name4,name5]
df['bwoc'] = [bowc1,bowc2,bowc3,bowc4,bowc5]
df['galsk'] = [galsk1,galsk2,galsk3,galsk4,galsk5]
try:           
  df['output-1'] = ((df['bwoc']/100)*94*cement_sk)
except:
  pass         
df['output-2'] = df['galsk']*cement_sk          
df['unit-1'] = np.where(df['output-1'] != 0 ,"Lbs","")     
df['unit-2'] = np.where(df['output-2'] != 0 ,"Gal","") 
df['output'] = df['output-1'] + df['output-2']           
df['output_s'] = df['output'].astype(str)
df['unit'] =   df['unit-1'] + df['unit-2'] 
df['final'] = df['receipe_name']+"-"+df['output_s']+" "+df['unit']
df1 = pd.DataFrame()
df1['receipe_name'] = df['receipe_name']
df1['output'] = df['output']
df1['unit'] = df['unit']

bt0 = st.button("SUBMIT")
bump_p =  ((toc*old_mud*0.052)+((tvd-toc)*cement_den*0.052)-((displacing_mud*fc*0.052)+((tvd-fc)*0.052*cement_den))+500)
if bt0:
  if 'total_slurry_need' not in st.session_state:
    st.session_state['total_slurry_need'] = total_slurry_needed
  if 'pump_out' not in st.session_state:
      st.session_state['pump_out'] = pump_out
  if 'displacement_fluid' not in st.session_state:
      st.session_state['displacement_fluid'] = displacement_fluid
  if 'displacing_mud' not in st.session_state:
      st.session_state['displacing_mud'] = displacing_mud
  if 'old_mud' not in st.session_state:
      st.session_state['old_mud'] = old_mud
  if 'toc' not in st.session_state:
      st.session_state['toc'] = toc
  if 'tvd' not in st.session_state:
      st.session_state['tvd'] = tvd
  if 'fc' not in st.session_state:
      st.session_state['fc'] = fc
  if 'od' not in st.session_state:
      st.session_state['od'] = od
  if 'csd' not in st.session_state:
      st.session_state['csd'] = csd
  if 'client' not in st.session_state:
      st.session_state['client'] = client
  if 'well_name' not in st.session_state:
      st.session_state['well_name'] = well_name
  if 'date' not in st.session_state:
      st.session_state['date'] = date   
  if 'excess_cement' not in st.session_state:
      st.session_state['excess_cement'] = excess_cement
  if 'dead_vol' not in st.session_state:
      st.session_state['dead_vol'] = dead_vol
  if 'md' not in st.session_state:
      st.session_state['md'] = md
  if 'bump_p' not in st.session_state: 
      st.session_state['bump_p'] = bump_p
  if 'cement_den' not in st.session_state: 
      st.session_state['cement_den'] = cement_den
  if 'cement_sk' not in st.session_state: 
      st.session_state['cement_sk'] = cement_sk
  if 'preflush' not in st.session_state: 
      st.session_state['preflush'] = preflush   
  if 'woc' not in st.session_state: 
      st.session_state['woc']  = woc
  if 'df' not in st.session_state:
      st.session_state.df=df1
  switch_page("output")
 
