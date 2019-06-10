import os
import rabbit
import random

from flask import Flask, request

rabbit.setup()
app = Flask(__name__)

@app.route("/")
def hello():
    user_agent = request.headers.get('User-Agent')
    queue = random.randint(1, int(os.environ['SCALE']))
    rabbit.send(str(queue), user_agent)
    return "Testing user agent stuff"
