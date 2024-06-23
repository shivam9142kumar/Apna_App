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


#Defining the function for fetching the Details of User in the Database from the email_id attribute
def userInfo(Email_id):
    try:
        cur.execute("SELECT * FROM user WHERE Email_id = %s", (Email_id,))
        value = cur.fetchone()
        con.commit()
        con.close()
        return value
    except mysql.connector.Error as err:
        print(f"Error: {err}")

#Defining the function for adding the Details of User in the Database
def addData(Name, Email_id, Skills, Phone_no, Degree, Password):
    try:
        cur.execute("INSERT INTO User (Name, Email_id, Skills, Phone_no, Degree, Password) VALUES (%s, %s, %s, %s, %s, %s)",
                    (Name, Email_id, Skills, Phone_no, Degree, Password))
        con.commit()
        con.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


#Defining the function for Viewing the Details of User in the Database
def viewData():
    try:
        cur.execute("SELECT * FROM User")
        user_val = cur.fetchall()
        con.commit()
        con.close()
        return user_val
    except mysql.connector.Error as err:
        print(f"Error: {err}")
