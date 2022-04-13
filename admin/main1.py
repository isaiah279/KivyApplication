import tkinter
from tkintermapview import TkinterMapView
from tkinter import ttk
from tkinter import *
import threading
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
import kivy
import json
import requests
from kivymd.uix.list import TwoLineListItem
from kivymd.app import MDApp
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.snackbar import Snackbar
# Floatlayout allows us to place the elements
# relatively based on the current window
# size and height especially in mobiles
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import mainthread
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
import pyrebase
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

Window.size = (1600, 1100)

root_tk = tkinter.Tk()

from kivy.animation import Animation, AnimationTransition, CompoundAnimation

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


class WindoManager(ScreenManager):
    pass


class Login(Screen):
    pass


class Home(Screen):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""


class Location(MDFloatLayout, MDTabsBase):
    pass


class Database(MDFloatLayout, MDTabsBase):
    pass

class Register(MDFloatLayout, MDTabsBase):
    def registered(self, register):
        print("yes")


class RootLayout(MDFloatLayout):
    stop = threading.Event()


class comments(MDFloatLayout, MDTabsBase):
    pass


class MainMDApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Team Project Application"
        self.auth_key = "lj6Vvz1LRVOjS4u5bG25GNGL6uap2WJF9NRlPbpk"
        super().__init__(**kwargs)
        self.screen = Builder.load_file('main1.kv')
        self.screen = Builder.load_file('login.kv')
        return self.screen

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.ww = WindoManager(transition=FadeTransition())
        screens = [Home(name="screen"),Login(name="")]
        for screen in screens:
            self.ww.add_widget(screen)
        return self.ww
    def change_screen(self, screen):
        self.ww.current = "screen"

    # ADMINISTRATOR LOGIN CONFIRMATION
    def verify(self, email, password):
        if email != "admin":
            err = Snackbar(text="Enter correct Detail", md_bg_color=[0, 0.3, 0, 1])
            err.open()
        else:
            if password != "1234":
                err = Snackbar(text="Can't Open An Application ", md_bg_color=[0, 0.3, 0, 1])
                err.open()

            else:
                err = Snackbar(text="Success")
                err.open()
                #self.change_screen(screen="screen")
            # return Home()

    # checking the database users
    def databaseRegistry(self, database):
        config["databaseURL"] = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
        from_database = requests.get(url=config["databaseURL"] + '?auth=' + self.auth_key)
        new_label = self.root.ids.list
        for key, value in enumerate(from_database):
            print(key, value)
            widget = TwoLineListItem(text=f"{value}")
            new_label.add_widget(widget)
            new_label.text = str(key)
        # for data in database.json():
        # new_label.text =x.text
        # db = new_label.text="

    def delete(self, database):
        requests.delete(url=self.url[:-1] + database + ".json")

        config["apiKey"] = "AIzaSyB2BZjMWxuuWGCxYiy39nM2QW6YNaEYejM"

    def update(self, database):
        requests.put(url=self.url[:-1] + database + ".json")

    config["apiKey"] = "AIzaSyB2BZjMWxuuWGCxYiy39nM2QW6YNaEYejM"

    def registered(self, register):
        print("am working well")

    def emergencies(self, emergency):
        print()

    def get_location(self, location):

        root_tk.geometry(f"{1000}x{900}")
        root_tk.title("Location of The Target point")
        # create map widget
        map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
        map_widget.pack(fill="both", expand=True)

        # google normal tile server
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        map_widget.set_address(location, marker=True)

        root_tk.mainloop()

        def findLocation(self, location):
            self.url = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
            if len(location) == 2:
                err = Snackbar(text="NO Blank Space Allowed")
                err.open()
            else:
                if len(location) >= 3:
                    err = Snackbar(text="Sucess")

                    """JSON = {"userLocation": f"{location}"}
                    re = requests.patch(url=self.url, json=JSON)"""

    def add_Records(self, get_patient_record):
        print("Records are:")

    def commenting(self, comments):
        print(" here are the comments:")


MainMDApp().run()
