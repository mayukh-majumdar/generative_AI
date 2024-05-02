import os
import google.generativeai as genai
import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


genai.configure(api_key=os.getenv('API_KEY'))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

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

model, chat_history = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                            generation_config=generation_config,
                                            safety_settings=safety_settings), []
if 0 <= datetime.datetime.now().hour < 12:
    speak("Good Morning!")
elif datetime.datetime.now().hour < 18:
    speak("Good Afternoon!")
else:
    speak("Good Evening!")
speak("This is a ChatBOT designed by MAYUKH MAJUMDAR powered by Gemini.")
print("Hi,how can I help you today?")
while True:
    convo, prompt = model.start_chat(history=chat_history), input()
    if prompt == 'Refresh':
        chat_history = []
        print("Hi,how can I help you today?\nENTER 'Exit' to quit.")
        continue
    elif prompt == 'Exit':
        speak("Thank you! Please visit again.")
        exit()
    convo.send_message(prompt)
    output = convo.last.text
    print(output)
    print("ENTER 'Refresh' to delete chat history and start a fresh chat.\nENTER 'Exit' to quit.")
    chat_history.append({"role": "user", "parts": [prompt]})
    chat_history.append({"role": "model", "parts": [output]})
