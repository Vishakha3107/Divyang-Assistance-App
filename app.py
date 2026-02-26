import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy_garden.mapview import MapView  
from kivy.core.window import Window
# from backend.firebase_config import db
from frontend.screens.py.voice_controller import VoiceController

import pyttsx3

# Set window size to mobile dimensions for testing
Window.size = (360, 640)

import speech_recognition as sr
import threading
from kivy.clock import Clock

from frontend.screens.py.user.map_home import MapHomeScreen
from frontend.screens.py.admin.admin_edit_services import AdminEditServicesScreen
from frontend.screens.py.admin.admin_organization import AdminOrganizationScreen
from frontend.screens.py.admin.admin_profile import AdminProfileScreen  
from frontend.screens.py.admin.business_home import BusinessHome  
from frontend.screens.py.admin.request_detail import RequestDetailScreen


# Load KV files
Builder.load_file("frontend/screens/kv/role_select.kv")
Builder.load_file("frontend/screens/kv/user/user_signup.kv")
Builder.load_file("frontend/screens/kv/user/map_home.kv")
Builder.load_file("frontend/screens/kv/admin/business_choice.kv")
Builder.load_file("frontend/screens/kv/admin/business_identity.kv")
Builder.load_file("frontend/screens/kv/admin/location_screen.kv")
Builder.load_file("frontend/screens/kv/admin/contact_screen.kv")
Builder.load_file("frontend/screens/kv/admin/verification_screen.kv")
Builder.load_file("frontend/screens/kv/admin/business_hours_screen.kv")
Builder.load_file("frontend/screens/kv/admin/photo_upload_screen.kv")
Builder.load_file("frontend/screens/kv/admin/business_home.kv") 
Builder.load_file("frontend/screens/kv/admin/request_detail.kv")
Builder.load_file("frontend/screens/kv/admin/business_profile.kv")
Builder.load_file("frontend/screens/kv/user/profile.kv")
Builder.load_file("frontend/screens/kv/user/service_map.kv")
Builder.load_file("frontend/screens/kv/user/service_screen.kv")
Builder.load_file("frontend/screens/kv/user/place_list.kv")
Builder.load_file("frontend/screens/kv/user/ai_chat.kv")
Builder.load_file("frontend/screens/kv/user/step_navigation.kv")
Builder.load_file("frontend/screens/kv/user/destination_select.kv")


class RoleSelectScreen(Screen):
    def show_admin_info(self):
        
        self.manager.current = "admin_signup"

class UserSignupScreen(Screen):
    def submit_form(self):
        # 1. Get inputs
        name = self.ids.full_name.text.strip()
        mobile = self.ids.mobile.text.strip()
        age = self.ids.age.text.strip() if 'age' in self.ids else "0"
        disability = self.ids.disability.text
        if disability == "Select Disability Type":
         print("Please select a disability type")
         return


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

        self.show_popup("Success", f"Welcome, {name}!")
        self.manager.current = 'map_home'

    def show_popup(self, title, msg):
        Popup(title=title, content=Label(text=msg), size_hint=(0.8, 0.3)).open()
         # 3. Save to Firestore
    #     try:
    #         db.collection("users").add({
    #             "name": name,
    #             "mobile": mobile,
    #             "age": age,
    #             "disability": disability
    #         })
    #         self.show_popup("\t \t Success", f"Welcome, {name}! \n  Your account has been created.")
    #         self.manager.current = 'map_home'

    #     except Exception as e:
    #         self.show_popup("Error", f"Failed to save data: {e}")

    # def show_popup(self, title, msg):
    # # Create a Label with centered text
    #  content = Label(
    #     text=msg,
    #     halign="center",
    #     valign="middle",
    #     text_size=(300, None)   # width constraint so text wraps nicely
    # )

    # # Create and open the popup
    #  Popup(
    #     title=title,
    #     content=content,
    #     size_hint=(0.8, 0.3)
    # ).open()

       

class MapScreen(Screen):
    pass

class BusinessChoiceScreen(Screen):
    pass

class BusinessIdentityScreen(Screen):
    pass

class LocationScreen(Screen):
    pass

class ContactScreen(Screen):
    pass

class VerificationScreen(Screen):
    pass

class BusinessHoursScreen(Screen):
    pass

class PhotoUploadScreen(Screen):
    pass

class BusinessHomeScreen(Screen):
    pass

class BusinessProfileScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass    

class ServiceMapScreen(Screen): 
    pass

class ServiceScreen(Screen):    
    pass

class PlaceListScreen(Screen):
    pass

class AiChatScreen(Screen):   
    pass

class StepNavigationScreen(Screen):
    pass

class DestinationSelectScreen(Screen):
    pass

class DivyangApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())

        sm.add_widget(RoleSelectScreen(name="role_select"))
        sm.add_widget(UserSignupScreen(name="user_signup"))
        sm.add_widget(MapHomeScreen(name="map_home"))
        sm.add_widget(BusinessChoiceScreen(name="business_choice"))
        sm.add_widget(BusinessIdentityScreen(name="business_identity"))
        sm.add_widget(LocationScreen(name="location_screen"))
        sm.add_widget(ContactScreen(name="contact_screen"))
        sm.add_widget(VerificationScreen(name="verification_screen"))
        sm.add_widget(BusinessHoursScreen(name="business_hours_screen"))
        sm.add_widget(PhotoUploadScreen(name="photo_upload_screen"))
        sm.add_widget(BusinessHome(name="business_home"))
        sm.add_widget(RequestDetailScreen(name="request_detail"))
        sm.add_widget(BusinessProfileScreen(name="business_profile"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(ServiceMapScreen(name="service_map"))
        sm.add_widget(ServiceScreen(name="service_screen"))
        sm.add_widget(PlaceListScreen(name="place_list"))
        sm.add_widget(AiChatScreen(name="ai_chat"))
        sm.add_widget(StepNavigationScreen(name="step_navigation"))
        sm.add_widget(DestinationSelectScreen(name="destination_select"))

        sm.current = "role_select"
        return sm



if __name__ == "__main__":
    DivyangApp().run()
