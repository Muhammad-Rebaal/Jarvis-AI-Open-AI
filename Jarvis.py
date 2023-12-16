# Modules and Libraies
import os
import webbrowser
from googletrans import Translator
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
from brain import cr_brain as r
import pyautogui
import psutil

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def cpu():
    usage = (psutil.cpu_percent)
    speak(f"The CPU is at usage of {usage}")
    battery = psutil.sensors_battery()
    speak(f"The battery is at usage of {battery.percent}")


def time():
    Time =datetime.datetime.now().strftime(f"The time is: %I:%M:%S")
    speak(Time)
    speak("For your assistance I'm printing it on the screen")
    print(f"The time is:{Time}")


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(f"The day is {day},the month is {month}and the year is {year}")
    speak("For your assistance I'm printing it on the screen")
    print(f"The day is {day},the month is {month} and the year is {year}.")

def wishme():
    speak("Welcome back sir!")
    # time()
    # date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    elif hour>=18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good Night sir")
    speak("Jarvis is at your service. Please tell me how may I assist you")

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\ICS\Desktop\Work\\Web Development\\Python Course\\Jarvis AI\\ss.png")

def tc():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold =3000 #--->There are other voices in the room use energy_threshold.
        audio = r.listen(source)
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language ='en-US')
        line = str(query)
        translate = Translator()
        result = translate.translate(line)
        data = result.text
        print(data)

    except Exception as e:
        print(e)
        speak("Sir,please say that again")
        return "None"
    return data





# Print the generated text


    


if __name__ == "__main__":
    wishme()
    
    while True:
        data= tc().lower()
        speak(r.reply(data))
        if "time" in data:
            time()
        # elif "remember" in data:
        #     speak("What should I remember?")
        #     get = tc()
        #     speak("you said me to remember?"+get)
        #     remember = open("get.txt","w")
        #     remember.write(get)
        #     remember.close()
        # elif "made" in data:
        #     speak("I'm made by Muhammad Rebaal")
        # elif "date" in data:
        #     date()
        # elif "name" in data:
        #     speak("My name is Jarvis")
        # elif "say" in data:
        #     say=open("get.txt","r")
        #     speak(say.read())
        # elif "who" in data:
        #     speak("I'm an AI assistant , of Muhammad Rebaal")
        elif "stop" in data:
            speak("ok sir! I am going offline")
            exit()# exit() or quit() --->same
        # elif 'wiki' in data:
        #     speak("Searching...")
        #     data = data.replace("wiki","")
        #     res=wikipedia.search(data,results=4)
        #     result = wikipedia.summary(data, sentences = 2)
        #     print(result)
        #     speak(result)
        #     speak(f"Some other searches are :{res}")
        #     speak("For your assistance I'm printing it on the screen")
        #     print("Some other searches are:" )
        #     print(res)
        elif "cpu" in data:
            cpu()
        elif "search" in data:
            speak("What should I search ?")
            chrome_path ="C:\Program Files\Google\Chrome\Application\chrome.exe%s"
            search = tc().lower()
            webbrowser.open(search+(".com"))
        elif "screenshot" in data:
            screenshot()
            speak("Done!")
        # elif "email" in data:
        #     try:
        #         speak("What should I say?")
        #         content = tc()
        #         to ="any@gmail.com"
        #         send_email(to,content)
        #         speak("Email has been sent!")
            # except Exception as e:
            #     print(e)
            #     speak("Sorry my sir, I am not able to send the email!")
        elif "open youtube" in data:
            webbrowser.open("youtube.com")
        elif "open google" in data:
            webbrowser.open("google.com")
        elif "open wikipedia" in data:
            webbrowser.open("wikipedia.com")
        elif "log out" in data:
            speak("OK sir! I'm logging out your pc")
            os.system("shutdown -l")