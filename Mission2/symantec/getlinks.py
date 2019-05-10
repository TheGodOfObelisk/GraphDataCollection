#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import xml.sax
 
class XmlHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.title = ""
      self.link = ""
      self.description = ""
      self.pubDate = ""

 
   # 元素开始事件处理
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "item":
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