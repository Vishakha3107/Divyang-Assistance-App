from kivy.uix.screenmanager import Screen

class PlaceListScreen(Screen):

    def open_map(self, lat, lon):
        map_screen = self.manager.get_screen("map")
        map_screen.set_location(lat, lon)
        self.manager.current = "map"