#!/usr/bin/python3
"""
3-my_safe_filter_states module
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the argument, safe from MySQL injection.
"""

import sys
import MySQLdb

def filter_states_by_name_safe():
    """
    Connects to the MySQL database and displays all states where the name matches
    the argument in ascending order by states.id, safe from SQL injection.
    """
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # Create the query using parameterized SQL to prevent injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the state_name_searched as parameter
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states_by_name_safe()

