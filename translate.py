from time import sleep
import datetime
import time
from googletrans import Translator,LANGUAGES
from gtts import gTTS
import googletrans
from playsound import playsound
import pyttsx3
import speech_recognition as speechR
import os


engine=pyttsx3.init('sapi5')  #sapi5 is used here to take the voice

voices=engine.getProperty('voices') #getProperty is used to get the voice
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)  # it will give me the hours 0-24
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("I am your coded robot . How may I help you,sir?")


def commandMe():  # it takes microphone input from the user and returns string output.
    recognizes = speechR.Recognizer()  # it will help to recognize the audio.

    with speechR.Microphone() as userVoice:

        print("please speak,I am listening...")

        recognizes.pause_threshold = 1

        audio = recognizes.listen(userVoice)

    try:  # try is written when we have doubt that there may be some error.
        print("Recognizing...")
        query = recognizes.recognize_google(audio, language='en-in')
        print(f"user's command:{query}\n")

    except Exception as exception:
        # print(exception)

        print("Please,say it again")
        return "None"

    return query


def translateGoogle(query):
    print(LANGUAGES)  # print the supported languages
    translator = Translator()

    # prompt the user to select the target language
    print("Select the language to translate to:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")
    a = input("Enter language code: ")

    # translate the input text to the target language
    try:
        text_translate = translator.translate(query, src="auto", dest=a)
        if text_translate is not None and hasattr(text_translate, "text"):
            text = text_translate.text
        else:
            print("Sorry, the translation could not be completed.")
            return
    except Exception as e:
        print(f"Sorry, there was an error during translation: {e}")
        return

    # convert the translated text to speech and play it
    try:
        tts = gTTS(text, lang=a)
        tts.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(5)
        os.remove("voice.mp3")
    except Exception as e:
        print(f"Sorry, there was an error during text-to-speech conversion: {e}")