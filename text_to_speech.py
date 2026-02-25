# text_to_speech.py
import pyttsx3
from kivy.clock import Clock

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        # Configure voice properties
        self.engine.setProperty('rate', 150)    # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
        
        # Get available voices
        voices = self.engine.getProperty('voices')
        if voices:
            # Use female voice if available
            self.engine.setProperty('voice', voices[1].id)
    
    def speak(self, text):
        """Speak the given text"""
        def _speak():
            self.engine.say(text)
            self.engine.runAndWait()
        
        from threading import Thread
        Thread(target=_speak).start()