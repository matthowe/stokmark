# Message Sender

import os
import time
from socket import *

import msvcrt 



def sender(data):
    host = "127.0.0.1" # set to IP address of target computer
    port = 13000
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    data = str.encode(data)
    DPSock.sendto(data, addr)

    UDPSock.close()
    os._exit(0)

def reciever(data):
    host = ""
    port = 13000
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    (data, addr) = UDPSock.recvfrom(buf)
    data = (data).decode()
    return data

    #UDPSock.close()
    #os._exit(0)

def checkKey():
    return ord(msvcrt.getch()) if msvcrt.kbhit() else 0


while True:
    key = checkKey()
    print(key)
