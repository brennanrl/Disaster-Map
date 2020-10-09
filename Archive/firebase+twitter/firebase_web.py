import json
import requests
import unidecode
import urllib.parse as uparse
import time
from flask import Flask, request, jsonify
import pickle
import numpy as np
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./creds.json")
firebase_admin.initialize_app(cred, {
  "databaseURL": "https://saved-fb17a.firebaseio.com/"
})

app = Flask(__name__)

@app.route('/map', methods=['GET'])
def api():
    start = time.time()
    disasters = db.reference().child("incidents").get()
    print(disasters)
    end = time.time()
    time_diff = end - start
    return jsonify({"disasters": disasters})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=444)