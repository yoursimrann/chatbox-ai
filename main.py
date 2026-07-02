import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
st.set_page_config(page_title="Chatbox AI", page_icon="🤖", layout="centered")

# Set the API key for Google Generative AI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the API key
genai.configure(api_key=GEMINI_API_KEY)

# load model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(user_role):
    if user_role=='model':
        return 'assistant'
    return user_role

# initialize session state 
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
st.title("Chatbox AI")
st.write('Ask me anything!')

# show chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(generate_response(message.role)):
        st.markdown(message.parts[0].text)

# user input
user_prompt = st.chat_input("Type your question here...")
if user_prompt:
    # display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate response from the model
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # display model response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

