from kivy.uix.screenmanager import Screen

class ServiceScreen(Screen):

    selected_service = ""

    def choose_service(self, service):
        self.selected_service = service
        print("Selected:", service)

    def confirm_service(self):
        self.manager.current = "service_map"
