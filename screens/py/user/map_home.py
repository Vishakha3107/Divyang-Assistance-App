import requests
from threading import Thread

from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.clock import Clock

from kivy_garden.mapview import MapMarker

# GPS (works on Android)
from plyer import gps


class MapHomeScreen(Screen):

    origin_lat = NumericProperty(19.9975)
    origin_lon = NumericProperty(73.7898)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_marker = None
        self.destination_marker = None
        self.route_line = None

    # Start GPS when screen opens
    def on_enter(self):
        try:
            gps.configure(on_location=self.on_location)
            gps.start(minTime=1000, minDistance=1)
        except NotImplementedError:
            print("GPS not supported on this platform")

   
    # GPS Callback
    def on_location(self, **kwargs):
        lat = kwargs.get("lat")
        lon = kwargs.get("lon")

        if lat and lon:
            Clock.schedule_once(lambda dt: self.update_user_location(lat, lon))

    def update_user_location(self, lat, lon):
        self.origin_lat = lat
        self.origin_lon = lon

        mapview = self.ids.mapview

        # First time → center map
        if not self.user_marker:
            mapview.center_on(lat, lon)

        # Update or create marker
        if not self.user_marker:
            self.user_marker = MapMarker(lat=lat, lon=lon)
            mapview.add_widget(self.user_marker)
        else:
            self.user_marker.lat = lat
            self.user_marker.lon = lon

   
    # Location Search (Threaded)
    def search_location(self, location_name):
        if not location_name:
            return

        Thread(
            target=self._search_thread,
            args=(location_name,),
            daemon=True
        ).start()

    def _search_thread(self, location_name):
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={location_name}"
        headers = {"User-Agent": "AccessibilityMappingApp"}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
        except Exception:
            return

        if not data:
            return

        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])

        Clock.schedule_once(lambda dt: self.update_destination(lat, lon))

    # Update Destination
    def update_destination(self, lat, lon):
        mapview = self.ids.mapview

        mapview.center_on(lat, lon)
        mapview.zoom = 15

        # Remove old marker
        if self.destination_marker:
            mapview.remove_widget(self.destination_marker)

        self.destination_marker = MapMarker(lat=lat, lon=lon)
        mapview.add_widget(self.destination_marker)

        # Draw route
        Thread(
            target=self._route_thread,
            args=(lat, lon),
            daemon=True
        ).start()

    # Routing (Threaded)
    def _route_thread(self, dest_lat, dest_lon):

        route_url = (
            f"http://router.project-osrm.org/route/v1/walking/"
            f"{self.origin_lon},{self.origin_lat};"
            f"{dest_lon},{dest_lat}"
            f"?overview=full&geometries=geojson"
        )

        try:
            data = requests.get(route_url, timeout=10).json()
        except Exception:
            return

        if data.get("code") != "Ok":
            return

        coordinates = data["routes"][0]["geometry"]["coordinates"]

        Clock.schedule_once(
            lambda dt: self.draw_route(coordinates)
        )

    # Draw Route
    def draw_route(self, coordinates):

        mapview = self.ids.mapview

        # Remove old route
        if self.route_line:
            mapview.canvas.remove(self.route_line)

        from kivy.graphics import Color, Line

        with mapview.canvas:
            Color(0, 0.4, 0.8, 1)
            points = []

            for coord in coordinates:
                x, y = mapview.get_window_xy_from(
                    coord[1], coord[0], mapview.zoom
                )
                points.extend([x, y])

            self.route_line = Line(points=points, width=3)