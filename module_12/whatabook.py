'''
Name: Charles Fisher
Date: 12 December 2021
Assignment name: WhatABook
Purpose: Create a program for users to access the WhatABook Database and modify their accounts
Sources: Matthes, E. 2019. Python Crash Course 2nd Edition, “A Hands-On, Project-Based Introduction To Programming. No Starch Press, Inc. San Francisco, CA. 
         Forta, B. (2018). SQL in 10 Minutes a Day, Sams Teach Yourself. Pearson Education (Us.
         Python Tutorial. (2019). W3schools.com. https://www.w3schools.com/python/default.asp
'''
from dns.rdatatype import NULL
import mysql.connector
from mysql.connector import errorcode

'''
Definition: Shows all books that are owned by WhatABook
Arguments: cursor - used to execute comands on selected MySQL database
'''
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = cursor.fetchall()

    print("\n-- DISPLAYING ALL BOOKS AT WHATABOOK --\n")
    for book in books:
        print("Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))

'''
Definition: Shows all WhatABook store Locations and their hours 
Arguments: cursor - used to execute comands on selected MySQL database
'''
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale, openHours FROM store")
    stores = cursor.fetchall()
    
    print("\n-- DISPLAYING ALL WHATABOOK STORES --\n")
    for store in stores:
        print("Store ID: {}\nLocation: {}\nHours: {}\n".format(store[0], store[1], store[2]))

'''
Definition: Shows the wishlist of a specific user
Arguments: cursor - used to execute comands on selected MySQL database
           userID - identifies which users wishlist to grab
'''
def show_wishlist(cursor, userID):
    #grab all books on wishlist that have the correct user_id
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id IN ( SELECT book_id FROM wishlist WHERE user_id = {})".format(userID))
    books = cursor.fetchall()

    #print all books on wish list
    print("\n-- DISPLAYING ALL BOOKS ON YOUR WISHLIST --\n")
    for book in books:
        print("Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))

'''
Definition: Displays the list of books not on the users wish list and allows them to add it to their wishlist
Arguments: cursor - used to execute comands on selected MySQL database
           userID - identifies which users wishlist update
'''
def add_book(cursor, userID):
    print("-- SHOWING BOOKS AVAILABLE TO ADD TO WISHLIST --")
    #grab and print all books not on the users wishlist
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN ( SELECT book_id FROM wishlist WHERE user_id = {})".format(userID))
    books = cursor.fetchall()
    for book in books:
        print("Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))
    
    #get book ID with error checking
    try:
        enteredID = int(input("\nPlease enter the ID of the book you would like to add or enter 0 to cancel: "))
    #return if a non number is entered
    except ValueError:
        print("Invalid Book ID. Returning to Account Menu")
        return
    
    #cancel operation if 0 is entered
    if enteredID == 0:
        print("Operation Canceled. Returning to Account Menu\n")
        return
    
    #flag for if book is found
    bookIsValid = False

    #loop through book list to find selected book
    for book in books:
        if(book[0] == enteredID):
            cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES((SELECT user_id FROM user WHERE user_id = {}), (SELECT book_id FROM book WHERE book_id = {}))".format(userID, book[0]))
            bookIsValid = True
            print("\"{}\" Successfully added to Wishlist\n".format(book[1]))
    
    #Send Error if an invalid book was selected
    if not bookIsValid:
        print("Invalid Book ID. Returning to Account Menu\n")
        return


'''
Definition: Allows the user see their wish list and add books to their wishlist
Arguments: cursor - used to execute comands on selected MySQL database
'''
def access_account(cursor):
    #get user ID with error checking
    try:
        enteredID = int(input("\nPlease Enter your account ID: "))
    #return if a non number is entered
    except ValueError:
        print("Invalid User ID. Returning to Main Menu")
        return
    
    #find user ID
    cursor.execute("SELECT user_id FROM user WHERE user_id = {}".format(enteredID))
    user = cursor.fetchall()
    
    #check if user ID is valid 
    if(len(user) == 0):
        print("Invalid User ID. Returning to Main Menu")
        return
    print("Valid User ID Entered")
    
    while(1):
	    #Account menu
        print("\nAccount Menu:"
            "\n1. View Wishlist"
            "\n2. Add Book to Wishlist"
            "\n3. Main Menu")
        selection = input("\nPlease input the number for your chosen action: ")
        
        if (selection == "1"):#View Wishlist
            show_wishlist(cursor, enteredID)
        
        elif(selection == "2"):#Add Book to Wishlist
            add_book(cursor, enteredID)

        elif(selection == "3"):#exit to main menu
            return

        else:
            print("\nInvalid input. Please select from the following options:")

#Program Start
#user configuration
config = {
    "user": "whatabook_user",
    "password" : "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database" : "whatabook",
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

print("-- Welcome To WhatABook --")
runProgram = True #loop flag
while(runProgram):
	#initial selection menu
    print("\nMain Menu:"
        "\n1. View Books"
        "\n2. View Store Locations"
        "\n3. My Account"
        "\n4. Exit Program")
    selection = input("\nPlease input the number for your chosen action: ")
    if (selection == "1"):
        show_books(cursor)
    
    elif(selection == "2"):
        show_locations(cursor)

    elif(selection == "3"):
        access_account(cursor)

    elif(selection == "4"):#trigger flag to exit code
        print("Exiting Program")
        runProgram = False
    else:
        print("\nInvalid input. Please select from the following options:")

#End program
db.close
input("\n\nPress Enter to Exit...")