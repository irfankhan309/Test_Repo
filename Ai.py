import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser





engine =  pyttsx3.init('sapi5') # to take voice from enduser... its using windows api
voices = engine.getProperty('voices') # it having the voices 
engine.setProperty('voice',voices[0].id)   # selecting the voice male or female...

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    
    speak('i am jarvis, how may i help you.')




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







