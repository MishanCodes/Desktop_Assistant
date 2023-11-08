import os
from time import sleep
import pyautogui
import webbrowser
import pyttsx3

engine=pyttsx3.init('sapi5')  #sapi5 is used here to take the voice

voices=engine.getProperty('voices') #getProperty is used to get the voice
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

apps={
    "commandprompt":"cmd",
    "word":"winword",
    "excel":"excel",
    "paint":"paint",
    "powerpoint":"powerpnt",
    "chrome":"chrome",
}

def openWebApp(query):
    speak("opening the app ,sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query=query.replace("open","")
        query=query.replace("launch","")
        query=query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys=list(apps.keys())

        for app in keys:
            if app in query:
                os.system(f"start {apps[app]}")
        
def closeWebApp(query):
    speak("closing the app ,sir")
    if "one tab" or"1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")

    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")
    else:
        keys=list(apps.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {apps[app]}.exe")
        
    
