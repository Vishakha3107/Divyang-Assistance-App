from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
import re

class UserSignupScreen(Screen):

    def submit_form(self):
        # 1. Get values and strip whitespace (removes accidental spaces at start/end)
        # Using specific IDs implies your KV file inputs have id: full_name and id: mobile
        name_input = self.ids.get("full_name")
        mobile_input = self.ids.get("mobile")

        name = name_input.text.strip() if name_input else ""
        mobile = mobile_input.text.strip() if mobile_input else ""

        # ---- VALIDATION STEP BY STEP ----

        # CHECK 1: Are fields empty?
        if not name or not mobile:
            self.show_popup("Error", "All fields are mandatory.")
            return # STOPS the function here. No redirection happens.

        # CHECK 2: Name Validation
        # logic: split by space. Must have at least 2 parts (First Last).
        # regex: checks that the whole string is only letters and spaces.
        name_parts = name.split()
        
        # Regex explanation: ^[a-zA-Z\s]+$ means start to end only letters and spaces
        is_alpha_only = re.fullmatch(r"^[a-zA-Z\s]+$", name)
        
        if len(name_parts) < 2 or not is_alpha_only:
            self.show_popup(
                "Invalid Name", 
                "Please enter your First and Last name.\n(Alphabets only, no numbers/symbols)"
            )
            return # STOPS the function here.

        # CHECK 3: Mobile Validation
        # logic: Must be exactly 10 characters and all must be numbers.
        if not mobile.isdigit() or len(mobile) != 10:
            self.show_popup(
                "Invalid Mobile", 
                "Phone number must be exactly 10 digits.\n(No spaces, no dashes, no +91)"
            )
            return # STOPS the function here.

        # ---- SUCCESS ----
        # If the code reaches here, all checks passed.
        self.show_popup("Success", f"Welcome, {name.title()}!")
        
        # ONLY NOW do we change the screen
        App.get_running_app().root.current = "home"

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(None, None),
            size=(400, 200) # Fixed size for better look
        )
        popup.open()