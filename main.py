import pyttsx3
import requests
import random
from plyer import notification
import datetime
import speech_recognition as speechR
import wikipedia
import webbrowser
import os
import smtplib
from twilio.rest import Client
from sinchsms import SinchSMS
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from bs4 import BeautifulSoup


TWILIO_SID = "ACc621a3f585aabdb41d5146441046d37f"
TWILIO_AUTH_TOKEN = "af4d1aa558c0f35a03e083dcb8f9080f"
TWILIO_MY_NUMBER = "+14344338551"

ipifyAPI = "at_BgY7OZvLzkIyNzg4scAm2wD83SyGH"
# CLIENT=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

my_email = "jellydiyamon@gmail.com"
my_password = "qzttrzrxticxanmw"


engine = pyttsx3.init('sapi5')  # sapi5 is used here to take the voice

voices = engine.getProperty('voices')  # getProperty is used to get the voice
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

# from gui import play_gif
# play_gif()

# print(voices[0].id)


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


def sendEmail(to, content):
    # this server will be depend from where we will send the mail.For example,for yahoo it will be smtp.mail.yahoo.com .
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.ehlo()
    # TLS- transport layer security. this is used to encrypt the email.
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(my_email, to, content)
    # once we have donen with sending the email, it will automatically close the connection.
    connection.close()


def message():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Hello",
        from_=TWILIO_MY_NUMBER,
        to='+918133025620'
    )


def makeCall():
    client_call = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    call = client_call.calls.create(
        twiml="hi there,how are you?",
        from_=TWILIO_MY_NUMBER,
        to='+918133025620',
        # url='<your-twiml-bin-url>'
    )

# def phoneDetails():
#   number=input("enter the phone number")
#   phone_number =phonenumbers.parse(number)
#   print(geocoder.description_for_number(phone_number,"en"))
#   print(carrier.name_for_number(phone_number,"en"))


if __name__ == "__main__":
    greetings()
    commandMe()

    while True:
        # if 1:
        query = commandMe().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)

            print(results)

            speak(f"According to wikipedia,{results}")

        elif 'open' in query:
            from app_dictionary import openWebApp
            openWebApp(query)
        elif 'close' in query:
            from app_dictionary import closeWebApp
            closeWebApp(query)

        elif 'go to youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search google' in query:
            webbrowser.open("google.com")

        elif ' linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'play music' in query:
            mymusic = "E:\my music"
            songs = os.listdir(mymusic)
            print(songs)
            os.startfile(os.path.join(mymusic, songs[0]))

        elif "relaxing music" in query or "romantic music" in query:
            speak("playing your favorite music, sir")
            l = (1, 2, 3)
            m = random.choice(l)
            if m == 1:
                webbrowser.open("https://www.youtube.com/watch?v=TuUVVKVdZm4")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,its,{strTime}")

        elif "today's news" in query:

            from news import todayNews
            todayNews()

        elif 'open vs program' in query:
            vsCode = "E:\\Downloadedc Softwares\\VS-CODE\\Code.exe"
            os.startfile(vsCode)

        elif 'email to vinod' in query: 
            try:
                speak("what should I say?")
                content = commandMe()
                to = "mishanrajk@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as exception:
                print("exception")
                speak(f"Sorry sir, there is an error ")

        elif 'send message' in query:
            try:
                # speak("what should I write ,Sir?")
                content = commandMe()
                to = "+918133025620"
                message()
                speak("message sent")
            except Exception as exception:
                print("failed to send message")
                speak(f"Sorry sir, there is an error ")

        elif 'please call him' in query:
            try:
                content = commandMe()
                to = "+918133025620"
                makeCall()
                speak("calling")
            except Exception as exception:
                print("failed to call")
                speak(f"Sorry sir, there is an error ")

        # elif 'details' in query:
        #   content=commandMe()
        #   phoneDetails()
        #   speak("please enter the number ,sir")
        #   speak("the details are in your screen")

        elif "cricket score" in query:
            url = "https://www.cricbuzz.com/cricket-match/live-scores"
            scores = requests.get(url)
            soup = BeautifulSoup(scores.text, "html.parser")
            teams = soup.find_all(class_="text-gray-700 font-weight-bold")
            scores = soup.find_all(class_="cb-col cb-col-100 cb-font-20 text-bold")

            try:
                team1 = teams[0].get_text().strip()
                team2 = teams[1].get_text().strip()
                scores_text = scores[0].get_text().strip()
                team1_score, team2_score = scores_text.split(",")
                team1_score = team1_score.strip()
                team2_score = team2_score.strip()

                print(f"{team1}: {team1_score}")
                print(f"{team2}: {team2_score}")

                notification.notify(
                    title="LIVE IPL SCORE: ",
                    message=f"{team1}: {team1_score}\n{team2}: {team2_score}",
                    timeout=5
                )
            except IndexError:
                print("Error: Could not find IPL score data.")
                notification.notify(
                    title="Error",
                    message="Could not find IPL score data.",
                    timeout=5
                )



        elif "translate" in query:
          from translate import translateGoogle
          query=query.replace("translate","")
          translateGoogle(query)

        elif "temperature" or "weather" in query:
            search = "temperature in Jorhat"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Sir, the current{search} is {temp}")
        