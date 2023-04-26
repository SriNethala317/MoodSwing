
from flask import Flask, redirect, render_template, session, url_for, request, send_from_directory, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo
from os import environ as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()

if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")
cluster = env.get("MONGODB_CLUSTER")
client = MongoClient(cluster)
db = client['MoodSwing']
users = db['users']

@app.route("/")
def get_index():
    users.insert_one({"name":"test"})
    return "working"
