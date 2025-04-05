#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the MySQL username, password, and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server running on localhost
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Query to fetch all states, sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results from the executed query
    states = cursor.fetchall()

    # Loop through the results and print each state
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
