import json

fajl = open("fajl.json", mode="r")

x = json.load(fajl)
print(x)
nov_dict = {"id": 1, "name": "John Doe", "position": "Manager", "salary": 50000}
x['employees'].append(nov_dict)

fajl = open("fajl.json", mode="w")
json.dump(x, fajl)



