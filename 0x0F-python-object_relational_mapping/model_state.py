#!/usr/bin/python3
"""
6-model_state module
This script defines the State class and initializes the database.
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create declarative_base instance
Base = declarative_base()

class State(Base):
    """
    State class that represents a state table in a MySQL database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Import all tables that inherit from Base
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)

    # Create all tables in the database if they do not exist
    Base.metadata.create_all(engine)

