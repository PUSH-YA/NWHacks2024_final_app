from tkinter import * 
from tkinter.ttk import *
import os
from PIL import Image, ImageTk
import cv2
import camera
import os
import joblib
import pyttsx3
import threading
import numpy as np
import speech_recognition as sr



"""
# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3 
 
# Initialize the recognizer 
r = sr.Recognizer() 
 
# Function to convert text to
# speech
def speakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
while True:
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise. Please wait...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = r.listen(source, timeout=5)  # Adjust the timeout as needed

            print("Processing audio...")
            text = r.recognize_google(audio).lower()

            print("You said:", text)
            speakText(text)

            # Check if the user wants to exit
            if "exit" in text:
                print("Exiting...")
                break

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
    except KeyboardInterrupt:
        print("User interrupted. Exiting...")
        break
"""

class App:

    def __init__(self):
        # initialising voice engine
        self.voice = pyttsx3.init()
        self.voice.setProperty('rate', 125)
        self.voice.setProperty('volume', 1.0)
        self.voice.setProperty('voice', self.voice.getProperty("voices")[1].id) # 0 for male, 1 for female

        self.record = sr.Recognizer()
        self.is_listening = False
        self.text = "hello"

        self.window = Tk()

        photo1 = PhotoImage(file = os.path.join(os.getcwd(), "image-30x30.jpg")) 
        self.speechbutton = Button(self.window,image=photo1, command=self.speak)
        self.speechbutton.grid(row = 1, column = 2, sticky = E)

        photo2 = PhotoImage(file = os.path.join(os.getcwd(), "image-18x30.jpg"))     
        self.speechbutton = Button(self.window,image=photo2, command=self.start)
        self.speechbutton.grid(row = 1, column = 1, sticky = E)

        self.init_gui()

        self.delay = 15
        self.microphone()
        self.window.mainloop()
        

    
    def init_gui(self):
        master = self.window

        self.l0 = Label(master, text = "Waiting for instruction")
        self.l0.grid(row = 0, column = 0, columnspan= 3)

        self.text_label = Label(master, text = self.text, width = 50, background="white",relief = "groove")
        self.text_label.grid(row = 1, column = 0, sticky = W)

    
    def microphone(self):
        if self.is_listening:
            self.text = ""
            self.text_label.config(text = self.text)
            try:
                with sr.Microphone() as source:
                    self.l0.config(text = "Adjusting for ambient noise. Please wait...")
                    self.record.adjust_for_ambient_noise(source, duration = 1)

                    self.l0.config(text = "Listening...")
                    audio = self.record.listen(source, timeout=2)  # No timeout set for continuous listening

                    self.l0.config(text = "Processing audio...")
                    audio = self.record.recognize_google(audio).lower()

                    self.l0.config(text = "Did you say...")
                    self.text = audio
                    self.text_label.config(text = self.text)
            except sr.RequestError as e:
                self.l0.config(text="Could understand audio. Please try again...")
            except sr.UnknownValueError:
                self.l0.config(text="Could understand audio. Please try again...")
            finally:
                is_listening = False
    
    def start(self):
        self.is_listening = True
        threading.Thread(target=self.microphone).start()
    
    def speak_voice(self):
        self.voice.say(self.text)
        self.voice.runAndWait()
        self.voice.stop()

    def speak(self):
        threading.Thread(target=self.speak_voice).start()

        