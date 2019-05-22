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