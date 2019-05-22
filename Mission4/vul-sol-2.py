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

# 处理vulnerability表中类型为2的漏洞与solution的关系
# 这种情况最麻烦，以为要处理不止一对顶点