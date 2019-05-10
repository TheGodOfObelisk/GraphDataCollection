import json
b = []
a = {}
str1 = "haha"
a[str1] = "das"
a["hh"] = "dasd"
a["cc"] = "dasfas"
b.append(a)
a.clear()
a[str1] = "das"
a["hh"] = "dasd"
b.append(a)


with open('data.json', 'w') as json_file:
    json_file.write(json.dumps(b))
print(a)
a.clear()
print(a)