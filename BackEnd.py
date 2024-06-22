#Importing the mysql.connector Module for the BackEnd
import mysql.connector

# Configuring 
config = {
    'user': 'root',
    'password': 'yash@7940',
    'host': '127.0.0.1',
    'database': 'apna'
}

def connect_to_database(config):
    try:
        con = mysql.connector.connect(**config)
        if con.is_connected():

            print("Connection successful")
            cur = con.cursor()

            return con
    except mysql.connector.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: # type: ignore
            print("Something is wrong with your user name or password")

        elif err.errno == errorcode.ER_BAD_DB_ERROR: # type: ignore
            print("Database does not exist")


        else:

            print(err)
    return None

con = connect_to_database(config)
if con:
    cur = con.cursor()


#Defining the function for adding the Details of User in the Database

def userInfo(Name):
    cur.execute("SELECT * FROM user WHERE Name = %s", (Name,))
    value = cur.fetchone()
    con.commit()
    con.close()
    return value

def addData(Name, Email_id, Skills, Phone_no, Degree, Password):
    cur.execute("INSERT INTO User VALUES (, %s, %s, %s, %s, %s, %s)", Name, Email_id, Skills, Phone_no, Degree, Password)
    con.commit()
    con.close()


#Defining the function for Viewing the Details of User in the Database
def viewData():
    cur.execute("SELECT * FROM User")
    user_val = cur.fetchall()
    con.close()
    return user_val


#Defining the function for deleting the Details of User in the Database
def DeleteData(uid):
    cur.execute("DELETE FROM User WHERE uid = ?", (uid ))
    user_val = cur.fetchall()
    con.close()

a = userInfo("Yash")
print(a)