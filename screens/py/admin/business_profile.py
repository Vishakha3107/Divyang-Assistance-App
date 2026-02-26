from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class BusinessProfile(Screen):
    business_name = StringProperty("Divyang Assistance Services")
    owner_name = StringProperty("Mr. Sharma")
    phone = StringProperty("+91 9876543210")
    email = StringProperty("business@email.com")
    address = StringProperty("Nashik, Maharashtra")
    description = StringProperty("We provide mobility and home assistance services.")