#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 仅完成type1数据带到type2数据的更新
# type2数据表示能与cnvd相关联的数据

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
    sys.exit(1)

def getCNVDIds(i):
    try:
        if i[1] == None:
            print "error! no cve number!"
            return
        sql = """
        select number from cve where cveNumber = "{cve}";
        """.format(cve = i[1])
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    except:
        err_log()

# 用于数据恢复,cnvdId拿$开头，类似下推自动机中的栈底符号
def resetVulnerability():
    try:
        cursor.execute("""
        update vulnerability set cnvdId = "$", type = 1;
        """)
        db.commit()
    except:
        err_log()

# 用于数据恢复
def resetMovedCol():
    try:
        cursor.execute("""
        update cnvd set moved = 0;
        """)
        db.commit()
    except:
        err_log()

# 接受一个id,更新moved字段
# moved为1代表被融合的，为0代表没被融合的
# 没被融合的cnvd需要在下一阶段以type=2存入vulnerability表中
def updateMovedCol(i): 
    sql = ""
    try:
        sql = """
        update cnvd set moved = 1 where number = "{cnvd}";
        """.format(cnvd = i)
        cursor.execute(sql)
        db.commit()
    except:
        print sql
        err_log()
    print "update moved successfully"

def updateCNVDIds(i, j):
    ids = ""
    sql = ""
    if len(i) == 0:
        return
    elif len(i) == 1:
        # i[0][0]就是想要的cnvdid
        ids = i[0][0]
        updateMovedCol(ids)
        try:
            sql = """
            update vulnerability set cnvdId = CONCAT(cnvdId,'',",{cnvd}"), type = 2 where id = {key} and not find_in_set("{cnvd}",cnvdId);
            """.format(cnvd = ids, key = j[0])
            print sql
            cursor.execute(sql)
            db.commit()
        except:
            print sql
            err_log()
    elif len(i) > 1:
        for k in i:
            for m in k:
                updateMovedCol(m)
                try:
                    sql = """
                    update vulnerability set cnvdId = CONCAT(cnvdId,'',",{cnvd}"), type = 2 where id = {key} and not find_in_set("{cnvd}",cnvdId);
                    """.format(cnvd = m, key = j[0])
                    print sql
                    cursor.execute(sql)
                    db.commit()
                except:
                    print sql
                    err_log()
    print "update cnvdids successfully"
    # 根据ids来更新vulnerability表中的cnvdid字段，以及cnvd表中的moved字段

# 先恢复
resetMovedCol()
resetVulnerability()
# 将nvd与cnvd关联起来
try:
    cursor.execute("""
    select id, cveId from vulnerability;
    """)
    data = cursor.fetchall()
    for item in data:
        cnvdids = getCNVDIds(item)
        # if len(cnvdids) > 1:
        #     print "!!!"
        #     print cnvdids
        updateCNVDIds(cnvdids, item)
except:
    err_log()

db.close()