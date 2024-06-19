#Importing the sqlinte3 Module for the BackEnd
import sqlite3

#Defining the function for adding the Details of User in the Database
def addData(Name, Email_id, Skills, Phone_no, Degree, Password):
    con = sqlite3.connect("apna.db")
    cur = con.cursor()
    cur.execute("INSERT INTO User VALUES (NULL, ?, ?, ?, ?, ?, ?)", Name, Email_id, Skills, Phone_no, Degree, Password)
    con.commit()
    con.close()


#Defining the function for Viewing the Details of User in the Database
def viewData():
    con = sqlite3.connect("apna.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM User")
    user_val = cur.fetchall()
    con.close()
    return user_val


#Defining the function for deleting the Details of User in the Database
def DeleteData(uid):
    con = sqlite3.connect("apna.db")
    cur = con.cursor()
    cur.execute("DELETE FROM User WHERE uid = ?", (uid ))
    user_val = cur.fetchall()
    con.close()