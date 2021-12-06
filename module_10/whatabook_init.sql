/*
Name: Charles Fisher
Date: 5 December 2021
Assignment name: WhatABook: Database and Table Creation
Purpose: whatabook initialization script
Sources: Forta, B. (2018). SQL in 10 Minutes a Day, Sams Teach Yourself. Pearson Education (Us.
*/

-- drop user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;

--create user table
CREATE TABLE user
(
    user_id     INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);

--create book table 
CREATE TABLE book
(
    book_id     INT             NOT NULL        AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

--create wishlist table
CREATE TABLE wishlist
(
wishlist_id     INT           NOT NULL       AUTO_INCREMENT,
user_id         INT           NOT NULL,
book_id         INT           NOT NULL,
PRIMARY KEY(wishlist_id),
CONSTRAINT fk_user     FOREIGN KEY(user_id)     REFERENCES user(user_id),
CONSTRAINT fk_book     FOREIGN KEY(book_id)     REFERENCES book(book_id)
);

--create store table
CREATE TABLE store
(
    store_id    INT                 NOT NULL,
    locale      VARCHAR (500)       NOT NULL,
    PRIMARY KEY(store_id)
);


--insert store records
INSERT INTO store(store_id, locale)
    VALUES(1, '1000 Galvin Rd S, Bellevue, NE 68005');

--insert book records
INSERT INTO book(book_name, author, details)
    VALUES('SQL in 10 Minutes a Day, Sams Teach Yourself', 'Ben Forta', 'Whether you are an application developer, database administrator, web application designer, mobile app developer, or Microsoft Office users, a good working knowledge of SQL is an important part of interacting with databases.');

INSERT INTO book(book_name, author, details)
    VALUES('Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming', 'Eric Matthes', "Python Crash Course is the world's best-selling guide to the Python programming language.");

INSERT INTO book(book_name, author, details)
    VALUES('JavaScript and JQuery: Interactive Front-End Web Development', 'Jon Duckett', "This full-color book will show you how to make your websites more interactive and your interfaces more interesting and intuitive.");

INSERT INTO book(book_name, author, details)
    VALUES('HTML and CSS QuickStart Guide', 'David DuRocher', "The Simplified Beginners Guide to Developing a Strong Coding Foundation, Building Responsive Websites, and Mastering The Fundamentals of Modern Web Design");

INSERT INTO book(book_name, author, details)
    VALUES('C++ for Beginners', 'Nathan Metzler', "An Introduction to C++ Programming and Object Oriented Programming with Tutorials and Hands-On Examples");

INSERT INTO book(book_name, author, details)
    VALUES('Learn C# in One Day and Learn It Well', 'Jamie Chan', "C# for Beginners with Hands-on Project (Learn Coding Fast with Hands-On Project)");

INSERT INTO book(book_name, author, details)
    VALUES('Learn Java 12 Programming', 'Nick Samoylov', "A step-by-step guide to learning essential concepts in Java SE 10, 11, and 12 ");

INSERT INTO book(book_name, author, details)
    VALUES('Introduction to Java Programming and Data Structures, Comprehensive Version', ' Y. Daniel Liang', "A fundamentals-first introduction to basic programming concepts and techniques.");

INSERT INTO book(book_name, author, details)
    VALUES('Hands-On Data Structures and Algorithms with Kotlin', 'Chandra Sekhar Nayak', "Level up your programming skills by understanding how Kotlin's data structure works");

--insert user records
INSERT INTO user(first_name, last_name)
    VALUES('Thorin', 'Oakenshield');

INSERT INTO user(first_name, last_name)
    VALUES('Bilbo', 'Baggins');

INSERT INTO user(first_name, last_name)
    VALUES('Frodo', 'Baggins');

--insert wishlist records
INSERT INTO wishlist(user_id, book_id)
    VALUES((SELECT user_id FROM user WHERE user_id = 1), (SELECT book_id FROM book WHERE book_id = 1));

INSERT INTO wishlist(user_id, book_id)
    VALUES((SELECT user_id FROM user WHERE user_id = 2), (SELECT book_id FROM book WHERE book_id = 2));

INSERT INTO wishlist(user_id, book_id)
    VALUES((SELECT user_id FROM user WHERE user_id = 3), (SELECT book_id FROM book WHERE book_id = 3));
