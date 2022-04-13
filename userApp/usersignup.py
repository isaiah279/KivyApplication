from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from  kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout

import pyrebase
Window.size = (450, 500)

class Signup(Screen):
    pass
class Tutorials(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.config.primary_color = "Green"
        login_page = Builder.load_file('signup.kv')
        return login_page


if __name__ == "__main__":
    Tutorials().run()
