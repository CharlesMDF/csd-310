'''
Name: Charles Fisher
Date: 14 November 2021
Assignment name: Collection Creation
Purpose: Create a Program to test connectivity with MongoDB
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
'''
from pymongo import MongoClient  
url = "mongodb+srv://admin:admin@cluster0.qtpgf.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech 

print("-- Pytech Collelection List --")
print(db.list_collection_names())
print("End of program, press Enter to exit... ")
input() #flag to exit 