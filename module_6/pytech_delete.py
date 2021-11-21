'''
Name: Charles Fisher
Date: 21 November 2021
Assignment name: Deleting Documents
Purpose: Create a program to update data in the MongoDB database
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
         MongoDB Tutorial | Studytonight. (2021). Www.studytonight.com; Studytonight Technologies Pvt. Ltd. https://www.studytonight.com/mongodb/
'''
import os
from pymongo import MongoClient

'''
Definition: function for printing all student accounts from the database
Arguments: db - database to get students from
'''
def printAllStudents(db):
    studentlist = db.students.find({})
    print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
    for doc in studentlist:
        print("Student ID: " + doc["student_id"] + "\nFirst Name: "+ doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n" )

#connect to database  
url = "mongodb+srv://admin:admin@cluster0.qtpgf.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#print student list
printAllStudents(db)

#create new student object
john = {
    "student_id":"1010",
    "first_name":"John",
    "last_name":"Doe",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": 4.0,
            "start_date": "1 August 2000",
            "end_date": "31 December 2000",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "A"

                },
                {
                    "course_id": "CSD310",
                    "description": "Programming with Java",
                    "instructor": "Professor Payne",
                    "grade": "A"

                }        
            ]
        
        }  
    ]
}

#insert new student into database
john_student_id = db.students.insert_one(john).inserted_id
print("-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id " + str(john_student_id) + "\n")

#find and print newly added student
singleStudent = db.students.find_one({"student_id":"1010"})
print("-- DISPLAYING STUDENT TEST DOC --")
print("Student ID: " + singleStudent["student_id"] + "\nFirst Name: "+ singleStudent["first_name"] + "\nLast Name: " + singleStudent["last_name"] + "\n" )

#deleting test student from database
db.students.delete_one({"student_id" : "1010"})

#printing student list to confirm deletion
printAllStudents(db)

print("End of program, press Enter to exit... ")
input() #flag to exit 