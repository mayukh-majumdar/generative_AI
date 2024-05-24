import os
import google.generativeai as genai
import pyttsx3
import datetime

from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

genai.configure(api_key=os.getenv('API_KEY'))
generation_config = genai.GenerationConfig(
    temperature= 1,
    top_p= 0.95,
    top_k= 0,
    max_output_tokens= 8192,
    response_mime_type= "text/plain",
)

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model,chat_history = genai.GenerativeModel('gemini-1.5-pro-latest', safety_settings = safety_settings, generation_config = generation_config), []
if 0 <= datetime.datetime.now().hour < 12:
    speak("Good Morning!")
elif datetime.datetime.now().hour < 18:
    speak("Good Afternoon!")
else:
    speak("Good Evening!")
speak("This is a ChatBOT designed by MAYUKH MAJUMDAR powered by Gemini.")
print("Hi,how can I help you today?")
while True:
    chat_session, prompt = model.start_chat(history=chat_history), input()
    if prompt == 'Refresh':
        chat_history = []
        speak("Chat history is deleted successfully. You can now have a fresh start.")
        print("Hi,how can I help you today?\nENTER 'Exit' to quit.")
        continue
    elif prompt == 'Exit':
        speak("Thank you! Please visit again.")
        break
    response = chat_session.send_message(prompt)
    print(response.text)
    chat_history = chat_session.history
    print("ENTER 'Refresh' to delete chat history and start a fresh chat.\nENTER 'Exit' to quit.")
