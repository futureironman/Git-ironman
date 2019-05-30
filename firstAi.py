import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr


engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am stark sir. Please tell me how can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")

        audio=r.listen(source)
    try:
        print("Recognizing....")
        query= r.recognize_google(audio,language='en-in')
        print(f" User said:{query}\n")
    except Exception as e:
        #print(e)

        print("Say that again please...")
        return"None"
    return query




if __name__=="__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackflow'in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music'in query:
            music_dir='?C:\\Users\\hp\\Documents\\audio'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open pycham'in query:
            pypath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.2\\bin\\pycharm64.exe"
            os.startfile(pypath)
