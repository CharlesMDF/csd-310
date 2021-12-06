'''
Name: Charles Fisher
Date: 5 December 2021
Assignment name: PySports: Update & Deletes
Purpose: Create a program to update and delete records from a MySQL database.
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
         Forta, B. (2018). SQL in 10 Minutes a Day, Sams Teach Yourself. Pearson Education (Us.
‌
'''
import mysql.connector
from mysql.connector import errorcode

'''
Definition: function for printing all players with team name in player number order
Arguments: cursor - used to execute comands on selected MySQL database
'''
def printPlayers(cursor):
    #execute comand to show players with team name information in player number order
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player LEFT OUTER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

    #print player information
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

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

#Add new player then display player list
cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol','Shire Folk', 1)")
print("\n-- DISPLAYING PLAYER RECORDS AFTER INSERT--")
printPlayers(cursor)

#Update new player then display player list
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
print("\n-- DISPLAYING PLAYER RECORDS AFTER UPDATE --")
printPlayers(cursor)

#Delete new player then display player list
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
print("\n-- DISPLAYING PLAYER RECORDS AFTER DELETE --")
printPlayers(cursor)

#End program
db.close
input("\n\nPress Enter to continue...")