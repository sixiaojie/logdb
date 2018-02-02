#!/usr/bin/env python
from socket import *
import json,sys,time

host = '127.0.0.1'
port = 12345

buffsize = 1024
addr = (host, port)
udpClientSocket = socket( AF_INET, SOCK_DGRAM )
a='status'
udpClientSocket.sendto(a,addr)
recvdata, addr = udpClientSocket.recvfrom(1024)
print recvdata

udpClientSocket.close()
