#!/usr/bin/python3
"""
12-model_state_update_id_2 module
This script changes the name of the State object where id = 2 to "New Mexico".
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

    # Query the State object where id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the name attribute
        state_to_update.name = "New Mexico"

        # Commit the session to save the changes
        session.commit()
    else:
        print("State with id = 2 not found")

    # Close the session
    session.close()

