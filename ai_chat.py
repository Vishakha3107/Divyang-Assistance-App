import os
from dotenv import load_dotenv

from openai import OpenAI
from kivy.uix.screenmanager import Screen
from kivy.app import App

# Load API key
load_dotenv()

print("API KEY IS:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key="ssk-proj-ybcl1SaVuNMRNs1SkMPPMN9sLJrTkqsuLLYjLZIE5w-7pFuUeYWjdlh4C_yr5T9W0w5hC0szDZT3BlbkFJ5qJ7Re18FK1PA7uWW2t_WuNT0xbUgt2o6d_iPBRBAOFLlmpvyW_cOevhTKo-sOQYDKvm4ZNI0A")


class AIChatScreen(Screen):

    def send_message(self):

        user_text = self.ids.user_input.text.strip()

        if not user_text:
            return

        # Show user message
        self.ids.chat_label.text += f"\n\nYou: {user_text}"
        self.ids.user_input.text = ""

        # Get AI response
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an accessibility navigation assistant."},
                    {"role": "user", "content": user_text}
                ]
            )

            ai_reply = response.choices[0].message.content

        except Exception as e:
            print("\n🔥 FULL OPENAI ERROR:\n", e, "\n")
            ai_reply = "Error connecting to AI service."

        # Show AI reply
        self.ids.chat_label.text += f"\nAI: {ai_reply}"

        # Speak reply
        App.get_running_app().speak(ai_reply)

    def open_voice(self):
        App.get_running_app().speak("Voice assistant activated")