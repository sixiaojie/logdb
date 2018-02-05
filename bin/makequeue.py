#!/usr/bin/env python
#coding:utf8
import Queue,time
from base import logger,config
import threading, json
from makesql import Make_Exec_Sql as sql


class test(object):
    def __init__(self):
	self.maxsize = int(config.get('queue','maxsize'))
	self.queue = Queue.Queue(maxsize=self.maxsize)
	self.file = config.get('queue','temp_file')+"/"+"insert"+"-"+time.strftime('%Y-%m-%d')
	self.limit = int(config.get('queue','limit'))
	self.lock = threading.Lock()
	self.usual = float(config.get('queue','usual'))
	self.all = float(config.get('queue','all'))
	self.sql = sql()
	
	self.f = self.write_log()
	self.run()
    def put(self,data):
	if self.queue.full():
	   self.Get_Queue_Into_Db() 
	   #print 'write %s to %s' %(data,self.file)
	   self.f.write('%s\n' %data)
	else:
	   self.queue.put(data) 

    def get(self):
	while True:
	    queue_data = []
	    if self.queue.qsize() >self.limit:
		if self.lock.acquire(False):
		    for i in range(self.queue.qsize()):
		   	 queue_data.append(json.loads(self.queue.get(timeout=1))) 
		    self.lock.release()
	    	    self.send(queue_data)
	    time.sleep(self.usual) 	
    
    def crontab(self):
	while True:
	     self.Get_Queue_Into_Db()
	     time.sleep(self.all)

    def Get_Queue_Into_Db(self):
	queue_data = []
	if self.queue.qsize()>0:
	  if self.lock.acquire(False):
	      for i in range(self.queue.qsize()):
		   queue_data.append(json.loads(self.queue.get(timeout=1)))
	      self.lock.release()
	      self.send(queue_data)

    def send(self,data):
	if not data:
	     return
	self.sql.parser(data)
    
    def write_log(self):
	f = open(self.file,'a+')
	return f

    def run(self):
	func = [self.get,self.crontab]
	do = []
	for i in range(len(func)):
	    do.append(threading.Thread(target = func[i]))
	for t in do:
	    t.setDaemon(True)
	    t.start()
	
