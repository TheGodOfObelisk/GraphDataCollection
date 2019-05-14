#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb
import json
import sys
import os

def get_result_list(root_dir):
    try:
        dirs = os.listdir(root_dir)
    except:
        error_info = sys.exc_info()
        if len(error_info) > 1:
            print(str(error_info[0]) + ' ' + str(error_info[1]))
        else:
            print 'Unexpected error:can not get access to the root path of result'
        return -1
    return dirs
lists = []
db = MySQLdb.connect("localhost", "root", "123456", "net_test")
cursor = db.cursor()
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)

# 这些意义不明或者是太少了，没必要单独为其增加字段
miss_list = [u'', u'     Version', u' Note', u' Name', u' Version', u'NOTE ', 
u'Adware.Look2Me', u'Simplocker', u' LIFEMONITOR', u'ALERTA', u'For APK',
u'For Name', u'APK', u'APKs', u'Important', u'Keys', u'Optional', u'Varies'
, u'Icon', u'ERROR', u'NOTE', u'Note']

res_dirs = get_result_list("../Mission2/symantec/data/")
# print res_dirs
for dir_item in res_dirs:
    with open("../Mission2/symantec/data/" + dir_item, "r") as load_f:
        load_dict = json.load(load_f)
        for item in load_dict:
            key_list = item.keys()
            for i in key_list:
                if i in miss_list:
                    print "strange property"
                    print i
                    print "it is in " + dir_item
                if i not in lists:
                    # if len(i) > 20:
                    #     print "too long : " + i
                    #     print "it is in " + dir_item
                    # else:
                    #     lists.append(i)
                    if len(i) <= 20 and i not in miss_list:
                        lists.append(i)
                    ## 大于20的明显有误
print "TOTAL:"
print lists

        # try:
        #     cursor.execute("""
        #     insert into `symantec_data` (`content`) values(:va);
        #     """, va = item)
        # except:
        #     print "error!"
        #     error_info = sys.exc_info()
        #     if len(error_info) > 1:
        #         print(str(error_info[0]) + ' ' + str(error_info[1]))

db.close()