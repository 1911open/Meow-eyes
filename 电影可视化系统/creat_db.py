# -*- coding: utf-8 -*-
# Time    : 2019/12/23 16:21
# Author  : 辛放
# Email   : 1374520110@qq.com
# ID      : SZ160110115
# File    : creat_db.py
# Software: PyCharm

import pymysql
def creat_db():
    db = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306)
    cursor = db.cursor()
    sql = 'CREATE DATABASE IF NOT EXISTS maoyan'
    cursor.execute(sql)
    db.close()
    db = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306, db='maoyan')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS films (name VARCHAR(255),time VARCHAR(255), type1 VARCHAR(255), type2 VARCHAR(255), type3 VARCHAR(255), type4 VARCHAR(255), type5 VARCHAR(255), country VARCHAR(255), length VARCHAR(255), year int,month int,day int,director VARCHAR(255),actor1 VARCHAR(255),actor2 VARCHAR(255),actor3 VARCHAR(255),actor4 VARCHAR(255), score VARCHAR(255), people INT, box_office BIGINT, PRIMARY KEY (name))'
    cursor.execute(sql)
    sql = 'CREATE TABLE IF NOT EXISTS userinfo (name VARCHAR(255),password VARCHAR(255),PRIMARY KEY (name))'
    cursor.execute(sql)
    db.close()

if __name__=="__main__":
    creat_db()