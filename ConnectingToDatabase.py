import sqlite3
from sqlite3 import Error

# connection = sqlite3.connect("nba_stats_database.sql")
# if connection.cursor():
# print("We are connected!")


def openConnection(database_file):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", database_file)

    connection = None
    try:
        connection = sqlite3.connect(database_file)
        print("Success!")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    return connection


def main():
    database = r"Project_Database.sql"
    connection = openConnection(database)


if __name__ == '__main__':
    main()
