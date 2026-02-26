from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class BusinessIdentityScreen(Screen):
    business_name = StringProperty("")
    business_type = StringProperty("Select Type")
    category = StringProperty("Select Category")

    def validate_and_next(self):
        name = self.ids.business_name_input.text.strip()
        btype = self.ids.business_type_spinner.text
        category = self.ids.category_spinner.text

        if not name:
            self.show_popup("Business Name is mandatory.")
            return

        if btype == "Select Type":
            self.show_popup("Please select a Business Type.")
            return

        if category == "Select Category":
            self.show_popup("Please select a Category.")
            return

        # Store temporarily (later we pass to next screen / database)
        self.business_name = name
        self.business_type = btype
        self.category = category

        print("Business Name:", name)
        print("Business Type:", btype)
        print("Category:", category)

        # Move to next section screen
        self.manager.current = "location_screen"

    def show_popup(self, message):
        popup = Popup(
            title="Form Error",
            content=Label(text=message),
            size_hint=(0.7, 0.3)
        )
        popup.open()
