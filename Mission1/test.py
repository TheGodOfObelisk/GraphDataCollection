# import json
# str1 = "asdkasjdhal {\"count\":199865,\"results\":[{\"vertexType\":\"software\",\"_type\":\"vertex\",\"source\":[\"Hone\"],\"processPath\":\"\/usr\/bin\/gnome-panel\",\"description\":\"\/usr\/bin\/gnome-panel\",\"name\":\"\/usr\/bin\/gnome-panel\",\"processArgs\":\"gnome-panel\",\"processPid\":2660,\"processPpid\":2401,\"_id\":2210304}],\"success\":true,\"version\":\"2.5.0\",\"queryTime\":2119.135322}"
# str2 = str1.split('{', 1)
# str3 = "{" + str2[1]
# print(str3)
# with open("./demo-data/test.json", "w") as f:
#     json.dump(str3, f)
#     print("write over")

t = ((u'CNVD-2018-11403',), (u'CNVD-2018-11403',))
t1 = ((u'CNVD-2018-11403',))
# for i in t1:
#     print i
print t1[0]