#!/usr/bin/python3
"""
11-model_state_insert module
This script adds a State object "Louisiana" to the database hbtn_0e_6_usa and prints its id after creation.
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

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to save the new state to the database
    session.commit()

    # Print the id of the newly added state
    print(new_state.id)

    # Close the session
    session.close()

