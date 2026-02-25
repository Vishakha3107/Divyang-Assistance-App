import requests
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapMarker
from kivy.graphics import Color, Line
from kivy.clock import Clock

from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen

class MapHomeScreen(Screen):

    origin_lat = NumericProperty(19.9975)
    origin_lon = NumericProperty(73.7898)


    def search_location(self, location_name):

        if not location_name:
            return

        # 🔎 1️⃣ Search using OpenStreetMap (Nominatim)
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={location_name}"

        headers = {
            "User-Agent": "AccessibilityMappingApp"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        if not data:
            print("Location not found")
            return

        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])

        mapview = self.ids.mapview

        # 📍 2️⃣ Move Map
        mapview.center_on(lat, lon)
        mapview.zoom = 15

        # 📌 3️⃣ Add Marker
        marker = MapMarker(lat=lat, lon=lon)
        mapview.add_widget(marker)

        # 🛣 4️⃣ Draw Route
        Clock.schedule_once(lambda dt: self.draw_route(lat, lon), 0.5)


    def draw_route(self, dest_lat, dest_lon):

        # OSRM Free Routing API
        route_url = f"http://router.project-osrm.org/route/v1/driving/{self.origin_lon},{self.origin_lat};{dest_lon},{dest_lat}?overview=full&geometries=geojson"

        data = requests.get(route_url).json()

        if data["code"] != "Ok":
            print("Route not found")
            return

        coordinates = data["routes"][0]["geometry"]["coordinates"]

        mapview = self.ids.mapview

        with mapview.canvas:
            Color(1, 0, 0, 1)  # 🔴 Red line
            points = []

            for coord in coordinates:
                x, y = mapview.get_window_xy_from(
                    coord[1], coord[0], mapview.zoom
                )
                points.extend([x, y])

            Line(points=points, width=2)

        print("Route drawn successfully!")
