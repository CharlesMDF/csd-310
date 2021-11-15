'''
Name: Charles Fisher
Date: 14 November 2021
Assignment name: Collection Queries
Purpose: Create a program to read data from the MongoDB database
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
'''
import os
from pymongo import MongoClient  
url = "mongodb+srv://admin:admin@cluster0.qtpgf.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

studentlist = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in studentlist:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: "+ doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n" )

singleStudent = db.students.find_one({"student_id":"1009"})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print("Student ID: " + singleStudent["student_id"] + "\nFirst Name: "+ singleStudent["first_name"] + "\nLast Name: " + singleStudent["last_name"] + "\n" )

print("End of program, press Enter to exit... ")
input() #flag to exit 