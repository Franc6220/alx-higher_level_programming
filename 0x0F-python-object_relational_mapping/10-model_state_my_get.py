#!/usr/bin/python3
"""
10-model_state_my_get module
This script retrieves the id of the State object with the specified name from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query for the State object with the specified name
    query = session.query(State).filter(State.name == state_name)

    # Get the first result
    state = query.first()

    # Check if state was found and print results accordingly
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

