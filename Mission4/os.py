#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb
import json
import sys
import os

def err_log():
    print "error"
    error_info = sys.exc_info()
    if len(error_info) > 1:
        print(str(error_info[0]) + ' ' + str(error_info[1]))


db = MySQLdb.connect(
    host = "localhost", port = 3306, user = "root", 
    passwd = "123456", db = "net_test", charset = "utf8"
    )

cursor = db.cursor()

# 分析软件列表，按照之前说好的，分为os，application，hardware

def insertOS(i):
    sql = """
    insert into OS  (`Name`) values ("{o}");
    """.format(o = i)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        err_log()

try:
    cursor.execute("""
    select distinct product from vulnerablesoftwarelist where product like '%/o:%';
    """)
    data = cursor.fetchall()
    for item in data:
        print item[0]
        insertOS(item[0])
except:
    err_log()

db.close()