#!/bin/bash
APP_HOME=`pwd`
project=`grep 'name' $APP_HOME/conf/default.ini|awk -F= '{print $2}'|awk '{print $1}'`
bin=${project}_server
if [ ! -L $APP_HOME/bin/$bin ];then
	ln -s $APP_HOME/bin/server.py $APP_HOME/bin/$bin
fi
start() {
    nohup $bin >$APP_HOME/start.log 2>&1 &
}
stop() {
   count=`ps -ef|grep -v grep|grep $bin|wc -l`
   if [ $count -eq 1 ];then
	kill -9 `ps -ef|grep -v grep|grep $bin|awk '{print $2}'` 
   fi
}

status() {
	count=`ps -ef|grep -v grep|grep $bin|wc -l`
	if [ $count -eq 1 ];then
	   echo "server is running"
	else
	   echo "server is not running"
	fi
}

deploy() {
	crontab -l >/tmp/.crontab.test
	echo "59 23 * * * python $APP_HOME/bin/sql.py" >>/tmp/.crontab.test
	crontab /tmp/.crontab.test	
}


case $1 in 
start)
	start
	;;
deploy)
	deploy
	;;
stop)
	stop
	;;
restart)
	stop
	start
	;;
status)
	status
	;;
*)
	echo "Usage:$0 start|stop|deploy|restart|status"
	;;
esac
