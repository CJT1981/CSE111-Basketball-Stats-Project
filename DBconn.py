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

    create_table_query = """
    CREATE TABLE IF NOT EXISTS stadium (
    st_stadiumid identity(1, 1) primary key,
    st_name varchar(50),
    st_size int,
    st_location varchar(50));
    """
    cursor.execute(create_table_query)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS team (
        t_teamid identity (1, 1) PRIMARY KEY, 
        t_name varchar (50), 
        t_foundyear date NOT NULL, 
        t_city varchar (50), 
        t_coachid int, 
        t_stadiumid int);
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
    cursor.execute("DROP TABLE IF EXISTS stadium")
    cursor.execute("DROP TABLE IF EXISTS team")
    _conn.commit()

    print("++++++++++++++++++++++++++++++++++")


def populateTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    insertValues(_conn, 'SQLfiles/populate_coaches.sql')
    print("++++++++++++++++++++++++++++++++++")
    print("Populate coaches")
    print("++++++++++++++++++++++++++++++++++")
    insertValues(_conn, 'SQLfiles/populate_game.sql')
    print("++++++++++++++++++++++++++++++++++")
    print("Populate game")
    print("++++++++++++++++++++++++++++++++++")
    insertValues(_conn, 'SQLfiles/populate_stadium.sql')
    print("++++++++++++++++++++++++++++++++++")
    print("Populate stadium")
    print("++++++++++++++++++++++++++++++++++")
    insertValues(_conn, 'SQLfiles/populate_teams.sql')
    print("++++++++++++++++++++++++++++++++++")
    print("Populate teams")
    print("++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++")


def insertValues(_conn, sql_file):

    cursor = _conn.cursor()

    with open(sql_file, 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    _conn.commit()


def playerByTeam(_conn, teamID):
    print("++++++++++++++++++++++++++++++++++")
    print("Players from: ", teamID)

    try:
        sql = """
            SELECT 
                p_name,
                p_teamname
            FROM player AS p
            WHERE
                p.p_teamid = ?
        """
        args = [teamID]

        cursor = _conn.cursor()
        cursor.execute(sql, args)

        l = '{:>10} {:>15}'.format("Player", "Team")
        print(l)
        print("-------------------------------")
        rows = cursor.fetchall()
        for row in rows:
            l = '{:>10} {:>20}'.format(row[0], row[1])
        print(l)
    except Error as e:
        print(e)
        print("++++++++++++++++++++++++++++++++++")
    return 0


def main():
    database = r"Project_Database.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTables(conn)

        teamID = input("Enter Team: ")
        playerByTeam(conn, teamID)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
