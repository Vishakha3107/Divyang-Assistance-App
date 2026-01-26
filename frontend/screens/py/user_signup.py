from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
import re

class UserSignupScreen(Screen):

    def submit_form(self):
        # Read inputs safely (guard if ids/widgets missing)
        ids = getattr(self, 'ids', {}) or {}
        full_name_widget = ids.get('full_name')
        mobile_widget = ids.get('mobile')
        name = (full_name_widget.text or '').strip() if full_name_widget else ''
        mobile = (mobile_widget.text or '').strip() if mobile_widget else ''

        # ---- VALIDATION ----

        # All fields mandatory
        if not name or not mobile:
            self.show_popup("Error", "All fields are mandatory.")
            return

        # Full name must contain at least first + last name
        name_parts = name.split()
        if len(name_parts) < 2:
            self.show_popup(
                "Error",
                "Please enter both first name and last name."
            )
            return

        # Mobile must be exactly 10 digits (digits only)
        if not re.fullmatch(r"\d{10}", mobile):
            self.show_popup(
                "Error",
                "Mobile number must be exactly 10 digits (digits only)."
            )
            return

        # ---- SUCCESS ----
        self.show_popup("Success", f"Welcome, {name}!")

        # Navigate to next screen ONLY if it exists
        app = App.get_running_app()
        if "home" in app.root.screen_names:
            app.root.current = "home"

    def show_popup(self, title, message):
        Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        ).open()

