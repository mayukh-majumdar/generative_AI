import os
import PIL.Image
import datetime
import google.generativeai as genai
import pyttsx3
from pathlib import Path

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
model = genai.GenerativeModel('gemini-pro-vision')
if 0 <= datetime.datetime.now().hour < 12:
    speak("Good Morning!")
elif datetime.datetime.now().hour < 18:
    speak("Good Afternoon!")
else:
    speak("Good Evening!")
speak("Myself Textify Image, an AI Image to text converter developed by MAYUKH MAJUMDAR. Please let me know how I can help you.")
img = PIL.Image.open(Path(input("Enter the path to image.")))
response = model.generate_content([input("Enter prompt based on which response will be generated."), img], stream=True)
response.resolve()
print(response.text)
speak("Response generated successfully. Please visit again. Thank you!")
