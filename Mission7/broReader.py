#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
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

cmd = "awk '/^[^#]/ {print $3, $5, $6}' host-summary.log"
sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
str1 = sub.stdout.read()
sub.communicate()
str1 = str1.decode()
items = str1.split('\n')
for item in items:
    if item != "":
        res = item.split(' ')
        ips = res[0]
        hostname = res[1]
        mac = res[2]
        if "192.168.1." in ips:
            ip_arr = ips.split(',')
            print ip_arr
            print ip_arr[len(ip_arr) - 1] # the latest ip
            ipp = ip_arr[len(ip_arr) - 1].split('|')
            ipt = ipp[1]
            ltt = ipp[0]
            print hostname
            print mac
            # avoid to insert duplicated System
            sql = """
            update `System` set `LastUpdate` = "{lt}" where `MACAddress` = "{ma}" and `IPV4` = "{ip_t}"
            """.format(lt = ltt, ma = mac, ip_t = ipt)
            try:
                print sql
                cursor.execute(sql)
                db.commit()
            except:
                err_log()
            sql = """
            insert into `System` (`MACAddress`, `DefaultGateway`, `IPV4`, `LastUpdate`, `Name`) select 
            "{ma}", "192.168.1.1", "{ip_t}", "{lt}", "{hn}" from DUAL where not exists
            (select `id` from `System` where `MACAddress` = "{ma}")
            """.format(ma = mac, ip_t = ipt, lt = ltt, hn = hostname)
            try:
                print sql
                cursor.execute(sql)
                db.commit()
            except:
                err_log()
    else:
        print "empty!"

db.close()