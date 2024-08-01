import pymongo

myclient = pymongo.MongoClient(host="mongodb://localhost:27017/")

mydb = myclient["VisitorDB"]

data2 = mydb["Info"].find()

for i in data2:
    print(i)
