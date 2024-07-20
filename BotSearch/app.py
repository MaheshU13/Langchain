from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

load_dotenv()  # take environment variables from .env.

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        if response and hasattr(response, 'text') and response.text:
            return response.text
        else:
            return "No valid response received."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Initialize Streamlit app
st.set_page_config(page_title="Q&A BOT")
st.header("Question Answering Bot")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    if input_text.strip():  # Check if the input is not empty or just whitespace
        response = get_gemini_response(input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")
st.markdown("© 2024 Mahesh U")
