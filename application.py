from flask import Flask
import json
import requests
application = Flask(__name__)

@application.route('/')
def hello_world():
   return "Hello World V2"

@application.post('/test')
def hello_world():
    return "test data"
