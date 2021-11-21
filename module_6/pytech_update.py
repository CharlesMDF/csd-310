'''
Name: Charles Fisher
Date: 21 November 2021
Assignment name: Updating Documents
Purpose: Create a program to update data in the MongoDB database
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
         MongoDB Tutorial | Studytonight. (2021). Www.studytonight.com; Studytonight Technologies Pvt. Ltd. https://www.studytonight.com/mongodb/
'''
import os
from pymongo import MongoClient
#connect to database  
url = "mongodb+srv://admin:admin@cluster0.qtpgf.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#grab and print current student information
studentlist = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in studentlist:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: "+ doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n" )

#change student_id 1007 last_name to new name
db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield II"}})

#grab and print updated student information
singleStudent = db.students.find_one({"student_id":"1007"})
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print("Student ID: " + singleStudent["student_id"] + "\nFirst Name: "+ singleStudent["first_name"] + "\nLast Name: " + singleStudent["last_name"] + "\n" )

print("End of program, press Enter to exit... ")
input() #flag to exit 