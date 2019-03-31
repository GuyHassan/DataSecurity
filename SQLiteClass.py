import sqlite3

class MySQLiteDB:
    def __init__(self):
        #   Connect to DB
        conn = sqlite3.connect('DefaultUser.db')
        c = conn.cursor()
        # Create tables
        c.execute("CREATE TABLE IF NOT EXISTS DefaultUsers (product text, username text, password text)")
        # Close connection
        conn.close()

    def insertIntoDefaultUsers(self, product, username, password):
        # Connect to DB
        conn = sqlite3.connect('DefaultUser.db')
        c = conn.cursor()
        # Insert a row of data
        c.execute("INSERT INTO DefaultUsers VALUES ('" + product + "' ,'" + username + "', '" + password + "')")
        # Save the changes
        conn.commit()
        # Close connection
        conn.close()

    def printDefaultUsers(self):
        # Connect to DB
        conn = sqlite3.connect('DefaultUser.db')
        c = conn.cursor()
        # Print iteration all rows:
        for row in c.execute('SELECT * FROM DefaultUsers'):
            print(row)
        # Close connection
        conn.close()

    def clearDefaultUsers(self):
        # Connect to DB
        conn = sqlite3.connect('DefaultUser.db')
        c = conn.cursor()
        # Clear all entries in default users
        c.execute("DELETE FROM DefaultUsers")
        # Save the changes
        conn.commit()
        # Close connection
        conn.close()

# newDB = MySQLiteDB()
# newDB.insertIntoDefaultUsers('Example1', 'Admin', '12345')
# newDB.insertIntoDefaultUsers('Example2', 'user', '1111')
# newDB.printDefaultUsers()
# newDB.clearDefaultUsers()


"""
Useful Commands
~~~~~~~~~~~~~~~
# Select and print
c.execute('SELECT * FROM DefaultUsers')
print(c.fetchone())     # Print 1 row as tuple
print(c.fetchall())     # Print all rows in tuple
~~~~~~~~~~~~~~~
# exception
try:
    c.execute("SOMETHING")
except sqlite3.Error as e:
    print("WHATEVER")

"""

