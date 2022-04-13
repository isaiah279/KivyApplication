from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (450, 500)


class Tutorials(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.config.primary_color = "Green"
        login_page = Builder.load_file('login.kv')

        return login_page




if __name__ == "__main__":
    Tutorials().run()
