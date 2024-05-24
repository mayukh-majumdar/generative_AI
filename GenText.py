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


genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro-latest')
if 0 <= datetime.datetime.now().hour < 12:
    speak("Good Morning!")
elif datetime.datetime.now().hour < 18:
    speak("Good Afternoon!")
else:
    speak("Good Evening!")
speak("Myself GenText, an AI Text Generator developed by MAYUKH MAJUMDAR. Please let me know how I can help you.")
while True:
    prompt = input("Enter prompt.\n")
    response = model.generate_content(prompt)
    print(response.text)
    with open(f'C:/Users/mayuk/PycharmProjects/Generative AI by MAYUKH/Responses/{prompt}.txt', 'w', encoding='utf-8') as f:
        f.write(response.text)
    speak("Response generated successfully.")
    if not bool(int(input("Enter 0 to exit.\nEnter 1 to continue generating.\n"))):
        break
speak("Thank you! Please visit again.")
print("Exiting...")
