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

import pygame
import threading
import pyttsx3
import pyaudio
import speech_recognition as sr
import time
import musicalbeeps
import pvporcupine
import struct
import os
import os.path
import subprocess
import webbrowser


# *******************************************
# *----------------Variables----------------*
# *******************************************
USER = "sir"
AiName = 'AARON'
USERNAME = 'Dave'
WAKE = 'n'
TALKING = False
SHOW = False
Count = 1
# *******************************************
# *----------------Libraries----------------*
# *******************************************

MONTHS = ["january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENSIONS = ["rd", "th", "st", "nd"]
CONFIRM = ["yes", "ok", "yeah", "correct", "affirmative", "roger", "right", "absolutely"]
DENY = ["no", "negative", "incorrect"]
TIME = ["when", "time", "schedule"]
EXIT = ["exit", "quit", "shutdown"]

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
    Readychirp()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...", end="")
        audio = r.listen(source)
        query = ''

        try:
            print("Recognizing...", end="")
            Capturechirp()
            query = r.recognize_google(audio, language='en-US')
            print(f"User said:{query}")

        except Exception as e:
            print("Exception:" + str(e))

        return query.lower()


def conversationFlow():
    talk = True
    while talk:
        userSaid = takeCommand()
        if "demo" in userSaid:
            speak(" I was designed as the Automatic AI Reconnaissance Observation Network, or A.A.R.O.N.")
            speak(" My brain is a nural net processor, a learning computer.")
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
# *                GUI INFO                 *
# *******************************************

class imageHandler:
    def __init__(self):
        self.pics = dict()

    def loadFromFile (self, filename, id=None):
        if id == None: id = filename
        self.pics[id] = pygame.image.load(filename).convert()

    def loadFromSurface (self, surface, id):
        self.pics[id] = surface.convert_alpha()

    def render(self, surface, id, position=None, clear=False, size=None):
        if clear == True:
            surface.fill ( (5, 2, 23))#

        if position == None:
            picX = int(surface.get_width()/2-self.pics[id].get_width()/2)
        else:
            picX = position[0]
            picY = position[1]

        if size == None:
            surface.blit(self.pics [id], (picX, picY))

        else:
            surface.blit(pygame.transform.smoothscale(self.pics[id], size), (picX, picY))


pygame.display.init()
pygame.display.set_caption("A.A.R.O.N")
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
handler = imageHandler()

def display():

# Idle Animation
    handler.loadFromFile("D://Jarvis/venv/face2/idle/1.jpg", "1")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/2.jpg", "2")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/3.jpg", "3")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/4.jpg", "4")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/5.jpg", "5")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/6.jpg", "6")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/7.jpg", "7")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/8.jpg", "8")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/9.jpg", "9")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/10.jpg", "10")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/11.jpg", "11")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/12.jpg", "12")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/13.jpg", "13")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/14.jpg", "14")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/15.jpg", "15")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/16.jpg", "16")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/17.jpg", "17")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/18.jpg", "18")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/19.jpg", "19")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/20.jpg", "20")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/21.jpg", "21")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/22.jpg", "22")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/23.jpg", "23")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/24.jpg", "24")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/25.jpg", "25")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/26.jpg", "26")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/27.jpg", "27")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/28.jpg", "28")
    handler.loadFromFile("D://Jarvis/venv/face2/idle/29.jpg", "29")

    # Talking Animation
    handler.loadFromFile("D://Jarvis/venv/face2/talking/101.jpg", "101")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/102.jpg", "102")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/103.jpg", "103")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/104.jpg", "104")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/105.jpg", "105")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/106.jpg", "106")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/107.jpg", "107")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/108.jpg", "108")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/109.jpg", "109")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/110.jpg", "110")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/111.jpg", "111")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/112.jpg", "112")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/113.jpg", "113")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/114.jpg", "114")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/115.jpg", "115")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/116.jpg", "116")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/117.jpg", "117")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/118.jpg", "118")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/119.jpg", "119")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/120.jpg", "120")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/121.jpg", "121")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/122.jpg", "122")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/123.jpg", "123")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/124.jpg", "124")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/125.jpg", "125")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/126.jpg", "126")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/127.jpg", "127")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/128.jpg", "128")
    handler.loadFromFile("D://Jarvis/venv/face2/talking/129.jpg", "129")


def face():
    # Variables#
    A = 0  # Left and Right on Screen
    B = 0  # Up and Down on Screen
    x = 400  # Size width
    y = 400  # Size Length

    Count = 1
    global TALKING
    while True:
        if not TALKING:
            if Count >= 100:
                Count = Count - 100
            print(Count)
            img = str(Count)
            handler.render(screen, img, (A, B),True, (x, y))
            pygame.display.update(A, B, x, y)
            time.sleep(.08)
            Count = Count +1
            if Count == 30:
                Count = 1

            elif TALKING:
                if Count <=100:
                    Count = Count + 100
                print(Count)
                img = str(Count)
                handler.render(screen, img, (A, B), True, (x, y))
                pygame.display.update(A, B, x, y)
                time.sleep(.08)
                Count = Count + 1
                if Count == 130:
                    Count = 101


# *******************************************
# *-------------Main Program----------------*
# *******************************************
def Amain():
    porcupine = None
    pa = None
    audio_stream = None
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
                print("A.A.R.O.N.: Awaiting your call " + USER)
    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()


def main():
    t1 = threading.Thread(target=Amain)
    t2 = threading.Thread(target=face)

    display()
    t1.start()
    t2.start()
main()
# ********************************************
# *----------------Notes---------------------*
# ********************************************
