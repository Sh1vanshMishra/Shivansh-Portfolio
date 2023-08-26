import speech_recognition as sr
import webbrowser
import os
import smtplib
import wikipedia
import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir/ma'am ")
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir/ma'am")
    else:
        speak("Good Evening Sir/ma'am")
    speak("Tell me, how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening to you.............")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        print("Say that again plz.......")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()


if __name__=="__main__" :
    wishMe()
    while True :
        query = takeCommand().lower()

        if 'wikipedia' in query :
            speak('searching wikipedia.........')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now()
            speak(f"Current time is {strTime}")
            
