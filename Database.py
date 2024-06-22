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
User = "CREATE TABLE User(uid VARCHAR(30) PRIMARY KEY, Name VARCHAR(100) NOT NULL, Email_id VARCHAR(70) NOT NULL UNIQUE, Skills VARCHAR(200) NOT NULL, Phone_no INT(11) NOT NULL UNIQUE, Degree VARCHAR(200), Password VARCHAR(100) NOT NULL)"

#"Company" Table Query
Company = "CREATE TABLE Company(cid VARCHAR(30) PRIMARY KEY, Name VARCHAR(100) NOT NULL, Email_id VARCHAR(100) NOT NULL UNIQUE)"

#"Jobs" Table Query
Jobs = "CREATE TABLE Jobs(jid VARCHAR(30) PRIMARY KEY, company_id VARCHAR(30) NOT NULL UNIQUE, FOREIGN KEY(company_id) REFERENCES Company(cid) ON DELETE CASCADE ON UPDATE CASCADE, Title VARCHAR(100) NOT NULL, Description VARCHAR(300) NOT NULL, Package INT(20) NOT NULL)"

#"Job_seeking" Table Query
Job_seeking = "CREATE TABLE Job_seeking(jsid VARCHAR(30) PRIMARY KEY, user_id VARCHAR(30) NOT NULL, FOREIGN KEY(user_id) REFERENCES User(uid) ON DELETE CASCADE ON UPDATE CASCADE, job_id VARCHAR(30) NOT NULL, FOREIGN KEY(job_id) REFERENCES Jobs(jid) ON DELETE CASCADE ON UPDATE CASCADE)"

#"Application" Table Query
Application = "CREATE TABLE Application(aid VARCHAR(30) PRIMARY KEY, user_id VARCHAR(30) NOT NULL, FOREIGN KEY(user_id) REFERENCES User(uid) ON DELETE CASCADE ON UPDATE CASCADE, job_id VARCHAR(30) NOT NULL, FOREIGN KEY(job_id) REFERENCES Jobs(jid) ON DELETE CASCADE ON UPDATE CASCADE, Status VARCHAR(50) NOT NULL)"

#"Feedback" Table Query
Feedback = "CREATE TABLE Feedback(fid VARCHAR(30) PRIMARY KEY, user_id VARCHAR(30) NOT NULL, FOREIGN KEY(user_id) REFERENCES User(uid) ON DELETE CASCADE ON UPDATE CASCADE, company_id VARCHAR(30) NOT NULL, FOREIGN KEY(company_id) REFERENCES Company(cid) ON DELETE CASCADE ON UPDATE CASCADE, Feedback VARCHAR(300) NOT NULL)"

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
