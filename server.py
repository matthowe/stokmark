# Message Receiver

import os
from socket import *



#sets up server, to wait until x number of unique player IP addresses have been collected

host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)


import socket
print("This Server IP addrss is",socket.gethostbyname(socket.gethostname()))
players = int(input("How many players are you expecting? "))

print ("Waiting to receive messages...")

clients = []
counter = 0
while True:
    print(counter)
    counter = counter + 1
    (data, addr) = UDPSock.recvfrom(buf)
    data = (data).decode()
    if data not in clients:
        clients.append(data)
    print ("Received message: " + data)
    if len(clients) == players:
        break
##########################################################

    
UDPSock.close()
os._exit(0)
