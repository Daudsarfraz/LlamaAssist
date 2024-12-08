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


# Image and text alignment (side-by-side)
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center;">
        <p style="font-size: 24px;">LlamaAssist 📋</p>
    </div>
""", 
        unsafe_allow_html=True
        )

# Initialize session state variables if they don't exist
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "no_of_words" not in st.session_state:
    st.session_state.no_of_words = ""
if "user_type" not in st.session_state:
    st.session_state.user_type = "Beginner"

# Input text box
st.session_state.input_text = st.text_area(
    "Write About Your Topic", 
    value=st.session_state.input_text,  # Store the input in session state
    height=150,  # Adjust the height if needed
    max_chars=None, 
    key="input_text", 
    label_visibility="visible"
)

# Columns for input length and difficulty level
column1, column2 = st.columns([10, 10])

with column1:
    st.session_state.no_of_words = st.text_input(
        "Enter length of Desired Output:", 
        value=st.session_state.no_of_words,  # Store in session state
        max_chars=None, 
        key="no_of_words", 
        type="default", 
        label_visibility="visible"
    )

with column2:
    st.session_state.user_type = st.selectbox(
        "Difficulty Level?",
        ("Beginner", "Intermediate", "Expert"), 
        index=("Beginner", "Intermediate", "Expert").index(st.session_state.user_type)  # Keep the default state
    )

# Submit button
submit_button = st.button("Start", help="Press Submit Button to Start")

# Handle button click
if submit_button:
    if not st.session_state.input_text:
        st.error("Please provide input text.")
    elif not st.session_state.no_of_words:
        st.error("Please provide the desired output length.")
    else:
        # Call the getresponse function with updated parameters
        output = getresponse(st.session_state.input_text, st.session_state.no_of_words, st.session_state.user_type)
        st.write(output)
