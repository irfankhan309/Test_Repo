import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import time
import datetime



engine =  pyttsx3.init('sapi5') # to take voice from enduser... its using windows api
voices = engine.getProperty('voices') # it having the voices 
engine.setProperty('voice',voices[0].id)   # selecting the voice male or female...

# current date
today = datetime.datetime.now()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    speak('i am jarvis,Personal Assistant How May i help you.')
    time.sleep(5)
    speak("still you thinking what to say right?")
    speak(today,"you have some thing to do now")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold =1
        Audio = r.listen(source)
        print(Audio)





if __name__=='__main__':
    wishMe()
    take_command()







