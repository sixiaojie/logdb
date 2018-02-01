#!/usr/bin/env python
from base import logger,config
import sys,json
from collections import OrderedDict
from crontab import table
from db import Mysql

class Make_Exec_Sql(object):
    def __init__(self):
	self.table = table
	self.database = config.get('db','database')
	self.mysql = Mysql()
	self.table_column = self.table_framework()
	self.sql = self.combination()
	self.file = config.get('db','fail')

    def combination(self):
	length = len(self.table_column)
	sql = "insert into %s" %(table)
	sql += '('
	for i in range(length):
		if i == length -1:
			sql += self.table_column[i]
		else:
			sql = sql + self.table_column[i] + ','
	sql += ") values"
	sql = sql + "("+"%s,"*(length-1) +"%s" +");"
	return sql

    def parser(self,data):
	data = self.convert(data)
	all_data = []
	length = len(data)
	for i in range(length):
	    all_data.append(tuple(data[i]))
	try:
    		self.mysql.insertMany(self.sql,all_data)
	except Exception,e:
		self.f.write(json.dumps(data))
		logger.logger(str(e))
    def write(self):
	self.f = open(self.file,'a+')

    def table_framework(self):
	sql = 'desc %s.%s;' %(self.database,self.table)
	try:
		table_info = self.mysql.getAll(sql)
	except Exception,e:
		logger.logger(str(e)+sql)
	table = []
	for item in table_info:
	    if item['Extra'] == "auto_increment" and item['Key'] =="PRI":
		continue
	    else:
		table.append(item['Field'])
	return table

    def convert(self,input):
    	if isinstance(input, dict):
        	return {self.convert(key): convert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
        	return [self.convert(element) for element in input]
    	elif isinstance(input, unicode):
        	return input.encode('utf-8')
    	else:
        	return input
 
