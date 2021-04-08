import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import numpy
import tkinter
import matplotlib

wikipedia.set_lang("de")
listener = sr.Recognizer()
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#en_voice_id = "HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_ZIRA_11.0"
#engine.setProperty('voice', en_voice_id)
alexaOn = True

# a function which can be called when alexa is supposed to say something
def talk(text):
    engine.say(text)
    engine.runAndWait()


def getCommand():
    global command
    try:
        #mic as source
        with sr.Microphone() as source:
            #prints listening... so that you know when to speak
            print("listening...")
            voice = listener.listen(source)
            #uses google to recognize the voice
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                return command
            else:
                print("...")
                run_alexa()
    except:
        pass
        


def run_alexa():
    global command
    global alexaOn
    command = getCommand()
    #play youtube songs
    while alexaOn == True:
        if command is None:
            run_alexa()
        if "play" in command:
            song = command.replace("play", "")
            print("Now playing" + song)
            #playing the songname given by the user
            pywhatkit.playonyt(song)
            run_alexa()
            #alexa tell the time
        elif "time" in command:
            time = datetime.datetime.now().strftime('%H:%M:')
            print(time)
            talk("The current time is" + time)
            run_alexa()
        elif "what is" in command:
            search = command.replace("what is", "")
            wikipedia.summary(search, sentences=1)
        elif "who is" in command:
            search = command.replace("who is", "")
            answer = wikipedia.summary(search, sentences=1)
            talk(answer)
        #stopping alexa
        elif "stop" in command:
        	
            print("alexa stopped...")
            alexaOn = False
        else:
            error = "I didn't understand you !"
            talk(error)
            run_alexa()



#run the alexa function
run_alexa()







