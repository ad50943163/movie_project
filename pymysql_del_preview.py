# -*- coding:utf-8 -*- 
#!/usr/bin/env python
# @Author  : tianbao
# @Contact : gmu1592618@gmail.com
# @Time    : 2018/5/13 9:55
# @File    : pymysql_del_preview.py
# @Software: PyCharm
import pymysql

connect = pymysql.connect(  # 连接数据库服务器
    user="root",
    password="root",
    host="205.266.87.91",
    port=3306,
    db="movie",
    charset="utf8"
)
conn = connect.cursor()        #创建操作游标

conn.execute("SELECT * FROM user")    #选择查看自带的user这个表  (若要查看自己的数据库中的表先use XX再查看)
rows = conn.fetchall()                #fetchall(): 接收全部的返回结果行，若没有则返回的是表的内容个数 int型
for i in rows:
    print(i)

conn.execute("drop table preview")

conn.close()           #   关闭游标连接
connect.close()        #   关闭数据库服务器连接 释放内存