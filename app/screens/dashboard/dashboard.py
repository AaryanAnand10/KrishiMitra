# import shutil
# import time
# from kivy.utils import get_color_from_hex
# from kivymd.app import MDApp
# from kivy.clock import Clock
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.uix.label import MDLabel
# from kivy.core.window import Window
# from kivy.lang import Builder
# from kivy.app import App
# from kivy.uix.camera import Camera
# from kivymd.uix.button import MDIconButton
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label 
# from kivy.core.window import Window

# class MyClock(MDLabel):
#     def update(self, *args):
#         self.text = time.strftime("%H:%M")

# class Demo(BoxLayout):
#     def send_message(self):
#         message = self.ids.message_input.text
#         if message:
#             message_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="40dp")
#             message_label = MDLabel(text=message, halign='left', size_hint_x=None, width=self.width * 0.8)
#             message_box.add_widget(message_label)
#             self.ids.chat_log.add_widget(message_box)
            
#             self.ids.message_input.text = ''
            
#             self.ids.chat_scroll.scroll_y = 0

#     def _init_(self, **kwargs):
#         super()._init_(**kwargs)
#         Clock.schedule_interval(self.update_clock, 1)

#     def update_clock(self, *args):
#         if self.ids.clock_label:
#             self.ids.clock_label.update()

#     # def start_camera(self):
#     #     print("Starting camera...")
#     #     layout = self.ids.cam  # Access the cam layout directly
#     #     layout.clear_widgets()  # Clear any existing widgets
    
#     #     try:
#     #         camera = Camera(play=True, index=0)
#     #         camera.resolution = (640, 480)
#     #         layout.add_widget(camera)
#     #         print("Camera started successfully.")
#     #     except Exception as e:
#     #         print(f"Error initializing camera: {e}")
#     #         layout.add_widget(Label(text="Camera initialization failed."))

#     def start_camera(self):
#         print("Starting camera...")
#         layout = self.ids.cam  
#         layout.clear_widgets() 

#         try:
#             # Create and configure the camera widget
#             camera = Camera(play=True, index=0)
#             camera.resolution = (640, 480)
#             layout.add_widget(camera)
#             print("Camera started successfully.")

#             # Add the capture button below the camera
#             capture_button = MDIconButton(
#                 icon="camera",
#                 md_bg_color=get_color_from_hex("#2e5817"),
#                 icon_color=get_color_from_hex("#b7de9d"),
#                 size_hint_x=0.08,
#                 size_hint_y=0.4,
#                 pos_hint={"center_x": 0.5},
#                 on_release=self.capture_image
#             )
#             layout.add_widget(capture_button)

#         except Exception as e:
#             print(f"Error initializing camera: {e}")
#             layout.add_widget(Label(text="Camera initialization failed."))

#     def capture_image(self, instance):
#         # Logic to capture the image and save it with the filename in the format 'ddmmyyhhmm'
#         print("Capturing image...")
#         current_time = time.strftime("%d%m%y%H%M")
#         file_path = f"./{current_time}.png"
#         self.ids.cam.children[1].export_to_png(file_path)

        
#         print(f"Image saved as {file_path}")

#     def open_file_manager(self):
#         # Logic to open the file manager and upload a picture
#         print("Opening file manager...")

#     def on_file_selected(self, selection):
#         if selection:
#             print(f"Selected file: {selection[0]}")
#             # Logic to handle the selected file, such as copying it to the save directory
#             current_time = time.strftime("%d%m%y%H%M")
#             save_path = f"./data/{current_time}.png"
#             shutil.copy(selection[0], save_path)
#             print(f"File saved as {save_path}")
    

# class Main(MDApp):
#     def build(self):
#         Window.size = (540, 960)
#         self.theme_cls.primary_palette = "LightGreen"
#         Builder.load_file("app/screens/dashtest/dashtest.kv")
#         return Demo()

#     def on_start(self):
#         # Ensure that clock_label is an instance of MyClock
#         clock_label = self.root.ids.clock_label
#         if not isinstance(clock_label, MyClock):
#             raise TypeError("clock_label should be an instance of MyClock")

# if __name__ == '_main_':
#     Main().run()






# import time
# from kivymd.app import MDApp
# from kivy.clock import Clock
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.uix.label import MDLabel
# from kivy.core.window import Window
# from kivy.lang import Builder
# from kivy.app import App
# from kivy.uix.camera import Camera
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label  # Import the Label class
# from kivy.core.window import Window

# class MyClock(MDLabel):
#     def update(self, *args):
#         self.text = time.strftime("%H:%M")

# class Demo(BoxLayout):
#     def send_message(self):
#         message = self.ids.message_input.text
#         if message:
#             # Create a new BoxLayout for the message
#             message_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="40dp")
#             message_label = MDLabel(text=message, halign='left', size_hint_x=None, width=self.width * 0.8)
#             message_box.add_widget(message_label)
#             self.ids.chat_log.add_widget(message_box)
            
#             # Clear the input field
#             self.ids.message_input.text = ''
            
#             # Scroll to the bottom
#             self.ids.chat_scroll.scroll_y = 0

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # Schedule the clock update method
#         Clock.schedule_interval(self.update_clock, 1)

#     def update_clock(self, *args):
#         if self.ids.clock_label:
#             self.ids.clock_label.update()

#     def start_camera(self):
#         print("Starting camera...")
#         Window.size = (540, 960)
#         layout = BoxLayout()
#         try:
#             camera = Camera(play=True, index=0)
#             camera.resolution = (640, 480)
#             layout.add_widget(camera)
#             print("Camera started successfully.")
#         except Exception as e:
#             print(f"Error initializing camera: {e}")
#             layout.add_widget(Label(text="Camera initialization failed."))
#         return layout
    

# class Main(MDApp):
#     def build(self):
#         Window.size = (540, 960)
#         self.theme_cls.primary_palette = "LightGreen"
#         Builder.load_file("dashboard.kv")
#         return Demo()

#     def on_start(self):
#         # Ensure that clock_label is an instance of MyClock
#         clock_label = self.root.ids.clock_label
#         if not isinstance(clock_label, MyClock):
#             raise TypeError("clock_label should be an instance of MyClock")
        
#     def on_tab_switch(self, instance, current_tab, previous_tab):
#         print(f"Switched to tab: {current_tab.name}")
#         if current_tab.name == "screen 3":
#             camera_layout = self.start_camera()
#             self.root.ids.screen_3.clear_widgets()
#             self.root.ids.screen_3.add_widget(camera_layout)

# if __name__ == '__main__':
#     Main().run()


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
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image

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
        
        
    # def on_enter_feed(self):
    #     # Example data for the news feed
    #     news_items = [
    #         {"image": "news1.png", "text": "Breaking News 1: Headline or description goes here"},
    #         {"image": "news2.png", "text": "Breaking News 2: Another headline or description"},
    #         {"image": "news3.png", "text": "Breaking News 3: Interesting news headline"},
    #         {"image": "news4.png", "text": "Breaking News 4: More news content here"},
    #         {"image": "news5.png", "text": "Breaking News 5: Last news item in this feed"}
    #     ]

    #     # Clear existing widgets
    #     self.ids.news_feed.clear_widgets()

    #     # Dynamically create news items and add them to the feed
    #     for item in news_items:
    #         news_widget = self.create_news_item(item["image"], item["text"])
    #         self.ids.news_feed.add_widget(news_widget)

    # def create_news_item(self, image_source, text):
    #     # Create a BoxLayout to represent a single news item
    #     news_item = BoxLayout(orientation='vertical', size_hint_y=None, height="400dp", spacing=10, padding=10)

    #     # Create and add an Image widget for the news
    #     news_image = Image(source=image_source, allow_stretch=True, keep_ratio=False, size_hint_y=0.7)
    #     news_item.add_widget(news_image)

    #     # Create and add a Label widget for the news text
    #     news_label = MDLabel(text=text, theme_text_color="Primary", size_hint_y=0.1, halign='left')
    #     news_item.add_widget(news_label)

    #     # Add buttons for like and comment actions
    #     actions_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, padding=5, spacing=20, pos_hint={"center_x": 0.5})
    #     like_button = MDIconButton(icon="thumb-up", md_bg_color=get_color_from_hex("#b7de9d"), size_hint=(None, None), size=("48dp", "48dp"), padding=10)
    #     comment_button = MDIconButton(icon="comment", md_bg_color=get_color_from_hex("#b7de9d"), size_hint=(None, None), size=("48dp", "48dp"), padding=10)
        
    #     actions_layout.add_widget(like_button)
    #     actions_layout.add_widget(comment_button)
        
    #     news_item.add_widget(actions_layout)

    #     return news_item
    
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
    Main().run()