import os
import streamlit as st

from chatbot import getresponse

st.set_page_config(
    page_title="LlamaAssist 📋",
    page_icon="",
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
        <p style="font-size: 24px;">LlamaAssist 📋</p>
    </div>
""", 
        unsafe_allow_html=True
        )


input_text = input_text = st.text_area(
    "Write About Your Topic", 
    value="", 
    height=200,  # You can adjust the height if you like
    max_chars=None, 
    key=None, 
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
    "Difficulty Level?",
    ("Student", "Teacher", "Content Writer"), index=0)

submit_button = st.button("Start Generate", help ="Press Submit Button to Start")

if submit_button:
    st.write(getresponse(input_text, no_of_words, user_type))

