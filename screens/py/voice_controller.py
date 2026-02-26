import speech_recognition as sr
import threading
import pyttsx3
from kivy.clock import Clock

class VoiceController:

    def __init__(self, app):
        self.app = app
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self.listen_loop, daemon=True).start()
        print("Voice system started")

    def listen_loop(self):
        while self.running:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = self.recognizer.listen(source)

            try:
                command = self.recognizer.recognize_google(audio).lower()
                print("You said:", command)
                Clock.schedule_once(lambda dt: self.process_command(command))

            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Speech API unavailable")

    def process_command(self, command):
        sm = self.app.root

        if "admin" in command:
            sm.current = "business_choice"
            self.speak("Opening admin panel")

        elif "user" in command:
            sm.current = "user_signup"
            self.speak("Opening user sign up")

        elif "home" in command:
            sm.current = "home"
            self.speak("Going home")

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()