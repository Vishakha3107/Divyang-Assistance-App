import os
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import camera


class PhotoUploadScreen(Screen):

    selected_image_path = ""

    def open_file_chooser(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        filechooser = FileChooserIconView(
            filters=["*.png", "*.jpg", "*.jpeg"],
            path=os.getcwd()
        )

        select_btn = Button(text="Select", size_hint_y=None, height=40)
        cancel_btn = Button(text="Cancel", size_hint_y=None, height=40)

        layout.add_widget(filechooser)
        layout.add_widget(select_btn)
        layout.add_widget(cancel_btn)

        popup = Popup(
            title="Select Business Photo",
            content=layout,
            size_hint=(0.9, 0.9)
        )

        def select_image(instance):
            if filechooser.selection:
                filepath = filechooser.selection[0]
                self.validate_and_set(filepath)
                popup.dismiss()

        select_btn.bind(on_release=select_image)
        cancel_btn.bind(on_release=popup.dismiss)

        popup.open()

    def capture_from_camera(self):
        filepath = os.path.join(os.getcwd(), "captured_photo.jpg")

        camera.take_picture(
            filename=filepath,
            on_complete=self.camera_callback
        )

    def camera_callback(self, filepath):
        if filepath and os.path.exists(filepath):
            self.validate_and_set(filepath)

    def validate_and_set(self, filepath):
        file_size_mb = os.path.getsize(filepath) / (1024 * 1024)

        if file_size_mb > 5:
            self.show_error("File size must be under 5 MB.")
            return

        self.selected_image_path = filepath
        self.ids.photo_preview.source = filepath
        self.ids.photo_preview.reload()

    def show_error(self, message):
        popup = Popup(
            title="Error",
            content=Label(text=message),
            size_hint=(0.6, 0.3)
        )
        popup.open()

    def save_photo(self):
        if not self.selected_image_path:
            self.show_error("Please upload or capture a photo.")
        else:
            print("Photo saved:", self.selected_image_path)
