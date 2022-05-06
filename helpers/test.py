from http import server
from pymongo import MongoClient

client = MongoClient(port=27017, username="admin", password="admin")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.temperature.insert_one({"temperature":12})
print(serverStatusResult)