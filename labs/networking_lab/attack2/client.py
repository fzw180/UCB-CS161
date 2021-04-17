import socket
import argparse

parser = argparse.ArgumentParser(description='Start the client.')
parser.add_argument('--port', help='Port to attach server to', type=int)
PORT = parser.parse_args().port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostbyname('localhost')                           
    s.connect((host, PORT))                               

    while True:
        msg = s.recv(1024)
        print (msg.decode('ascii'))
except ConnectionRefusedError:
    print(f"Could not connect to server on port {PORT}. Have you run python server.py?")
except Exception as e:
    print(e)
    exit()
