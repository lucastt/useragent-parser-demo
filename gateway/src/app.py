import os
import rabbit
import random

from flask import Flask, request

rabbit.setup()
app = Flask(__name__)

@app.route("/")
def hello():
    user_agent = request.headers.get('User-Agent')
    rabbit.send(user_agent, random.randint(1, os.environ['SCALE']))
    return "Testing user agent stuff"
