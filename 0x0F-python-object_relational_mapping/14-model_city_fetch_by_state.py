#!/usr/bin/python3
# 14-model_city_fetch_by_state.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Read command line arguments
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects, joined with State objects, ordered by City.id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

