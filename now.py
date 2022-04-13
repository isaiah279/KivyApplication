'''from kivy.storage.jsonstore import JsonStore


def start_backup(self):
    store = JsonStore("user.json")

    def check_reg():
        email = store.get("userdata")["email"]
        if email != "":
            print(f"your screen is:")
        else:
            print("Enter the following credentials")
            print("enter email account ")
            name = input(f"register {email}")
            password = input("Password")
            store.put("userdata", email=name, password=password)

    try:
        check_reg()
    except:
        store.put("User data", email="", password="")
        print("file not available creating a file")
        check_reg()
'''
import random
import pyrebase

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
id = random.randint(0, 1000)
firebase = pyrebase.initialize_app(config)
# Getting reference to storage feature of Firebase
db = firebase.database()
data = {"name": "john", "phone": "099876", "location": "Nakuru"}
db.child("users").child("USER-ID").child(f"UserId{id}").set(data)
