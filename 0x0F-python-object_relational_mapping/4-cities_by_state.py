#!/usr/bin/python3
"""
4-cities_by_state module
This script lists all cities from the database hbtn_0e_4_usa along with their state names.
"""

import sys
import MySQLdb

def list_cities_by_state():
    """
    Connects to the MySQL database and lists all cities with their state names,
    sorted by cities.id.
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

    # Execute the query to retrieve cities with state names
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
    
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_cities_by_state()

