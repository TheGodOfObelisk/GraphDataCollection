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
# 处理vulnerability表中的漏洞和hardware的关系，按照目前的数据源，仅有CVE的
# 只关心type为1或者2的漏洞

def getHardwareId(i):
    sql = """
    select id from Hardware where Name = "{name}";
    """.format(name = i)
    try:
        cursor.execute(sql)
        res = cursor.fetchone()
        if res != None:
            return res[0]
        else:
            return None
    except:
        err_log()

def getCVEId(i):
    sql = """
    select id from vulnerability where cveId = "{cve}" and type <> 3;
    """.format(cve = i)
    try:
        cursor.execute(sql)
        res = cursor.fetchone()
        if res != None:
            return res[0]
        else:
            return None
    except:
        err_log()

def insertVertex(i, t):
    try:
        sql = """
        insert into `vertex` (`type`, `id_search`) values ({m}, {n});
        """.format(m = t, n = i)
        print sql
        cursor.execute(sql)
        db.commit()
    except:
        err_log()
        db.rollback()

def getVertexId(i, t):
    try:
        sql = """
        select id from `vertex` where type = {m} and id_search = {n};
        """.format(m = t, n = i)
        print sql
        cursor.execute(sql)
        res = cursor.fetchone()
        if res != None:
            return res[0]
        else:
            return None 
    except:
        err_log()
        return None

def insertEdge(inId, outId, rel):
    try:
        sql = """
        insert into `Edges` (`type`, `in_vertex_id`, `out_vertex_id`) values ("{relation}", {m}, {n});
        """.format(relation = rel, m = inId, n = outId)
        print sql
        cursor.execute(sql)
        db.commit()
    except:
        err_log()
        db.rollback()

def UpdateRelation(CVEId, HardwareId):
    print "inserting..."
    insertVertex(HardwareId, 4) # 我知道hardware还没插
    # vulnerability大概率不用插
    outId = getVertexId(CVEId, 1)
    inId = getVertexId(HardwareId, 4)
    if outId == None: # 可能是vulnerability真的没插
        insertVertex(CVEId, 1)
        outId = getVertexId(CVEId, 1)
    if outId != None and inId != None:
        insertEdge(inId, outId, "affect")
    else:
        print "fail to insert an edge"    
try:
    cursor.execute("""
    select number, product from vulnerablesoftwarelist where product like '%/h:%';
    """)
    data = cursor.fetchall()
    for item in data:
        CVEId = getCVEId(item[0])
        HardwareId = getHardwareId(item[1])
        if CVEId == None or HardwareId == None:
            continue
        else:
            UpdateRelation(CVEId, HardwareId)
except:
    err_log()

db.close()