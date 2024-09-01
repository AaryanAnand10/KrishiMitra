from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
import time

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
from kivy.uix.label import Label  # Import the Label class
from kivy.core.window import Window 
class LoginScreen(Screen):
    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    result_label = ObjectProperty(None)

    credentials = {
        "u": "p",
        "user2@example.com": "password2",
        "user3@example.com": "password3",
        "user4@example.com": "password4"
    }

    def check_login(self):
        email = self.email_input.text
        password = self.password_input.text
        
        if email in self.credentials and self.credentials[email] == password:
            self.result_label.text = "Logging in..."
            self.result_label.color = (0, 1, 0, 1)  # Green color
            Krishi().stop()
            Main().run()
           
        else:
            self.result_label.text = "Invalid user, Sign up?"
            self.result_label.color = (1, 0, 0, 1)  # Red color

class SignUpScreen(Screen):
    username_input = ObjectProperty(None)
    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    confirm_password_input = ObjectProperty(None)
    result_label = ObjectProperty(None)
    
    def sign_up(self):
        username = self.username_input.text.strip()
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        confirm_password = self.confirm_password_input.text.strip()
        
        if password == confirm_password:
            self.result_label.text = "Signed up successfully!"
            self.result_label.color = (0, 1, 0, 1)  # Green color
            
        else:
            self.result_label.text = "Passwords do not match!"
            self.result_label.color = (1, 0, 0, 1)

class MyClock(MDLabel):
    def update(self, *args):
        self.text = time.strftime("%H:%M")

class Demo(BoxLayout):
    def send_message(self):
        message = self.ids.message_input.text
        if message:
            # Create a new BoxLayout for the message
            message_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="40dp")
            message_label = MDLabel(text=message, halign='left', size_hint_x=None, width=self.width * 0.8)
            message_box.add_widget(message_label)
            self.ids.chat_log.add_widget(message_box)
            
            # Clear the input field
            self.ids.message_input.text = ''
            
            # Scroll to the bottom
            self.ids.chat_scroll.scroll_y = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Schedule the clock update method
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        if self.ids.clock_label:
            self.ids.clock_label.update()
            
    def start_camera(self):
        print("Starting camera...")
        layout = self.ids.cam  # Access the cam layout directly
        layout.clear_widgets()  # Clear any existing widgets
    
        try:
            # Create a BoxLayout to hold the camera and button in a vertical alignment
            camera_box = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
            camera_box.size_hint = (0.8, 0.8)  # Make it take 80% of the available width and height
            camera_box.pos_hint = {"center_x": 0.5, "center_y": 0.5}  # Center the BoxLayout
    
            # Create and configure the camera widget
            camera = Camera(play=True, index=0)
            camera.resolution = (640, 480)
            camera.size_hint = (1, 0.9)  # Camera takes up 90% of the box layout's height
            camera_box.add_widget(camera)
    
            # Create the capture button and add it below the camera
            capture_button = MDIconButton(
                icon="camera",
                md_bg_color=get_color_from_hex("#2e5817"),
                icon_color=get_color_from_hex("#b7de9d"),
                size_hint=(None, None),
                size=(64, 64),
                pos_hint={"center_x": 0.5},
                on_release=self.capture_image
            )
            camera_box.add_widget(capture_button)
    
            # Add the BoxLayout to the main layout
            layout.add_widget(camera_box)
            print("Camera started successfully.")
    
        except Exception as e:
            print(f"Error initializing camera: {e}")
            layout.add_widget(Label(text="Camera initialization failed."))
    
    def capture_image(self, instance):
        # Logic to capture the image and save it with the filename in the format 'ddmmyyhhmm'
        print("Capturing image...")
        current_time = time.strftime("%d%m%y%H%M")
        file_path = f"./data/{current_time}.png"
        self.ids.cam.children[0].children[1].export_to_png(file_path)
        
        print(f"Image saved as {file_path}")

class Krishi(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen"
        return Builder.load_file('app/screens/login/login.kv')

class Main(MDApp):
    def build(self):
        Window.size = (540, 960)
        self.theme_cls.primary_palette = "LightGreen"
        Builder.load_file("app/screens/dashboard/dashboard.kv")
        return Demo()

    def on_start(self):
        # Ensure that clock_label is an instance of MyClock
        clock_label = self.root.ids.clock_label
        if not isinstance(clock_label, MyClock):
            raise TypeError("clock_label should be an instance of MyClock")

if __name__ == '__main__':
    Krishi().run()
