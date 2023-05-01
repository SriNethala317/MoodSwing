
from flask import Flask, redirect, render_template, session, url_for, request, send_from_directory, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo
from os import environ as env
from dotenv import find_dotenv, load_dotenv
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import json


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
   return render_template("home.html")

@app.route("/registration", methods=['GET','POST'])
def registration():
    return render_template("registration.html")

@app.route("/registrationProcess", methods=['GET','POST'])
def registrationProcess():
    username = request.get_json()['usern']
    password = request.get_json()['pass']
    users.insert_one({"username":username, "password":password})
    return json.dumps('login')
    

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route("/loginProcess", methods=['GET','POST'])
def loginProcess():
    username = request.get_json()['usern']
    password = request.get_json()['pass']
    existing_details = users.find_one({"username": username, "password": password})
    if existing_details:
        return json.dumps(url_for('home'))
    else:
        return json.dumps(url_for('register'))

    





    
 
