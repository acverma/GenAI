from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro model and get responses

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
# Initialize our streamlit app

st.set_page_config(page_title="Doc Q&A", page_icon=":robot:")

st.title("Doc Q&A")
st.header("Gemini LLM App")

input = st.text_input("Input: ",key = "input")
submit = st.button("Ask the question")

# when submit is clicked
if submit:
    response = get_gemini_response(input)
    st.write(response)
