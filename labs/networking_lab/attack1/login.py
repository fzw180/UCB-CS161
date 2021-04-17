import argparse
import base64
import requests
import json

parser = argparse.ArgumentParser(description='Start the login.')
parser.add_argument('--port', help='Port to attach server to', type=int)
PORT = parser.parse_args().port

try:
    requests.post(f'http://127.0.0.1:{PORT}/api/login', data=json.dumps({
        'username': 'evanbot',
        'password': 'bot>human'
    }))
    print("Successfully simulated a login event!")
except requests.exceptions.ConnectionError:
    print("A connection error occurred. Have you started the web server by running app.py?")
