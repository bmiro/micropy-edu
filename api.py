#!/usr/bin/env python3

from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a simple Python/Flask API to capture POSTed data to /esp32-data'


@app.route('/esp32-data',  methods=['POST'])
def esp32_data():
    print("Received: ")
    print(request.json)
    return 'OK'
