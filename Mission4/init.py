#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 仅完成type1数据的插入

import MySQLdb
import json
import sys
import os

db = MySQLdb.connect(
    host = "localhost", port = 3306, user = "root", 
    passwd = "123456", db = "net_test", charset = "utf8"
    )

cursor = db.cursor()

def err_log():
    print "error"
    error_info = sys.exc_info()
    if len(error_info) > 1:
        print(str(error_info[0]) + ' ' + str(error_info[1]))

# 初始情形，type都是1, cveId, cnvdId和type构成组合唯一性约束，防止重复插入
# summary中可能本身含有双引号，所以这里试试单引号。
def insertInitItem(item):
    sql = ""
    try:
        if item[3] == None:
            sql = """
            insert into vulnerability (`cveId`, `publishedDatetime`, `lastModifiedDatetime`, `type`) values 
            ("{cve}", "{pub}", "{last}", 1);
            """.format(cve = item[0], pub = item[1], last = item[2])
        else:
            sql = """
            insert into vulnerability (`cveId`, `publishedDatetime`, `lastModifiedDatetime`, `cweId`, `type`) values 
            ("{cve}", "{pub}", "{last}", "{cwe}", 1) ;
            """.format(cve = item[0], pub = item[1], last = item[2], cwe = item[3])
        cursor.execute(sql)
        print "success"
        db.commit()
    except:
        print "failure"
        print sql
        err_log()

def clearVulnerability():
    try:
        cursor.execute("""
        delete from vulnerability;
        """)
        db.commit()
    except:
        err_log()


# 初始化vulnerability表，需要整合CNVD和NVD信息
try:
    cursor.execute("""
    select distinct number, publishedDatetime, lastModifiedDatetime, cweId from
    entry;
    """)
    data = cursor.fetchall()
    for item in data:
        insertInitItem(item)
except:
    err_log()

db.close()