#!/usr/bin/env python
#coding:utf8

from base import config,mysql,logger
import time, sys
project_name = config.get('project','name')
if config.get('refresh','shift_table') =="day":
	table = time.strftime('%Y%m%d')
elif config.get('refresh','shift_table') =='month':
	table = time.strftime('%Y%m')
elif config.get('refresh','shift_table') =="year":
	table = time.strftime('%Y')
elif config.get('refresh','shift_table') =="":
	table = time.strftime('%Y%m')
else:
	logger.logger('refresh values is mistakes')
	sys.exit(20)
table = project_name + '_' + table
try:
	engine = config.get('db','engine')
except:
	engine = 'innodb'

