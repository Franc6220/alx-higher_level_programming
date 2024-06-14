#!/usr/bin/python3
# 102-relationship_cities_states_list.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Read command line arguments
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects and their associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()

