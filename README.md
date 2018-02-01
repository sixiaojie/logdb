# logdb
select log into mysql
1.进入conf目录，修改项目名，添加数据库连接信息等

2.queue: 
	maxsize: 为内置的queue可接受的长度
	limit: 设置queue到什么量的时候处理请求
	usual: 与limit合用，多长时间检测一次limit
	all:   不管什么时候，都会讲queue的刷新到数据库，usual&all 都是以s为单位的

3.refresh
	可选项：day/month/year  代表：一天一张表，一月一张表。。。。。。

4.启动
	./manage.sh deploy
