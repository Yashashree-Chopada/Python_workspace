import pymongo

myclient = pymongo.MongoClient(host="mongodb://localhost:27017/")

mydb = myclient["VisitorDB"]

#mydb.create_collection("Info")

name = input("Enter your name")
phone = input("Enter your phone")
email = input("Enter your email")
query = input("Enter your query")

data = {
    "name" : name,
    "phone" : phone,
    "email" : email,
    "query" : query
}

mydb["Info"].insert_one(data)

data2 = mydb["Info"].find()

for i in data2:
    print(i)