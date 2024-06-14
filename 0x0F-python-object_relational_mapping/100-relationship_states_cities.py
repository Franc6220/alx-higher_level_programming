#!/usr/bin/python3
# 100-relationship_states_cities.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Read command line arguments
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new state and city
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Add and commit to the session
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()

