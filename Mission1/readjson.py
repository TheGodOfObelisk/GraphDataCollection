import json
with open("./demo-data/address/address_0.json", "r") as load_f:
    load_dict = json.load(load_f)
# encodedjson = json.dump(load_dict)
# print(type(load_dict))
# print(type(encodedjson))
# print(encodedjson[1])
l1 = json.loads(load_dict)
print(l1["results"][0])