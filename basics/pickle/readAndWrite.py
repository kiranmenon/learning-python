import pickle

data = {"Name": "Kiran", "Hobbies": ["electronics", "programming", "cad"]}

with open("dump.pickle", 'wb') as pickleFile:
    pickle.dump(data, pickleFile)

with open("dump.pickle", 'rb') as pickleFile:
    dataReadBin = pickleFile.read()

dataRead = pickle.loads(dataReadBin)

print("Type of pickle data read: {0}".format(type(dataRead)))
print(dataRead)

