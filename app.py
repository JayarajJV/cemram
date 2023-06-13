import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import time
background_image = "https://github.com/JVJayarah3/cementing-one/blob/main/images/pexels-monstera-7794441.jpg?raw=true"
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://github.com/JVJayarah3/cementing-one/blob/main/images/pexels-monstera-7794441.jpg?raw=true");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
    
    
add_bg_from_url() 
st.title("CEMENTING-ONE")
st.header("LOGIN CREDENTIALS")
with st.container():
    col2,col3=  st.columns(2)
    with col2:
        username = st.text_input("USERNAME")
with st.container():
    col2,col3 = st.columns(2)
    with col2:
        password = st.text_input('PASSWORD',type='password')
with st.container():
    col1,col2,col3 = st.columns(3)
    with col2:
        login_button = st.button('LOGIN')
if login_button:
    if username == "admin" and password == "abc@123":
        st.write('LOGGING IN .....')
        with st.spinner("LOADING..."):
            time.sleep(2)
        
        switch_page("project")

    else:
        st.write('INCORRECT USERNAME/PASSWORD')
