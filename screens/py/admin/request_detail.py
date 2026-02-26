from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class RequestDetailScreen(Screen):
    user_name = StringProperty("Rahul Sharma")
    service_name = StringProperty("Wheelchair Assistance")
    phone = StringProperty("+91 9876543210")
    status = StringProperty("Pending")
    address = StringProperty("Nashik, Maharashtra")
    description = StringProperty("Needs wheelchair support from home to hospital.")

    def go_back(self):
        if self.manager:
            self.manager.current = "business_home"

    def mark_completed(self):
        self.status = "Completed"

    def cancel_service(self):
        self.status = "Cancelled"