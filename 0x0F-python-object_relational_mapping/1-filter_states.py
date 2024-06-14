#!/usr/bin/python3
"""
1-filter_states module
This script lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def filter_states():
    """
    Connects to the MySQL database and lists all states with a name starting with 'N'
    in ascending order by states.id.
    """
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states with name starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states()

