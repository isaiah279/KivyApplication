from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

Window.size = (350, 600)
UI = '''
#:import Snackbar kivymd.uix.snackbar.Snackbar

MDBoxLayout:
    orientation : 'vertical'
    MDToolbar :
        title : "Wordpress Post"
        right_action_items :[["weather-sunny",lambda x : app.blackwhit()]]
        elevation : 20

    MDGridLayout:
        cols : 1
        padding : 30,60,30,100
        spacing : 10
        pos_hint : {"center_x":.5,"center_y":.5}
        MDCard:
            #size_hint: None, None
            #size: "280dp", "180dp"
            pos_hint: {"center_x": .5, "center_y": .5}
            radius: [20,]
            elevation : 30
            opacity : .9
            MDBoxLayout:
                orientation : 'vertical'
                padding :10,10,10,70
                spacing : 10
                Image :
                    source : "wordpress.png"
                    #opacity : .9
                    pos_hint: {"center_x": .5, "center_y": .2}
                    size_hint : .8,.8

                MDTextField :
                    id : username 
                    hint_text : "Enter username "
                    helper_text:'Hint : codepyy,codeaj'
                    helper_text_mode : "on_focus"
                    icon_right : "wordpress"
                    icon_right_color : app.theme_cls.primary_color
                    pos_hint : {'center_x': 0.5, 'center_y': 1}
                    size_hint_x: None
                    width : 250

                MDTextField :
                    id : pass 
                    hint_text : "Password"
                    helper_text:'Hint : CodeAj123'
                    helper_text_mode : "on_focus"
                    icon_right : "eye-off"
                    password : True
                    icon_right_color : app.theme_cls.primary_color
                    pos_hint : {'center_x': 0.5, 'center_y': 0.8}
                    required: True
                    size_hint_x: None
                    width : 250

                MDRoundFlatButton :
                    text : "Post"
                    pos_hint : {'center_x': 0.5, 'center_y': 0.1}
                    on_press : app.post()
                    on_release: Snackbar(text="news is poated").open()




'''


class WordPressUI(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(UI)

    def blackwhit(self):

        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Gray"
        else:
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"

    def close_dilog(self, obj):
        self.dialog.dismiss()

    def post(self):
        print(self.root.ids.username.text)
        close = MDRectangleFlatButton(text="Close", on_release=self.close_dilog)
        more = MDRectangleFlatButton(text="Download")
        self.dialog = MDDialog(title=f"POSTING...",
                               size_hint_y=None,
                               height="600",
                               text=f"Author : ",
                               size_hint=(0.9, 1),
                               buttons=[close, more],
                               )
        self.dialog.open()


if __name__ == '__main__':
    WordPressUI().run()