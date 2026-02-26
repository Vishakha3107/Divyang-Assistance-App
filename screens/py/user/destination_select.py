from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy_garden.mapview import MapMarker

class DestinationSelectScreen(Screen):

    def open_map(self, place):
        app = App.get_running_app()
        map_screen = app.root.get_screen("google_map")
        mapview = map_screen.ids.mapview

        # Coordinates for each destination
        locations = {
            "Sandip Foundation": (20.9950, 75.5630),
            "City Center mall": (20.5530, 74.1230),
            "Civil Hospital": (20.7000, 74.5000),
        }

        lat, lon = locations.get(place, (0, 0))

        # Center map on destination
        mapview.center_on(lat, lon)

        # Remove only old markers (not entire map)
        for child in mapview.children[:]:
            if isinstance(child, MapMarker):
                mapview.remove_widget(child)

        # Add new marker
        marker = MapMarker(
            lat=lat,
            lon=lon,
            source="assets/pin.png"
        )
        mapview.add_widget(marker)

        # Navigate to map screen
        app.root.current = "google_map"
