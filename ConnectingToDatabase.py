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
        print("In opening connection")
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    return connection


def closeConnection(connection, databaseFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", databaseFile)

    try:
        connection.close()
        print("Success")
    except Error as e:
        print("In closing connection")
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTables(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Create Tables")

    connection.execute("BEGIN")
    try:
        sql = """CREATE TABLE IF NOT EXISTS coaches (
            c_coachid identity(1, 1) primary key,
            c_name varchar(50),
            c_startyear date not null,
            c_numofchamp int)"""
        connection.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS games (
            g_gameid INTEGER PRIMARY KEY, 
            g_home INTEGER, g_away INTEGER, 
            g_date TEXT, 
            g_winner INTEGER, 
            g_score TEXT, 
            g_stadium INTEGER)"""
        connection.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS news (
            n_newsid INTEGER PRIMARY KEY, 
            n_type TEXT, n_date TEXT, 
            n_news TEXT)"""
        connection.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS player (
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
            p_salary INTEGER)"""
        connection.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS shots (
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
            s_FTPCT REAL)"""
        connection.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS stadium (
            st_stadiumid identity(1, 1) primary key,
            st_name varchar(50),
            st_size int,
            st_location varchar(50))"""
        connection.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS team (
            t_teamid identity (1, 1) PRIMARY KEY, 
            t_name varchar (50), 
            t_foundyear date NOT NULL, 
            t_city varchar (50), 
            t_coachid int, 
            t_stadiumid int)"""
        connection.execute(sql)

        connection.execute("COMMIT")
        print("Success")
    except Error as e:
        print("In creating tables")
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def insertCoaches(connection, coachID, coachName, startYear, NumOfChampion):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Coaches")

    try:
        sql = """INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) 
            VALUES(?, ?, ?, ?)"""
        args = [coachID, coachName, startYear, NumOfChampion]
        connection.execute(sql, args)

        connection.execute("COMMIT")
    except Error as e:
        connection.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insertGames(connection, gameID, home, away, date, winner, score, stadium):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Games")

    try:
        sql = """INSERT INTO games (g_gameid, g_home, g_away, g_date, g_winner, g_score, g_stadium)
            VALUES(?,?,?,?,?,?,?)"""
        args = [gameID, home, away, date, winner, score, stadium]
        connection.execute(sql, args)

        connection.execute("COMMIT")
    except Error as e:
        connection.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insertNews(connection, newsID, type, date, news):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert News")

    try:
        sql = """INSERT INTO news (n_newsid, n_type, n_date, n_news)
            VALUES(?,?,?,?)"""
        args = [newsID, type, date, news]
        connection.execute(sql, args)

        connection.execute("COMMIT")
    except Error as e:
        connection.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insertPlayer(connection, playerID, name, teamname, teamid, position, height, weight, ppg, rpg, apg, spg, bpg, FGpercent, ThreePPercent, startYear, salary):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Player")

    try:
        sql = """INSERT INTO player (p_playerid, p_name, p_teamname, p_teamid, p_position, p_height, p_weight, p_ppg, p_rpg, p_apg, p_spg, p_bpg, p_FGpercent, p_3ppercent, p_startyear, p_salary)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        args = [playerID, name, teamname, teamid, position, height, weight,
                ppg, rpg, apg, spg, bpg, FGpercent, ThreePPercent, startYear, salary]
        connection.execute(sql, args)

        connection.execute("COMMIT")
    except Error as e:
        connection.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insertShots(connection, playerID, playerName, FG, FGA, FGPCT, ThreePoint, ThreePA, ThreePPCT, TwoP, TwoPA, TwoPPCT, eFGPCT, FT, FTA, FTPCT):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Shots")

    try:
        sql = """INSERT INTO shots (s_playerid, s_playername, s_FG, s_FGA, s_FGPCT, s_3P, s_3PA, s_3PPCT, s_2P, s_2PA, s_2PPCT, s_eFGPCT, s_FT, s_FTA, s_FTPCT)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        args = [playerID, playerName, FG, FGA, FGPCT, ThreePoint, ThreePA,
                ThreePPCT, TwoP, TwoPA, TwoPPCT, eFGPCT, FT, FTA, FTPCT]
        connection.execute(sql, args)

        connection.execute("COMMIT")
    except Error as e:
        connection.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insertStadium(connection, stadiumID, name, size, location):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Stadiums")

    try:
        sql = """INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location)
            VALUES(?, ?, ?, ?)"""
        args = [stadiumID, name, size, location]
        connection.execute(sql, args)

        connection.execute("COMMIT")
    except Error as e:
        connection.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insertTeam(connection, teamID, name, foundYear, city, coachID, stadiumID):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Teams")

    try:
        sql = """INSERT INTO team (t_teamid, t_name, t_foundyear, t_city, t_coachid, t_stadiumid)
            VALUES(?, ?, ?, ?, ?, ?)"""
        args = [teamID, name, foundYear, city, coachID, stadiumID]
        connection.execute(sql, args)

        connection.execute("COMMIT")
    except Error as e:
        connection.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Team(connection):

    insertTeam(connection, 26, 'Sacramento Kings', 1985, 'Sacramento', 26, 26)
    insertTeam(connection, 10, 'Golden State Warriors',
               1971, 'San Francisco', 10, 10)
    insertTeam(connection, 1, 'Atlanta Hawks', 1968, 'Atlanta', 1, 1)
    insertTeam(connection, 2, 'Boston Celtics', 1946, 'Boston', 2, 2)
    insertTeam(connection, 21, 'Oklahoma City Thunder',
               2008, 'Oklahoma City', 21, 21)
    insertTeam(connection, 14, 'Los Angeles Lakers',
               1960, 'Los Angeles', 14, 13)
    insertTeam(connection, 29, 'Utah Jazz', 1979, 'Salt Lake City', 29, 29)
    insertTeam(connection, 15, 'Memphis Grizzlies', 2001, 'Memphis', 15, 15)
    insertTeam(connection, 17, 'Milwaukee Bucks', 1968, 'Milwaukee', 17, 17)
    insertTeam(connection, 12, 'Indiana Pacers', 1976, 'Indianapolis', 12, 12)
    insertTeam(connection, 20, 'New York Knicks', 1946, 'New York', 20, 20)
    insertTeam(connection, 8, 'Denver Nuggets', 1976, 'Denver', 8, 8)
    insertTeam(connection, 18, 'Minnesota Timberwolves',
               1989, 'Minneapolis', 18, 18)
    insertTeam(connection, 23, 'Philadelphia 76ers',
               1963, 'Philadelphia', 23, 23)
    insertTeam(connection, 19, 'New Orleans Pelicans',
               2013, 'New Orleans', 19, 19)
    insertTeam(connection, 7, 'Dallas Mavericks', 1980, 'Dallas', 7, 7)
    insertTeam(connection, 24, 'Phoenix Suns', 1968, 'Phoenix', 24, 24)
    insertTeam(connection, 13, 'Los Angeles Clippers',
               1984, 'Los Angeles', 13, 13)
    insertTeam(connection, 25, 'Portland Trail Blazers',
               1970, 'Portland', 25, 25)
    insertTeam(connection, 3, 'Brooklyn Nets', 2012, 'Brooklyn', 3, 3)
    insertTeam(connection, 30, 'Washington Wizards',
               1997, 'Washington', 30, 30)
    insertTeam(connection, 4, 'Chicago Bulls', 1966, 'Chicago', 4, 4)
    insertTeam(connection, 27, 'San Antonio Spurs',
               1976, 'San Antonio', 27, 27)
    insertTeam(connection, 28, 'Toronto Raptors', 1995, 'Toronto', 28, 28)
    insertTeam(connection, 6, 'Cleveland Cavaliers', 1970, 'Cleveland', 6, 6)
    insertTeam(connection, 22, 'Orlando Magic', 1989, 'Orlando', 22, 22)
    insertTeam(connection, 5, 'Charlotte Hornets', 1988, 'Charlotte', 5, 5)
    insertTeam(connection, 11, 'Houston Rockets', 1971, 'Houston', 11, 11)
    insertTeam(connection, 9, 'Detroit Pistons', 1957, 'Detroit', 9, 9)
    insertTeam(connection, 16, 'Miami Heat', 1988, 'Miami', 16, 16)


def main():
    database = r"Project_Database.sqlite"
    connection = openConnection(database)
    cursor = connection.cursor()

    with connection:
        createTables(connection)

    closeConnection(connection, database)


if __name__ == '__main__':
    main()
