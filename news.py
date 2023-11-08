import requests
import json
import pyttsx3

engine=pyttsx3.init('sapi5')  #sapi5 is used here to take the voice

voices=engine.getProperty('voices') #getProperty is used to get the voice
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def todayNews():
    apiNews={"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d556bc7e57a445f0b508ebf42a6ac67b",
            "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=d556bc7e57a445f0b508ebf42a6ac67b",
            "political":"https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey=d556bc7e57a445f0b508ebf42a6ac67b",
            "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d556bc7e57a445f0b508ebf42a6ac67b",
            "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d556bc7e57a445f0b508ebf42a6ac67b",
    }

    content=None
    url=None
    speak("sir,tell me the topic that you're intersted in. The available topics are, [Business], [Science], [Political], [Technology], [Sports]")
    topic=input("Please, enter the topic to get the respective news\n")

    for key,value in apiNews.items():
        if key.lower() in topic.lower():
            url=value
            print(url)
            print("Executed")
            break
        else:
            url=True
    if url is True:
        print("This topic is not available right now")

    news=requests.get(url).text
    news=json.loads(news)
    speak("today's news are as follows")


    arts=news["articles"]

    for articles in arts:
        article=articles["title"]
        print(article)
        speak(article)
        news_url=articles["url"]
        print(f"for more info,visit: {news_url}")

        a=input("[press 1 to continue] and [press 2 to stop]")
        if str(a)=="1":
            pass
        elif str(a)=="2":
            break
    