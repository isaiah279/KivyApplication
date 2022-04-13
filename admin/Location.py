"""import tkinter
from tkintermapview import TkinterMapView
from tkinter import ttk
from tkinter import *
def new_fun(self,*args):
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{600}x{400}")
    root_tk.title("map_view_simple_example.py")
    # create map widget
    map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
    map_widget.pack(fill="both", expand=True)

    # google normal tile server
    self = map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    map_widget.set_address('Nairobi', marker=True)

    root_tk.mainloop()
new_fun('yt')"""

import pyrebase

from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import crypt

config = {

    "apiKey": "AIzaSyB2BZjMWxuuWGCxYiy39nM2QW6YNaEYejM",

    "authDomain": "isaifirst-434b9.firebaseapp.com",

    "databaseURL": "https://isaifirst-434b9-default-rtdb.firebaseio.com/",

    "projectId": "isaifirst-434b9",

    " storageBucket": "isaifirst-434b9.appspot.com",

    "  messagingSenderId": "577271030988",

    " appId": "1:577271030988:web:bc9f35c4b8c6501b248e69",
    "measurementId": "G-K8KL14RGJG"

};
"""
firebase = pyrebase.initialize_app(config)
data = {}
db = firebase.storage()
db.child("users").push(data)
"""
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
files = storage.list_files()
for file in files:
    print(storage.child(file.name).get_url(None))
