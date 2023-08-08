
import pyttsx3
import speech_recognition as sr
import wikipedia
import pyaudio
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=2 and hour<18:
        speak("Hello Waqar How are you!")
    else:
        speak(" I am  Jarvis sir  please tell me how may I help you ")

    speak("Its my pleasure that I am following   you sir!!! ")
   
    speak("Muhammad","Abu-Bakar","Omar Farooq","Ali-Ibne Haider","Hasan","Husain","..")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
        print("say that again please...")

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__=="__main__" :
        #wishMe()
       # takecommand()
        while True:
            query = takecommand().lower()

            if 'wikipedia' in query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=3)
                speak("According to wikipedia.. ")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open Online editor' in query:
                webbrowser.open("onlinegdb.com")

           

            elif 'open Microsoft Bing' in query:
                webbrowser.open("bing.com")

            elif 'open Dev C++ editor' in query:
                codePath = "C:\Program Files (x86)\Dev-Cpp\devcpp.exe"
                os.startfile(codePath)

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com") 

            

            






    
       
