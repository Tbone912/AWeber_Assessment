from flask import Flask
from backEnd import *
app = Flask(__name__)

@app.route("/")
def home():
    return '<html><body><h1>Hello World</h1></body></html>'