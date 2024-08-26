from typing import Mapping
import pyttsx3 # type: ignore
import speech_recognition as sr # type: ignore
import datetime
import wikipedia # type: ignore
import webbrowser
import os
import requests
import subprocess
import json
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:  
        speak("Good Evening!")

    speak("Hello, I am Meta. Please tell me how may I help you?")    


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300 
        audio=r.listen(source)


    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:  {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please...")
        speak("Say that again please...")

        return "None"
    return query




if __name__ == "__main__":
    wishMe()
    while(True):
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'great' in query:
            print("thank you sir")
            speak('thank you sir')
        
        elif "it is too chilly day" in query:
            print("yes sir I think you should be in your blanket")
            speak('Yes sir I think you should be in your blanket')

        elif 'open geeks for geeks' in query:
            print('opening geeks for geeks sir')
            speak('opening geeks for geeks sir')
            webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'open portal' in query:
            print('opening C U I M S sir')
            speak('opening C U I M S sir')
            webbrowser.open("https://uims.cuchd.in/uims/")

        elif 'play music' in query:
            print('playing music sir')
            speak('playing music sir')
            music_dir = 'D:\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time right now' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir the time is{strTime}")
            speak(f"Sir the time is{strTime}" )
        
        elif 'lunch' in query:
            print('have you eaten your lunch sir')
            speak('have you eaten your lunch sir')
        
        elif 'yes' in query:
            print('wow sir, how was it')
            speak('wow sir, how was it')
        
        elif 'tasty' in query:
            print('mummy toh aacha bnati hai')
            speak('mummy toh aacha banati hai')
        
        elif 'open code' in query:
            codePath="C:\\Users\\ADITYA SHRIVASTAV\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        
        elif 'open chrome' in query:
            speak("Opening Mozilla Firefox")
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        
        elif "google search" in query:
            query = query.replace("google search","")
            url = f"https://google.com/search?q={query}"
            webbrowser.open(url)
            speak(f'Here is what I found {query} on google')
        
        elif "youtube search" in query:
            query = query.replace("youtube search","")
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for{query} on youtube')
        
        elif "show map of" in query:
            query = query.replace("show map of","")
            url = f"https://www.google.com/maps?q={query}"
            webbrowser.get().open(url)  
            speak('opening map sir')

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")        
        
        elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6) 
        
        elif "good bye" in query or "ok bye" in query or "stop" in query:
            speak("Thanks for giving me your time")
            speak('your personal assistant meta is shutting down')
            print('your personal assistant meta is shutting down')
            exit()  
        
        elif "log off" in query or "sign out" in query:
             speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
             subprocess.call(["shutdown", "/l"])
                