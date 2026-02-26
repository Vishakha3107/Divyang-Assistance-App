from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class BusinessHoursScreen(Screen):

    def collect_hours(self):
        days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        business_hours = {}

        for day in days:
            open_time = self.ids[f"{day}_open"].text.strip()
            close_time = self.ids[f"{day}_close"].text.strip()
            is_closed = self.ids[f"{day}_closed"].active

            if not is_closed:
                if not open_time or not close_time:
                    self.show_popup(f"Enter opening and closing time for {day.capitalize()}.")
                    return

            business_hours[day] = {
                "open": open_time,
                "close": close_time,
                "closed": is_closed
            }

        print("Business Hours:", business_hours)
        self.show_popup("Business Hours Saved Successfully!")

    def show_popup(self, message):
        popup = Popup(
            title="Business Hours",
            content=Label(text=message),
            size_hint=(0.7, 0.3)
        )
        popup.open()
