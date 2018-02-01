#!/usr/bin/env python
#coding:utf8

import MySQLdb,os,time,sys
from ConfigParser import ConfigParser
current_dir=os.path.dirname(os.path.abspath(__file__))
default_config=current_dir+"/../conf/default.ini"

class Config(object):
     def __init__(self):
	self.config = default_config
	self.con = self.parser()	
     def parser(self):
	cf = ConfigParser()
	cf.read(self.config)
	return cf

class Logger(object):
     def __init__(self):
	self.con = self.con_Get()	
	self.logfile = self.logfile()
     def con_Get(self):
	con = Config()
	return con.con

     def logfile(self):
	directory = self.con.get('log','log')
	if not os.path.exists(directory):
	     os.mkdir(directory)
	if not directory.endswith('/'):
		directory += "/"	
	name = self.con.get('project','name')
	logfile = directory+name+time.strftime('%Y-%m-%d')
	return logfile	

     def logger(self,msg):
	f = open(self.logfile,'a+')
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	print >>f,"[%s] %s" %(now,msg)
	f.close()

		
Con = Config()
config = Con.con
logger = Logger()
