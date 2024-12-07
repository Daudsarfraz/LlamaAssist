import os
import streamlit as st

from chatbot import getresponse

st.set_page_config(
    page_title="LlamaAssist",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# st.header(
#     "LlamaAssist", 
#     anchor=None, 
#     help=None, 
#     divider=False
#       )


import streamlit as st

# Image and text alignment (side-by-side)
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="image.png" style="width:150px; margin-right: 10px;">
        <p style="font-size: 24px;">LlamaAssist</p>
    </div>
""", unsafe_allow_html=True)


input_text = st.text_input(
              "Specify your topic", 
              value="", 
              max_chars=None, 
              key=None, 
              type="default", 
              label_visibility="visible"
              )

column1, column2 = st.columns([10, 10])

with column1:
    no_of_words = st.text_input("Enter length og blog", 
              value="", 
              max_chars=None, 
              key=None, 
              type="default", 
              label_visibility="visible"
              )
    
with column2:
    user_type = st.selectbox(
    "How are you?",
    ("Student", "Teacher", "Content Writer"), index=0)

submit_button = st.button("Start Generate", help ="Press Submit Button to Start Generation")

if submit_button:
    st.write(getresponse(input_text, no_of_words, user_type))

