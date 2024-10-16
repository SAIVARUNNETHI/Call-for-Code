import speech_recognition as sr
from playsound import playsound
from transformers import pipeline
import os
from gtts import gTTS
import streamlit as st
import tempfile
import threading
import time
import streamlit.components.v1 as components

import copilot
import chatgpt
import gemini
import simplified
import craiyon

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")

Wake_Word = "hey"

# animation for listening
def show_listening_animation():
    st.markdown("""
        <div style="width:100%;height:150px;background:transparent;display:flex;justify-content:center;align-items:center;">
            <div class="dot-pulse"></div>
            <style>
                .dot-pulse {
                    width: 30px;
                    height: 30px;
                    border-radius: 50%;
                    background-color: #3498db;
                    animation: pulse 1.2s infinite ease-in-out;
                }
                @keyframes pulse {
                    0% { transform: scale(1); opacity: 1; }
                    50% { transform: scale(1.5); opacity: 0.5; }
                    100% { transform: scale(1); opacity: 1; }
                }
            </style>
        </div>
    """, unsafe_allow_html=True)

# animation for processing
def show_processing_animation():
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
            <div class="spinner"></div>
            <style>
                .spinner {
                    width: 40px;
                    height: 40px;
                    border: 5px solid rgba(0, 0, 0, 0.1);
                    border-top-color: #3498db;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                }
                @keyframes spin {
                    to { transform: rotate(360deg); }
                }
            </style>
        </div>
    """, unsafe_allow_html=True)

# Handle user queries and tasks
def query(user_query):
    if user_query.lower().startswith("ask bing"):
        show_processing_animation()
        question = user_query.lower()[len("ask pilot"):].strip()
        st.write(f"question for copilot:{question}")
        copilot.task(question)
    elif user_query.lower().startswith("ask gpt"):
        show_processing_animation()
        question = user_query.lower()[len("ask gpt"):].strip()
        st.write(f"Question for ChatGPT: '{question}'")
        chatgpt.interact_with_ai_service(question)
    elif user_query.lower().startswith("ask gemini"):
        show_processing_animation()
        question = user_query.lower()[len("ask gemini"):].strip()
        st.write(f"Question for Gemini:'{question}'")
        gemini.interact_with_ai_service(question)
        
    elif user_query.lower().startswith("create"):
        show_processing_animation()
        simplified.generate_ppt(user_query)
        
    elif user_query.lower().startswith("generate"):
        show_processing_animation()
        craiyon.generate_image(user_query)
        
        

#  Listening for the wake word
def listen_wake_word():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        show_listening_animation() 
        with microphone as source:
             #  animation for listening
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio).lower()
                if Wake_Word.lower() in text:
                    speak("Hello! How can I help you?")
                    listen_for_command()
                    st.write("Hello! How can I help you?")
                    #listen_for_command()
            except sr.UnknownValueError:
                st.write("uv")
                speak("Sorry, I couldn't understand you!")
            except sr.RequestError:
                st.write("RE")
                speak("Sorry, I couldn't process your request!")

# Listen for commands after the wake word is heard
def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        st.write("Listening for command:")
        recognizer.adjust_for_ambient_noise(source)

        show_listening_animation()  # Ensure the animation is shown while listening

        audio = recognizer.listen(source)
        
        
        try:
            text = recognizer.recognize_google(audio).lower()
            st.write(text)
            query(text)
        except sr.UnknownValueError:
            st.write("")
        except sr.RequestError:
            st.write("Sorry, I couldn't process your request!")

# Streamlit app structure
st.title("Welcome to Julie")

# Start listening for the wake word in a background thread
threading.Thread(target=listen_wake_word, daemon=True).start()

# Button for manual command input
if st.button("Press to give Command"):
    listen_for_command()
