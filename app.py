from flask import Flask, redirect, render_template, session, url_for, request, send_from_directory, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo
from os import environ as env
import os
from dotenv import find_dotenv, load_dotenv
import json
from spotify_songs import *


from spotify_songs import * 

ENV_FILE = find_dotenv()

if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")
cluster = env.get("MONGODB_CLUSTER")
client = MongoClient(cluster)
db = client['MoodSwing']
users = db['Users']

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/registrationProcess", methods=['GET','POST'])
def registrationProcess():
    username = request.get_json()['usern']
    password = request.get_json()['pass']
    users.insert_one({"username":username, "password":password})
    return json.dumps('/login')
    
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginProcess", methods=['GET','POST'])
def loginProcess():
    username = request.get_json()['usern']
    password = request.get_json()['pass']
    existing_details = users.find_one({"username": username, "password": password})
    if existing_details:
        return json.dumps('/survey2')
    else:
        return json.dumps('/signup')
    
@app.route('/songs/<path:path>')
def send_song(path):
    return send_from_directory('./song_downloads/', path)

@app.route('/music-player')
def musicPlayer():
    return render_template("music-player.html")

@app.route('/getSong', methods=['POST'])
def get_song_info():
    check = request.get_json()['check']
    song = get_song()
    return jsonify(song.get_song_info())

@app.route('/survey2')
def survey2():
    return render_template("survey2.html")
    




    





    
 
