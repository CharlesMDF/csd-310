from pymongo import MongoClient  
url = "mongodb+srv://admin:admin@cluster0.qtpgf.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech 
print("-- Pytech Collelection List --")
print(db.list_collection_names())

print("End of program, press any key to exit... ")
input() #flag to exit 