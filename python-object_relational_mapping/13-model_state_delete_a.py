#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Check if correct number of arguments are provided
    if len(sys.argv) < 4:
        print("Usage: ./script.py <mysql_user> <mysql_pass> <db_name>")
        sys.exit(1)

    try:
        # Create an engine and establish a session
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
            ),
            pool_pre_ping=True
        )
        
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for states containing the letter 'a'
        states = session.query(State).filter(State.name.like('%a%')).all()

        # Delete states that match the condition
        for state in states:
            session.delete(state)

        # Commit the transaction
        session.commit()

    except Exception as e:
        print("Error: {}".format(e))
        session.rollback()

    finally:
        # Ensure session is closed after use
        session.close()
