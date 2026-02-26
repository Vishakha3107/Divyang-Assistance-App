import random
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class VerificationScreen(Screen):

    generated_otp = None
    verification_type = None

    def send_otp(self):
        selected_type = self.ids.verification_spinner.text

        if selected_type == "Select Verification Type":
            self.show_popup("Please select verification method.")
            return

        self.verification_type = selected_type
        self.generated_otp = str(random.randint(100000, 999999))

        # In real app this would be sent via SMS or Email
        print(f"Generated OTP ({selected_type}):", self.generated_otp)

        self.show_popup(f"OTP sent via {selected_type} (Check console for demo).")

    def verify_otp(self):
        entered_otp = self.ids.otp_input.text.strip()

        if not entered_otp:
            self.show_popup("Enter OTP.")
            return

        if entered_otp == self.generated_otp:
            self.show_popup("Verification Successful!")
            print("Status: VERIFIED")
        else:
            self.show_popup("Invalid OTP. Try again.")

    def show_popup(self, message):
        popup = Popup(
            title="Verification",
            content=Label(text=message),
            size_hint=(0.7, 0.3)
        )
        popup.open()
