from abc import ABC
import uuid
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
import random
import uuid

from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.snackbar import Snackbar
import requests
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivy.uix.colorpicker import ColorPicker
from kivymd.uix.picker import MDThemePicker
import pyrebase
from kivy.core.window import Window
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

import os
from kivy.clock import Clock


config = {
    "apiKey": "AIzaSyB2BZjMWxuuWGCxYiy39nM2QW6YNaEYejM",
    "authDomain": "isaifirst-434b9.firebaseapp.com",
    "databaseURL": "https://isaifirst-434b9-default-rtdb.firebaseio.com/",
    "projectId": "isaifirst-434b9",
    "storageBucket": "isaifirst-434b9.appspot.com",
    "messagingSenderId": "577271030988",
    "appId": "1:577271030988:web:976a274ab323063c248e69",
    "measurementId": "G-DRBH86S46X"
};
firebase = pyrebase.initialize_app(config)
# Getting reference to storage feature of Firebase
db = firebase.database()
auth = firebase.auth()


# added


class WindowManger(ScreenManager):
    pass


class Home(Screen):
    pass


class WelcomeScreen(MDApp):
    pass


class Signup(Screen):
    pass


class Login(Screen):
    pass


class Services(MDApp):
    pass


class MDTopAppBar(MDApp):
    pass


class MDScreen(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class NavigationDrawer(MDApp):
    def __init__(self, **kwargs):
        self.title = "Home Care"
        super().__init__(**kwargs)
        self.screen = Builder.load_file('user.kv')
        self.screen = Builder.load_file('login.kv')
        self.screen = Builder.load_file('signup.kv')
        return self.screen

    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.screen = Builder.load_file('user.kv')
        self.ww = WindowManger(transition=FadeTransition())

        screens = [Login(name="login"), Signup(name="signup"), Home(name="mainscreen")]
        for screen in screens:
            self.ww.add_widget(screen)
        return self.ww

    def change_screen(self, screen):
        self.ww.current = screen

    def verifying_user_login(self, email, password):
        # self.change_screen(screen="screen")
        self.ww.get_screen('screen')
        # signup

        #self.id = random.randint(0, 1000)

    # Printing random id
    # using uuid1()
    # print("The random id using uuid1() is : ", end="")
    def signing_up(self, email, password):
        store = JsonStore("user.json")
        # config["databaseURL"] = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
        # for i in range(1,10):
        try:
            self.user = auth.create_user_with_email_and_password(email=email, password=password)
            err = Snackbar(text="Registered successfully", md_bg_color=[0, 0.3, 0, 1])
            err.open()

        except:
            err = Snackbar(text="email exist", md_bg_color=[0, 0, 1, 1])
            err.open()

    def signup_real(self, email):
        """myid = {"USER-ID": self.id}

        data = {"user account": self.user}

        db.child("users").child("USER-ID").child(f"UserId{myid}").set(data)"""

    def open_app(self, email, password):
        pass

    def login(self, email, password):
        try:
            self.user = auth.sign_in_with_email_and_password(email=email, password=password)
            err = Snackbar(text=f"logged in with {email}", md_bg_color=[0, 0.3, 0, 1])
            err.open()
            self.change_screen(screen="mainscreen")
        except:
            err = Snackbar(text="enter correct details", md_bg_color=[0, 0, 1, 1])
            err.open()

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.open()

    def color_theme_callback(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def userinput(self, phone, email, name, location, issue):
        if len(phone) != 10:
            err = Snackbar(text="invalid phone number", md_bg_color=[0.9, 1, 0, 1])
            err.open()
        else:
            if len(phone) == 10:
                err = Snackbar(text="Success")
                err.open()
        # def userinput(self, phone, email, name):
        # def userinput(self, phone, email, name):
        '''if len(name) == len(phone) == "":
            err = Snackbar(text="invalid information")
            err.open()
        else:
            if len(phone) == 10 and len(name) >= 1:
                err = Snackbar(text="success")
                err.open()'''
        if len(name) == "":
            err = Snackbar(text="must me more than 5 characters ")
            err.open()
        else:
            if len(name) > 5:
                err = Snackbar(text=" success")
                err.open()
            # valid=re.search("r^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",email)
            # SUBMITTING data to database.
            # Getting reference to storage feature of Firebase
            # Pass the user's idToken to the push method
            config["databaseURL"] = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
            JSON = {"phoneNum": f"{phone}", "useremail": f"{email}", "username": f"{name}", "location": f"{location}",
                    "issue": f"{issue}"}
            id = random.randint(0, 1000)
            db.child("users").child("USER-ID").child(f"{id}").set(JSON)

    def send_comment(self, *args):
        """JSON = {"comment":}
        id = random.randint(0, 1000)
        db.child("users").child("USER-ID").child(f"{id}").set(JSON)
"""

    def view_information(self, view_information):
        # config["databaseURL"] = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
        self.auth_key = 'bTwFAO5zo89eyXpTu30B4C3Fh2hsw3p3JBDZOgYA'
        from_database = requests.get(url=config["databaseURL"] + '?auth=' + self.auth_key)
        # for data in database.json():
        print(from_database.json())
        new_label = self.root.ids.view_information
        new_label.text = from_database.text


NavigationDrawer().run()
