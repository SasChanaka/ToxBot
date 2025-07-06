import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model (text-only)
model = genai.GenerativeModel("gemini-2.5-flash")  # fallback model

chat = model.start_chat()

while True:
    question = input("User: ")
    
    if question.lower() == "bye":
        print("AI: Bye...")
        break

    response = chat.send_message(question)
    print(f"AI: {response.text}")
