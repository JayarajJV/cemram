import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import numpy as np


total_slurry_needed = st.session_state['total_slurry_need'] 
pump_out = st.session_state['pump_out']
displacement_fluid = st.session_state['displacement_fluid']
displacing_mud = st.session_state['displacing_mud']
old_mud = st.session_state['old_mud']
toc = st.session_state['toc']
tvd = st.session_state['tvd']
fc = st.session_state['fc']
od = st.session_state['od']
csd = st.session_state['csd']
excess_cement = st.session_state['excess_cement']
client = st.session_state['client']
well_name = st.session_state['well_name']
date = st.session_state['date']
dead_vol = st.session_state['dead_vol']
bump_p = st.session_state['bump_p']
cement_den = st.session_state['cement_den']
cement_sk = st.session_state['cement_sk']
preflush = st.session_state['preflush']
woc = st.session_state['woc']
md = st.session_state['md']
df = st.session_state['df']



st.title(str(well_name) + " - "+ str(od)+"INCH CEMENTING PROGRAMME")
st.header("OBJECTIVE : TO CEMENT "+str(od)+" INCH CASING/LINER")
st.write("DATE :"+str(date))
#st.write("WELL DEPTH - "+str(tvd)+" FT TVD /"+str(md)+" FT MD")
st.write("SHOE @ "+str(csd)+" FT "+"FLOAT COLLAR @ "+str(fc)+" FT")
st.header("PLAN")
st.write("PREPARE CEMENTING HEAD WITH PLUGS AND MAKE UP FLOWLINES")
st.write("PRESSURE TEST THE LINES")
st.write("PREPARE SLURRY AS PER RECEPIE AND PUMP - WOC.")
st.header("CARRYOUT OPERATIONS AS PER CEMENTING PROGRAM")
st.write("LOWER "+str(od)+" CASING AND LAND SHOE @ "+str(csd)+"FT AND F/C @ "+str(fc)+"FT")
st.write("M/UP CIRCULATING HEAD AND CIRCULATE AND CONDITION MUD PRIOR TO "+ str(od) +" CASING CEMENT JOB") 
st.write("CARRY OUT PRE-JOB SAFETY MEETINGS.")
st.write("PRESSURE TEST CEMENTING LINES @500 AND 2000 PSI")
st.write("PRE MIX CEMENT AS PER RECEIPE AND PREPARE "+str(total_slurry_needed)+" OF CEMENT SLURRY ")
st.dataframe(df)
preflush_stk = preflush/pump_out
st.write("PUMP "+str(preflush)+" OF PRE FLUSH THROUGH RIG PUMP. "+"STROKES - "+str(preflush_stk))
st.write("DROP BOTTOM PLUG.")
st.write("MIX AND PUMP "+str(total_slurry_needed)+" OF "+str(cement_den)+" PPG SLURRY BY CEMENTING UNIT.")          
st.write("DROP TOP PLUG")
displace_stk = displacement_fluid/pump_out
st.write("DISPLACE CEMENT WITH "+str(displacement_fluid)+" BBLS ("+str(displace_stk)+" STK) OF MUD TILL PLUG BUMPS. (BUMPING PRESSUE @ "+str(bump_p)+". PRESSURISE PLUG FURTHER TO 500 PSI)")
st.write("BLEED OFF PRESSURE AND CHECK FOR BPV HOLDING")          
st.write("WOC FOR "+str(woc)+" HRS TILL THE SURFACE CEMENT SETS  test ")
