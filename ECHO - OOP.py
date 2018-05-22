# Echo client program

import socket

class Network:


    def __init__(self):

        # +HOST ADDRESS
        # +PORT ADDRESS

        choice = False
        while choice != "s" and choice != "":
            print("[s + enter] Server")
            print("[enter] Client")
            choice = input()

        if choice == "s":
            print("This Server IP address is",socket.gethostbyname(socket.gethostname()))

            self.HOST = ''                 # Symbolic name meaning all available interfaces for server
            self.PORT = 13000              # Arbitrary non-privileged port

            print(self.receive())


        else:
            self.HOST = input("Server IP address ") 
            self.PORT = 13000              # The same port as used by the server

            self.registerIP()

        print(self.HOST)



    

    def receive(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #opens socket
        s.bind((self.HOST, self.PORT))
        s.listen(1)
        conn, addr = s.accept()
        print ('Connected by', addr[0])
        while 1:
            capture = conn.recv(1024)
            data = capture.decode('UTF-8')
            return(data)
            if not data: break
            conn.sendall(data)
        conn.close()

    def send(self,data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        data = socket.gethostbyname(socket.gethostname())
        data = str.encode(data)
        s.sendall(data)
        data = s.recv(1024)
        s.close()
        print ('Received', data)

    def registerIP(self):
        data = socket.gethostbyname(socket.gethostname())
        self.send(data)
        


    def receiveData(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        print ('Connected by', addr[0])
        while 1:
            capture = conn.recv(1024)
            data = capture.decode('UTF-8')
            return(data)
            if not data: break
            conn.sendall(data)
        conn.close()

    def sendData(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        data = socket.gethostbyname(socket.gethostname())
        data = str.encode(data)
        s.sendall(data)
        data = s.recv(1024)
        s.close()
        print ('Received', data)

run = Network()

