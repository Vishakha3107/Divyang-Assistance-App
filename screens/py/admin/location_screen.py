from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapMarker
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock

class LocationScreen(Screen):
    selected_lat = NumericProperty(0)
    selected_lon = NumericProperty(0)
    marker = None

    def on_enter(self):
        Clock.schedule_once(self.bind_map)

    def bind_map(self, *args):
        self.ids.mapview.bind(on_touch_down=self.on_map_touch)

    def on_map_touch(self, mapview, touch):
        if not mapview.collide_point(*touch.pos):
            return False  # let other widgets handle it

        lat, lon = mapview.get_latlon_at(*touch.pos)

        self.selected_lat = lat
        self.selected_lon = lon

        if self.marker:
            mapview.remove_widget(self.marker)

        self.marker = MapMarker(lat=lat, lon=lon)
        mapview.add_widget(self.marker)

        print("Pinned Location:", lat, lon)

        return False  # VERY IMPORTANT
