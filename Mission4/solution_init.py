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

def insertCNVD2Sol(id, cnvdnumber):
    sql = """
    insert into solution (`cnvdId`, `type`, `origin_id`) values ("{cnvdid}", 2, "{ori_id}");
    """.format(cnvdid = cnvdnumber, ori_id = id)
    try:
        print sql
        cursor.execute(sql)
        db.commit()
    except:
        err_log()

def insertNVD2Sol(id, nvdnumber):
    sql = """
    insert into solution (`cveId`, `type`, `origin_id`) values ("{cveid}", 1, "{ori_id}");
    """.format(cveid = nvdnumber, ori_id = id)
    try:
        print sql
        cursor.execute(sql)
        db.commit()
    except:
        err_log()

# 初始化solution表，将NVD的和CNVD的内容导入
try:
    cursor.execute("""
    select id, number from cnvd;
    """)
    data = cursor.fetchall()
    for item in data:
        print item[0]
        print item[1]
        insertCNVD2Sol(item[0], item[1])
except:
    err_log()

try:
    cursor.execute("""
    select id, number from reference;
    """)
    data = cursor.fetchall()
    for item in data:
        print item[0]
        print item[1]
        insertNVD2Sol(item[0], item[1])
except:
    err_log()

db.close()