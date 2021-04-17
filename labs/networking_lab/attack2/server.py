import socket                                         
import time
import argparse

parser = argparse.ArgumentParser(description='Start the server.')
parser.add_argument('--port', help='Port to attach server to', type=int)
PORT = parser.parse_args().port

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostbyname('localhost')                           
serversocket.bind((host, PORT))                         

serversocket.listen(10000)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))

    msg = f'Opened a TCP connection on port {PORT}. Your goal is to terminate this connection via a RST Packet.'

    time.sleep(1)
    clientsocket.send(msg.encode('ascii'))

    i = 0
    while True:
        time.sleep(1)
        try:
            clientsocket.send(f'Heartbeat message {i}.'.encode('ascii'))
            i += 1
        except BrokenPipeError:
            print('-'*20)
            print("BrokenPipeError: this connection was terminated!\n")
            print("If you see this message directly after you ran your RST Injection Attack code, you successfully terminated the connection. Good job!")
            print()
            print("The code is: evanbot-is-sad")
            print()
            exit()
