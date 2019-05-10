#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import urllib3
import requests

from bs4 import BeautifulSoup
#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
requests.packages.urllib3.disable_warnings()
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 通过request()方法创建一个请求：
r = http.request('GET', 'http://www.symantec.com/security_response/writeup.jsp?docid=2000-122015-2208-99')
print(r.status)

html_doc = r.data.decode()

soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")

# p_node = soup.find('div', class_='content')
# print(p_node)
# print(soup.div.attrs)
# print(soup.find_all(name='p'))
res = soup.find_all(attrs={'name': 'panel-summary'})
res_str = ""
for i in res:
    print('***')
    print(type(i))
    res_str = i.get_text()
    res_arr = res_str.split('\n')
    # print(res_arr)
    for item in res_arr:
        an = re.search('.*: .*', item)
        if an:
            print(item)
            tmp = item.split(': ')
            print(tmp)
        else:
            print('no!! ' + item)
    # res_arr = re.match(r'(.*): (.*)', res_str)
    # print(res_arr)
