#!/usr/bin/env python
#coding:utf8
from crontab import table,engine
from db import Mysql
mysql = Mysql()
sql = '''
create table if not exists `%s` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `log_id` varchar(128) NOT NULL DEFAULT '',
  `log_type` int(10) unsigned NOT NULL DEFAULT '0',
  `domain` varchar(128) NOT NULL DEFAULT '',
  `server_ip` varchar(128) NOT NULL DEFAULT '',
  `username` varchar(128) NOT NULL DEFAULT '',
  `email` varchar(128) NOT NULL DEFAULT '',
  `user_ip` varchar(128) NOT NULL DEFAULT '',
  `api_name` varchar(128) NOT NULL DEFAULT '',
  `params` varchar(4096) NOT NULL DEFAULT '',
  `http_code` varchar(16) NOT NULL DEFAULT '',
  `err_code` varchar(32) NOT NULL DEFAULT '',
  `err_message` varchar(128) NOT NULL DEFAULT '',
  `spend_time` float NOT NULL DEFAULT '0',
  `request_method` varchar(128) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `index_log_id` (`log_id`),
  KEY `index_username` (`username`)
) ENGINE=%s DEFAULT CHARSET=utf8
''' %(table,engine)
mysql._cursor.execute(sql)
