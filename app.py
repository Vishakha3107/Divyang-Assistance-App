from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy_garden.mapview import MapView  
from kivy.core.window import Window

# Set window size to mobile dimensions for testing
Window.size = (360, 640)


# Load KV files
Builder.load_file("frontend/screens/kv/role_select.kv")
Builder.load_file("frontend/screens/kv/user_signup.kv")
Builder.load_file("frontend/screens/kv/map_home.kv")
Builder.load_file("frontend/screens/kv/google_map.kv")
Builder.load_file("frontend/screens/kv/admin_signup.kv")
Builder.load_file("frontend/screens/kv/admin_home.kv")  


class RoleSelectScreen(Screen):
    def show_admin_info(self):
        # Navigate to the new Admin Signup page
        self.manager.current = "admin_signup"

class UserSignupScreen(Screen):
    def submit_form(self):
        # 1. Get inputs
        name = self.ids.full_name.text.strip()
        mobile = self.ids.mobile.text.strip()
        age = self.ids.age.text.strip() if 'age' in self.ids else "0"
        disability = self.ids.disability.text.strip() if 'disability' in self.ids else "None"

        # 2. Validation
        if not name or not mobile:
             self.show_popup("Error", "Mandatory fields missing.")
             return

        if len(mobile) != 10 or not mobile.isdigit():
             self.show_popup("Error", "Mobile must be 10 digits.")
             return

        if len(name.split()) < 2:
             self.show_popup("Error", "Please enter First and Last name.")
             return

        # 3. Success
        self.show_popup("Success", f"Welcome, {name}!")
        self.manager.current = 'map_home'

    def show_popup(self, title, msg):
        Popup(title=title, content=Label(text=msg), size_hint=(0.8, 0.3)).open()

class AdminSignupScreen(Screen):
    def submit_form(self):
        # 1. Get inputs (Using IDs defined in admin_signup.kv)
        name = self.ids.admin_name.text.strip()
        mobile = self.ids.admin_mobile.text.strip()
        org = self.ids.org_name.text.strip()

        # 2. Validation
        if not name or not mobile or not org:
            self.show_popup("Error", "All fields are mandatory.")
            return

        if len(mobile) != 10 or not mobile.isdigit():
            self.show_popup("Error", "Mobile number must be 10 digits.")
            return
        
        if len(name.split()) < 2:
            self.show_popup("Error", "Please enter Full Name (First & Last).")
            return

        # 3. Success
        print("Admin Validation Passed.")
        self.manager.current = "admin_home"

    def show_popup(self, title, msg):
        Popup(title=title, content=Label(text=msg), size_hint=(0.8, 0.3)).open()


class MapHomeScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class AdminHomeScreen(Screen):
    pass


class DivyangApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())

        sm.add_widget(RoleSelectScreen(name="role_select"))
        sm.add_widget(UserSignupScreen(name="user_signup"))
        sm.add_widget(MapHomeScreen(name="map_home"))
        sm.add_widget(MapScreen(name="google_map"))
        sm.add_widget(AdminSignupScreen(name="admin_signup"))
        sm.add_widget(AdminHomeScreen(name="admin_home"))

        sm.current = "role_select"
        return sm



if __name__ == "__main__":
    DivyangApp().run()
