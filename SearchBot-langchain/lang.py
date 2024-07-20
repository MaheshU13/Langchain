import streamlit as st
import textwrap
from google.generativeai import GenerativeModel

import google.generativeai as genai
from google.generativeai import GenerativeModel


from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Directly insert your API key here
API_KEY = "AIzaSyBxTLi6zZyorJqsH-lJgaATaXil0o4QOjA"
genai.configure(api_key=API_KEY)

## Function to load Gemini model and get responses

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

## Initialize our Streamlit app

st.set_page_config(page_title="Q&A BOT")

st.header("Question Answering Bot")

input_text = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

## If ask button is clicked

if submit:
    if input_text.strip():  # Check if the input is not empty or just whitespace
        response = get_gemini_response(input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")

logo_path = r"logo4.jpg"  

col1, col2 = st.columns([1, 5])
with col1:
    st.image(logo_path, width=50)
with col2:
    st.markdown(" © 2024 Mahesh U")
