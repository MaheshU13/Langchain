from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A BOT")
st.header("Question Answering Bot")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit button is clicked
if submit:
    if input.strip():  # Check if the input is not empty or just whitespace
        response = get_gemini_response(input)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")

# Display logo and copyright
logo_path = "logo4.jpg"
col1, col2 = st.columns([1, 5])
with col1:
    st.image(logo_path, width=50)
with col2:
    st.markdown("© 2024 Mahesh U")
