from kivy.uix.screenmanager import Screen
class BusinessChoiceScreen(Screen):
    def go_to_identity(self):
        if self.manager:
            self.manager.current = "business_identity"