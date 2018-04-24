# Message Sender


import os
from socket import *


# connnect to a server to send ip address
server = input("Server IP address ")
host = ""
port = 13000
buf = 1024
addr = (server, port)
recaddr = (host, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)

import socket
ipAddress = (socket.gethostbyname(socket.gethostname()))


#keeps sending ip  address until server sends message back saying it received
#client ip address
from socket import *
counter = 0
while True:
    print(counter)
    counter = counter + 1
    data = str.encode(ipAddress)
    UDPSock.sendto(data, addr)


    #receivedData = (receivedData).decode()
    #print("receiving message")
    #if recievedData == str.encode("exit"):
    #    break
#print("complete")
#####################################
UDPSock.close()
os._exit(0)
