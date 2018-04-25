# Echo client program
import socket
HOST = input("Server IP address ")

PORT = 13000              # The same port as used by the server

def send(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = socket.gethostbyname(socket.gethostname())
    data = str.encode(data)
    s.sendall(data)
    data = s.recv(1024)
    s.close()
    print ('Received', repr(data))

def registerIP():
    data = socket.gethostbyname(socket.gethostname())
    send(data)

registerIP()
