#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb
import json
import sys
import os

db = MySQLdb.connect(
    host = "localhost", port = 3306, user = "root", 
    passwd = "123456", db = "net_test", charset = "utf8"
    )

cursor = db.cursor()

# 联系vulnerability与CVSSScore

def err_log():
    print "error"
    error_info = sys.exc_info()
    if len(error_info) > 1:
        print(str(error_info[0]) + ' ' + str(error_info[1]))

def getCVSSId(i):
    try:
        cursor.execute("""
        select id from CVSSScore where CVENumber = "{cveid}";
        """.format(cveid = i))
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

def UpdateRelation(CVEId, CVSSId):
    print "inserting..."
    print CVEId
    print CVSSId
    insertVertex(CVEId, 1)
    insertVertex(CVSSId, 2)
    outId = getVertexId(CVEId, 1)
    inId = getVertexId(CVSSId, 2)
    print outId
    print inId
    if outId != None and inId != None:
        insertEdge(inId, outId, "hasCVSSScore")
    else:
        print "fail to insert an edge"

try:
    cursor.execute("""
    select id, cveId from vulnerability where type <> 3;
    """)
    data = cursor.fetchall()
    # 没有和NVD关联起来的CNVD得不到这样的关系，因为CVSSScore是用NVD来标识的
    for item in data:
        print item
        CVEId = item[0]
        CVSSId = getCVSSId(item[1])
        if CVEId == None or CVSSId == None:
            continue
        else:
            UpdateRelation(CVEId, CVSSId)
except:
    err_log()

db.close()