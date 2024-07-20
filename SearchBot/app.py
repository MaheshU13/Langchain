# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A BOT")

st.header("Question Answering Bot")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

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
