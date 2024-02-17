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
    mycursor.execute("""SELECT cities.name
            FROM cities JOIN states ON cities.state_id=states.id
            WHERE states.name LIKE '{}'
            ORDER BY cities.id""".format(sys.argv[4]))
    cities = mycursor.fetchall()
    print(', '.join(city[0] for city in cities))
    mycursor.close()
    data.close()
