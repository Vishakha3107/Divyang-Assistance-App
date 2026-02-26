from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivy.app import App
from frontend.screens.py.voice_controller import VoiceController

from frontend.screens.py.role_select import RoleSelectScreen
from frontend.screens.py.admin.business_profile import BusinessProfileScreen
from frontend.screens.py.admin.business_choice import BusinessChoiceScreen
from frontend.screens.py.user.user_signup import UserSignupScreen
from frontend.screens.py.user.map_home import MapHomeScreen
from frontend.screens.py.user.service_map import ServiceMapScreen
from frontend.screens.py.user.service_screen import ServiceScreen
from frontend.screens.py.user.place_list import PlaceListScreen
from frontend.screens.py.user.profile import ProfileScreen
from frontend.screens.py.user.ai_chat import AiChatScreen
from frontend.screens.py.user.destination_select import DestinationSelectScreen
from frontend.screens.py.user.step_navigation import StepNavigationScreen



class DivyangApp(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(RoleSelectScreen(name="role_select"))
        sm.add_widget(UserSignupScreen(name="user_signup"))
        sm.add_widget(BusinessChoiceScreen(name="business_choice"))
        sm.add_widget(MapHomeScreen(name="map_home"))
        sm.add_widget(BusinessProfileScreen(name="business_profile"))
        sm.add_widget(ServiceMapScreen(name="service_map"))
        sm.add_widget(ServiceScreen(name="service_screen"))
        sm.add_widget(PlaceListScreen(name="place_list"))
        sm.add_widget(ProfileScreen(name="profile"))    
        sm.add_widget(AiChatScreen(name="ai_chat"))
        sm.add_widget(DestinationSelectScreen(name="destination_select"))
        sm.add_widget(StepNavigationScreen(name="step_navigation"))

        self.voice = VoiceController(self)
        Clock.schedule_once(lambda dt: self.voice.start(), 1)

        return sm

    def speak(self, text):
        self.voice.speak(text)


if __name__ == "__main__":
    DivyangApp().run()