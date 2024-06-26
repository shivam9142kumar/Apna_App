#Importing MySQL connector
import mysql.connector

#Importing everything else (like- connect, execute, etc...) from Connector
from mysql.connector import *

#PHASE - I

#Defining an object for MySQL
mydb = mysql.connector.connect(host="localhost", user="root", password="yash@7940")

#Initialising a Cursor-> It is the object that entirely communicates with the entire MySQL server
apna = mydb.cursor()

#Creating Database for the project
apna.execute("CREATE DATABASE apna")

#Executing the MySQL Query to check if databse is created
apna.execute("SHOW DATABASES")

#Python code for executing above MySQL Query
for db in apna:
    print(db)

#PHASE - II
#For phase 2 we will use the same cursor which was in phase 1

#Defining an object for MySQL with the database created above
mydb = mysql.connector.connect(host="localhost", user="root", password="yash@7940", database="apna")

#Creating Queries for Tables for the database
#"User" Table Query
User = "CREATE TABLE User(uid INT(30) AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100) NOT NULL, Email_id VARCHAR(70) NOT NULL UNIQUE, Skills VARCHAR(200) NOT NULL, Phone_no INT(11) NOT NULL UNIQUE, Degree VARCHAR(200), Password VARCHAR(100) NOT NULL)"

#"Company" Table Query
Company = "CREATE TABLE Company(cid INT(30) AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100) NOT NULL, Email_id VARCHAR(100) NOT NULL UNIQUE)"

#"Jobs" Table Query
Jobs = "CREATE TABLE Jobs(jid INT(30) AUTO_INCREMENT PRIMARY KEY, company_id INT(30) NOT NULL UNIQUE, FOREIGN KEY(company_id) REFERENCES Company(cid) ON DELETE CASCADE ON UPDATE CASCADE, Title VARCHAR(100) NOT NULL, Description VARCHAR(300) NOT NULL, Package INT(20) NOT NULL)"

#"Job_seeking" Table Query
Job_seeking = "CREATE TABLE Job_seeking(jsid INT(30) AUTO_INCREMENT PRIMARY KEY, user_id INT(30) NOT NULL, FOREIGN KEY(user_id) REFERENCES User(uid) ON DELETE CASCADE ON UPDATE CASCADE, job_id INT(30) NOT NULL, FOREIGN KEY(job_id) REFERENCES Jobs(jid) ON DELETE CASCADE ON UPDATE CASCADE)"

#"Application" Table Query
Application = "CREATE TABLE Application(aid INT(30) AUTO_INCREMENT PRIMARY KEY, user_id INT(30) NOT NULL, FOREIGN KEY(user_id) REFERENCES User(uid) ON DELETE CASCADE ON UPDATE CASCADE, job_id INT(30) NOT NULL, FOREIGN KEY(job_id) REFERENCES Jobs(jid) ON DELETE CASCADE ON UPDATE CASCADE, Status VARCHAR(50) NOT NULL)"

#"Feedback" Table Query
Feedback = "CREATE TABLE Feedback(fid INT(30) AUTO_INCREMENT PRIMARY KEY, user_id INT(30) NOT NULL, FOREIGN KEY(user_id) REFERENCES User(uid) ON DELETE CASCADE ON UPDATE CASCADE, company_id INT(30) NOT NULL, FOREIGN KEY(company_id) REFERENCES Company(cid) ON DELETE CASCADE ON UPDATE CASCADE, Feedback VARCHAR(300) NOT NULL)"

#Executing the above Quries to create the tables
apna.execute(User)
apna.execute(Company)
apna.execute(Jobs)
apna.execute(Job_seeking)
apna.execute(Application)
apna.execute(Feedback)

#Query to check the Tables if created or not
apna.execute("SHOW TABLES")

#Python code to execute the above Query
for tb in apna:
    print(tb)


#Inserting values into the database

#Creating a Query for Inserting Data into the table
user_form = "INSERT INTO User (Name, Email_id, Skills, Phone_no, Degree, Password) VALUES (%s, %s, %s, %s, %s, %s)"

#Declaring a array to store all the values that I want to insert into the table 
Values = [("Yash", "yash@gmail.com", "Pyhton", "2348576", "B.Tech.", "yash"),
          ("Shivam", "shivam@gmail.com", "Python", "52358", "B.Tech.", "shivam"),
          ("Gautam", "gautam@gmail.com", "Pyhton, Java", "1235789", "B.Tech.", "gautam"),
          ("Amaan", "amaan@gmail.com", "C++, Java", "1547693", "B.Tech.", "amaan"),
          ("Roshan", "roshan@gmail.com", "C, C++", "2547693", "B.Tech.", "roshan")]

#Executing the above to variables for insertion
apna.executemany(user_form, Values)

#Commiting the queries to the table and database (if not commited then no changes will be done in the table)
mydb.commit()


#Displaying all the data from the prefered table

# Creating Query for displaying all the data in the table
display = "SELECT * FROM user"

#Executing the above queries
apna.execute(display)

#Fetching all the data from the last executed statement
result = apna.fetchall()

#Python code for executing the above query
for row in result:
    print(row)
