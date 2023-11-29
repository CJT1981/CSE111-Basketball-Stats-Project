import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    cursor = _conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS warehouse")
    
    
    create_table_query = """CREATE TABLE IF NOT EXISTS coaches (
            c_coachid identity(1, 1) primary key,
            c_name varchar(50),
            c_startyear date not null,
            c_numofchamp int)"""
    
    cursor.execute(create_table_query)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS game 
            (g_gameid INTEGER PRIMARY KEY, 
            g_home INTEGER, g_away INTEGER, 
            g_date TEXT, g_winner INTEGER, 
            g_score TEXT, 
            g_stadium INTEGER);
    """
    
    cursor.execute(create_table_query)
    _conn.commit()

    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    cursor = _conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS coaches")
    cursor.execute("DROP TABLE IF EXISTS game")
    _conn.commit()

    print("++++++++++++++++++++++++++++++++++")


def populateTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    populateCoaches(_conn, 'SQLfiles/populate_coaches.sql')
    populateGame(_conn, 'SQLfiles/populate_game.sql')
    
    print("++++++++++++++++++++++++++++++++++")


def populateCoaches(_conn, sql_file):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    cursor = _conn.cursor()

    with open(sql_file, 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    _conn.commit()
    
    print("++++++++++++++++++++++++++++++++++")


def populateGame(_conn, sql_file):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    cursor = _conn.cursor()

    with open(sql_file, 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    _conn.commit()
    
    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"Project_Database.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTables(conn)

    
    closeConnection(conn, database)


if __name__ == '__main__':
    main()
