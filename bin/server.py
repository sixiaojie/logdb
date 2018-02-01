#!/usr/bin/env python
#coding:utf8
import socket
import time,sys,json
import threading
from base import config,logger
from makequeue import test
try:
        ip = config.get('project','ip')
        port = config.get('project','port')
except:
        logger.logger('need bind ip,port')
        sys.exit(10)

class Udpsocket(object):
     def __init__(self):
	self.udpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	self.udpServerSocket.bind((ip,int(port)))
        self.buffer_size = 1024
	self.queue = test()

     "这里可以写一些监控"
     def receive(self):
	raw_data, addr = self.udpServerSocket.recvfrom(int(self.buffer_size))
	if raw_data == "status":
	    size=self.queue.queue.qsize()
	    self.send(addr,str(size))
	    raw_data = False
	#print 'conn from:',addr
	#print 'receive from udp client:', raw_data
	return (raw_data,addr)

     def process(self,data):
	self.queue.put(data)


     def send(self,addr,result):
	self.udpServerSocket.sendto(result,addr)

     def listen(self):
	while True:
	     socket_data = self.receive()
	     if socket_data[0]:
	     	self.process(socket_data[0])
	     #self.send(socket_data[1],str(result))

     def close():
	self.udpServerSocket.close()




if __name__ =="__main__":
	p = Udpsocket()
	p.listen()
