#!/usr/bin/python3
# 14-model_city_fetch_by_state.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query all City objects and order by id
    cities = session.query(City).order_by(City.id).all()

    # Print results grouped by state name
    for city in cities:
        print(f"{city.state.name}: {city}")

    # Close the session
    session.close()

