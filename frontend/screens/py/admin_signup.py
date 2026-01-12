from kivy.uix.screenmanager import Screen

class AdminSignupScreen(Screen):
    def submit_form(self):
        print("Navigating to Admin Home...")
        self.manager.current = "admin_home"
