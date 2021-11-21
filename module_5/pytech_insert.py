'''
Name: Charles Fisher
Date: 14 November 2021
Assignment name: Collection Queries
Purpose: Create a program to insert data into the MongoDB database
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
'''
from pymongo import MongoClient 
import os 
url = "mongodb+srv://admin:admin@cluster0.qtpgf.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

thorin = {
    "student_id":"1007",
    "first_name":"Thorin",
    "last_name":"Oakenshield",
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

bilbo = {
    "student_id":"1008",
    "first_name":"Bilbo",
    "last_name":"Baggins",
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
frodo = {
    "student_id":"1009",
    "first_name":"Frodo",
    "last_name":"Baggins",
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

thorin_student_id = students.insert_one(thorin).inserted_id
print("Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))

bilbo_student_id = students.insert_one(bilbo).inserted_id
print("Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

frodo_student_id = students.insert_one(frodo).inserted_id
print("Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

print("End of program, press Enter to exit... ")
input() #flag to exit 