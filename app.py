from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.text import LabelBase
import re

# Optional: register Atkinson Hyperlegible (comment this if font file isn't present)
try:
    LabelBase.register(
        name="Atkinson",
        fn_regular="assets/fonts/Atkinson-Hyperlegible-Regular.ttf"
    )
except Exception as e:
    print("Font registration skipped:", e)

# Load KV files
Builder.load_file("frontend/screens/kv/role_select.kv")
Builder.load_file("frontend/screens/kv/user_signup.kv")
Builder.load_file("frontend/screens/kv/home.kv")
Builder.load_file("frontend/screens/kv/fullmap.kv")

class RoleSelectScreen(Screen):
    def show_admin_info(self):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        Popup(
            title="Admin",
            content=Label(text="Admin sign-up coming soon."),
            size_hint=(0.8, 0.4)
        ).open()

class UserSignupScreen(Screen):
    def submit_form(self):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        from kivy.app import App

        # 1. Get all inputs safely
        name = self.ids.full_name.text.strip()
        mobile = self.ids.mobile.text.strip()
        age = self.ids.age.text.strip()
        disability = self.ids.disability.text.strip()

        # 2. VALIDATION: Check if ANY field is empty
        if not name or not mobile or not age or not disability:
            self.show_error_popup("All fields are mandatory.\nPlease fill in Name, Mobile, Age, and Disability.")
            return  # STOP here. Do not navigate.

        # 3. VALIDATION: Name (Must be First + Last, Alphabets only)
        # Logic: Split by space to count words, and use Regex to ensure no numbers/symbols
        name_parts = name.split()
        if len(name_parts) < 2 or not re.fullmatch(r"^[A-Za-z\s]+$", name):
            self.show_error_popup("Invalid Name.\nPlease enter First and Last name (Alphabets only).")
            return  # STOP here.

        # 4. VALIDATION: Mobile (Must be exactly 10 digits)
        # Note: input_filter: 'int' in KV handles the typing, but we must check length here
        if len(mobile) != 10:
            self.show_error_popup("Invalid Mobile.\nNumber must be exactly 10 digits.")
            return  # STOP here.

        # 5. SUCCESS
        # If code reaches here, all checks passed.
        Popup(
            title="Success",
            content=Label(text=f"Welcome, {name.title()}!"),
            size_hint=(0.8, 0.4)
        ).open()

        print("Validation Passed. Navigating to HomeScreen...")
        # ONLY NOW do we navigate
        App.get_running_app().root.current = 'home'

    def show_error_popup(self, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        
        # Helper function to avoid repeating Popup code
        Popup(
            title="Error",
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        ).open()

        

class HomeScreen(Screen):
    pass

class FullMapScreen(Screen):
    pass

class DivyangApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition(duration=0.2))
        sm.add_widget(RoleSelectScreen(name='role_select'))
        sm.add_widget(UserSignupScreen(name='user_signup'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(FullMapScreen(name='fullmap'))
        sm.current = 'role_select'
        return sm

if __name__ == '__main__':
    DivyangApp().run()
