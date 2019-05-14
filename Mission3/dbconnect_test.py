#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost", "root", "123456", "net_test")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
db.close()