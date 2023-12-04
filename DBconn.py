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

    create_table_query = """
    CREATE TABLE IF NOT EXISTS coaches (
        c_coachid identity(1, 1) primary key,
        c_name varchar(50),
        c_startyear date not null,
        c_numofchamp int)
    """

    cursor.execute(create_table_query)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS game (
        g_gameid INTEGER PRIMARY KEY, 
        g_home INTEGER, g_away INTEGER, 
        g_date TEXT, g_winner INTEGER, 
        g_score TEXT, 
        g_stadium INTEGER);
    """
    cursor.execute(create_table_query)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS news (
        n_newsid INTEGER PRIMARY KEY, 
        n_type TEXT, 
        n_date TEXT, 
        n_news TEXT);
    """
    cursor.execute(create_table_query)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS player (
        p_playerid INTEGER PRIMARY KEY, 
        p_name TEXT, 
        p_teamname TEXT, 
        p_teamid INTEGER, 
        p_position INTEGER, 
        p_height REAL, 
        p_weight INTEGER, 
        p_ppg REAL, 
        p_rpg REAL, 
        p_apg REAL, 
        p_spg REAL, 
        p_bpg REAL, 
        p_FGpercent REAL, 
        p_3ppercent REAL, 
        p_startyear INTEGER, 
        p_salary INTEGER);
    """
    cursor.execute(create_table_query)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS shots (
        s_playerid INTEGER REFERENCES Player (p_playerid), 
        s_playername TEXT, 
        s_FG REAL, 
        s_FGA REAL, 
        s_FGPCT REAL, 
        s_3P REAL, 
        s_3PA REAL, 
        s_3PPCT REAL, 
        s_2P REAL, 
        s_2PA REAL, 
        s_2PPCT REAL, 
        s_eFGPCT REAL, 
        s_FT REAL, 
        s_FTA REAL, 
        s_FTPCT REAL);
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
    cursor.execute("DROP TABLE IF EXISTS news")
    cursor.execute("DROP TABLE IF EXISTS player")
    cursor.execute("DROP TABLE IF EXISTS shots")
    cursor.execute("DROP TABLE IF EXISTS stadium")
    cursor.execute("DROP TABLE IF EXISTS team")
    _conn.commit()

    print("++++++++++++++++++++++++++++++++++")


def populateTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate tables:")

    print("++++++++++++++++++++++++++++++++++")
    print("Populate coaches")
    insertValues(_conn, 'SQLfiles/populate_coaches.sql')
    print("++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++")
    print("Populate game")
    insertValues(_conn, 'SQLfiles/populate_game.sql')
    print("++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++")

    print("Populate news")
    insertValues(_conn, 'SQLfiles/populate_news.sql')
    print("++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++")
    print("Populate player")
    insertValues(_conn, 'SQLfiles/populate_player.sql')
    print("++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++")
    print("Populate shots")
    insertValues(_conn, 'SQLfiles/populate_shots.sql')
    print("++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++")
    print("Populate stadium")
    insertValues(_conn, 'SQLfiles/populate_stadium.sql')
    print("++++++++++++++++++++++++++++++++++")
    
    print("++++++++++++++++++++++++++++++++++")
    print("Populate team")
    insertValues(_conn, 'SQLfiles/populate_team.sql')
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
