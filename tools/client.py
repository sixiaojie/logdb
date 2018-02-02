#!/usr/bin/env python
from socket import *
import json,sys,time

host = '127.0.0.1'
port = 12345

buffsize = 1024
addr = (host, port)
udpClientSocket = socket( AF_INET, SOCK_DGRAM )
#a = ['name','tet']
#udpClientSocket.sendto( json.dumps(a), addr )
#sys.exit(0)
a = ['{65C744BC-366B-98B9-D4C7-70B1595D32CC}',1,'65C744BC-366B-98B9-D4C7-70B1595D32CC','10.105.104.190','','','127.0.0.1','','','','302','Found',0.0000290871,'HEAD']
udpClientSocket.sendto(json.dumps(a),addr)
#recvdata, addr = udpClientSocket.recvfrom(1024)
#print recvdata

for i in range(10000):
    print i
    udpClientSocket.sendto( json.dumps(a), addr )
    time.sleep(0.05)
udpClientSocket.close()
