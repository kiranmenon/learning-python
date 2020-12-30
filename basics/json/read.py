import json

with open('test.json', 'r') as jsonFile:
    data = jsonFile.read()

print("Data read from file: {0}".format(data))

js = json.loads(data)
print("Type of data loaded: {0}".format(type(js)))
print(js)

