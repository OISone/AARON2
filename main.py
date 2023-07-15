# ************************************************************************************
# *                  Automatic AI Reconnaissance Observation Network                 *
# *                                   A.A.R.O.N.                                     *
# ************************************************************************************


# ************************************************************************************
# *           Some Code from the "Tech Moto" YouTube channel                         *
# *           Additional Code from S-Tech's YouTube Channel                          *
# ************************************************************************************

# *******************************************
# *--------------Libraries------------------*
# *******************************************


import pyttsx3
import pyaudio
import speech_recognition as sr
import time
import musicalbeeps
import pvporcupine
import struct
import os
import subprocess
import webbrowser


# *******************************************
# *----------------Variables----------------*
# *******************************************
USER = "sir"
# keywords = [("aaron", 1), ("hey aaron", 1), ]


# *******************************************
# *----------------Functions----------------*
# *******************************************


def Website(url):
    webbrowser.get().open(url)


def Readychirp():
    player = musicalbeeps.Player(volume = 0.1, mute_output = True)
    player.play_note("E5b", 0.1)
    player.play_note("G5b", 0.1)
    player.play_note("E5b", 0.1)


def Capturechirp():
    player = musicalbeeps.Player(volume = 0.1, mute_output = True)
    player.play_note("G5b", 0.1)
    player.play_note("E5b", 0.1)



def speak(text):
    global TALKING
    rate = 100
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    TALKING = True
    print("A.A.R.O.N.: "+text+"\n")
    engine.setProperty('rate', rate+50)
    engine.say(text)
    engine.runAndWait()
    TALKING = False


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        Readychirp()
        print("Listening...", end="")
        audio = r.listen(source)
        query = ''
        Capturechirp()

        try:
            print("recognizing...", end="")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said:{query}")

        except Exception as e:
            print("Exception:" + str(e))

        return query.lower()

def conversationFlow():
    talk = True
    while talk:
        userSaid = takeCommand()
        if "hello" in userSaid:
            speak("hello")
        if "bye" in userSaid:
            speak("goodbye")
        if "how are you" in userSaid:
            speak("Doing well")
        if "stop" in userSaid:
            speak("Stopping sir")
            break
        if "exit" in userSaid:
            speak("ending program")
            talk = False
        if "calculator" in userSaid:
            try:
                subprocess.Popen("calc")
                speak("Opening it now sir.")
            except:
                speak(" I can't do that Dave")
                pass
            break

        if "notepad" in userSaid:
            try:
                subprocess.Popen("notepad")
                speak("Opening notepad now sir")
            except:
                speak("There was a problem sir")
                pass
            break

        if "flipper" in userSaid:
            try:
                subprocess.Popen("c:\\program files\\qflipper\\qflipper.exe")
                speak("Opening q flipper now sir")
            except:
                speak("There was a problem sir")
                pass
            break
        if "firefox" in userSaid:
            try:
                subprocess.Popen("c:\\program files\\mozilla firefox\\firefox.exe")
                speak ("Opening browser now sir")
            except:
                speak("there was an error sir")
                pass
            break
        if "obsidian" in userSaid:
            try:
                subprocess.Popen("C:\\Users\\OISLT\\AppData\\Local\\Obsidian\\obsidian.exe")
                speak ("Opening Obsidian now sir")
            except:
                speak("there was an error")
                pass
            break
        if"open youtube" in userSaid:
            speak("opening YouTube " + USER)
            Website('https://www.youtube.com')
            break


        time.sleep(2)

# *******************************************
# *-------------Main Program----------------*
# *******************************************
def main():
    porcupine = None
    pa = None
    audio_stream =None
    print("A.A.R.O.N. version 0.01 - Online and Ready!")
    print("*****************************************************")
    print("A.A.R.O.N.: Awaiting your call " + USER)

    try:
        porcupine = pvporcupine.create(keywords=["terminator", "computer"])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hotword Detected... ", end="")
                conversationFlow()
                time.sleep(1)
                print("A.A.R.O.N.: Awating your call " + USER)
    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()



main()
# ********************************************
# *----------------Notes---------------------*
# ********************************************
