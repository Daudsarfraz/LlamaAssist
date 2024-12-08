import streamlit as st

from chatbot import getresponse
from save_to_file import create_file


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

import streamlit as st

# Initialize session state variables if they don't exist
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "no_of_words" not in st.session_state:
    st.session_state.no_of_words = ""
if "user_type" not in st.session_state:
    st.session_state.user_type = "Beginner"

# Callback functions to handle updates
def update_input_text():
    st.session_state.input_text = st.session_state.input_area

def update_no_of_words():
    st.session_state.no_of_words = st.session_state.length_input

# Text area for input text
st.text_area(
    "Write About Your Topic", 
    value=st.session_state.input_text,
    height=150,
    max_chars=None,
    key="input_area",
    on_change=update_input_text
)

# Columns for input length and difficulty level
column1, column2 = st.columns(2)

with column1:
    st.text_input(
        "Enter length of Desired Output:", 
        value=st.session_state.no_of_words,
        max_chars=None,
        key="length_input",
        on_change=update_no_of_words
    )

with column2:
    st.selectbox(
        "Difficulty Level?",
        ("Beginner", "Intermediate", "Expert"), 
        index=("Beginner", "Intermediate", "Expert").index(st.session_state.user_type),
        key="user_type"
    )

# Submit button
if st.button("Start", help="Press Submit Button to Start"):
    if not st.session_state.input_text.strip():
        st.error("Please provide input text.")
    elif not st.session_state.no_of_words.strip():
        st.error("Please provide the desired output length.")
    else:
        # Call the getresponse function with updated parameters
        output = getresponse(
            st.session_state.input_text, 
            st.session_state.no_of_words, 
            st.session_state.user_type
        )
        st.write(output)

        # Create and save the output file
        file_name = "llama"
        write_to_file = create_file(file_name, output)
        
        # Reset input fields
        # st.session_state.input_text = ""
        # st.session_state.no_of_words = ""
