import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Set up Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("💬 ToxBot ")
st.caption("Powered by Google's Gemini API")

# Create or load chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user message
user_input = st.chat_input("Type your message...")

# When message is entered
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get Gemini response
    response = st.session_state.chat.send_message(user_input)
    ai_message = response.text

    # Display AI message
    st.chat_message("assistant").markdown(ai_message)
    st.session_state.messages.append({"role": "assistant", "content": ai_message})


