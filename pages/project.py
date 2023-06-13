import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
logo = "https://github.com/JVJayarah3/cementing-one/blob/main/images/kirilogo.png?raw=true"
col1,col2 = st.columns([5,2])
with col1:
  st.header("CEMENTING-ONE")
with col2:
  st.image(logo)




  
for key in st.session_state.keys():
  del st.session_state[key]
with st.container():
  st.title("PROJECT-DETAILS")
  well_name = st.text_input("ENTER THE WELL NAME - ")
  date = st.date_input("SELECT DATE",)
  client = st.text_input("CLIENT NAME")
  
  
with st.container():
  st.title("WELL-DETAILS")
  tvd = st.number_input("ENTER THE TVD (ft)",)
  md = st.number_input("ENTER THE MD  (ft)",)
  csd = st.number_input("ENTER THE SHOE DEPTH  (ft)",)
  fc = st.number_input("ENTER THE F/C DEPTH  (ft)",)
  toc = st.number_input("ENTER THE TOC  (ft)",)
  excess_cement = st.number_input("Excess Volume Pecentage (normally 20%)",)
  holesize = st.number_input("ENTER THE AVERAGE HOLE SIZE (IN)",)
  old_mud = st.number_input("ENTER THE OLD MUD DENSITY (PPG)",)
  displacing_mud =  st.number_input("ENTER THE DISPLACING MUD DENSITY (PPG)",)
  dead_vol = st.number_input("ENTER THE DEAD VOLUME (BBLS) - ")
st.write("----------------------------------------------------")

with st.container():
  st.title("CASING - DETAILS")
  od = st.number_input("ENTER THE OD OF CASING",)
  id = st.number_input("ENTER THE ID OF CASING",)
  pump_out = st.number_input("PUMP OUTPUT (BBLS/STK)",)
casing_cap = ((id**2)/1029.4)
shoetrack = casing_cap*(csd-fc)
rathole = ((od**2)/1029.4)*(md-csd)
annulus_vol = (((holesize**2)-(od**2))/1029.4)*((md-toc)-(md-csd))
total_slurry_needed = (excess_cement/100)*(shoetrack+rathole+annulus_vol)+((shoetrack+rathole+annulus_vol)+dead_vol)
displacement_fluid = casing_cap*fc
sub1 = st.button("SUBMIT")
if sub1:
  st.write("total_slurry_needed"+str(total_slurry_needed))
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
  switch_page("receipe")
st.write("----------------------------------------------------")
