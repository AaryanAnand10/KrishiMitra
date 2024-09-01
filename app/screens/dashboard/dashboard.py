import shutil
import time
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.camera import Camera
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.core.window import Window

class MyClock(MDLabel):
    def update(self, *args):
        self.text = time.strftime("%H:%M")

class Demo(BoxLayout):
    def send_message(self):
        message = self.ids.message_input.text
        if message:
            message_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="40dp")
            message_label = MDLabel(text=message, halign='left', size_hint_x=None, width=self.width * 0.8)
            message_box.add_widget(message_label)
            self.ids.chat_log.add_widget(message_box)
            
            self.ids.message_input.text = ''
            
            self.ids.chat_scroll.scroll_y = 0

    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        if self.ids.clock_label:
            self.ids.clock_label.update()

    # def start_camera(self):
    #     print("Starting camera...")
    #     layout = self.ids.cam  # Access the cam layout directly
    #     layout.clear_widgets()  # Clear any existing widgets
    
    #     try:
    #         camera = Camera(play=True, index=0)
    #         camera.resolution = (640, 480)
    #         layout.add_widget(camera)
    #         print("Camera started successfully.")
    #     except Exception as e:
    #         print(f"Error initializing camera: {e}")
    #         layout.add_widget(Label(text="Camera initialization failed."))

    def start_camera(self):
        print("Starting camera...")
        layout = self.ids.cam  
        layout.clear_widgets() 

        try:
            # Create and configure the camera widget
            camera = Camera(play=True, index=0)
            camera.resolution = (640, 480)
            layout.add_widget(camera)
            print("Camera started successfully.")

            # Add the capture button below the camera
            capture_button = MDIconButton(
                icon="camera",
                md_bg_color=get_color_from_hex("#2e5817"),
                icon_color=get_color_from_hex("#b7de9d"),
                size_hint_x=0.08,
                size_hint_y=0.4,
                pos_hint={"center_x": 0.5},
                on_release=self.capture_image
            )
            layout.add_widget(capture_button)

        except Exception as e:
            print(f"Error initializing camera: {e}")
            layout.add_widget(Label(text="Camera initialization failed."))

    def capture_image(self, instance):
        # Logic to capture the image and save it with the filename in the format 'ddmmyyhhmm'
        print("Capturing image...")
        current_time = time.strftime("%d%m%y%H%M")
        file_path = f"./{current_time}.png"
        self.ids.cam.children[1].export_to_png(file_path)

        
        print(f"Image saved as {file_path}")

    def open_file_manager(self):
        # Logic to open the file manager and upload a picture
        print("Opening file manager...")

    def on_file_selected(self, selection):
        if selection:
            print(f"Selected file: {selection[0]}")
            # Logic to handle the selected file, such as copying it to the save directory
            current_time = time.strftime("%d%m%y%H%M")
            save_path = f"./data/{current_time}.png"
            shutil.copy(selection[0], save_path)
            print(f"File saved as {save_path}")
    

class Main(MDApp):
    def build(self):
        Window.size = (540, 960)
        self.theme_cls.primary_palette = "LightGreen"
        Builder.load_file("app/screens/dashtest/dashtest.kv")
        return Demo()

    def on_start(self):
        # Ensure that clock_label is an instance of MyClock
        clock_label = self.root.ids.clock_label
        if not isinstance(clock_label, MyClock):
            raise TypeError("clock_label should be an instance of MyClock")

if __name__ == '_main_':
    Main().run()