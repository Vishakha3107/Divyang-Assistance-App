from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class BusinessHome(Screen):
    availability_status = BooleanProperty(True)

    def on_enter(self):
        self.load_dummy_requests()

    def load_dummy_requests(self):
        self.ids.pending_container.clear_widgets()
        self.ids.accepted_container.clear_widgets()

        self.pending_requests = [
            {
                "name": "Rahul Patil",
                "service": "Wheelchair Assistance",
                "location": "Nashik Road",
                "time": "10:30 AM"
            },
            {
                "name": "Sneha Joshi",
                "service": "Guide request",
                "location": "Gangapur Road",
                "time": "2:00 PM"
            }
        ]

        for request in self.pending_requests:
            card = self.create_pending_card(request)
            self.ids.pending_container.add_widget(card)

    def create_pending_card(self, request):
        layout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=70,   # smaller height
            spacing=8,
            padding=8
        )

        info = BoxLayout(orientation="vertical")
        info.add_widget(Label(text=request["name"], bold=True, color=(0,0,1,1)))
        info.add_widget(Label(text=request["service"], color=(0,0,1,1)))
        info.add_widget(Label(text=f'{request["location"]} | {request["time"]}', color=(0,0,1,1)))

        accept_btn = Button(
            text="Accept",
            size_hint=(None, None),
            size=(80, 35),   # smaller button
            background_color=(0.2, 0.7, 0.2, 1),
            color=(1,1,1,1)
        )

        decline_btn = Button(
            text="Decline",
            size_hint=(None, None),
            size=(80, 35),   # smaller button
            background_color=(0.9, 0.3, 0.3, 1),
            color=(1,1,1,1)
        )

        accept_btn.bind(on_release=lambda x: self.accept_request(request, layout))
        decline_btn.bind(on_release=lambda x: self.decline_request(layout))

        layout.add_widget(info)
        layout.add_widget(accept_btn)
        layout.add_widget(decline_btn)

        return layout

    def accept_request(self, request, card_layout):
        self.ids.pending_container.remove_widget(card_layout)

        accepted_layout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=70,
            padding=8,
            spacing=8
        )

        accepted_layout.add_widget(Label(text=f'{request["name"]} - {request["service"]}', color=(0,0,1,1)))

        complete_btn = Button(
            text="Mark Completed",
            size_hint=(None, None),
            size=(120, 35),
            background_color=(0, 0, 1, 1),
            color=(1,1,1,1)
        )

        complete_btn.bind(on_release=lambda x: self.complete_request(accepted_layout))
        accepted_layout.add_widget(complete_btn)

        self.ids.accepted_container.add_widget(accepted_layout)

    def decline_request(self, card_layout):
        self.ids.pending_container.remove_widget(card_layout)

    def complete_request(self, card_layout):
        self.ids.accepted_container.remove_widget(card_layout)

    def toggle_availability(self, value):
        self.availability_status = value
        if self.availability_status:
            self.ids.availability_btn.text = "Available"
            self.ids.availability_btn.background_color = (0, 0.4, 0.8, 1)
        else:
            self.ids.availability_btn.text = "Unavailable"
            self.ids.availability_btn.background_color = (0, 0.4, 0.8, 1)