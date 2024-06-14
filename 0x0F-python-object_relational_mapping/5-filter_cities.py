#!/usr/bin/python3
"""
5-filter_cities module
This script lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def filter_cities_by_state():
    """
    Connects to the MySQL database and lists all cities of the given state,
    sorted by cities.id.
    """
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute the query to retrieve cities of the given state
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Extract city names from the result set
    cities = [row[0] for row in rows]

    # Print the cities as a comma-separated string
    if cities:
        print(", ".join(cities))

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_cities_by_state()

