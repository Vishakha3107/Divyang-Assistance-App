from kivy.clock import Clock
import speech_recognition as sr
import threading
from kivy.uix.screenmanager import Screen


class RoleSelectScreen(Screen):

    def on_enter(self):
        self.listening = True
        self.start_listening()

    def on_leave(self):
        self.listening = False

    def start_listening(self):
        threading.Thread(target=self.listen_loop, daemon=True).start()

    def listen_loop(self):
        recognizer = sr.Recognizer()

        while self.listening:
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    print("Listening for voice command...")
                    audio = recognizer.listen(source, timeout=5)

                command = recognizer.recognize_google(audio).lower()
                print("You said:", command)

                Clock.schedule_once(lambda dt: self.process_command(command))

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue

    def process_command(self, command):
        if "admin" in command:
            self.listening = False
            self.manager.current = "business_choice"

        elif "user" in command:
            self.listening = False
            self.manager.current = "user_signup"