from kivymd.app import *
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

class Demo(FloatLayout):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("dashboard.kv")
        self.theme_cls.theme_style = "Dark"
        return Demo()
    
Main().run()