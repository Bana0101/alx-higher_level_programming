#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys


if __name__ == "__main__":
    data = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            host="localhost",
            port=3306
            )
    mycursor = data.cursor()
    mycursor.execute("""SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON cities.state_id=states.id
            ORDER BY cities.id""")
    states = mycursor.fetchall()
    for state in states:
        print(state)
    mycursor.close()
    data.close()