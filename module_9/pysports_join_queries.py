'''
Name: Charles Fisher
Date: 5 December 2021
Assignment name: PySports: Basic Table Joins
Purpose: Create a program to construct and execute aggregate queries in a MySQL database.
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

#establish connection to database
try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

#create cursor for executing MySql commands
cursor = db.cursor()
#get data from both team and player tables using INNER JOIN
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

#print INNER JOIN information
print("\n-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

db.close

input("\n\nPress Enter to continue...")