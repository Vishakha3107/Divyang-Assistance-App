from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class UserSignupScreen(Screen):

    def submit_form(self):

        name = self.ids.full_name.text.strip()

        if not name:
            Popup(
                title="Error",
                content=Label(text="Name required"),
                size_hint=(0.7, 0.3)
            ).open()
        else:
            Popup(
                title="Success",
                content=Label(text="Signup Successful"),
                size_hint=(0.7, 0.3)
            ).open()

            # GO TO HOME
            self.manager.current = "map_home"
            
