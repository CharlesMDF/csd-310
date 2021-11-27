'''
Name: Charles Fisher
Date: 27 November 2021
Assignment name: PySports: Setup
Purpose: Create a program test connections to a mySQL database
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
         MongoDB Tutorial | Studytonight. (2021). Www.studytonight.com; Studytonight Technologies Pvt. Ltd. https://www.studytonight.com/mongodb/
'''
import mysql.connector
from mysql.connector import errorcode

#user configuration
config = {
    "user": "pysports_user",
    "password" : "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warnings" : True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    db.close