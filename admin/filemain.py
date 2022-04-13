import pyrebase

from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import crypt

# teamproject-cbe48.firebaseapp.com
config = {
  "apiKey": "AIzaSyB2BZjMWxuuWGCxYiy39nM2QW6YNaEYejM",
  "authDomain": "isaifirst-434b9.firebaseapp.com",
  "databaseURL": "https://isaifirst-434b9-default-rtdb.firebaseio.com/",
  "projectId": "isaifirst-434b9",
  "storageBucket": "isaifirst-434b9.appspot.com",
  "messagingSenderId": "577271030988",
  "appId": "1:577271030988:web:976a274ab323063c248e69",
  "measurementId":"G-DRBH86S46X"

};
firebase = pyrebase.initialize_app(config)
# Getting reference to storage feature of Firebase
db = firebase.database()
db.child("users").child("Morty")
# Pass the user's idToken to the push method
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
