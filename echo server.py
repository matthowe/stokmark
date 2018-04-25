# Echo server program
import socket

print("This Server IP address is",socket.gethostbyname(socket.gethostname()))

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 13000              # Arbitrary non-privileged port

def receive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print ('Connected by', addr)
    while 1:
        data = conn.recv(1024)
        print(data)
        if not data: break
        conn.sendall(data)
    conn.close()

receive()
