import re
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class ContactScreen(Screen):

    def validate_contact(self):
        country_code = self.ids.country_code_input.text.strip()
        phone = self.ids.phone_input.text.strip()
        website = self.ids.website_input.text.strip()
        email = self.ids.email_input.text.strip()

        # Phone validation
        if not phone:
            self.show_popup("Phone number is mandatory.")
            return

        if not phone.isdigit() or len(phone) != 10:
            self.show_popup("Enter a valid 10-digit phone number.")
            return

        # Country code validation (optional)
        if country_code:
            if not country_code.startswith("+") or not country_code[1:].isdigit():
                self.show_popup("Enter valid country code (e.g., +91).")
                return

        # Website validation (optional)
        if website:
            website_pattern = r"^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/[\w\-._~:\/?#[\]@!$&'()*+,;=]*)?$"
            if not re.match(website_pattern, website):
                self.show_popup("Enter a valid website URL.")
                return

        # Email validation (optional)
        if email:
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(email_pattern, email):
                self.show_popup("Enter a valid email address.")
                return

        print("Country Code:", country_code)
        print("Phone:", phone)
        print("Website:", website)
        print("Email:", email)

        self.show_popup("Contact Section Completed!")

    def show_popup(self, message):
        popup = Popup(
            title="Message",
            content=Label(text=message),
            size_hint=(0.7, 0.3)
        )
        popup.open()
