# app.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to https://cs161.org.

"""
Network Security: Coffee Shop Attacks
ATTACK #1: Server-Side Logic

This file simulates a web server fulfilling POST requests to http://127.0.0.1:5000/api/login.
"""
import argparse
from flask import Flask, jsonify, request
import hashlib
import json
import base64
import os

parser = argparse.ArgumentParser(description='Start the server.')
parser.add_argument('--port', help='Port to attach server to', type=int)
PORT = parser.parse_args().port

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    password_hash = hashlib.md5(password.encode()).hexdigest()
    if username == 'eb@berkeley.edu' and password_hash == "e283cd40ae2dea30587a3ca18c449e2e":
        success = "Congratulations! Your exploit succeeded."
    else:
        success = "Incorrect password!"

    return jsonify({'success': success})

if __name__ == '__main__':
    app.run(debug=False, port=PORT)
