#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb
import json
import sys
import os
import re

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

f = open('test.txt', 'r')
pattern = re.compile(r'Process \d+')
line = 1
while line:
    line = f.readline()
    line = line[:-1]
    str1 = ' '.join(line.split())
    if 'Process' in str1:
        res = re.findall(pattern, str1)
        print res[0]
        str1 = str1.split(res[0] + ' ')
        print str1[1]
        id = res[0].split(' ')
        id = int(id[1])
        info = str1[1]
        try:
            sql = ""
            st = ""
            if "exit" not in info:
                st = "running"
            else:
                st = "exited"
            sql = """
            insert into Process (`ProcessId`, `ProcessInfo`, `Status`, `SystemId`)
            values ({pid}, "{pinfo}", "{status}", 1);
            """.format(pid = id, pinfo = info, status = st)
            cursor.execute(sql)
            db.commit()
        except:
            err_log()
f.close()
db.close()