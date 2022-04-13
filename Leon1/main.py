from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
from kivy.core.window import Window
Window.size=(320,600)

class WindowManager(ScreenManager):
    pass
class Register(Screen):
    pass
class Login(Screen):
    pass
Builder.load_file("login.kv")
Builder.load_file("reg.kv")

class MainApp(MDApp):
    def build(self):
        self.wm=WindowManager(transition=FadeTransition())
        screens=[Login(name="login"),Register(name="reg")]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
    def change_screen(self,screen):
        self.wm.current=screen
MainApp().run()