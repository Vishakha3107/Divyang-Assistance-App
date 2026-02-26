from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapMarkerPopup


class MapScreen(Screen):

    def set_location(self, lat, lon):

        self.ids.mapview.center_on(lat, lon)

        marker = MapMarkerPopup(lat=lat, lon=lon)
        self.ids.mapview.add_marker(marker)