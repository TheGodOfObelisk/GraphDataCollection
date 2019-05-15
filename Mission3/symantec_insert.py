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

def convert2field(src):
    if src == u'Risk Impact':
        return u'Risk_Impact'
    elif src == u'Infection Length':
        return u'Infection_Length'
    elif src == u'Systems Affected':
        return u'System_Affected'
    elif src == u'Writeup By':
        return u'Writeup_By'
    elif src == u'File Names':
        return u'File_Names'
    elif src == u'Also Known As':
        return u'Also_Known_As'
    elif src == u'Target Platform':
        return u'Target_Platform'
    elif src == u'Region Reported':
        return u'Region_Reported'
    elif src == u'Area of infection':
        return u'Area_of_infection'
    elif src == u'Package name':
        return u'Package_name'
    elif src == u'CVE References':
        return u'CVE_References'
    else:
        return src

lists = []

db = MySQLdb.connect(
    host = "localhost", port = 3306, user = "root", 
    passwd = "123456", db = "net_test", charset = "utf8"
    )
cursor = db.cursor()

# 这些意义不明或者是太少了，没必要单独为其增加字段
miss_list = [u'', u'     Version', u' Note', u' Name', u' Version', u'NOTE ', 
u'Adware.Look2Me', u'Simplocker', u' LIFEMONITOR', u'ALERTA', u'For APK',
u'For Name', u'APK', u'APKs', u'Important', u'Keys', u'Optional', u'Varies'
, u'Icon', u'ERROR', u'NOTE', u'Note', u'Message', u'ALERT', u'Trigger date',
u'Application Name', u'Title']

res_dirs = get_result_list("../Mission2/symantec/data/")

print "Step1: analyze data source and extract useful fields"
for dir_item in res_dirs:
    with open("../Mission2/symantec/data/" + dir_item, "r") as load_f:
        load_dict = json.load(load_f)
        for item in load_dict:
            key_list = item.keys()
            for i in key_list:
                if i not in lists:
                    if len(i) <= 20 and i not in miss_list:
                        lists.append(i)
                        # lists_with_length.append(i + ": " + str(len(item[i])))
                    ## 大于20的明显有误
print "TOTAL:"
print lists

# fields of TABLE symantec
# id, x_description, x_link, x_title, Updated, Risk_Impact, Infection_Length, 
# x_pubDate, Type, System_Affected, Name, Writeup_By, Version, Publisher, 
# File_Names, Discovered, Also_Known_As, Target_Platform, Characteristics, 
# Region_Reported, Area_of_infection, Likelihood, Package_name, CVE_References

print "Step2: analyze data source and store it into MYSQL"
for dir_item in res_dirs:
    with open("../Mission2/symantec/data/" + dir_item, "r") as load_f:
        load_dict = json.load(load_f)
        for item in load_dict:
            key_list = item.keys()
            sql_cols = []
            sql_vals = []
            for i in key_list:
                if i in lists:
                    # 这里才是我们所关心的数据，分为字段类型和字段值
                    sql_cols.append(convert2field(i))
                    sql_vals.append(item[i])
            count = 0
            cols = ""
            vals = ""
            for j in sql_cols:
                # print count
                count += 1
                if count == len(sql_cols):
                    cols += ("`" + j + "`")
                else:
                    cols += ("`" + j + "`")
                    cols += ','
            count = 0
            for j in sql_vals:
                # print count
                count += 1
                if count == len(sql_vals):
                    vals += ("\"" + j + "\"")
                else:
                    vals += ("\"" + j + "\"")
                    vals += ','
            sql = "insert into `symantec` (" + cols + ") values (" + vals + ");"
            print sql
            try:
                cursor.execute(sql)
                db.commit()
            except:
                print "error!"
                error_info = sys.exc_info()
                if len(error_info) > 1:
                    print(str(error_info[0]) + ' ' + str(error_info[1]))
                db.rollback()


db.close()