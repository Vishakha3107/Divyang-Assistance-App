# voice_assistant.py
import speech_recognition as sr
from kivy.clock import Clock

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
    def listen_for_command(self, callback):
        """Listen for voice command and return transcribed text"""
        def _listen():
            with self.microphone as source:
                print("Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = self.recognizer.listen(source)
            
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                Clock.schedule_once(lambda dt: callback(text))
            except sr.UnknownValueError:
                print("Could not understand audio")
                Clock.schedule_once(lambda dt: callback(None))
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                Clock.schedule_once(lambda dt: callback(None))
        
        # Run in a separate thread to not block UI
        from threading import Thread
        Thread(target=_listen).start()