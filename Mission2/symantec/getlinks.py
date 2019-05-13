#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import xml.sax
import sys
import re
import urllib3
import requests
import json
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')
global tmp_arr
tmp_arr = []

class XmlHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.title = ""
      self.link = ""
      self.description = ""
      self.pubDate = ""
      self.total = 0
      self.tmp_dict = {}
      self.count = 0
#    def write_json(self):
#       with open("data" + str(self.count) + ".json", w) as f:
#             global tmp_arr
#             f.write(json.dumps(tmp_arr))
#             tmp_arr = [] # 清空
   # 元素开始事件处理
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "item":
         print self.total
         self.total += 1
         if(self.link != ""):
               self.tmp_dict["x_title"] = self.title
               self.tmp_dict["x_link"] = self.link
               self.tmp_dict["x_description"] = self.description
               self.tmp_dict["x_pubDate"] = self.pubDate
               requests.packages.urllib3.disable_warnings()
               http = urllib3.PoolManager()
               # 先校验url格式
               if not re.match(r'^https?:/{2}\w.+$', self.link):
                     print "an invalid url!"
                     return
               r = http.request('GET', self.link)
               if r.status != 200:
                     print "Error occurred when GETTING url!!"
                     return
               html_doc = r.data.decode()
               soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
               res = soup.find_all(attrs={'name': 'panel-summary'})
               res_str = ""
               for i in res:
                     res_str = i.get_text()
                     res_arr = res_str.split('\n')
                     for item in res_arr:
                           an = re.search('.*: .*', item)
                           if an:
                                 print "yes!!!"
                                 print item
                                 tmp = item.split(": ")
                                 self.tmp_dict[tmp[0]] = tmp[1]
                           else:
                                 print "no!! "
               global tmp_arr
               tmp_arr.append(self.tmp_dict)
            #    print "*********************************"
            #    print tmp_arr
            #    self.tmp_dict.clear()
               print tmp_arr
               self.tmp_dict = {}
               if self.total >= 10:# 每10个存一个
                     with open("data" + str(self.count) + ".json", 'w') as f:
                           print "*******************************"
                           print tmp_arr
                           f.write(json.dumps(tmp_arr))
                           tmp_arr = []
                           self.total = 0
                           self.count += 1
         print "*****Item*****"
 
   # 元素结束事件处理
   def endElement(self, tag):
      if self.CurrentData == "title":
         print "Title:", self.title
      elif self.CurrentData == "link":
         print "Link:", self.link
      elif self.CurrentData == "description":
         print "Description:", self.description
      elif self.CurrentData == "pubDate":
         print "PubDate:", self.pubDate
      self.CurrentData = ""

 
   # 内容事件处理
   def characters(self, content):
      if self.CurrentData == "title":
         print "it is a title"
         self.title = content
      elif self.CurrentData == "link":
         self.link = content
      elif self.CurrentData == "description":
         self.description = content
      elif self.CurrentData == "pubDate":
         self.pubDate = content
  
if ( __name__ == "__main__"):
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)
 
   # 重写 ContextHandler
   Handler = XmlHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("srlisting.xml")
   with open('data.json', 'w') as f:
         f.write(json.dumps(tmp_arr))