from collections import ChainMap

dict1 = {"a":1, "b":2}
dict2 = {"b":1, "c":3}

cm = ChainMap(dict1, dict2)

print(cm.maps)
print(cm["b"])

