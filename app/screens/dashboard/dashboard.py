import time
from kivymd.app import *
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivymd.uix.label import MDLabel

class MyClock(MDLabel):
    def update(self, *args):
        self.text = time.strftime("%H:%M")

class Demo(FloatLayout):
    pass

def _init_(self, **kwargs):
        super()._init_(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

def update_clock(self, *args):
    if self.ids.clock_label:
        self.ids.clock_label.update()

class Main(MDApp):
    def build(self):
        Builder.load_file("dashboard.kv")
        self.theme_cls.theme_style = "Dark"
        return Demo()
    
Main().run()