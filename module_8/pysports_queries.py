'''
Name: Charles Fisher
Date: 27 November 2021
Assignment name: PySports: Table Queries
Purpose: Create a program to query data from tables in a MySQL database
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
         Forta, B. (2018). SQL in 10 Minutes a Day, Sams Teach Yourself. Pearson Education (Us.
‌
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
#get team table information
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()

#print team table information
print("\n-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

#get team table information
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

#print team table information
print("\n-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

db.close

input("\n\nPress Enter to continue...")