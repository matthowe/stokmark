# Message Sender


import os
from socket import *
host = "127.0.0.1" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter message to send or type 'exit': ")
    data = str.encode(data)
    UDPSock.sendto(data, addr)
    if data == str.encode("exit"):
        break
UDPSock.close()
os._exit(0)
