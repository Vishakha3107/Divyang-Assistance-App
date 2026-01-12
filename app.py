import re
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition, Screen

from frontend.screens.admin_signup import AdminSignupScreen
from frontend.screens.admin_home import AdminHomeScreen

# Load KV files
Builder.load_file("frontend/screens/kv/role_select.kv")
Builder.load_file("frontend/screens/kv/user_signup.kv")
Builder.load_file("frontend/screens/kv/home.kv")
Builder.load_file("frontend/screens/kv/fullmap.kv")
Builder.load_file("frontend/screens/kv/admin_signup.kv")
Builder.load_file("frontend/screens/kv/admin_home.kv")

class RoleSelectScreen(Screen):
    def show_admin_info(self):
        self.manager.current = "admin_signup"

class UserSignupScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class FullMapScreen(Screen):
    pass

class DivyangApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())

        sm.add_widget(RoleSelectScreen(name="role_select"))
        sm.add_widget(UserSignupScreen(name="user_signup"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(FullMapScreen(name="fullmap"))
        sm.add_widget(AdminSignupScreen(name="admin_signup"))
        sm.add_widget(AdminHomeScreen(name="admin_home"))

        sm.current = "role_select"
        return sm
