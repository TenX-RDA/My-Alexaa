import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes 
listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk (text):
    engine.say(text)
    engine.runAndWait()
def take_command():
       with sr.Microphone() as source:
           print('listening......')
           listner.adjust_for_ambient_Noise(source)
           command = listner.recognize_google(voices)
           command = command.lower()
           if 'alexa' in command.replace('alexa',''):
            print (command)

       return command    

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
      song = command.replace('play','')
      talk('playing' + song)
      pywhatkit.playonyt(song) 
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%1:%m %p')
        talk('Current time is'+ time)
    elif 'who the heck is ' in command :
      Person = command.replace('who the heck is', '')
      info  = wikipedia.summary(Person, 1)
      print(info)
      talk(info)
    elif'are you single' in command:
        talk('I am in a realationship with the WIFI')
    elif ' joke ' in command:
        talk(pyjokes.get_joke())
    else:
     talk('Please say the command again.')         
    
while True:
    run_alexa()