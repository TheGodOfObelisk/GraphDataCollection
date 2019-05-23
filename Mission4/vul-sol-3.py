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

# 处理vulnerability表中类型为3的漏洞与solution的关系
# 类型为3的漏洞是纯CNVD的漏洞了

def getSolId(i):
    sql = """
    select id from solution where type = 2 and cnvdId = "{cnvdId}";
    """.format(cnvdId = i)
    try:
        cursor.execute(sql)
        res = cursor.fetchone()
        if res != None:
            return res[0]
        else:
            return None
    except:
        err_log()
        return None

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

def UpdateRelation(CNVDId, SolId):
    print "inserting..."
    insertVertex(CNVDId, 1)
    insertVertex(SolId, 5)
    outId = getVertexId(CNVDId, 1)
    inId = getVertexId(SolId, 5)
    if outId != None and inId != None:
        insertEdge(inId, outId, "hasSolution")
    else:
        print "fail to insert an edge"    

try:
    cursor.execute("""
    select id, cnvdId from vulnerability where type = 3;
    """)
    data = cursor.fetchall()
    for item in data:
        CNVDId = item[0]
        SolId = getSolId(item[1])
        if CNVDId == None or SolId == None:
            continue
        else:
            UpdateRelation(CNVDId, SolId)
except:
    err_log()

db.close()