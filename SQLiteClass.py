import sqlite3
from tabulate import tabulate

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
        #   tableString = tabulate(c.execute('SELECT * FROM DefaultUsers'), headers=['Model', 'Username', 'Password'],
        #                 tablefmt='orgtbl')
        table = []
        for row in c.execute('SELECT * FROM DefaultUsers'):
            table.append(row)
        # Close connection
        conn.close()
        self.clearDefaultUsers()
        return table


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



