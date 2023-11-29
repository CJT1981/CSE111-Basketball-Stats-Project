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


def populateTable_Games(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Games")

    insertGames(connection, 1, 2, 23, '2022-10-18', 2, '126(H) - 117(A)', 2)
    insertGames(connection, 2, 10, 14, '2022-10-18', 10, '123(H) - 109(A)', 10)
    insertGames(connection, 3, 9, 22, '2022-10-19', 9, '113(H) - 109(A)', 9)
    insertGames(connection, 4, 12, 30, '2022-10-19', 30, '114(A) - 107(H)', 12)
    insertGames(connection, 5, 1, 11, '2022-10-19', 1, '117(H) - 107(A)', 1)
    insertGames(connection, 6, 3, 19, '2022-10-19', 19, '130(A) - 108(H)', 3)
    insertGames(connection, 7, 15, 20, '2022-10-19', 15, '115(H) - 112(A)', 15)
    insertGames(connection, 8, 16, 4, '2022-10-19', 4, '116(A) - 108(H)', 16)
    insertGames(connection, 9, 28, 6, '2022-10-19', 28, '108(H) - 105(A)', 28)
    insertGames(connection, 10, 18, 21, '2022-10-19',
                18, '115(H) - 108(A)', 18)
    insertGames(connection, 11, 27, 5, '2022-10-19', 5, '129(A) - 102(H)', 27)
    insertGames(connection, 12, 29, 8, '2022-10-19', 29, '123(H) - 102(A)', 29)
    insertGames(connection, 13, 24, 7, '2022-10-19', 24, '107(H) - 105(A)', 24)
    insertGames(connection, 14, 26, 25, '2022-10-19',
                25, '115(A) - 108(H)', 26)
    insertGames(connection, 15, 23, 17, '2022-10-20', 17, '90(A) - 88(H)', 23)
    insertGames(connection, 16, 14, 13, '2022-10-20', 13, '103(A) - 97(H)', 13)
    insertGames(connection, 17, 5, 19, '2022-10-21', 19, '124(A) - 112(H)', 5)
    insertGames(connection, 18, 12, 27, '2022-10-21',
                27, '137(A) - 134(H)', 12)
    insertGames(connection, 19, 30, 4, '2022-10-21', 30, '102(H) - 100(A)', 30)
    insertGames(connection, 20, 1, 22, '2022-10-21', 1, '108(H) - 98(A)', 1)
    insertGames(connection, 21, 3, 28, '2022-10-21', 3, '109(H) - 105(A)', 3)
    insertGames(connection, 22, 16, 2, '2022-10-21', 2, '111(A) - 104(H)', 16)
    insertGames(connection, 23, 20, 9, '2022-10-21', 20, '130(H) - 106(A)', 20)
    insertGames(connection, 24, 11, 15, '2022-10-21',
                15, '129(A) - 122(H)', 11)
    insertGames(connection, 25, 18, 29, '2022-10-21',
                29, '132(A) - 126(H)', 18)
    insertGames(connection, 26, 10, 8, '2022-10-21', 8, '128(A) - 123(H)', 10)
    insertGames(connection, 27, 25, 24, '2022-10-21',
                25, '113(H) - 111(A)', 25)
    insertGames(connection, 28, 23, 27, '2022-10-22',
                27, '114(A) - 105(H)', 23)
    insertGames(connection, 29, 12, 9, '2022-10-22', 12, '124(H) - 115(A)', 12)
    insertGames(connection, 30, 22, 2, '2022-10-22', 2, '126(A) - 120(H)', 22)
    insertGames(connection, 31, 4, 6, '2022-10-22', 6, '128(A) - 96(H)', 4)
    insertGames(connection, 32, 16, 28, '2022-10-22',
                16, '112(H) - 109(A)', 16)
    insertGames(connection, 33, 17, 11, '2022-10-22',
                17, '125(H) - 105(A)', 17)
    insertGames(connection, 34, 7, 15, '2022-10-22', 7, '137(H) - 96(A)', 7)
    insertGames(connection, 35, 8, 21, '2022-10-22', 8, '122(H) - 117(A)', 8)
    insertGames(connection, 36, 26, 13, '2022-10-22',
                13, '111(A) - 109(H)', 26)
    insertGames(connection, 37, 14, 25, '2022-10-23',
                25, '106(A) - 104(H)', 13)
    insertGames(connection, 38, 1, 5, '2022-10-23', 5, '126(A) - 109(H)', 1)
    insertGames(connection, 39, 6, 30, '2022-10-23', 6, '117(H) - 107(A)', 6)
    insertGames(connection, 40, 19, 29, '2022-10-23',
                29, '122(A) - 121(H)', 19)
    insertGames(connection, 41, 21, 18, '2022-10-23',
                18, '116(A) - 106(H)', 21)
    insertGames(connection, 42, 10, 26, '2022-10-23',
                10, '130(H) - 125(A)', 10)
    insertGames(connection, 43, 13, 24, '2022-10-23', 24, '112(A) - 95(H)', 13)
    insertGames(connection, 44, 23, 12, '2022-10-24',
                23, '120(H) - 106(A)', 23)
    insertGames(connection, 45, 16, 28, '2022-10-24', 28, '98(A) - 90(H)', 16)
    insertGames(connection, 46, 20, 22, '2022-10-24',
                20, '115(H) - 102(A)', 20)
    insertGames(connection, 47, 4, 2, '2022-10-24', 4, '120(H) - 102(A)', 4)
    insertGames(connection, 48, 11, 29, '2022-10-24',
                11, '114(H) - 108(A)', 11)
    insertGames(connection, 49, 15, 3, '2022-10-24', 15, '134(H) - 124(A)', 15)
    insertGames(connection, 50, 18, 27, '2022-10-24',
                27, '115(A) - 106(H)', 18)
    insertGames(connection, 51, 25, 8, '2022-10-24', 25, '135(H) - 110(A)', 25)
    insertGames(connection, 52, 30, 9, '2022-10-25', 30, '120(H) - 99(A)', 30)
    insertGames(connection, 53, 19, 7, '2022-10-25', 19, '113(H) - 111(A)', 19)
    insertGames(connection, 54, 21, 13, '2022-10-25', 21, '108(H) - 94(A)', 21)
    insertGames(connection, 55, 24, 10, '2022-10-25',
                24, '134(H) - 105(A)', 24)
    insertGames(connection, 56, 6, 22, '2022-10-26', 6, '103(H) - 92(A)', 6)
    insertGames(connection, 57, 9, 1, '2022-10-26', 1, '118(A) - 113(H)', 9)
    insertGames(connection, 58, 17, 3, '2022-10-26', 17, '110(H) - 99(A)', 17)
    insertGames(connection, 59, 20, 5, '2022-10-26', 20, '134(H) - 131(A)', 20)
    insertGames(connection, 60, 28, 23, '2022-10-26',
                28, '119(H) - 109(A)', 28)
    insertGames(connection, 61, 4, 12, '2022-10-26', 4, '124(H) - 109(A)', 4)
    insertGames(connection, 62, 18, 27, '2022-10-26',
                18, '134(H) - 122(A)', 18)
    insertGames(connection, 63, 29, 11, '2022-10-26',
                29, '109(H) - 101(A)', 29)
    insertGames(connection, 64, 8, 14, '2022-10-26', 8, '110(H) - 99(A)', 8)
    insertGames(connection, 65, 25, 16, '2022-10-26', 16, '119(A) - 98(H)', 25)
    insertGames(connection, 66, 3, 7, '2022-10-27', 7, '129(A) - 125(H)', 3)
    insertGames(connection, 67, 21, 13, '2022-10-27',
                21, '118(H) - 110(A)', 21)
    insertGames(connection, 68, 10, 16, '2022-10-27',
                10, '123(H) - 110(A)', 10)
    insertGames(connection, 69, 26, 15, '2022-10-27',
                15, '125(A) - 110(H)', 26)
    insertGames(connection, 70, 9, 1, '2022-10-28', 1, '136(A) - 112(H)', 9)
    insertGames(connection, 71, 22, 5, '2022-10-28', 22, '113(H) - 93(A)', 22)
    insertGames(connection, 72, 2, 6, '2022-10-28', 6, '132(A) - 123(H)', 2)
    insertGames(connection, 73, 28, 23, '2022-10-28', 23, '112(A) - 90(H)', 28)
    insertGames(connection, 74, 30, 12, '2022-10-28',
                12, '127(A) - 117(H)', 30)
    insertGames(connection, 75, 17, 20, '2022-10-28',
                17, '119(H) - 108(A)', 17)
    insertGames(connection, 76, 18, 14, '2022-10-28',
                18, '111(H) - 102(A)', 18)
    insertGames(connection, 77, 27, 4, '2022-10-28', 27, '129(H) - 124(A)', 27)
    insertGames(connection, 78, 8, 29, '2022-10-28', 8, '117(H) - 101(A)', 8)
    insertGames(connection, 79, 24, 19, '2022-10-28',
                24, '124(H) - 111(A)', 24)
    insertGames(connection, 80, 25, 11, '2022-10-28',
                25, '125(H) - 111(A)', 25)
    insertGames(connection, 81, 26, 16, '2022-10-29',
                26, '119(H) - 113(A)', 26)
    insertGames(connection, 82, 5, 10, '2022-10-29', 5, '120(H) - 113(A)', 5)
    insertGames(connection, 83, 3, 12, '2022-10-29', 12, '125(A) - 116(H)', 3)
    insertGames(connection, 84, 4, 23, '2022-10-29', 23, '114(A) - 109(H)', 4)
    insertGames(connection, 85, 17, 1, '2022-10-29', 17, '123(H) - 115(A)', 17)
    insertGames(connection, 86, 7, 21, '2022-10-29', 21, '117(A) - 111(H)', 7)
    insertGames(connection, 87, 29, 15, '2022-10-29',
                29, '124(H) - 123(A)', 29)
    insertGames(connection, 88, 13, 19, '2022-10-30', 19, '112(A) - 91(H)', 13)
    insertGames(connection, 89, 2, 30, '2022-10-30', 2, '112(H) - 94(A)', 2)
    insertGames(connection, 90, 6, 20, '2022-10-30', 6, '121(H) - 108(A)', 6)
    insertGames(connection, 91, 9, 10, '2022-10-30', 9, '128(H) - 114(A)', 9)
    insertGames(connection, 92, 27, 18, '2022-10-30', 27, '107(H) - 98(A)', 27)
    insertGames(connection, 93, 7, 22, '2022-10-30', 7, '114(H) - 105(A)', 7)
    insertGames(connection, 94, 24, 11, '2022-10-30',
                24, '124(H) - 109(A)', 24)
    insertGames(connection, 95, 14, 8, '2022-10-30', 14, '121(H) - 110(A)', 13)
    insertGames(connection, 96, 5, 26, '2022-10-31', 26, '115(A) - 108(H)', 5)
    insertGames(connection, 97, 30, 23, '2022-10-31',
                23, '118(A) - 111(H)', 30)
    insertGames(connection, 98, 3, 12, '2022-10-31', 3, '116(H) - 109(A)', 3)
    insertGames(connection, 99, 28, 1, '2022-10-31', 28, '139(H) - 109(A)', 28)
    insertGames(connection, 100, 17, 9, '2022-10-31',
                17, '110(H) - 108(A)', 17)
    insertGames(connection, 101, 29, 15, '2022-10-31',
                29, '121(H) - 105(A)', 29)
    insertGames(connection, 102, 13, 11, '2022-10-31', 13, '95(H) - 93(A)', 13)
    insertGames(connection, 103, 3, 4, '2022-11-01', 4, '108(A) - 99(H)', 3)
    insertGames(connection, 104, 16, 10, '2022-11-01',
                16, '116(H) - 109(A)', 16)
    insertGames(connection, 105, 21, 22, '2022-11-01',
                21, '116(H) - 108(A)', 21)
    insertGames(connection, 106, 24, 18, '2022-11-01',
                24, '116(H) - 107(A)', 24)
    insertGames(connection, 107, 23, 30, '2022-11-02',
                30, '121(A) - 111(H)', 23)
    insertGames(connection, 108, 6, 2, '2022-11-02', 6, '114(H) - 113(A)', 6)
    insertGames(connection, 109, 16, 26, '2022-11-02',
                16, '110(H) - 107(A)', 16)
    insertGames(connection, 110, 20, 1, '2022-11-02', 1, '112(A) - 99(H)', 20)
    insertGames(connection, 111, 4, 5, '2022-11-02', 4, '106(H) - 88(A)', 4)
    insertGames(connection, 112, 11, 13, '2022-11-02',
                13, '109(A) - 101(H)', 11)
    insertGames(connection, 113, 17, 9, '2022-11-02', 17, '116(H) - 91(A)', 17)
    insertGames(connection, 114, 27, 28, '2022-11-02',
                28, '143(A) - 100(H)', 27)
    insertGames(connection, 115, 7, 29, '2022-11-02', 7, '103(H) - 100(A)', 7)
    insertGames(connection, 116, 25, 15, '2022-11-02',
                15, '111(A) - 106(H)', 25)
    insertGames(connection, 117, 14, 19, '2022-11-02',
                14, '120(H) - 117(A)', 13)
    insertGames(connection, 118, 22, 10, '2022-11-03',
                22, '130(H) - 129(A)', 22)
    insertGames(connection, 119, 21, 8, '2022-11-03', 8, '122(A) - 110(H)', 21)
    insertGames(connection, 120, 9, 6, '2022-11-04', 6, '112(A) - 88(H)', 9)
    insertGames(connection, 121, 12, 16, '2022-11-04',
                12, '101(H) - 99(A)', 12)
    insertGames(connection, 122, 23, 20, '2022-11-04',
                20, '106(A) - 104(H)', 23)
    insertGames(connection, 123, 30, 3, '2022-11-04', 3, '128(A) - 86(H)', 30)
    insertGames(connection, 124, 2, 4, '2022-11-04', 2, '123(H) - 119(A)', 2)
    insertGames(connection, 125, 15, 5, '2022-11-04', 15, '130(H) - 99(A)', 15)
    insertGames(connection, 126, 27, 13, '2022-11-04',
                13, '113(A) - 106(H)', 27)
    insertGames(connection, 127, 7, 28, '2022-11-04', 7, '111(H) - 110(A)', 7)
    insertGames(connection, 128, 19, 10, '2022-11-04',
                19, '114(H) - 105(A)', 19)
    insertGames(connection, 129, 18, 17, '2022-11-04',
                17, '115(A) - 102(H)', 18)
    insertGames(connection, 130, 24, 25, '2022-11-04',
                25, '108(A) - 106(H)', 24)
    insertGames(connection, 131, 14, 29, '2022-11-04',
                29, '130(A) - 116(H)', 13)
    insertGames(connection, 132, 22, 26, '2022-11-05',
                26, '126(A) - 123(H)', 22)
    insertGames(connection, 133, 5, 3, '2022-11-05', 3, '98(A) - 94(H)', 5)
    insertGames(connection, 134, 1, 19, '2022-11-05', 1, '124(H) - 121(A)', 1)
    insertGames(connection, 135, 20, 2, '2022-11-05', 2, '133(A) - 118(H)', 20)
    insertGames(connection, 136, 17, 21, '2022-11-05',
                17, '108(H) - 94(A)', 17)
    insertGames(connection, 137, 18, 11, '2022-11-05',
                18, '129(H) - 117(A)', 18)
    insertGames(connection, 138, 8, 27, '2022-11-05', 8, '126(H) - 101(A)', 8)
    insertGames(connection, 139, 24, 25, '2022-11-05',
                24, '102(H) - 82(A)', 24)
    insertGames(connection, 140, 14, 6, '2022-11-06', 6, '114(A) - 100(H)', 13)
    insertGames(connection, 141, 15, 30, '2022-11-06',
                15, '103(H) - 97(A)', 15)
    insertGames(connection, 142, 28, 4, '2022-11-06',
                28, '113(H) - 104(A)', 28)
    insertGames(connection, 143, 13, 29, '2022-11-06',
                29, '110(A) - 102(H)', 13)
    insertGames(connection, 144, 5, 30, '2022-11-07', 30, '108(A) - 100(H)', 5)
    insertGames(connection, 145, 22, 11, '2022-11-07',
                11, '134(A) - 127(H)', 22)
    insertGames(connection, 146, 9, 21, '2022-11-07', 9, '112(H) - 103(A)', 9)
    insertGames(connection, 147, 12, 19, '2022-11-07',
                12, '129(H) - 122(A)', 12)
    insertGames(connection, 148, 23, 24, '2022-11-07',
                23, '100(H) - 88(A)', 23)
    insertGames(connection, 149, 1, 17, '2022-11-07', 1, '117(H) - 98(A)', 1)
    insertGames(connection, 150, 16, 25, '2022-11-07',
                25, '110(A) - 107(H)', 16)
    insertGames(connection, 151, 4, 28, '2022-11-07', 4, '111(H) - 97(A)', 4)
    insertGames(connection, 152, 15, 2, '2022-11-07', 2, '109(A) - 106(H)', 15)
    insertGames(connection, 153, 18, 20, '2022-11-07',
                20, '120(A) - 107(H)', 18)
    insertGames(connection, 154, 27, 8, '2022-11-07', 8, '115(A) - 109(H)', 27)
    insertGames(connection, 155, 7, 3, '2022-11-07', 7, '96(H) - 94(A)', 7)
    insertGames(connection, 156, 10, 26, '2022-11-07',
                10, '116(H) - 113(A)', 10)
    insertGames(connection, 157, 29, 14, '2022-11-07',
                29, '139(H) - 116(A)', 29)
    insertGames(connection, 158, 13, 6, '2022-11-07',
                13, '119(H) - 117(A)', 13)
    insertGames(connection, 159, 22, 7, '2022-11-09', 22, '94(H) - 87(A)', 22)
    insertGames(connection, 160, 5, 25, '2022-11-09', 25, '105(A) - 95(H)', 5)
    insertGames(connection, 161, 12, 8, '2022-11-09', 8, '122(A) - 119(H)', 12)
    insertGames(connection, 162, 1, 29, '2022-11-09', 29, '125(A) - 119(H)', 1)
    insertGames(connection, 163, 2, 9, '2022-11-09', 2, '128(H) - 112(A)', 2)
    insertGames(connection, 164, 3, 20, '2022-11-09', 3, '112(H) - 85(A)', 3)
    insertGames(connection, 165, 28, 11, '2022-11-09',
                28, '116(H) - 109(A)', 28)
    insertGames(connection, 166, 4, 19, '2022-11-09', 19, '115(A) - 111(H)', 4)
    insertGames(connection, 167, 18, 24, '2022-11-09',
                24, '129(A) - 117(H)', 18)
    insertGames(connection, 168, 21, 17, '2022-11-09',
                17, '136(A) - 132(H)', 21)
    insertGames(connection, 169, 27, 15, '2022-11-09',
                15, '124(A) - 122(H)', 27)
    insertGames(connection, 170, 13, 14, '2022-11-09',
                13, '114(H) - 101(A)', 13)
    insertGames(connection, 171, 26, 6, '2022-11-09',
                26, '127(H) - 120(A)', 26)
    insertGames(connection, 172, 30, 7, '2022-11-10',
                30, '113(H) - 105(A)', 30)
    insertGames(connection, 173, 1, 23, '2022-11-10', 1, '104(H) - 95(A)', 1)
    insertGames(connection, 174, 16, 5, '2022-11-10',
                16, '117(H) - 112(A)', 16)
    insertGames(connection, 175, 19, 25, '2022-11-10',
                25, '106(A) - 95(H)', 19)
    insertGames(connection, 176, 2, 8, '2022-11-11', 2, '131(H) - 112(A)', 2)
    insertGames(connection, 177, 22, 24, '2022-11-11',
                22, '114(H) - 97(A)', 22)
    insertGames(connection, 178, 20, 9, '2022-11-11',
                20, '121(H) - 112(A)', 20)
    insertGames(connection, 179, 21, 28, '2022-11-11',
                21, '132(H) - 113(A)', 21)
    insertGames(connection, 180, 27, 17, '2022-11-11',
                27, '111(H) - 93(A)', 27)
    insertGames(connection, 181, 15, 18, '2022-11-11',
                15, '114(H) - 103(A)', 15)
    insertGames(connection, 182, 10, 6, '2022-11-11',
                10, '106(H) - 101(A)', 10)
    insertGames(connection, 183, 14, 26, '2022-11-11',
                26, '120(A) - 114(H)', 13)
    insertGames(connection, 184, 13, 3, '2022-11-12', 3, '110(A) - 95(H)', 13)
    insertGames(connection, 185, 30, 29, '2022-11-12',
                30, '121(H) - 112(A)', 30)
    insertGames(connection, 186, 9, 2, '2022-11-12', 2, '117(A) - 108(H)', 9)
    insertGames(connection, 187, 12, 28, '2022-11-12',
                12, '118(H) - 104(A)', 12)
    insertGames(connection, 188, 23, 1, '2022-11-12',
                23, '121(H) - 109(A)', 23)
    insertGames(connection, 189, 16, 5, '2022-11-12',
                16, '132(H) - 115(A)', 16)
    insertGames(connection, 190, 7, 25, '2022-11-12', 7, '117(H) - 112(A)', 7)
    insertGames(connection, 191, 19, 11, '2022-11-12',
                19, '119(H) - 106(A)', 19)
    insertGames(connection, 192, 20, 21, '2022-11-13',
                21, '145(A) - 135(H)', 20)
    insertGames(connection, 193, 6, 18, '2022-11-13', 18, '129(A) - 124(H)', 6)
    insertGames(connection, 194, 30, 15, '2022-11-13',
                30, '102(H) - 92(A)', 30)
    insertGames(connection, 195, 23, 29, '2022-11-13',
                23, '105(H) - 98(A)', 23)
    insertGames(connection, 196, 4, 8, '2022-11-13', 8, '126(A) - 103(H)', 4)
    insertGames(connection, 197, 26, 10, '2022-11-13',
                26, '122(H) - 115(A)', 26)
    insertGames(connection, 198, 14, 3, '2022-11-13',
                14, '116(H) - 103(A)', 13)
    insertGames(connection, 199, 9, 28, '2022-11-14', 28, '115(A) - 111(H)', 9)
    insertGames(connection, 200, 22, 5, '2022-11-14', 5, '112(A) - 105(H)', 22)
    insertGames(connection, 201, 2, 21, '2022-11-14', 2, '126(H) - 122(A)', 2)
    insertGames(connection, 202, 16, 24, '2022-11-14',
                16, '113(H) - 112(A)', 16)
    insertGames(connection, 203, 11, 13, '2022-11-14',
                13, '122(A) - 106(H)', 11)
    insertGames(connection, 204, 17, 1, '2022-11-14', 1, '121(A) - 106(H)', 17)
    insertGames(connection, 205, 10, 27, '2022-11-14',
                10, '132(H) - 95(A)', 10)
    insertGames(connection, 206, 19, 15, '2022-11-15',
                19, '113(H) - 102(A)', 19)
    insertGames(connection, 207, 7, 13, '2022-11-15', 7, '103(H) - 101(A)', 7)
    insertGames(connection, 208, 29, 20, '2022-11-15',
                20, '118(A) - 111(H)', 29)
    insertGames(connection, 209, 25, 27, '2022-11-15',
                25, '117(H) - 110(A)', 25)
    insertGames(connection, 210, 26, 3, '2022-11-15',
                26, '153(H) - 121(A)', 26)
    insertGames(connection, 211, 5, 12, '2022-11-16', 12, '125(A) - 113(H)', 5)
    insertGames(connection, 212, 22, 18, '2022-11-16',
                18, '126(A) - 108(H)', 22)
    insertGames(connection, 213, 30, 21, '2022-11-16',
                21, '121(A) - 120(H)', 30)
    insertGames(connection, 214, 1, 2, '2022-11-16', 2, '126(A) - 101(H)', 1)
    insertGames(connection, 215, 28, 16, '2022-11-16',
                28, '112(H) - 104(A)', 28)
    insertGames(connection, 216, 17, 6, '2022-11-16', 17, '113(H) - 98(A)', 17)
    insertGames(connection, 217, 19, 4, '2022-11-16',
                19, '124(H) - 110(A)', 19)
    insertGames(connection, 218, 7, 11, '2022-11-16', 11, '101(A) - 92(H)', 7)
    insertGames(connection, 219, 8, 20, '2022-11-16', 20, '106(A) - 103(H)', 8)
    insertGames(connection, 220, 24, 10, '2022-11-16',
                24, '130(H) - 119(A)', 24)
    insertGames(connection, 221, 25, 3, '2022-11-17', 3, '109(A) - 107(H)', 25)
    insertGames(connection, 222, 26, 27, '2022-11-17',
                26, '130(H) - 112(A)', 26)
    insertGames(connection, 223, 13, 9, '2022-11-17', 13, '96(H) - 91(A)', 13)
    insertGames(connection, 224, 30, 16, '2022-11-18',
                30, '107(H) - 106(A)', 30)
    insertGames(connection, 225, 6, 5, '2022-11-18', 6, '132(H) - 122(A)', 6)
    insertGames(connection, 226, 23, 17, '2022-11-18',
                23, '110(H) - 102(A)', 23)
    insertGames(connection, 227, 4, 22, '2022-11-18', 22, '108(A) - 107(H)', 4)
    insertGames(connection, 228, 11, 12, '2022-11-18', 12, '99(A) - 91(H)', 11)
    insertGames(connection, 229, 15, 21, '2022-11-18',
                15, '121(H) - 110(A)', 15)
    insertGames(connection, 230, 7, 8, '2022-11-18', 7, '127(H) - 99(A)', 7)
    insertGames(connection, 231, 19, 2, '2022-11-18', 2, '117(A) - 109(H)', 19)
    insertGames(connection, 232, 29, 24, '2022-11-18',
                29, '134(H) - 133(A)', 29)
    insertGames(connection, 233, 10, 20, '2022-11-18',
                10, '111(H) - 101(A)', 10)
    insertGames(connection, 234, 14, 9, '2022-11-18',
                14, '128(H) - 121(A)', 13)
    insertGames(connection, 235, 1, 28, '2022-11-19', 1, '124(H) - 122(A)', 1)
    insertGames(connection, 236, 12, 22, '2022-11-19',
                12, '114(H) - 113(A)', 12)
    insertGames(connection, 237, 23, 18, '2022-11-19',
                18, '112(A) - 109(H)', 23)
    insertGames(connection, 238, 25, 29, '2022-11-19',
                29, '118(A) - 113(H)', 25)
    insertGames(connection, 239, 13, 27, '2022-11-19',
                13, '119(H) - 97(A)', 13)
    insertGames(connection, 240, 24, 20, '2022-11-20',
                24, '116(H) - 95(A)', 24)
    insertGames(connection, 241, 26, 9, '2022-11-20',
                26, '137(H) - 129(A)', 26)
    insertGames(connection, 242, 30, 5, '2022-11-20',
                30, '106(H) - 102(A)', 30)
    insertGames(connection, 243, 3, 15, '2022-11-20', 3, '127(H) - 115(A)', 3)
    insertGames(connection, 244, 6, 16, '2022-11-20', 6, '113(H) - 87(A)', 6)
    insertGames(connection, 245, 11, 10, '2022-11-20',
                10, '127(A) - 120(H)', 11)
    insertGames(connection, 246, 7, 8, '2022-11-20', 8, '98(A) - 97(H)', 7)
    insertGames(connection, 247, 14, 27, '2022-11-20',
                14, '123(H) - 92(A)', 13)
    insertGames(connection, 248, 6, 1, '2022-11-21', 6, '114(H) - 102(A)', 6)
    insertGames(connection, 249, 12, 22, '2022-11-21',
                12, '123(H) - 102(A)', 12)
    insertGames(connection, 250, 4, 2, '2022-11-21', 4, '121(H) - 107(A)', 4)
    insertGames(connection, 251, 17, 25, '2022-11-21',
                17, '119(H) - 111(A)', 17)
    insertGames(connection, 252, 18, 16, '2022-11-21',
                18, '105(H) - 101(A)', 18)
    insertGames(connection, 253, 19, 10, '2022-11-21',
                19, '128(H) - 83(A)', 19)
    insertGames(connection, 254, 21, 20, '2022-11-21',
                20, '129(A) - 119(H)', 21)
    insertGames(connection, 255, 13, 29, '2022-11-21',
                13, '121(H) - 114(A)', 13)
    insertGames(connection, 256, 23, 3, '2022-11-22',
                23, '115(H) - 106(A)', 23)
    insertGames(connection, 257, 15, 26, '2022-11-22',
                26, '113(A) - 109(H)', 15)
    insertGames(connection, 258, 8, 9, '2022-11-22', 9, '110(A) - 108(H)', 8)
    insertGames(connection, 259, 24, 14, '2022-11-22',
                24, '115(H) - 105(A)', 24)
    insertGames(connection, 260, 5, 23, '2022-11-23', 5, '107(H) - 101(A)', 5)
    insertGames(connection, 261, 6, 25, '2022-11-23', 6, '114(H) - 96(A)', 6)
    insertGames(connection, 262, 12, 18, '2022-11-23',
                18, '115(A) - 101(H)', 12)
    insertGames(connection, 263, 1, 26, '2022-11-23', 1, '115(H) - 106(A)', 1)
    insertGames(connection, 264, 2, 7, '2022-11-23', 2, '125(H) - 112(A)', 2)
    insertGames(connection, 265, 16, 30, '2022-11-23',
                16, '113(H) - 105(A)', 16)
    insertGames(connection, 266, 28, 3, '2022-11-23', 3, '112(A) - 98(H)', 28)
    insertGames(connection, 267, 17, 4, '2022-11-23', 4, '118(A) - 113(H)', 17)
    insertGames(connection, 268, 21, 8, '2022-11-23', 8, '131(A) - 126(H)', 21)
    insertGames(connection, 269, 27, 19, '2022-11-23',
                19, '129(A) - 110(H)', 27)
    insertGames(connection, 270, 29, 9, '2022-11-23', 9, '125(A) - 116(H)', 29)
    insertGames(connection, 271, 10, 13, '2022-11-23',
                10, '124(H) - 107(A)', 10)
    insertGames(connection, 272, 5, 18, '2022-11-25', 5, '110(H) - 108(A)', 5)
    insertGames(connection, 273, 22, 23, '2022-11-25',
                23, '107(A) - 99(H)', 22)
    insertGames(connection, 274, 20, 25, '2022-11-25',
                25, '132(A) - 129(H)', 20)
    insertGames(connection, 275, 2, 26, '2022-11-25', 2, '122(H) - 104(A)', 2)
    insertGames(connection, 276, 11, 1, '2022-11-25',
                11, '128(H) - 122(A)', 11)
    insertGames(connection, 277, 12, 3, '2022-11-25',
                12, '128(H) - 117(A)', 12)
    insertGames(connection, 278, 15, 19, '2022-11-25',
                15, '132(H) - 111(A)', 15)
    insertGames(connection, 279, 16, 30, '2022-11-25',
                16, '110(H) - 107(A)', 16)
    insertGames(connection, 280, 17, 6, '2022-11-25',
                17, '117(H) - 102(A)', 17)
    insertGames(connection, 281, 21, 4, '2022-11-25',
                21, '123(H) - 119(A)', 21)
    insertGames(connection, 282, 27, 14, '2022-11-25',
                14, '105(A) - 94(H)', 27)
    insertGames(connection, 283, 24, 9, '2022-11-25',
                24, '108(H) - 102(A)', 24)
    insertGames(connection, 284, 10, 29, '2022-11-25',
                10, '129(H) - 118(A)', 10)
    insertGames(connection, 285, 13, 8, '2022-11-25', 8, '114(A) - 104(H)', 13)
    insertGames(connection, 286, 28, 7, '2022-11-26',
                28, '105(H) - 100(A)', 28)
    insertGames(connection, 287, 11, 21, '2022-11-26',
                11, '118(H) - 105(A)', 11)
    insertGames(connection, 288, 27, 14, '2022-11-26',
                14, '143(A) - 138(H)', 27)
    insertGames(connection, 289, 24, 29, '2022-11-26',
                24, '113(H) - 112(A)', 24)
    insertGames(connection, 290, 3, 25, '2022-11-27', 3, '111(H) - 97(A)', 3)
    insertGames(connection, 291, 18, 10, '2022-11-27',
                10, '137(A) - 114(H)', 18)
    insertGames(connection, 292, 13, 12, '2022-11-27',
                13, '114(H) - 100(A)', 13)
    insertGames(connection, 293, 1, 16, '2022-11-27', 16, '106(A) - 98(H)', 1)
    insertGames(connection, 294, 2, 30, '2022-11-27', 2, '130(H) - 121(A)', 2)
    insertGames(connection, 295, 9, 6, '2022-11-27', 6, '102(A) - 94(H)', 9)
    insertGames(connection, 296, 20, 15, '2022-11-27',
                15, '127(A) - 123(H)', 20)
    insertGames(connection, 297, 22, 23, '2022-11-27',
                23, '133(A) - 103(H)', 22)
    insertGames(connection, 298, 17, 7, '2022-11-27',
                17, '124(H) - 115(A)', 17)
    insertGames(connection, 299, 23, 1, '2022-11-28',
                23, '104(H) - 101(A)', 23)
    insertGames(connection, 300, 30, 18, '2022-11-28',
                30, '142(H) - 127(A)', 30)
    insertGames(connection, 301, 2, 5, '2022-11-28', 2, '140(H) - 105(A)', 2)
    insertGames(connection, 302, 3, 22, '2022-11-28', 3, '109(H) - 102(A)', 3)
    insertGames(connection, 303, 28, 6, '2022-11-28', 28, '100(H) - 88(A)', 28)
    insertGames(connection, 304, 19, 21, '2022-11-28',
                19, '105(H) - 101(A)', 19)
    insertGames(connection, 305, 8, 11, '2022-11-28', 8, '129(H) - 113(A)', 8)
    insertGames(connection, 306, 29, 4, '2022-11-28', 4, '114(A) - 107(H)', 29)
    insertGames(connection, 307, 26, 24, '2022-11-28',
                24, '122(A) - 117(H)', 26)
    insertGames(connection, 308, 14, 12, '2022-11-28',
                12, '116(A) - 115(H)', 13)
    insertGames(connection, 309, 9, 20, '2022-11-29', 20, '140(A) - 110(H)', 9)
    insertGames(connection, 310, 7, 10, '2022-11-29', 7, '116(H) - 113(A)', 7)
    insertGames(connection, 311, 25, 13, '2022-11-29',
                13, '118(A) - 112(H)', 25)
    insertGames(connection, 312, 6, 23, '2022-11-30', 6, '113(H) - 85(A)', 6)
    insertGames(connection, 313, 22, 1, '2022-11-30', 1, '125(A) - 108(H)', 22)
    insertGames(connection, 314, 2, 16, '2022-11-30', 2, '134(H) - 121(A)', 2)
    insertGames(connection, 315, 3, 30, '2022-11-30', 3, '113(H) - 107(A)', 3)
    insertGames(connection, 316, 20, 17, '2022-11-30',
                17, '109(A) - 103(H)', 20)
    insertGames(connection, 317, 18, 15, '2022-11-30',
                18, '109(H) - 101(A)', 18)
    insertGames(connection, 318, 19, 28, '2022-11-30',
                19, '126(H) - 108(A)', 19)
    insertGames(connection, 319, 21, 27, '2022-11-30',
                21, '119(H) - 111(A)', 21)
    insertGames(connection, 320, 8, 11, '2022-11-30', 8, '120(H) - 100(A)', 8)
    insertGames(connection, 321, 24, 4, '2022-11-30',
                24, '132(H) - 113(A)', 24)
    insertGames(connection, 322, 29, 13, '2022-11-30',
                29, '125(H) - 112(A)', 29)
    insertGames(connection, 323, 26, 12, '2022-11-30',
                26, '137(H) - 114(A)', 26)
    insertGames(connection, 324, 14, 25, '2022-11-30',
                14, '128(H) - 109(A)', 13)
    insertGames(connection, 325, 9, 7, '2022-12-01', 9, '131(H) - 125(A)', 9)
    insertGames(connection, 326, 5, 30, '2022-12-02', 5, '117(H) - 116(A)', 5)
    insertGames(connection, 327, 1, 8, '2022-12-02', 1, '117(H) - 109(A)', 1)
    insertGames(connection, 328, 2, 16, '2022-12-02', 16, '120(A) - 116(H)', 2)
    insertGames(connection, 329, 3, 28, '2022-12-02', 3, '114(H) - 105(A)', 3)
    insertGames(connection, 330, 6, 22, '2022-12-02', 6, '107(H) - 96(A)', 6)
    insertGames(connection, 331, 17, 14, '2022-12-02',
                14, '133(A) - 129(H)', 17)
    insertGames(connection, 332, 15, 23, '2022-12-02',
                15, '117(H) - 109(A)', 15)
    insertGames(connection, 333, 27, 19, '2022-12-02',
                19, '117(A) - 99(H)', 27)
    insertGames(connection, 334, 24, 11, '2022-12-02',
                11, '122(A) - 121(H)', 24)
    insertGames(connection, 335, 29, 12, '2022-12-02',
                29, '139(H) - 119(A)', 29)
    insertGames(connection, 336, 10, 4, '2022-12-02',
                10, '119(H) - 111(A)', 10)
    insertGames(connection, 337, 20, 7, '2022-12-03', 7, '121(A) - 100(H)', 20)
    insertGames(connection, 338, 13, 26, '2022-12-03',
                26, '123(A) - 96(H)', 13)
    insertGames(connection, 339, 5, 17, '2022-12-03', 17, '105(A) - 96(H)', 5)
    insertGames(connection, 340, 18, 21, '2022-12-03',
                21, '135(A) - 128(H)', 18)
    insertGames(connection, 341, 28, 22, '2022-12-03',
                28, '121(H) - 108(A)', 28)
    insertGames(connection, 342, 10, 11, '2022-12-03',
                10, '120(H) - 101(A)', 10)
    insertGames(connection, 343, 29, 25, '2022-12-03',
                25, '116(A) - 111(H)', 29)
    insertGames(connection, 344, 19, 8, '2022-12-04',
                19, '121(H) - 106(A)', 19)
    insertGames(connection, 345, 27, 24, '2022-12-04',
                24, '133(A) - 95(H)', 27)
    insertGames(connection, 346, 3, 2, '2022-12-04', 2, '103(A) - 92(H)', 3)
    insertGames(connection, 347, 9, 15, '2022-12-04', 15, '122(A) - 112(H)', 9)
    insertGames(connection, 348, 20, 6, '2022-12-04', 20, '92(H) - 81(A)', 20)
    insertGames(connection, 349, 26, 4, '2022-12-04',
                26, '110(H) - 101(A)', 26)
    insertGames(connection, 350, 30, 14, '2022-12-04',
                14, '130(A) - 119(H)', 30)
    insertGames(connection, 351, 25, 12, '2022-12-04',
                25, '116(H) - 100(A)', 25)
    insertGames(connection, 352, 5, 13, '2022-12-05', 13, '119(A) - 117(H)', 5)
    insertGames(connection, 353, 22, 17, '2022-12-05',
                17, '109(A) - 102(H)', 22)
    insertGames(connection, 354, 1, 21, '2022-12-05', 21, '121(A) - 114(H)', 1)
    insertGames(connection, 355, 28, 2, '2022-12-05', 2, '116(A) - 110(H)', 28)
    insertGames(connection, 356, 11, 23, '2022-12-05',
                11, '132(H) - 123(A)', 11)
    insertGames(connection, 357, 15, 16, '2022-12-05',
                15, '101(H) - 93(A)', 15)
    insertGames(connection, 358, 7, 24, '2022-12-05', 7, '130(H) - 111(A)', 7)
    insertGames(connection, 359, 10, 12, '2022-12-05',
                12, '112(A) - 104(H)', 10)
    insertGames(connection, 360, 6, 14, '2022-12-06', 6, '116(H) - 102(A)', 6)
    insertGames(connection, 361, 16, 9, '2022-12-06', 9, '116(A) - 96(H)', 16)
    insertGames(connection, 362, 8, 7, '2022-12-06', 7, '116(A) - 115(H)', 8)
    insertGames(connection, 363, 22, 13, '2022-12-07',
                22, '116(H) - 111(A)', 22)
    insertGames(connection, 364, 3, 5, '2022-12-07', 3, '122(H) - 116(A)', 3)
    insertGames(connection, 365, 20, 1, '2022-12-07', 20, '113(H) - 89(A)', 20)
    insertGames(connection, 366, 28, 14, '2022-12-07',
                28, '126(H) - 113(A)', 28)
    insertGames(connection, 367, 4, 30, '2022-12-07', 4, '115(H) - 111(A)', 4)
    insertGames(connection, 368, 15, 21, '2022-12-07',
                15, '123(H) - 102(A)', 15)
    insertGames(connection, 369, 17, 26, '2022-12-07',
                17, '126(H) - 113(A)', 17)
    insertGames(connection, 370, 18, 12, '2022-12-07',
                18, '121(H) - 115(A)', 18)
    insertGames(connection, 371, 19, 9, '2022-12-07', 19, '104(H) - 98(A)', 19)
    insertGames(connection, 372, 29, 10, '2022-12-07',
                29, '124(H) - 123(A)', 29)
    insertGames(connection, 373, 24, 2, '2022-12-07', 2, '125(A) - 98(H)', 24)
    insertGames(connection, 374, 16, 13, '2022-12-08',
                16, '115(H) - 110(A)', 16)
    insertGames(connection, 375, 27, 11, '2022-12-08',
                27, '118(H) - 109(A)', 27)
    insertGames(connection, 376, 25, 8, '2022-12-08', 8, '121(A) - 120(H)', 25)
    insertGames(connection, 377, 5, 20, '2022-12-09', 20, '121(A) - 102(H)', 5)
    insertGames(connection, 378, 12, 30, '2022-12-09',
                12, '121(H) - 111(A)', 12)
    insertGames(connection, 379, 22, 28, '2022-12-09',
                22, '113(H) - 109(A)', 22)
    insertGames(connection, 380, 3, 1, '2022-12-09', 3, '120(H) - 116(A)', 3)
    insertGames(connection, 381, 6, 26, '2022-12-09', 26, '106(A) - 95(H)', 6)
    insertGames(connection, 382, 23, 14, '2022-12-09',
                23, '133(H) - 122(A)', 23)
    insertGames(connection, 383, 15, 9, '2022-12-09',
                15, '114(H) - 103(A)', 15)
    insertGames(connection, 384, 19, 24, '2022-12-09',
                19, '128(H) - 117(A)', 19)
    insertGames(connection, 385, 29, 18, '2022-12-09',
                18, '118(A) - 108(H)', 29)
    insertGames(connection, 386, 7, 17, '2022-12-09', 17, '106(A) - 105(H)', 7)
    insertGames(connection, 387, 16, 27, '2022-12-10',
                27, '115(A) - 111(H)', 16)
    insertGames(connection, 388, 12, 3, '2022-12-10', 3, '136(A) - 133(H)', 12)
    insertGames(connection, 389, 30, 13, '2022-12-10',
                13, '114(A) - 107(H)', 30)
    insertGames(connection, 390, 6, 21, '2022-12-10', 6, '110(H) - 102(A)', 6)
    insertGames(connection, 391, 4, 7, '2022-12-10', 4, '144(H) - 115(A)', 4)
    insertGames(connection, 392, 10, 2, '2022-12-10',
                10, '123(H) - 107(A)', 10)
    insertGames(connection, 393, 8, 29, '2022-12-10', 8, '115(H) - 110(A)', 8)
    insertGames(connection, 394, 25, 18, '2022-12-10',
                25, '124(H) - 118(A)', 25)
    insertGames(connection, 395, 19, 24, '2022-12-11',
                19, '129(H) - 124(A)', 19)
    insertGames(connection, 396, 9, 14, '2022-12-11', 14, '124(A) - 117(H)', 9)
    insertGames(connection, 397, 20, 26, '2022-12-11',
                20, '112(H) - 99(A)', 20)
    insertGames(connection, 398, 22, 28, '2022-12-11',
                22, '111(H) - 99(A)', 22)
    insertGames(connection, 399, 23, 5, '2022-12-11',
                23, '131(H) - 113(A)', 23)
    insertGames(connection, 400, 1, 4, '2022-12-11', 1, '123(H) - 122(A)', 1)
    insertGames(connection, 401, 11, 17, '2022-12-11', 11, '97(H) - 92(A)', 11)
    insertGames(connection, 402, 12, 16, '2022-12-12', 16, '87(A) - 82(H)', 12)
    insertGames(connection, 403, 30, 3, '2022-12-12', 3, '112(A) - 100(H)', 30)
    insertGames(connection, 404, 15, 1, '2022-12-12',
                15, '128(H) - 103(A)', 15)
    insertGames(connection, 405, 7, 21, '2022-12-12', 7, '121(H) - 114(A)', 7)
    insertGames(connection, 406, 27, 6, '2022-12-12',
                27, '112(H) - 111(A)', 27)
    insertGames(connection, 407, 25, 18, '2022-12-12',
                25, '133(H) - 112(A)', 25)
    insertGames(connection, 408, 13, 2, '2022-12-12', 13, '113(H) - 93(A)', 13)
    insertGames(connection, 409, 23, 26, '2022-12-13',
                23, '123(H) - 103(A)', 23)
    insertGames(connection, 410, 17, 10, '2022-12-13',
                17, '128(H) - 111(A)', 17)
    insertGames(connection, 411, 11, 24, '2022-12-13',
                11, '111(H) - 97(A)', 11)
    insertGames(connection, 412, 29, 19, '2022-12-13',
                29, '121(H) - 100(A)', 29)
    insertGames(connection, 413, 14, 2, '2022-12-13', 2, '122(A) - 118(H)', 13)
    insertGames(connection, 414, 5, 9, '2022-12-14', 9, '141(A) - 134(H)', 5)
    insertGames(connection, 415, 12, 10, '2022-12-14',
                12, '125(H) - 119(A)', 12)
    insertGames(connection, 416, 22, 1, '2022-12-14',
                22, '135(H) - 124(A)', 22)
    insertGames(connection, 417, 4, 20, '2022-12-14', 20, '128(A) - 120(H)', 4)
    insertGames(connection, 418, 28, 26, '2022-12-14',
                26, '124(A) - 123(H)', 28)
    insertGames(connection, 419, 21, 16, '2022-12-14',
                16, '110(A) - 108(H)', 21)
    insertGames(connection, 420, 27, 25, '2022-12-14',
                25, '128(A) - 112(H)', 27)
    insertGames(connection, 421, 7, 6, '2022-12-14', 6, '105(A) - 90(H)', 7)
    insertGames(connection, 422, 8, 30, '2022-12-14', 8, '141(H) - 128(A)', 8)
    insertGames(connection, 423, 13, 18, '2022-12-14', 13, '99(H) - 88(A)', 13)
    insertGames(connection, 424, 11, 16, '2022-12-15',
                16, '111(A) - 108(H)', 11)
    insertGames(connection, 425, 15, 17, '2022-12-15',
                15, '142(H) - 101(A)', 15)
    insertGames(connection, 426, 29, 19, '2022-12-15',
                29, '132(H) - 129(A)', 29)
    insertGames(connection, 427, 13, 24, '2022-12-15',
                24, '111(A) - 95(H)', 13)
    insertGames(connection, 428, 5, 1, '2022-12-16', 1, '125(A) - 106(H)', 5)
    insertGames(connection, 429, 9, 26, '2022-12-16', 26, '122(A) - 113(H)', 9)
    insertGames(connection, 430, 2, 22, '2022-12-16', 22, '117(A) - 109(H)', 2)
    insertGames(connection, 431, 6, 12, '2022-12-16', 6, '118(H) - 112(A)', 6)
    insertGames(connection, 432, 23, 10, '2022-12-16',
                23, '118(H) - 106(A)', 23)
    insertGames(connection, 433, 28, 3, '2022-12-16', 3, '119(A) - 116(H)', 28)
    insertGames(connection, 434, 4, 20, '2022-12-16', 20, '114(A) - 91(H)', 4)
    insertGames(connection, 435, 21, 18, '2022-12-16',
                18, '112(A) - 110(H)', 21)
    insertGames(connection, 436, 7, 25, '2022-12-16', 7, '130(H) - 110(A)', 7)
    insertGames(connection, 437, 14, 8, '2022-12-16',
                14, '126(H) - 108(A)', 13)
    insertGames(connection, 438, 13, 30, '2022-12-17',
                13, '102(H) - 93(A)', 13)
    insertGames(connection, 439, 27, 16, '2022-12-17',
                16, '111(A) - 101(H)', 27)
    insertGames(connection, 440, 6, 7, '2022-12-17', 6, '100(H) - 99(A)', 6)
    insertGames(connection, 441, 11, 25, '2022-12-17',
                25, '107(A) - 95(H)', 11)
    insertGames(connection, 442, 17, 29, '2022-12-17',
                17, '123(H) - 97(A)', 17)
    insertGames(connection, 443, 21, 15, '2022-12-17',
                21, '115(H) - 109(A)', 21)
    insertGames(connection, 444, 24, 19, '2022-12-17',
                24, '118(H) - 114(A)', 24)
    insertGames(connection, 445, 2, 22, '2022-12-18', 22, '95(A) - 92(H)', 2)
    insertGames(connection, 446, 12, 20, '2022-12-18',
                20, '109(A) - 106(H)', 12)
    insertGames(connection, 447, 9, 3, '2022-12-18', 3, '124(A) - 121(H)', 9)
    insertGames(connection, 448, 28, 10, '2022-12-18',
                10, '126(A) - 110(H)', 28)
    insertGames(connection, 449, 18, 4, '2022-12-18',
                18, '150(H) - 126(A)', 18)
    insertGames(connection, 450, 8, 5, '2022-12-18', 8, '119(H) - 115(A)', 8)
    insertGames(connection, 451, 14, 30, '2022-12-18',
                14, '119(H) - 117(A)', 13)
    insertGames(connection, 452, 6, 29, '2022-12-19', 6, '122(H) - 99(A)', 6)
    insertGames(connection, 453, 23, 28, '2022-12-19',
                23, '104(H) - 101(A)', 23)
    insertGames(connection, 454, 1, 22, '2022-12-19', 1, '126(H) - 125(A)', 1)
    insertGames(connection, 455, 11, 27, '2022-12-19',
                27, '124(A) - 105(H)', 11)
    insertGames(connection, 456, 18, 7, '2022-12-19',
                18, '116(H) - 106(A)', 18)
    insertGames(connection, 457, 19, 17, '2022-12-19',
                17, '128(A) - 119(H)', 19)
    insertGames(connection, 458, 21, 25, '2022-12-19',
                21, '123(H) - 121(A)', 21)
    insertGames(connection, 459, 24, 14, '2022-12-19',
                24, '130(H) - 104(A)', 24)
    insertGames(connection, 460, 26, 5, '2022-12-19', 5, '125(A) - 119(H)', 26)
    insertGames(connection, 461, 9, 29, '2022-12-20', 29, '126(A) - 111(H)', 9)
    insertGames(connection, 462, 16, 4, '2022-12-20', 4, '113(A) - 103(H)', 16)
    insertGames(connection, 463, 20, 10, '2022-12-20',
                20, '132(H) - 94(A)', 20)
    insertGames(connection, 464, 24, 30, '2022-12-20',
                30, '113(A) - 110(H)', 24)
    insertGames(connection, 465, 8, 15, '2022-12-20', 8, '105(H) - 91(A)', 8)
    insertGames(connection, 466, 6, 17, '2022-12-21', 6, '114(H) - 106(A)', 6)
    insertGames(connection, 467, 23, 9, '2022-12-21', 23, '113(H) - 93(A)', 23)
    insertGames(connection, 468, 1, 4, '2022-12-21', 4, '110(A) - 108(H)', 1)
    insertGames(connection, 469, 2, 12, '2022-12-21', 12, '117(A) - 112(H)', 2)
    insertGames(connection, 470, 3, 10, '2022-12-21', 3, '143(H) - 113(A)', 3)
    insertGames(connection, 471, 20, 28, '2022-12-21',
                28, '113(A) - 106(H)', 20)
    insertGames(connection, 472, 11, 22, '2022-12-21',
                22, '116(A) - 110(H)', 11)
    insertGames(connection, 473, 18, 7, '2022-12-21', 7, '104(A) - 99(H)', 18)
    insertGames(connection, 474, 21, 25, '2022-12-21',
                21, '101(H) - 98(A)', 21)
    insertGames(connection, 475, 26, 14, '2022-12-21',
                26, '134(H) - 120(A)', 26)
    insertGames(connection, 476, 13, 5, '2022-12-21',
                13, '126(H) - 105(A)', 13)
    insertGames(connection, 477, 19, 27, '2022-12-22',
                19, '126(H) - 117(A)', 19)
    insertGames(connection, 478, 29, 30, '2022-12-22',
                29, '120(H) - 112(A)', 29)
    insertGames(connection, 479, 22, 27, '2022-12-23',
                22, '133(H) - 113(A)', 22)
    insertGames(connection, 480, 23, 13, '2022-12-23',
                23, '119(H) - 114(A)', 23)
    insertGames(connection, 481, 1, 9, '2022-12-23', 1, '130(H) - 105(A)', 1)
    insertGames(connection, 482, 2, 18, '2022-12-23', 2, '121(H) - 109(A)', 2)
    insertGames(connection, 483, 3, 17, '2022-12-23', 3, '118(H) - 100(A)', 3)
    insertGames(connection, 484, 6, 28, '2022-12-23', 28, '118(A) - 107(H)', 6)
    insertGames(connection, 485, 20, 4, '2022-12-23', 4, '118(A) - 117(H)', 20)
    insertGames(connection, 486, 11, 7, '2022-12-23', 7, '112(A) - 106(H)', 11)
    insertGames(connection, 487, 16, 12, '2022-12-23',
                12, '111(A) - 108(H)', 16)
    insertGames(connection, 488, 21, 19, '2022-12-23',
                19, '128(A) - 125(H)', 21)
    insertGames(connection, 489, 8, 25, '2022-12-23', 8, '120(H) - 107(A)', 8)
    insertGames(connection, 490, 24, 15, '2022-12-23',
                15, '125(A) - 100(H)', 24)
    insertGames(connection, 491, 26, 30, '2022-12-23',
                30, '125(A) - 111(H)', 26)
    insertGames(connection, 492, 14, 5, '2022-12-23', 5, '134(A) - 130(H)', 13)
    insertGames(connection, 493, 20, 23, '2022-12-25',
                23, '119(A) - 112(H)', 20)
    insertGames(connection, 494, 7, 14, '2022-12-25', 7, '124(H) - 115(A)', 7)
    insertGames(connection, 495, 2, 17, '2022-12-25', 2, '139(H) - 118(A)', 2)
    insertGames(connection, 496, 10, 15, '2022-12-25',
                10, '123(H) - 109(A)', 10)
    insertGames(connection, 497, 8, 24, '2022-12-25', 8, '128(H) - 125(A)', 8)
    insertGames(connection, 498, 6, 3, '2022-12-26', 3, '125(A) - 117(H)', 6)
    insertGames(connection, 499, 9, 13, '2022-12-26', 13, '142(A) - 131(H)', 9)
    insertGames(connection, 500, 16, 18, '2022-12-26',
                16, '113(H) - 110(A)', 16)
    insertGames(connection, 501, 4, 11, '2022-12-26', 11, '133(A) - 118(H)', 4)
    insertGames(connection, 502, 19, 12, '2022-12-26',
                19, '113(H) - 93(A)', 19)
    insertGames(connection, 503, 27, 29, '2022-12-26',
                27, '126(H) - 122(A)', 27)
    insertGames(connection, 504, 25, 5, '2022-12-26',
                25, '124(H) - 113(A)', 25)
    insertGames(connection, 505, 22, 14, '2022-12-27',
                14, '129(A) - 110(H)', 22)
    insertGames(connection, 506, 30, 23, '2022-12-27',
                30, '116(H) - 111(A)', 30)
    insertGames(connection, 507, 2, 11, '2022-12-27', 2, '126(H) - 102(A)', 2)
    insertGames(connection, 508, 12, 1, '2022-12-27',
                12, '129(H) - 114(A)', 12)
    insertGames(connection, 509, 28, 13, '2022-12-27',
                13, '124(A) - 113(H)', 28)
    insertGames(connection, 510, 15, 24, '2022-12-27',
                24, '125(A) - 108(H)', 15)
    insertGames(connection, 511, 21, 27, '2022-12-27',
                21, '130(H) - 114(A)', 21)
    insertGames(connection, 512, 7, 20, '2022-12-27', 7, '126(H) - 121(A)', 7)
    insertGames(connection, 513, 10, 5, '2022-12-27',
                10, '110(H) - 105(A)', 10)
    insertGames(connection, 514, 26, 8, '2022-12-27', 8, '113(A) - 106(H)', 26)
    insertGames(connection, 515, 9, 22, '2022-12-28', 9, '121(H) - 101(A)', 9)
    insertGames(connection, 516, 30, 24, '2022-12-28',
                30, '127(H) - 102(A)', 30)
    insertGames(connection, 517, 1, 3, '2022-12-28', 3, '108(A) - 107(H)', 1)
    insertGames(connection, 518, 16, 14, '2022-12-28',
                16, '112(H) - 98(A)', 16)
    insertGames(connection, 519, 4, 17, '2022-12-28', 4, '119(H) - 113(A)', 4)
    insertGames(connection, 520, 19, 18, '2022-12-28',
                19, '119(H) - 118(A)', 19)
    insertGames(connection, 521, 10, 29, '2022-12-28',
                10, '112(H) - 107(A)', 10)
    insertGames(connection, 522, 26, 8, '2022-12-28',
                26, '127(H) - 126(A)', 26)
    insertGames(connection, 523, 5, 21, '2022-12-29', 5, '121(H) - 113(A)', 5)
    insertGames(connection, 524, 12, 6, '2022-12-29',
                12, '135(H) - 126(A)', 12)
    insertGames(connection, 525, 2, 13, '2022-12-29', 2, '116(H) - 110(A)', 2)
    insertGames(connection, 526, 28, 15, '2022-12-29',
                15, '119(A) - 106(H)', 28)
    insertGames(connection, 527, 27, 20, '2022-12-29',
                27, '122(H) - 115(A)', 27)
    insertGames(connection, 528, 7, 11, '2022-12-29', 7, '129(H) - 114(A)', 7)
    insertGames(connection, 529, 22, 30, '2022-12-30',
                30, '119(A) - 100(H)', 22)
    insertGames(connection, 530, 1, 14, '2022-12-30', 14, '130(A) - 121(H)', 1)
    insertGames(connection, 531, 28, 24, '2022-12-30',
                28, '113(H) - 104(A)', 28)
    insertGames(connection, 532, 4, 9, '2022-12-30', 4, '132(H) - 118(A)', 4)
    insertGames(connection, 533, 17, 18, '2022-12-30',
                17, '123(H) - 114(A)', 17)
    insertGames(connection, 534, 19, 23, '2022-12-30',
                19, '127(H) - 116(A)', 19)
    insertGames(connection, 535, 8, 16, '2022-12-30', 8, '124(H) - 119(A)', 8)
    insertGames(connection, 536, 10, 25, '2022-12-30',
                10, '118(H) - 112(A)', 10)
    insertGames(connection, 537, 26, 29, '2022-12-30',
                26, '126(H) - 125(A)', 26)
    insertGames(connection, 538, 12, 13, '2022-12-31',
                12, '131(H) - 130(A)', 12)
    insertGames(connection, 539, 4, 6, '2022-12-31', 6, '103(A) - 102(H)', 4)
    insertGames(connection, 540, 5, 3, '2022-12-31', 3, '123(A) - 106(H)', 5)
    insertGames(connection, 541, 11, 20, '2022-12-31',
                20, '108(A) - 88(H)', 11)
    insertGames(connection, 542, 27, 7, '2022-12-31', 7, '126(A) - 125(H)', 27)
    insertGames(connection, 543, 15, 19, '2022-12-31',
                15, '116(H) - 101(A)', 15)
    insertGames(connection, 544, 18, 9, '2022-12-31', 9, '116(A) - 104(H)', 18)
    insertGames(connection, 545, 21, 23, '2022-12-31',
                23, '115(A) - 96(H)', 21)
    insertGames(connection, 546, 29, 16, '2022-12-31',
                16, '126(A) - 123(H)', 29)
    insertGames(connection, 547, 8, 2, '2023-01-01', 8, '123(H) - 111(A)', 8)
    insertGames(connection, 548, 15, 26, '2023-01-01',
                15, '118(H) - 108(A)', 15)
    insertGames(connection, 549, 17, 30, '2023-01-01',
                30, '118(A) - 95(H)', 17)
    insertGames(connection, 550, 20, 24, '2023-01-02',
                20, '102(H) - 83(A)', 20)
    insertGames(connection, 551, 5, 14, '2023-01-02', 14, '121(A) - 115(H)', 5)
    insertGames(connection, 552, 6, 5, '2023-01-02', 6, '145(H) - 134(A)', 6)
    insertGames(connection, 553, 12, 28, '2023-01-02',
                12, '122(H) - 114(A)', 12)
    insertGames(connection, 554, 23, 19, '2023-01-02',
                23, '120(H) - 111(A)', 23)
    insertGames(connection, 555, 3, 27, '2023-01-02', 3, '139(H) - 103(A)', 3)
    insertGames(connection, 556, 11, 7, '2023-01-02', 7, '111(A) - 106(H)', 11)
    insertGames(connection, 557, 18, 8, '2023-01-02',
                18, '124(H) - 111(A)', 18)
    insertGames(connection, 558, 10, 1, '2023-01-02',
                10, '143(H) - 141(A)', 10)
    insertGames(connection, 559, 25, 9, '2023-01-02',
                25, '135(H) - 106(A)', 25)
    insertGames(connection, 560, 13, 16, '2023-01-02',
                16, '110(A) - 100(H)', 13)
    insertGames(connection, 561, 17, 30, '2023-01-03',
                17, '123(H) - 113(A)', 17)
    insertGames(connection, 562, 21, 2, '2023-01-03',
                21, '150(H) - 117(A)', 21)
    insertGames(connection, 563, 29, 26, '2023-01-03',
                26, '117(A) - 115(H)', 29)
    insertGames(connection, 564, 5, 15, '2023-01-04', 15, '131(A) - 107(H)', 5)
    insertGames(connection, 565, 6, 24, '2023-01-04', 6, '90(H) - 88(A)', 6)
    insertGames(connection, 566, 22, 21, '2023-01-04',
                22, '126(H) - 115(A)', 22)
    insertGames(connection, 567, 23, 12, '2023-01-04',
                23, '129(H) - 126(A)', 23)
    insertGames(connection, 568, 20, 27, '2023-01-04',
                20, '117(H) - 114(A)', 20)
    insertGames(connection, 569, 28, 17, '2023-01-04',
                17, '104(A) - 101(H)', 28)
    insertGames(connection, 570, 5, 3, '2023-01-04', 5, '121(H) - 112(A)', 5)
    insertGames(connection, 571, 18, 25, '2023-01-04',
                18, '113(H) - 106(A)', 18)
    insertGames(connection, 572, 19, 11, '2023-01-04',
                19, '119(H) - 108(A)', 19)
    insertGames(connection, 573, 10, 9, '2023-01-04', 9, '122(A) - 119(H)', 10)
    insertGames(connection, 574, 14, 16, '2023-01-04',
                14, '112(H) - 109(A)', 13)
    insertGames(connection, 575, 26, 1, '2023-01-04', 1, '120(A) - 117(H)', 26)
    insertGames(connection, 576, 22, 15, '2023-01-05',
                15, '123(A) - 115(H)', 22)
    insertGames(connection, 577, 7, 2, '2023-01-05', 2, '124(A) - 95(H)', 7)
    insertGames(connection, 578, 11, 29, '2023-01-05',
                29, '131(A) - 114(H)', 11)
    insertGames(connection, 579, 8, 13, '2023-01-05', 8, '122(H) - 91(A)', 8)
    insertGames(connection, 580, 12, 25, '2023-01-06',
                12, '108(H) - 99(A)', 12)
    insertGames(connection, 581, 23, 5, '2023-01-06', 5, '126(A) - 112(H)', 23)
    insertGames(connection, 582, 19, 3, '2023-01-06', 3, '108(A) - 102(H)', 19)
    insertGames(connection, 583, 28, 20, '2023-01-06',
                20, '112(A) - 108(H)', 28)
    insertGames(connection, 584, 17, 5, '2023-01-06', 5, '138(A) - 109(H)', 17)
    insertGames(connection, 585, 21, 30, '2023-01-06',
                21, '127(H) - 110(A)', 21)
    insertGames(connection, 586, 27, 9, '2023-01-06',
                27, '121(H) - 109(A)', 27)
    insertGames(connection, 587, 8, 6, '2023-01-06', 8, '121(H) - 108(A)', 8)
    insertGames(connection, 588, 18, 13, '2023-01-06',
                18, '128(H) - 115(A)', 18)
    insertGames(connection, 589, 24, 16, '2023-01-06',
                16, '104(A) - 96(H)', 24)
    insertGames(connection, 590, 14, 1, '2023-01-06',
                14, '130(H) - 114(A)', 13)
    insertGames(connection, 591, 27, 2, '2023-01-07', 2, '121(A) - 116(H)', 27)
    insertGames(connection, 592, 5, 29, '2023-01-07', 5, '126(H) - 118(A)', 5)
    insertGames(connection, 593, 7, 19, '2023-01-07', 7, '127(H) - 117(A)', 7)
    insertGames(connection, 594, 10, 22, '2023-01-07',
                22, '115(A) - 101(H)', 10)
    insertGames(connection, 595, 26, 14, '2023-01-07',
                14, '136(A) - 134(H)', 26)
    insertGames(connection, 596, 9, 23, '2023-01-08', 23, '123(A) - 111(H)', 9)
    insertGames(connection, 597, 28, 25, '2023-01-08',
                28, '117(H) - 105(A)', 28)
    insertGames(connection, 598, 12, 5, '2023-01-08',
                12, '116(H) - 111(A)', 12)
    insertGames(connection, 599, 15, 29, '2023-01-08',
                15, '123(H) - 118(A)', 15)
    insertGames(connection, 600, 16, 3, '2023-01-08', 3, '102(A) - 101(H)', 16)
    insertGames(connection, 601, 11, 18, '2023-01-08',
                18, '104(A) - 96(H)', 11)
    insertGames(connection, 602, 21, 7, '2023-01-08',
                21, '120(H) - 109(A)', 21)
    insertGames(connection, 603, 24, 6, '2023-01-08', 6, '112(A) - 98(H)', 24)
    insertGames(connection, 604, 13, 1, '2023-01-08', 1, '112(A) - 108(H)', 13)
    insertGames(connection, 605, 30, 19, '2023-01-09',
                19, '132(A) - 112(H)', 30)
    insertGames(connection, 606, 2, 5, '2023-01-09', 2, '107(H) - 99(A)', 2)
    insertGames(connection, 607, 20, 17, '2023-01-09',
                17, '111(A) - 107(H)', 20)
    insertGames(connection, 608, 15, 27, '2023-01-09',
                15, '121(H) - 113(A)', 15)
    insertGames(connection, 609, 8, 14, '2023-01-09', 8, '122(H) - 109(A)', 8)
    insertGames(connection, 610, 26, 22, '2023-01-09',
                26, '136(H) - 111(A)', 26)
    insertGames(connection, 611, 23, 9, '2023-01-10',
                23, '147(H) - 116(A)', 23)
    insertGames(connection, 612, 16, 21, '2023-01-10',
                16, '112(H) - 111(A)', 16)
    insertGames(connection, 613, 28, 5, '2023-01-10',
                28, '132(H) - 120(A)', 28)
    insertGames(connection, 614, 29, 6, '2023-01-10',
                29, '116(H) - 114(A)', 29)
    insertGames(connection, 615, 10, 24, '2023-01-10',
                24, '125(A) - 113(H)', 10)
    insertGames(connection, 616, 25, 22, '2023-01-10',
                22, '109(A) - 106(H)', 25)
    insertGames(connection, 617, 13, 7, '2023-01-10',
                13, '113(H) - 101(A)', 13)
    insertGames(connection, 618, 9, 18, '2023-01-11', 9, '135(H) - 118(A)', 9)
    insertGames(connection, 619, 30, 5, '2023-01-11', 30, '100(H) - 97(A)', 30)
    insertGames(connection, 620, 1, 17, '2023-01-11', 17, '114(A) - 105(H)', 1)
    insertGames(connection, 621, 2, 19, '2023-01-11', 2, '125(H) - 114(A)', 2)
    insertGames(connection, 622, 20, 12, '2023-01-11',
                20, '119(H) - 113(A)', 20)
    insertGames(connection, 623, 15, 27, '2023-01-11',
                15, '135(H) - 129(A)', 15)
    insertGames(connection, 624, 8, 24, '2023-01-11', 8, '126(H) - 97(A)', 8)
    insertGames(connection, 625, 26, 11, '2023-01-11',
                26, '135(H) - 115(A)', 26)
    insertGames(connection, 626, 23, 21, '2023-01-12',
                21, '133(A) - 114(H)', 23)
    insertGames(connection, 627, 3, 2, '2023-01-12', 2, '109(A) - 98(H)', 3)
    insertGames(connection, 628, 16, 17, '2023-01-12',
                16, '108(H) - 102(A)', 16)
    insertGames(connection, 629, 28, 5, '2023-01-12',
                28, '124(H) - 114(A)', 28)
    insertGames(connection, 630, 14, 7, '2023-01-12', 7, '119(A) - 115(H)', 13)
    insertGames(connection, 631, 25, 6, '2023-01-12', 6, '119(A) - 113(H)', 25)
    insertGames(connection, 632, 9, 19, '2023-01-13', 19, '116(A) - 110(H)', 9)
    insertGames(connection, 633, 12, 1, '2023-01-13', 1, '113(A) - 111(H)', 12)
    insertGames(connection, 634, 30, 20, '2023-01-13',
                20, '112(A) - 108(H)', 30)
    insertGames(connection, 635, 27, 10, '2023-01-13',
                10, '144(A) - 113(H)', 27)
    insertGames(connection, 636, 5, 21, '2023-01-13', 21, '124(A) - 110(H)', 5)
    insertGames(connection, 637, 18, 24, '2023-01-13',
                18, '121(H) - 116(A)', 18)
    insertGames(connection, 638, 29, 22, '2023-01-13',
                29, '112(H) - 108(A)', 29)
    insertGames(connection, 639, 13, 8, '2023-01-13', 8, '115(A) - 103(H)', 13)
    insertGames(connection, 640, 26, 11, '2023-01-13',
                26, '139(H) - 114(A)', 26)
    insertGames(connection, 641, 16, 17, '2023-01-14',
                16, '111(H) - 95(A)', 16)
    insertGames(connection, 642, 5, 2, '2023-01-14', 2, '122(A) - 106(H)', 5)
    insertGames(connection, 643, 12, 15, '2023-01-14',
                15, '130(A) - 112(H)', 12)
    insertGames(connection, 644, 28, 1, '2023-01-14', 1, '114(A) - 103(H)', 28)
    insertGames(connection, 645, 18, 6, '2023-01-14',
                18, '110(H) - 102(A)', 18)
    insertGames(connection, 646, 29, 23, '2023-01-14',
                23, '118(A) - 117(H)', 29)
    insertGames(connection, 647, 25, 7, '2023-01-14',
                25, '136(H) - 119(A)', 25)
    insertGames(connection, 648, 9, 20, '2023-01-15', 20, '117(A) - 104(H)', 9)
    insertGames(connection, 649, 13, 11, '2023-01-15',
                13, '121(H) - 100(A)', 13)
    insertGames(connection, 650, 5, 10, '2023-01-15', 5, '132(H) - 118(A)', 5)
    insertGames(connection, 651, 3, 21, '2023-01-15', 21, '112(A) - 102(H)', 3)
    insertGames(connection, 652, 27, 26, '2023-01-15',
                26, '132(A) - 119(H)', 27)
    insertGames(connection, 653, 8, 22, '2023-01-15', 8, '119(H) - 116(A)', 8)
    insertGames(connection, 654, 25, 7, '2023-01-15',
                25, '140(H) - 123(A)', 25)
    insertGames(connection, 655, 14, 23, '2023-01-15',
                23, '113(A) - 112(H)', 13)
    insertGames(connection, 656, 5, 2, '2023-01-16', 2, '130(A) - 118(H)', 5)
    insertGames(connection, 657, 17, 12, '2023-01-16',
                17, '132(H) - 119(A)', 17)
    insertGames(connection, 658, 6, 19, '2023-01-16', 6, '113(H) - 103(A)', 6)
    insertGames(connection, 659, 20, 28, '2023-01-16',
                28, '123(A) - 121(H)', 20)
    insertGames(connection, 660, 30, 10, '2023-01-16',
                10, '127(A) - 118(H)', 30)
    insertGames(connection, 661, 1, 16, '2023-01-16', 1, '121(H) - 113(A)', 1)
    insertGames(connection, 662, 18, 29, '2023-01-16',
                29, '126(A) - 125(H)', 18)
    insertGames(connection, 663, 15, 24, '2023-01-16',
                15, '136(H) - 106(A)', 15)
    insertGames(connection, 664, 14, 11, '2023-01-16',
                14, '140(H) - 132(A)', 13)
    insertGames(connection, 665, 17, 28, '2023-01-17',
                17, '130(H) - 122(A)', 17)
    insertGames(connection, 666, 27, 3, '2023-01-17', 27, '106(H) - 98(A)', 27)
    insertGames(connection, 667, 8, 25, '2023-01-17', 8, '122(H) - 113(A)', 8)
    insertGames(connection, 668, 13, 23, '2023-01-17',
                23, '120(A) - 110(H)', 13)
    insertGames(connection, 669, 7, 1, '2023-01-18', 1, '130(A) - 122(H)', 7)
    insertGames(connection, 670, 20, 30, '2023-01-18',
                30, '116(A) - 105(H)', 20)
    insertGames(connection, 671, 11, 5, '2023-01-18', 5, '122(A) - 117(H)', 11)
    insertGames(connection, 672, 15, 6, '2023-01-18',
                15, '115(H) - 114(A)', 15)
    insertGames(connection, 673, 19, 16, '2023-01-18',
                16, '124(A) - 98(H)', 19)
    insertGames(connection, 674, 21, 12, '2023-01-18',
                21, '126(H) - 106(A)', 21)
    insertGames(connection, 675, 29, 13, '2023-01-18',
                29, '126(H) - 103(A)', 29)
    insertGames(connection, 676, 8, 18, '2023-01-18', 8, '122(H) - 118(A)', 8)
    insertGames(connection, 677, 14, 26, '2023-01-18',
                26, '116(A) - 111(H)', 13)
    insertGames(connection, 678, 9, 5, '2023-01-19', 5, '126(A) - 108(H)', 9)
    insertGames(connection, 679, 2, 10, '2023-01-19', 2, '121(H) - 118(A)', 2)
    insertGames(connection, 680, 18, 28, '2023-01-19',
                18, '128(H) - 126(A)', 18)
    insertGames(connection, 681, 24, 3, '2023-01-19',
                24, '117(H) - 112(A)', 24)
    insertGames(connection, 682, 25, 23, '2023-01-19',
                23, '105(A) - 95(H)', 25)
    insertGames(connection, 683, 22, 19, '2023-01-20',
                22, '123(H) - 110(A)', 22)
    insertGames(connection, 684, 1, 20, '2023-01-20', 1, '139(H) - 124(A)', 1)
    insertGames(connection, 685, 6, 10, '2023-01-20', 10, '120(A) - 114(H)', 6)
    insertGames(connection, 686, 7, 16, '2023-01-20', 7, '115(H) - 90(A)', 7)
    insertGames(connection, 687, 27, 13, '2023-01-20',
                13, '131(A) - 126(H)', 27)
    insertGames(connection, 688, 8, 12, '2023-01-20', 8, '134(H) - 111(A)', 8)
    insertGames(connection, 689, 29, 3, '2023-01-20', 3, '117(A) - 106(H)', 29)
    insertGames(connection, 690, 14, 15, '2023-01-20',
                14, '122(H) - 121(A)', 13)
    insertGames(connection, 691, 26, 21, '2023-01-20',
                26, '118(H) - 113(A)', 26)
    insertGames(connection, 692, 28, 2, '2023-01-21', 2, '106(A) - 104(H)', 28)
    insertGames(connection, 693, 30, 22, '2023-01-21',
                30, '138(H) - 118(A)', 30)
    insertGames(connection, 694, 1, 5, '2023-01-21', 5, '122(A) - 118(H)', 1)
    insertGames(connection, 695, 6, 17, '2023-01-21', 6, '114(H) - 102(A)', 6)
    insertGames(connection, 696, 18, 11, '2023-01-21',
                18, '113(H) - 104(A)', 18)
    insertGames(connection, 697, 24, 12, '2023-01-21',
                24, '112(H) - 107(A)', 24)
    insertGames(connection, 698, 26, 23, '2023-01-21',
                23, '129(A) - 127(H)', 26)
    insertGames(connection, 699, 7, 13, '2023-01-22', 13, '112(A) - 98(H)', 7)
    insertGames(connection, 700, 16, 19, '2023-01-22',
                16, '100(H) - 96(A)', 16)
    insertGames(connection, 701, 28, 20, '2023-01-22',
                28, '125(H) - 116(A)', 28)
    insertGames(connection, 702, 8, 21, '2023-01-22', 21, '101(A) - 99(H)', 8)
    insertGames(connection, 703, 24, 15, '2023-01-22',
                24, '112(H) - 110(A)', 24)
    insertGames(connection, 704, 10, 3, '2023-01-22', 3, '120(A) - 116(H)', 10)
    insertGames(connection, 705, 25, 14, '2023-01-22',
                14, '121(A) - 112(H)', 25)
    insertGames(connection, 706, 9, 17, '2023-01-23', 17, '150(A) - 130(H)', 9)
    insertGames(connection, 707, 22, 2, '2023-01-23', 22, '113(H) - 98(A)', 22)
    insertGames(connection, 708, 5, 1, '2023-01-23', 5, '111(H) - 100(A)', 5)
    insertGames(connection, 709, 11, 18, '2023-01-23',
                11, '119(H) - 114(A)', 11)
    insertGames(connection, 710, 29, 5, '2023-01-23',
                29, '120(H) - 102(A)', 29)
    insertGames(connection, 711, 25, 27, '2023-01-23',
                25, '147(H) - 127(A)', 25)
    insertGames(connection, 712, 26, 15, '2023-01-23',
                26, '133(H) - 100(A)', 26)
    insertGames(connection, 713, 12, 5, '2023-01-24',
                12, '116(H) - 110(A)', 12)
    insertGames(connection, 714, 16, 2, '2023-01-24', 16, '98(H) - 95(A)', 16)
    insertGames(connection, 715, 20, 6, '2023-01-24',
                20, '105(H) - 103(A)', 20)
    insertGames(connection, 716, 19, 8, '2023-01-24', 8, '99(A) - 98(H)', 19)
    insertGames(connection, 717, 7, 30, '2023-01-24', 30, '127(A) - 126(H)', 7)
    insertGames(connection, 718, 24, 5, '2023-01-24', 24, '128(H) - 97(A)', 24)
    insertGames(connection, 719, 14, 13, '2023-01-24',
                13, '133(A) - 115(H)', 13)
    insertGames(connection, 720, 22, 12, '2023-01-25',
                22, '126(H) - 120(A)', 22)
    insertGames(connection, 721, 23, 3, '2023-01-25',
                23, '137(H) - 133(A)', 23)
    insertGames(connection, 722, 11, 30, '2023-01-25',
                30, '108(A) - 103(H)', 11)
    insertGames(connection, 723, 17, 8, '2023-01-25', 17, '107(H) - 99(A)', 17)
    insertGames(connection, 724, 19, 18, '2023-01-25',
                18, '111(A) - 102(H)', 19)
    insertGames(connection, 725, 21, 1, '2023-01-25', 1, '137(A) - 132(H)', 21)
    insertGames(connection, 726, 10, 15, '2023-01-25',
                10, '122(H) - 120(A)', 10)
    insertGames(connection, 727, 25, 29, '2023-01-25',
                25, '134(H) - 124(A)', 25)
    insertGames(connection, 728, 26, 28, '2023-01-25',
                28, '113(A) - 95(H)', 26)
    insertGames(connection, 729, 14, 27, '2023-01-25',
                14, '113(H) - 104(A)', 13)
    insertGames(connection, 730, 2, 20, '2023-01-26', 20, '120(A) - 117(H)', 2)
    insertGames(connection, 731, 3, 9, '2023-01-26', 9, '130(A) - 122(H)', 3)
    insertGames(connection, 732, 5, 5, '2023-01-26', 5, '111(H) - 96(A)', 5)
    insertGames(connection, 733, 11, 6, '2023-01-26', 6, '113(A) - 95(H)', 11)
    insertGames(connection, 734, 24, 7, '2023-01-26', 7, '99(A) - 95(H)', 24)
    insertGames(connection, 735, 13, 27, '2023-01-26',
                13, '138(H) - 100(A)', 13)
    insertGames(connection, 736, 12, 17, '2023-01-27',
                17, '141(A) - 131(H)', 12)
    insertGames(connection, 737, 18, 15, '2023-01-27',
                18, '111(H) - 100(A)', 18)
    insertGames(connection, 738, 16, 22, '2023-01-27',
                16, '110(H) - 105(A)', 16)
    insertGames(connection, 739, 21, 6, '2023-01-27',
                21, '112(H) - 100(A)', 21)
    insertGames(connection, 740, 10, 28, '2023-01-27',
                10, '129(H) - 117(A)', 10)
    insertGames(connection, 741, 23, 8, '2023-01-28',
                23, '126(H) - 119(A)', 23)
    insertGames(connection, 742, 3, 20, '2023-01-28', 3, '122(H) - 115(A)', 3)
    insertGames(connection, 743, 9, 11, '2023-01-28', 11, '117(A) - 114(H)', 9)
    insertGames(connection, 744, 22, 5, '2023-01-28', 5, '128(A) - 109(H)', 22)
    insertGames(connection, 745, 1, 13, '2023-01-28', 13, '120(A) - 113(H)', 1)
    insertGames(connection, 746, 18, 26, '2023-01-28',
                18, '117(H) - 110(A)', 18)
    insertGames(connection, 747, 19, 30, '2023-01-28',
                30, '113(A) - 103(H)', 19)
    insertGames(connection, 748, 27, 24, '2023-01-28',
                24, '128(A) - 118(H)', 27)
    insertGames(connection, 749, 2, 14, '2023-01-28', 2, '125(H) - 121(A)', 2)
    insertGames(connection, 750, 29, 7, '2023-01-28',
                29, '108(H) - 100(A)', 29)
    insertGames(connection, 751, 25, 28, '2023-01-28',
                28, '123(A) - 105(H)', 25)
    insertGames(connection, 752, 5, 16, '2023-01-29', 5, '122(H) - 117(A)', 5)
    insertGames(connection, 753, 15, 12, '2023-01-29',
                15, '112(H) - 100(A)', 15)
    insertGames(connection, 754, 6, 13, '2023-01-29', 6, '122(H) - 99(A)', 6)
    insertGames(connection, 755, 17, 19, '2023-01-29',
                17, '135(H) - 110(A)', 17)
    insertGames(connection, 756, 23, 22, '2023-01-30',
                22, '119(A) - 109(H)', 23)
    insertGames(connection, 757, 3, 14, '2023-01-30', 3, '121(H) - 104(A)', 3)
    insertGames(connection, 758, 18, 26, '2023-01-30',
                26, '118(A) - 111(H)', 18)
    insertGames(connection, 759, 21, 10, '2023-01-30',
                10, '128(A) - 120(H)', 21)
    insertGames(connection, 760, 27, 30, '2023-01-30',
                30, '127(A) - 106(H)', 27)
    insertGames(connection, 761, 7, 9, '2023-01-30', 7, '111(H) - 105(A)', 7)
    insertGames(connection, 762, 24, 28, '2023-01-30',
                24, '114(H) - 106(A)', 24)
    insertGames(connection, 763, 25, 1, '2023-01-30',
                25, '129(H) - 125(A)', 25)
    insertGames(connection, 764, 6, 16, '2023-01-31', 16, '100(A) - 97(H)', 6)
    insertGames(connection, 765, 20, 14, '2023-01-31',
                14, '129(A) - 123(H)', 20)
    insertGames(connection, 766, 5, 13, '2023-01-31', 13, '108(A) - 103(H)', 5)
    insertGames(connection, 767, 17, 5, '2023-01-31',
                17, '124(H) - 115(A)', 17)
    insertGames(connection, 768, 8, 19, '2023-01-31', 8, '122(H) - 113(A)', 8)
    insertGames(connection, 769, 15, 25, '2023-02-01',
                25, '122(A) - 112(H)', 15)
    insertGames(connection, 770, 23, 22, '2023-02-01',
                23, '105(H) - 94(A)', 23)
    insertGames(connection, 771, 2, 3, '2023-02-01', 2, '139(H) - 96(A)', 2)
    insertGames(connection, 772, 11, 21, '2023-02-01',
                11, '112(H) - 106(A)', 11)
    insertGames(connection, 773, 18, 10, '2023-02-01',
                18, '119(H) - 114(A)', 18)
    insertGames(connection, 774, 27, 26, '2023-02-01',
                26, '119(A) - 109(H)', 27)
    insertGames(connection, 775, 29, 28, '2023-02-01',
                29, '131(H) - 128(A)', 29)
    insertGames(connection, 776, 24, 1, '2023-02-01', 1, '132(A) - 100(H)', 24)
    insertGames(connection, 777, 12, 14, '2023-02-02',
                14, '112(A) - 111(H)', 12)
    insertGames(connection, 778, 6, 15, '2023-02-02', 6, '128(H) - 113(A)', 6)
    insertGames(connection, 779, 20, 16, '2023-02-02',
                20, '106(H) - 104(A)', 20)
    insertGames(connection, 780, 4, 5, '2023-02-02', 4, '114(H) - 98(A)', 4)
    insertGames(connection, 781, 7, 19, '2023-02-02', 7, '111(H) - 106(A)', 7)
    insertGames(connection, 782, 8, 10, '2023-02-02', 8, '134(H) - 117(A)', 8)
    insertGames(connection, 783, 17, 13, '2023-02-02',
                17, '106(H) - 105(A)', 17)
    insertGames(connection, 784, 9, 5, '2023-02-03', 9, '118(H) - 112(A)', 9)
    insertGames(connection, 785, 12, 26, '2023-02-03',
                12, '107(H) - 104(A)', 12)
    insertGames(connection, 786, 30, 25, '2023-02-03',
                25, '124(A) - 116(H)', 30)
    insertGames(connection, 787, 2, 24, '2023-02-03', 24, '106(A) - 94(H)', 2)
    insertGames(connection, 788, 11, 28, '2023-02-03',
                28, '117(A) - 111(H)', 11)
    insertGames(connection, 789, 18, 22, '2023-02-03',
                22, '127(A) - 120(H)', 18)
    insertGames(connection, 790, 27, 23, '2023-02-03',
                23, '137(A) - 125(H)', 27)
    insertGames(connection, 791, 29, 1, '2023-02-03', 1, '115(A) - 108(H)', 29)
    insertGames(connection, 792, 3, 30, '2023-02-04', 3, '125(H) - 123(A)', 3)
    insertGames(connection, 793, 19, 14, '2023-02-04',
                19, '131(H) - 126(A)', 19)
    insertGames(connection, 794, 9, 24, '2023-02-04', 24, '116(A) - 100(H)', 9)
    insertGames(connection, 795, 20, 13, '2023-02-04',
                13, '134(A) - 128(H)', 20)
    insertGames(connection, 796, 4, 25, '2023-02-04', 4, '129(H) - 121(A)', 4)
    insertGames(connection, 797, 17, 16, '2023-02-04',
                17, '123(H) - 115(A)', 17)
    insertGames(connection, 798, 21, 11, '2023-02-04',
                21, '153(H) - 121(A)', 21)
    insertGames(connection, 799, 10, 7, '2023-02-04',
                10, '119(H) - 113(A)', 10)
    insertGames(connection, 800, 8, 1, '2023-02-04', 8, '128(H) - 108(A)', 8)
    insertGames(connection, 801, 5, 22, '2023-02-05', 22, '119(A) - 113(H)', 5)
    insertGames(connection, 802, 12, 6, '2023-02-05', 6, '122(A) - 103(H)', 12)
    insertGames(connection, 803, 15, 28, '2023-02-05',
                28, '106(A) - 103(H)', 15)
    insertGames(connection, 804, 20, 23, '2023-02-05',
                20, '108(H) - 97(A)', 20)
    insertGames(connection, 805, 18, 8, '2023-02-05', 18, '128(H) - 98(A)', 18)
    insertGames(connection, 806, 19, 26, '2023-02-05',
                19, '136(H) - 104(A)', 19)
    insertGames(connection, 807, 9, 2, '2023-02-06', 2, '111(A) - 99(H)', 9)
    insertGames(connection, 808, 30, 6, '2023-02-06', 6, '114(A) - 91(H)', 30)
    insertGames(connection, 809, 3, 13, '2023-02-06', 13, '124(A) - 116(H)', 3)
    insertGames(connection, 810, 4, 27, '2023-02-06', 4, '128(H) - 104(A)', 4)
    insertGames(connection, 811, 11, 26, '2023-02-06',
                26, '140(A) - 120(H)', 11)
    insertGames(connection, 812, 29, 7, '2023-02-06', 7, '124(A) - 111(H)', 29)
    insertGames(connection, 813, 10, 21, '2023-02-06',
                10, '141(H) - 114(A)', 10)
    insertGames(connection, 814, 25, 17, '2023-02-06',
                17, '127(A) - 108(H)', 25)
    insertGames(connection, 815, 22, 20, '2023-02-07',
                20, '102(A) - 98(H)', 22)
    insertGames(connection, 816, 3, 24, '2023-02-07', 24, '116(A) - 112(H)', 3)
    insertGames(connection, 817, 19, 1, '2023-02-07',
                19, '116(H) - 107(A)', 19)
    insertGames(connection, 818, 15, 4, '2023-02-07', 15, '104(H) - 89(A)', 15)
    insertGames(connection, 819, 8, 18, '2023-02-07', 8, '146(H) - 112(A)', 8)
    insertGames(connection, 820, 14, 21, '2023-02-07',
                21, '133(A) - 130(H)', 13)
    insertGames(connection, 821, 6, 9, '2023-02-08', 6, '113(H) - 85(A)', 6)
    insertGames(connection, 822, 30, 5, '2023-02-08',
                30, '118(H) - 104(A)', 30)
    insertGames(connection, 823, 2, 23, '2023-02-08', 2, '106(H) - 99(A)', 2)
    insertGames(connection, 824, 16, 12, '2023-02-08',
                16, '116(H) - 111(A)', 16)
    insertGames(connection, 825, 28, 27, '2023-02-08',
                28, '112(H) - 98(A)', 28)
    insertGames(connection, 826, 11, 26, '2023-02-08',
                26, '130(A) - 128(H)', 11)
    insertGames(connection, 827, 29, 18, '2023-02-08',
                18, '143(A) - 118(H)', 29)
    insertGames(connection, 828, 13, 7, '2023-02-08', 7, '110(A) - 104(H)', 13)
    insertGames(connection, 829, 25, 10, '2023-02-08',
                25, '125(H) - 122(A)', 25)
    insertGames(connection, 830, 22, 8, '2023-02-09',
                22, '115(H) - 104(A)', 22)
    insertGames(connection, 831, 1, 24, '2023-02-09', 1, '116(H) - 107(A)', 1)
    insertGames(connection, 832, 3, 4, '2023-02-09', 3, '116(H) - 105(A)', 3)
    insertGames(connection, 833, 14, 17, '2023-02-09',
                17, '115(A) - 106(H)', 13)
    insertGames(connection, 834, 9, 27, '2023-02-10', 9, '138(H) - 131(A)', 9)
    insertGames(connection, 835, 12, 24, '2023-02-10',
                24, '117(A) - 104(H)', 12)
    insertGames(connection, 836, 23, 20, '2023-02-10',
                23, '119(H) - 108(A)', 23)
    insertGames(connection, 837, 2, 5, '2023-02-10', 2, '127(H) - 116(A)', 2)
    insertGames(connection, 838, 28, 29, '2023-02-10',
                29, '122(A) - 116(H)', 28)
    insertGames(connection, 839, 15, 18, '2023-02-10',
                15, '128(H) - 107(A)', 15)
    insertGames(connection, 840, 16, 11, '2023-02-10', 16, '97(H) - 95(A)', 16)
    insertGames(connection, 841, 19, 6, '2023-02-10', 6, '118(A) - 107(H)', 19)
    insertGames(connection, 842, 25, 21, '2023-02-10',
                21, '138(A) - 129(H)', 25)
    insertGames(connection, 843, 26, 7, '2023-02-10', 7, '122(A) - 114(H)', 26)
    insertGames(connection, 844, 13, 17, '2023-02-10',
                17, '119(A) - 106(H)', 13)
    insertGames(connection, 845, 3, 23, '2023-02-11', 23, '101(A) - 98(H)', 3)
    insertGames(connection, 846, 5, 8, '2023-02-11', 8, '119(A) - 105(H)', 5)
    insertGames(connection, 847, 22, 16, '2023-02-11',
                16, '107(A) - 103(H)', 22)
    insertGames(connection, 848, 30, 12, '2023-02-11',
                30, '127(H) - 113(A)', 30)
    insertGames(connection, 849, 1, 27, '2023-02-11', 1, '125(H) - 106(A)', 1)
    insertGames(connection, 850, 20, 29, '2023-02-11',
                20, '126(H) - 120(A)', 20)
    insertGames(connection, 851, 6, 4, '2023-02-11', 6, '97(H) - 89(A)', 6)
    insertGames(connection, 852, 10, 14, '2023-02-11',
                14, '109(A) - 103(H)', 10)
    insertGames(connection, 853, 26, 7, '2023-02-11',
                26, '133(H) - 128(A)', 26)
    insertGames(connection, 854, 2, 15, '2023-02-12', 2, '119(H) - 109(A)', 2)
    insertGames(connection, 855, 28, 9, '2023-02-12',
                28, '119(H) - 118(A)', 28)
    insertGames(connection, 856, 5, 1, '2023-02-13', 5, '144(H) - 138(A)', 5)
    insertGames(connection, 857, 6, 27, '2023-02-13', 6, '117(H) - 109(A)', 6)
    insertGames(connection, 858, 12, 29, '2023-02-13',
                29, '123(A) - 117(H)', 12)
    insertGames(connection, 859, 23, 11, '2023-02-13',
                23, '123(H) - 104(A)', 23)
    insertGames(connection, 860, 16, 8, '2023-02-13', 8, '112(A) - 108(H)', 16)
    insertGames(connection, 861, 20, 3, '2023-02-13',
                20, '124(H) - 106(A)', 20)
    insertGames(connection, 862, 4, 22, '2023-02-13', 22, '100(A) - 91(H)', 4)
    insertGames(connection, 863, 21, 19, '2023-02-13',
                19, '103(A) - 100(H)', 21)
    insertGames(connection, 864, 7, 18, '2023-02-13', 18, '124(A) - 121(H)', 7)
    insertGames(connection, 865, 10, 30, '2023-02-13',
                10, '135(H) - 126(A)', 10)
    insertGames(connection, 866, 25, 14, '2023-02-13',
                25, '127(H) - 115(A)', 25)
    insertGames(connection, 867, 17, 2, '2023-02-14',
                17, '131(H) - 125(A)', 17)
    insertGames(connection, 868, 28, 22, '2023-02-14',
                28, '123(H) - 113(A)', 28)
    insertGames(connection, 869, 24, 26, '2023-02-14',
                24, '120(H) - 109(A)', 24)
    insertGames(connection, 870, 13, 10, '2023-02-14',
                13, '134(H) - 124(A)', 13)
    insertGames(connection, 871, 25, 30, '2023-02-14',
                30, '126(A) - 101(H)', 25)
    insertGames(connection, 872, 5, 27, '2023-02-15', 5, '120(H) - 110(A)', 5)
    insertGames(connection, 873, 12, 4, '2023-02-15',
                12, '117(H) - 113(A)', 12)
    insertGames(connection, 874, 1, 20, '2023-02-15', 20, '122(A) - 101(H)', 1)
    insertGames(connection, 875, 2, 9, '2023-02-15', 2, '127(H) - 109(A)', 2)
    insertGames(connection, 876, 3, 16, '2023-02-15', 3, '116(H) - 105(A)', 3)
    insertGames(connection, 877, 23, 6, '2023-02-15',
                23, '118(H) - 112(A)', 23)
    insertGames(connection, 878, 15, 29, '2023-02-15',
                15, '117(H) - 111(A)', 15)
    insertGames(connection, 879, 21, 11, '2023-02-15',
                21, '133(H) - 96(A)', 21)
    insertGames(connection, 880, 8, 7, '2023-02-15', 8, '118(H) - 109(A)', 8)
    insertGames(connection, 881, 14, 19, '2023-02-15',
                14, '120(H) - 102(A)', 13)
    insertGames(connection, 882, 4, 17, '2023-02-16', 17, '112(A) - 100(H)', 4)
    insertGames(connection, 883, 18, 30, '2023-02-16',
                30, '114(A) - 106(H)', 18)
    insertGames(connection, 884, 24, 13, '2023-02-16',
                13, '116(A) - 107(H)', 24)
    insertGames(connection, 885, 6, 8, '2023-02-23', 8, '115(A) - 109(H)', 6)
    insertGames(connection, 886, 12, 2, '2023-02-23', 2, '142(A) - 138(H)', 12)
    insertGames(connection, 887, 22, 9, '2023-02-23',
                22, '108(H) - 106(A)', 22)
    insertGames(connection, 888, 23, 15, '2023-02-23',
                23, '110(H) - 105(A)', 23)
    insertGames(connection, 889, 28, 19, '2023-02-23',
                28, '115(H) - 110(A)', 28)
    insertGames(connection, 890, 7, 27, '2023-02-23', 7, '142(H) - 116(A)', 7)
    insertGames(connection, 891, 29, 21, '2023-02-23',
                29, '120(H) - 119(A)', 29)
    insertGames(connection, 892, 14, 10, '2023-02-23',
                14, '124(H) - 111(A)', 13)
    insertGames(connection, 893, 26, 25, '2023-02-23',
                26, '133(H) - 116(A)', 26)
    insertGames(connection, 894, 30, 20, '2023-02-24',
                20, '115(A) - 109(H)', 30)
    insertGames(connection, 895, 1, 6, '2023-02-24', 1, '136(H) - 119(A)', 1)
    insertGames(connection, 896, 17, 16, '2023-02-24',
                17, '128(H) - 99(A)', 17)
    insertGames(connection, 897, 4, 3, '2023-02-24', 4, '131(H) - 87(A)', 4)
    insertGames(connection, 898, 18, 5, '2023-02-24', 5, '121(A) - 113(H)', 18)
    insertGames(connection, 899, 10, 11, '2023-02-24',
                10, '116(H) - 101(A)', 10)
    insertGames(connection, 900, 24, 21, '2023-02-24',
                24, '124(H) - 115(A)', 24)
    insertGames(connection, 901, 13, 26, '2023-02-24',
                26, '176(A) - 175(H)', 13)
    insertGames(connection, 902, 9, 28, '2023-02-25', 28, '95(A) - 91(H)', 9)
    insertGames(connection, 903, 5, 16, '2023-02-25', 5, '108(H) - 103(A)', 5)
    insertGames(connection, 904, 22, 12, '2023-02-25',
                12, '121(A) - 108(H)', 22)
    insertGames(connection, 905, 20, 19, '2023-02-25',
                20, '128(H) - 106(A)', 20)
    insertGames(connection, 906, 15, 8, '2023-02-25', 15, '112(H) - 94(A)', 15)
    insertGames(connection, 907, 23, 2, '2023-02-25', 2, '110(A) - 107(H)', 23)
    insertGames(connection, 908, 29, 27, '2023-02-25',
                29, '118(H) - 102(A)', 29)
    insertGames(connection, 909, 17, 24, '2023-02-26',
                17, '104(H) - 101(A)', 17)
    insertGames(connection, 910, 1, 3, '2023-02-26', 1, '129(H) - 127(A)', 1)
    insertGames(connection, 911, 4, 30, '2023-02-26', 4, '102(H) - 82(A)', 4)
    insertGames(connection, 912, 7, 14, '2023-02-26', 14, '111(A) - 108(H)', 7)
    insertGames(connection, 913, 6, 28, '2023-02-26', 6, '118(H) - 93(A)', 6)
    insertGames(connection, 914, 21, 26, '2023-02-26',
                26, '124(A) - 115(H)', 21)
    insertGames(connection, 915, 10, 18, '2023-02-26',
                10, '109(H) - 104(A)', 10)
    insertGames(connection, 916, 25, 11, '2023-02-26',
                25, '131(H) - 114(A)', 25)
    insertGames(connection, 917, 8, 13, '2023-02-26', 8, '134(H) - 124(A)', 8)
    insertGames(connection, 918, 5, 9, '2023-02-27', 5, '117(H) - 106(A)', 5)
    insertGames(connection, 919, 23, 16, '2023-02-27',
                16, '101(A) - 99(H)', 23)
    insertGames(connection, 920, 20, 2, '2023-02-27', 20, '109(H) - 94(A)', 20)
    insertGames(connection, 921, 19, 22, '2023-02-27',
                22, '101(A) - 93(H)', 19)
    insertGames(connection, 922, 1, 30, '2023-02-28', 30, '119(A) - 116(H)', 1)
    insertGames(connection, 923, 3, 17, '2023-02-28', 17, '118(A) - 104(H)', 3)
    insertGames(connection, 924, 15, 14, '2023-02-28',
                15, '121(H) - 109(A)', 15)
    insertGames(connection, 925, 28, 4, '2023-02-28', 28, '104(H) - 98(A)', 28)
    insertGames(connection, 926, 11, 8, '2023-02-28', 8, '133(A) - 112(H)', 11)
    insertGames(connection, 927, 21, 26, '2023-02-28',
                26, '123(A) - 117(H)', 21)
    insertGames(connection, 928, 7, 12, '2023-02-28', 12, '124(A) - 122(H)', 7)
    insertGames(connection, 929, 29, 27, '2023-02-28',
                27, '102(A) - 94(H)', 29)
    insertGames(connection, 930, 10, 25, '2023-02-28',
                10, '123(H) - 105(A)', 10)
    insertGames(connection, 931, 13, 18, '2023-02-28',
                18, '108(A) - 101(H)', 13)
    insertGames(connection, 932, 5, 24, '2023-03-01', 24, '105(A) - 91(H)', 5)
    insertGames(connection, 933, 9, 4, '2023-03-01', 4, '117(A) - 115(H)', 9)
    insertGames(connection, 934, 2, 6, '2023-03-01', 2, '117(H) - 113(A)', 2)
    insertGames(connection, 935, 16, 23, '2023-03-01',
                23, '119(A) - 96(H)', 16)
    insertGames(connection, 936, 20, 3, '2023-03-01',
                20, '142(H) - 118(A)', 20)
    insertGames(connection, 937, 11, 15, '2023-03-01',
                15, '113(A) - 99(H)', 11)
    insertGames(connection, 938, 17, 22, '2023-03-01',
                17, '139(H) - 117(A)', 17)
    insertGames(connection, 939, 21, 14, '2023-03-01',
                14, '123(A) - 117(H)', 21)
    insertGames(connection, 940, 25, 19, '2023-03-01',
                19, '121(A) - 110(H)', 25)
    insertGames(connection, 941, 30, 28, '2023-03-02',
                30, '119(H) - 108(A)', 30)
    insertGames(connection, 942, 7, 23, '2023-03-02', 7, '133(H) - 126(A)', 7)
    insertGames(connection, 943, 27, 12, '2023-03-02',
                27, '110(H) - 99(A)', 27)
    insertGames(connection, 944, 10, 13, '2023-03-02',
                10, '115(H) - 91(A)', 10)
    insertGames(connection, 945, 5, 22, '2023-03-03', 22, '117(A) - 106(H)', 5)
    insertGames(connection, 946, 1, 25, '2023-03-03', 1, '129(H) - 111(A)', 1)
    insertGames(connection, 947, 2, 3, '2023-03-03', 3, '115(A) - 105(H)', 2)
    insertGames(connection, 948, 4, 24, '2023-03-03', 24, '125(A) - 104(H)', 4)
    insertGames(connection, 949, 16, 20, '2023-03-03',
                20, '122(A) - 120(H)', 16)
    insertGames(connection, 950, 21, 29, '2023-03-03',
                21, '130(H) - 103(A)', 21)
    insertGames(connection, 951, 8, 15, '2023-03-03', 8, '113(H) - 97(A)', 8)
    insertGames(connection, 952, 10, 19, '2023-03-03',
                10, '108(H) - 99(A)', 10)
    insertGames(connection, 953, 26, 13, '2023-03-03',
                26, '128(H) - 127(A)', 26)
    insertGames(connection, 954, 14, 18, '2023-03-03',
                18, '110(A) - 102(H)', 13)
    insertGames(connection, 955, 30, 28, '2023-03-04',
                28, '116(A) - 109(H)', 30)
    insertGames(connection, 956, 6, 9, '2023-03-04', 6, '114(H) - 90(A)', 6)
    insertGames(connection, 957, 16, 1, '2023-03-04',
                16, '117(H) - 109(A)', 16)
    insertGames(connection, 958, 27, 11, '2023-03-04',
                11, '122(A) - 110(H)', 27)
    insertGames(connection, 959, 17, 23, '2023-03-04',
                23, '133(A) - 130(H)', 17)
    insertGames(connection, 960, 26, 18, '2023-03-04',
                18, '138(A) - 134(H)', 26)
    insertGames(connection, 961, 7, 24, '2023-03-05', 24, '130(A) - 126(H)', 7)
    insertGames(connection, 962, 4, 12, '2023-03-05', 12, '125(A) - 122(H)', 4)
    insertGames(connection, 963, 14, 10, '2023-03-05',
                14, '113(H) - 105(A)', 13)
    insertGames(connection, 964, 3, 5, '2023-03-05', 3, '102(H) - 86(A)', 3)
    insertGames(connection, 965, 22, 25, '2023-03-05',
                25, '122(A) - 119(H)', 22)
    insertGames(connection, 966, 11, 27, '2023-03-05',
                11, '142(H) - 110(A)', 11)
    insertGames(connection, 967, 21, 29, '2023-03-05',
                21, '129(H) - 119(A)', 21)
    insertGames(connection, 968, 2, 20, '2023-03-05', 20, '131(A) - 129(H)', 2)
    insertGames(connection, 969, 30, 17, '2023-03-05',
                17, '117(A) - 111(H)', 30)
    insertGames(connection, 970, 13, 15, '2023-03-05',
                13, '135(H) - 129(A)', 13)
    insertGames(connection, 971, 6, 2, '2023-03-06', 6, '118(H) - 114(A)', 6)
    insertGames(connection, 972, 9, 25, '2023-03-06', 25, '110(A) - 104(H)', 9)
    insertGames(connection, 973, 12, 23, '2023-03-06',
                23, '147(A) - 143(H)', 12)
    insertGames(connection, 974, 16, 1, '2023-03-06',
                16, '130(H) - 128(A)', 16)
    insertGames(connection, 975, 8, 28, '2023-03-06', 8, '118(H) - 113(A)', 8)
    insertGames(connection, 976, 26, 19, '2023-03-06',
                26, '123(H) - 108(A)', 26)
    insertGames(connection, 977, 9, 30, '2023-03-07', 30, '119(A) - 117(H)', 9)
    insertGames(connection, 978, 22, 17, '2023-03-07',
                17, '134(A) - 123(H)', 22)
    insertGames(connection, 979, 18, 23, '2023-03-07',
                23, '117(A) - 94(H)', 18)
    insertGames(connection, 980, 20, 5, '2023-03-07', 5, '112(A) - 105(H)', 20)
    insertGames(connection, 981, 11, 3, '2023-03-07', 3, '118(A) - 96(H)', 11)
    insertGames(connection, 982, 21, 10, '2023-03-07',
                21, '137(H) - 128(A)', 21)
    insertGames(connection, 983, 7, 29, '2023-03-07', 7, '120(H) - 116(A)', 7)
    insertGames(connection, 984, 14, 15, '2023-03-07',
                14, '112(H) - 103(A)', 13)
    insertGames(connection, 985, 30, 1, '2023-03-08', 1, '122(A) - 120(H)', 30)
    insertGames(connection, 986, 2, 25, '2023-03-08', 2, '115(H) - 93(A)', 2)
    insertGames(connection, 987, 16, 6, '2023-03-08', 6, '104(A) - 100(H)', 16)
    insertGames(connection, 988, 19, 7, '2023-03-08',
                19, '113(H) - 106(A)', 19)
    insertGames(connection, 989, 8, 4, '2023-03-08', 4, '117(A) - 96(H)', 8)
    insertGames(connection, 990, 24, 21, '2023-03-08',
                24, '132(H) - 101(A)', 24)
    insertGames(connection, 991, 13, 28, '2023-03-08',
                13, '108(H) - 100(A)', 13)
    insertGames(connection, 992, 9, 5, '2023-03-09', 5, '113(A) - 103(H)', 9)
    insertGames(connection, 993, 12, 11, '2023-03-09',
                12, '134(H) - 125(A)', 12)
    insertGames(connection, 994, 22, 29, '2023-03-09',
                29, '131(A) - 124(H)', 22)
    insertGames(connection, 995, 15, 10, '2023-03-09',
                15, '131(H) - 110(A)', 15)
    insertGames(connection, 996, 17, 3, '2023-03-09',
                17, '118(H) - 113(A)', 17)
    insertGames(connection, 997, 26, 20, '2023-03-09',
                26, '122(H) - 117(A)', 26)
    insertGames(connection, 998, 23, 25, '2023-03-10',
                23, '120(H) - 119(A)', 23)
    insertGames(connection, 999, 30, 1, '2023-03-10', 1, '114(A) - 107(H)', 30)
    insertGames(connection, 1000, 16, 6, '2023-03-10',
                16, '119(H) - 115(A)', 16)
    insertGames(connection, 1001, 18, 3, '2023-03-10',
                3, '124(A) - 123(H)', 18)
    insertGames(connection, 1002, 27, 8, '2023-03-10',
                27, '128(H) - 120(A)', 27)
    insertGames(connection, 1003, 14, 28, '2023-03-10',
                14, '122(H) - 112(A)', 13)
    insertGames(connection, 1004, 13, 20,
                '2023-03-11', 13, '106(H) - 95(A)', 13)
    insertGames(connection, 1005, 5, 29, '2023-03-11',
                29, '119(A) - 111(H)', 5)
    insertGames(connection, 1006, 9, 12, '2023-03-11',
                12, '121(A) - 115(H)', 9)
    insertGames(connection, 1007, 22, 16, '2023-03-11',
                22, '126(H) - 114(A)', 22)
    insertGames(connection, 1008, 1, 2, '2023-03-11', 2, '134(A) - 125(H)', 1)
    insertGames(connection, 1009, 11, 4, '2023-03-11',
                4, '119(A) - 111(H)', 11)
    insertGames(connection, 1010, 15, 7, '2023-03-11',
                15, '112(H) - 108(A)', 15)
    insertGames(connection, 1011, 10, 17, '2023-03-11',
                10, '125(H) - 116(A)', 10)
    insertGames(connection, 1012, 19, 21,
                '2023-03-11', 21, '110(A) - 96(H)', 19)
    insertGames(connection, 1013, 24, 26, '2023-03-11',
                26, '128(A) - 119(H)', 24)
    insertGames(connection, 1014, 8, 3, '2023-03-12', 3, '122(A) - 120(H)', 8)
    insertGames(connection, 1015, 5, 6, '2023-03-12', 6, '114(A) - 108(H)', 5)
    insertGames(connection, 1016, 23, 30,
                '2023-03-12', 23, '112(H) - 93(A)', 23)
    insertGames(connection, 1017, 19, 25, '2023-03-12',
                19, '127(H) - 110(A)', 19)
    insertGames(connection, 1018, 27, 21,
                '2023-03-12', 21, '102(A) - 90(H)', 27)
    insertGames(connection, 1019, 14, 20, '2023-03-12',
                20, '112(A) - 108(H)', 13)
    insertGames(connection, 1020, 9, 12, '2023-03-13', 9, '117(H) - 97(A)', 9)
    insertGames(connection, 1021, 1, 18, '2023-03-13',
                18, '136(A) - 115(H)', 1)
    insertGames(connection, 1022, 7, 15, '2023-03-13', 15, '104(A) - 88(H)', 7)
    insertGames(connection, 1023, 16, 29, '2023-03-13',
                16, '119(H) - 115(A)', 16)
    insertGames(connection, 1024, 11, 2, '2023-03-13',
                11, '111(H) - 109(A)', 11)
    insertGames(connection, 1025, 10, 24, '2023-03-13',
                10, '123(H) - 112(A)', 10)
    insertGames(connection, 1026, 26, 17, '2023-03-13',
                17, '133(A) - 124(H)', 26)
    insertGames(connection, 1027, 5, 6, '2023-03-14', 6, '120(A) - 104(H)', 5)
    insertGames(connection, 1028, 30, 9, '2023-03-14',
                30, '117(H) - 97(A)', 30)
    insertGames(connection, 1029, 28, 8, '2023-03-14',
                28, '125(H) - 110(A)', 28)
    insertGames(connection, 1030, 19, 14, '2023-03-14',
                14, '123(A) - 108(H)', 19)
    insertGames(connection, 1031, 21, 3, '2023-03-14',
                21, '121(H) - 107(A)', 21)
    insertGames(connection, 1032, 27, 22, '2023-03-14',
                27, '132(H) - 114(A)', 27)
    insertGames(connection, 1033, 24, 17, '2023-03-14',
                17, '116(A) - 104(H)', 24)
    insertGames(connection, 1034, 25, 20, '2023-03-14',
                20, '123(A) - 107(H)', 25)
    insertGames(connection, 1035, 6, 23, '2023-03-15',
                23, '118(A) - 109(H)', 6)
    insertGames(connection, 1036, 16, 15, '2023-03-15',
                16, '138(H) - 119(A)', 16)
    insertGames(connection, 1037, 4, 26, '2023-03-15',
                26, '117(A) - 114(H)', 4)
    insertGames(connection, 1038, 11, 14, '2023-03-15',
                11, '114(H) - 110(A)', 11)
    insertGames(connection, 1039, 18, 2, '2023-03-15',
                2, '104(A) - 102(H)', 18)
    insertGames(connection, 1040, 27, 7, '2023-03-15',
                7, '137(A) - 128(H)', 27)
    insertGames(connection, 1041, 13, 10, '2023-03-15',
                13, '134(H) - 126(A)', 13)
    insertGames(connection, 1042, 9, 8, '2023-03-16', 8, '119(A) - 100(H)', 9)
    insertGames(connection, 1043, 3, 26, '2023-03-16', 26, '101(A) - 96(H)', 3)
    insertGames(connection, 1044, 28, 21, '2023-03-16',
                28, '128(H) - 111(A)', 28)
    insertGames(connection, 1045, 17, 12, '2023-03-16',
                12, '139(A) - 123(H)', 17)
    insertGames(connection, 1046, 24, 22, '2023-03-16',
                24, '116(H) - 113(A)', 24)
    insertGames(connection, 1047, 5, 23, '2023-03-17', 23, '121(A) - 82(H)', 5)
    insertGames(connection, 1048, 1, 10, '2023-03-17', 1, '127(H) - 119(A)', 1)
    insertGames(connection, 1049, 6, 30, '2023-03-17', 6, '117(H) - 94(A)', 6)
    insertGames(connection, 1050, 4, 18, '2023-03-17', 4, '139(H) - 131(A)', 4)
    insertGames(connection, 1051, 11, 19, '2023-03-17',
                11, '114(H) - 112(A)', 11)
    insertGames(connection, 1052, 27, 15, '2023-03-17',
                15, '126(A) - 120(H)', 27)
    insertGames(connection, 1053, 25, 2, '2023-03-17',
                2, '126(A) - 112(H)', 25)
    insertGames(connection, 1054, 14, 7, '2023-03-17',
                7, '111(A) - 110(H)', 13)
    insertGames(connection, 1055, 20, 8, '2023-03-18',
                20, '116(H) - 110(A)', 20)
    insertGames(connection, 1056, 13, 22, '2023-03-18',
                22, '113(A) - 108(H)', 13)
    insertGames(connection, 1057, 12, 23, '2023-03-18',
                23, '141(A) - 121(H)', 12)
    insertGames(connection, 1058, 28, 18, '2023-03-18',
                28, '122(H) - 107(A)', 28)
    insertGames(connection, 1059, 4, 16, '2023-03-18', 4, '113(H) - 99(A)', 4)
    insertGames(connection, 1060, 15, 10, '2023-03-18',
                15, '133(H) - 119(A)', 15)
    insertGames(connection, 1061, 30, 26, '2023-03-18',
                26, '132(A) - 118(H)', 30)
    insertGames(connection, 1062, 29, 2, '2023-03-18',
                29, '118(H) - 117(A)', 29)
    insertGames(connection, 1063, 3, 8, '2023-03-19', 8, '108(A) - 102(H)', 3)
    insertGames(connection, 1064, 21, 24, '2023-03-19',
                21, '124(H) - 120(A)', 21)
    insertGames(connection, 1065, 27, 1, '2023-03-19',
                27, '126(H) - 118(A)', 27)
    insertGames(connection, 1066, 9, 16, '2023-03-19',
                16, '112(A) - 100(H)', 9)
    insertGames(connection, 1067, 11, 19, '2023-03-19',
                19, '117(A) - 107(H)', 11)
    insertGames(connection, 1068, 17, 28, '2023-03-19',
                17, '118(H) - 111(A)', 17)
    insertGames(connection, 1069, 25, 13, '2023-03-19',
                13, '117(A) - 102(H)', 25)
    insertGames(connection, 1070, 14, 22, '2023-03-19',
                14, '111(H) - 105(A)', 13)
    insertGames(connection, 1071, 5, 12, '2023-03-20', 5, '115(H) - 109(A)', 5)
    insertGames(connection, 1072, 23, 4, '2023-03-20',
                4, '109(A) - 105(H)', 23)
    insertGames(connection, 1073, 20, 18, '2023-03-20',
                18, '140(A) - 134(H)', 20)
    insertGames(connection, 1074, 11, 10, '2023-03-20',
                10, '121(A) - 108(H)', 11)
    insertGames(connection, 1075, 15, 7, '2023-03-20',
                15, '112(H) - 108(A)', 15)
    insertGames(connection, 1076, 29, 26, '2023-03-20',
                29, '128(H) - 120(A)', 29)
    insertGames(connection, 1077, 22, 30, '2023-03-21',
                22, '122(H) - 112(A)', 22)
    insertGames(connection, 1078, 1, 9, '2023-03-21', 1, '129(H) - 107(A)', 1)
    insertGames(connection, 1079, 3, 6, '2023-03-21', 6, '115(A) - 109(H)', 3)
    insertGames(connection, 1080, 19, 27,
                '2023-03-21', 19, '119(H) - 84(A)', 19)
    insertGames(connection, 1081, 26, 2, '2023-03-21',
                2, '132(A) - 109(H)', 26)
    insertGames(connection, 1082, 13, 21, '2023-03-21',
                21, '101(A) - 100(H)', 13)
    insertGames(connection, 1083, 30, 8, '2023-03-22',
                8, '118(A) - 104(H)', 30)
    insertGames(connection, 1084, 7, 10, '2023-03-22',
                10, '127(A) - 125(H)', 7)
    insertGames(connection, 1085, 16, 20, '2023-03-22',
                16, '127(H) - 120(A)', 16)
    insertGames(connection, 1086, 28, 12, '2023-03-22',
                12, '118(A) - 114(H)', 28)
    insertGames(connection, 1087, 4, 23, '2023-03-22', 23, '116(A) - 91(H)', 4)
    insertGames(connection, 1088, 15, 11, '2023-03-22',
                15, '130(H) - 125(A)', 15)
    insertGames(connection, 1089, 17, 27,
                '2023-03-22', 17, '130(H) - 94(A)', 17)
    insertGames(connection, 1090, 18, 1, '2023-03-22',
                18, '125(H) - 124(A)', 18)
    insertGames(connection, 1091, 29, 25, '2023-03-22',
                25, '127(A) - 115(H)', 29)
    insertGames(connection, 1092, 14, 24, '2023-03-22',
                14, '122(H) - 111(A)', 13)
    insertGames(connection, 1093, 22, 20, '2023-03-23',
                22, '111(H) - 106(A)', 22)
    insertGames(connection, 1094, 3, 6, '2023-03-23', 6, '116(A) - 114(H)', 3)
    insertGames(connection, 1095, 19, 5, '2023-03-23',
                19, '115(H) - 96(A)', 19)
    insertGames(connection, 1096, 13, 21, '2023-03-23',
                13, '127(H) - 105(A)', 13)
    insertGames(connection, 1097, 2, 12, '2023-03-24', 2, '120(H) - 95(A)', 2)
    insertGames(connection, 1098, 30, 27, '2023-03-24',
                30, '136(H) - 124(A)', 30)
    insertGames(connection, 1099, 28, 9, '2023-03-24',
                28, '118(H) - 97(A)', 28)
    insertGames(connection, 1100, 15, 11, '2023-03-24',
                15, '151(H) - 114(A)', 15)
    insertGames(connection, 1101, 7, 5, '2023-03-24', 5, '117(A) - 109(H)', 7)
    insertGames(connection, 1102, 29, 17, '2023-03-24',
                17, '144(A) - 116(H)', 29)
    insertGames(connection, 1103, 10, 23, '2023-03-24',
                10, '120(H) - 112(A)', 10)
    insertGames(connection, 1104, 25, 4, '2023-03-24', 4, '124(A) - 96(H)', 25)
    insertGames(connection, 1105, 26, 24, '2023-03-24',
                26, '135(H) - 127(A)', 26)
    insertGames(connection, 1106, 14, 21, '2023-03-24',
                14, '116(H) - 111(A)', 13)
    insertGames(connection, 1107, 1, 12, '2023-03-25', 1, '143(H) - 130(A)', 1)
    insertGames(connection, 1108, 16, 3, '2023-03-25',
                3, '129(A) - 100(H)', 16)
    insertGames(connection, 1109, 8, 17, '2023-03-25', 8, '129(H) - 106(A)', 8)
    insertGames(connection, 1110, 24, 23, '2023-03-25',
                24, '125(H) - 105(A)', 24)
    insertGames(connection, 1111, 26, 29, '2023-03-25',
                26, '121(H) - 113(A)', 26)
    insertGames(connection, 1112, 13, 19, '2023-03-25',
                19, '131(A) - 110(H)', 13)
    insertGames(connection, 1113, 5, 7, '2023-03-26', 5, '110(H) - 104(A)', 5)
    insertGames(connection, 1114, 14, 4, '2023-03-26',
                4, '118(A) - 108(H)', 13)
    insertGames(connection, 1115, 1, 15, '2023-03-26',
                15, '123(A) - 119(H)', 1)
    insertGames(connection, 1116, 2, 27, '2023-03-26', 2, '137(H) - 93(A)', 2)
    insertGames(connection, 1117, 6, 11, '2023-03-26', 6, '108(H) - 91(A)', 6)
    insertGames(connection, 1118, 22, 3, '2023-03-26',
                22, '119(H) - 106(A)', 22)
    insertGames(connection, 1119, 28, 30, '2023-03-26',
                28, '114(H) - 104(A)', 28)
    insertGames(connection, 1120, 25, 21, '2023-03-26',
                21, '118(A) - 112(H)', 25)
    insertGames(connection, 1121, 10, 18,
                '2023-03-26', 18, '99(A) - 96(H)', 10)
    insertGames(connection, 1122, 9, 17, '2023-03-27',
                17, '126(A) - 117(H)', 9)
    insertGames(connection, 1123, 12, 7, '2023-03-27',
                7, '127(A) - 104(H)', 12)
    insertGames(connection, 1124, 20, 11, '2023-03-27',
                20, '137(H) - 115(A)', 20)
    insertGames(connection, 1125, 29, 24, '2023-03-27',
                24, '117(A) - 103(H)', 29)
    insertGames(connection, 1126, 8, 23, '2023-03-27', 8, '116(H) - 111(A)', 8)
    insertGames(connection, 1127, 25, 19,
                '2023-03-27', 19, '124(A) - 90(H)', 25)
    insertGames(connection, 1128, 26, 18, '2023-03-27',
                18, '119(A) - 115(H)', 26)
    insertGames(connection, 1129, 13, 4, '2023-03-27',
                13, '124(H) - 112(A)', 13)
    insertGames(connection, 1130, 30, 2, '2023-03-28',
                30, '130(H) - 111(A)', 30)
    insertGames(connection, 1131, 1, 6, '2023-03-28', 1, '120(H) - 118(A)', 1)
    insertGames(connection, 1132, 28, 16,
                '2023-03-28', 28, '106(H) - 92(A)', 28)
    insertGames(connection, 1133, 15, 22, '2023-03-28',
                15, '113(H) - 108(A)', 15)
    insertGames(connection, 1134, 21, 5, '2023-03-28',
                5, '137(A) - 134(H)', 21)
    insertGames(connection, 1135, 10, 19, '2023-03-28',
                10, '120(H) - 109(A)', 10)
    insertGames(connection, 1136, 12, 17, '2023-03-29',
                17, '149(A) - 136(H)', 12)
    insertGames(connection, 1137, 3, 11, '2023-03-29', 3, '123(H) - 114(A)', 3)
    insertGames(connection, 1138, 20, 16,
                '2023-03-29', 20, '101(H) - 92(A)', 20)
    insertGames(connection, 1139, 23, 7, '2023-03-29',
                23, '116(H) - 108(A)', 23)
    insertGames(connection, 1140, 4, 14, '2023-03-29',
                14, '121(A) - 110(H)', 4)
    insertGames(connection, 1141, 15, 13, '2023-03-29',
                13, '141(A) - 132(H)', 15)
    insertGames(connection, 1142, 21, 9, '2023-03-29',
                21, '107(H) - 106(A)', 21)
    insertGames(connection, 1143, 27, 29, '2023-03-29',
                29, '128(A) - 117(H)', 27)
    insertGames(connection, 1144, 24, 18, '2023-03-29',
                24, '107(H) - 100(A)', 24)
    insertGames(connection, 1145, 25, 26,
                '2023-03-29', 26, '120(A) - 80(H)', 25)
    insertGames(connection, 1146, 17, 2, '2023-03-30', 2, '140(A) - 99(H)', 17)
    insertGames(connection, 1147, 8, 19, '2023-03-30', 19, '107(A) - 88(H)', 8)
    insertGames(connection, 1148, 5, 4, '2023-03-31', 4, '121(A) - 91(H)', 5)
    insertGames(connection, 1149, 12, 21, '2023-03-31',
                12, '121(H) - 117(A)', 12)
    insertGames(connection, 1150, 23, 28, '2023-03-31',
                23, '117(H) - 110(A)', 23)
    insertGames(connection, 1151, 30, 22, '2023-03-31',
                22, '116(A) - 109(H)', 30)
    insertGames(connection, 1152, 2, 29, '2023-03-31', 2, '122(H) - 114(A)', 2)
    insertGames(connection, 1153, 3, 1, '2023-03-31', 3, '124(H) - 107(A)', 3)
    insertGames(connection, 1154, 6, 20, '2023-03-31',
                20, '130(A) - 116(H)', 6)
    insertGames(connection, 1155, 11, 9, '2023-03-31',
                11, '121(H) - 115(A)', 11)
    insertGames(connection, 1156, 15, 13,
                '2023-03-31', 15, '108(H) - 94(A)', 15)
    insertGames(connection, 1157, 18, 14, '2023-03-31',
                14, '123(A) - 111(H)', 18)
    insertGames(connection, 1158, 10, 27, '2023-03-31',
                10, '130(H) - 115(A)', 10)
    insertGames(connection, 1159, 25, 26, '2023-03-31',
                26, '138(A) - 114(H)', 25)
    insertGames(connection, 1160, 24, 8, '2023-03-31',
                24, '100(H) - 93(A)', 24)
    insertGames(connection, 1161, 16, 7, '2023-04-01',
                16, '129(H) - 122(A)', 16)
    insertGames(connection, 1162, 19, 13, '2023-04-01',
                19, '122(H) - 114(A)', 19)
    insertGames(connection, 1163, 5, 28, '2023-04-02',
                28, '128(A) - 108(H)', 5)
    insertGames(connection, 1164, 3, 29, '2023-04-02', 3, '111(H) - 110(A)', 3)
    insertGames(connection, 1165, 4, 15, '2023-04-02', 4, '128(H) - 107(A)', 4)
    insertGames(connection, 1166, 18, 25, '2023-04-02',
                25, '107(A) - 105(H)', 18)
    insertGames(connection, 1167, 1, 7, '2023-04-02', 1, '132(H) - 130(A)', 1)
    insertGames(connection, 1168, 20, 30, '2023-04-02',
                20, '118(H) - 109(A)', 20)
    insertGames(connection, 1169, 22, 9, '2023-04-02',
                22, '128(H) - 102(A)', 22)
    insertGames(connection, 1170, 26, 27, '2023-04-02',
                27, '142(A) - 134(H)', 26)
    insertGames(connection, 1171, 11, 14, '2023-04-02',
                14, '134(A) - 109(H)', 11)
    insertGames(connection, 1172, 21, 24, '2023-04-02',
                24, '128(A) - 118(H)', 21)
    insertGames(connection, 1173, 6, 12, '2023-04-02', 6, '115(H) - 105(A)', 6)
    insertGames(connection, 1174, 17, 23, '2023-04-02',
                17, '117(H) - 104(A)', 17)
    insertGames(connection, 1175, 8, 10, '2023-04-02', 8, '112(H) - 110(A)', 8)
    insertGames(connection, 1176, 5, 28, '2023-04-04',
                28, '120(A) - 100(H)', 5)
    insertGames(connection, 1177, 9, 16, '2023-04-04',
                16, '118(A) - 105(H)', 9)
    insertGames(connection, 1178, 22, 6, '2023-04-04',
                6, '117(A) - 113(H)', 22)
    insertGames(connection, 1179, 30, 17, '2023-04-04',
                17, '140(A) - 128(H)', 30)
    insertGames(connection, 1180, 3, 18, '2023-04-04',
                18, '107(A) - 102(H)', 3)
    insertGames(connection, 1181, 4, 1, '2023-04-04', 1, '123(A) - 105(H)', 4)
    insertGames(connection, 1182, 11, 8, '2023-04-04',
                11, '124(H) - 103(A)', 11)
    insertGames(connection, 1183, 15, 25, '2023-04-04',
                15, '119(H) - 109(A)', 15)
    insertGames(connection, 1184, 19, 26, '2023-04-04',
                26, '121(A) - 103(H)', 19)
    insertGames(connection, 1185, 23, 2, '2023-04-04',
                23, '103(H) - 101(A)', 23)
    insertGames(connection, 1186, 29, 14, '2023-04-04',
                14, '135(A) - 133(H)', 29)
    insertGames(connection, 1187, 10, 21, '2023-04-04',
                10, '136(H) - 125(A)', 10)
    insertGames(connection, 1188, 24, 27,
                '2023-04-04', 24, '115(H) - 94(A)', 24)
    insertGames(connection, 1189, 9, 3, '2023-04-05', 3, '123(A) - 108(H)', 9)
    insertGames(connection, 1190, 12, 20, '2023-04-05',
                20, '138(A) - 129(H)', 12)
    insertGames(connection, 1191, 1, 30, '2023-04-05', 1, '134(H) - 116(A)', 1)
    insertGames(connection, 1192, 2, 28, '2023-04-05', 2, '97(H) - 93(A)', 2)
    insertGames(connection, 1193, 17, 4, '2023-04-05',
                17, '105(H) - 92(A)', 17)
    insertGames(connection, 1194, 19, 15, '2023-04-05',
                19, '138(H) - 131(A)', 19)
    insertGames(connection, 1195, 7, 26, '2023-04-05', 7, '123(H) - 119(A)', 7)
    insertGames(connection, 1196, 13, 14, '2023-04-05',
                13, '125(H) - 118(A)', 13)
    insertGames(connection, 1197, 22, 6, '2023-04-06', 6, '118(A) - 94(H)', 22)
    insertGames(connection, 1198, 23, 16, '2023-04-06',
                16, '129(A) - 101(H)', 23)
    insertGames(connection, 1199, 27, 25, '2023-04-06',
                27, '129(H) - 127(A)', 27)
    insertGames(connection, 1200, 29, 21,
                '2023-04-06', 21, '114(A) - 98(H)', 29)
    insertGames(connection, 1201, 24, 8, '2023-04-06',
                24, '119(H) - 115(A)', 24)
    insertGames(connection, 1202, 5, 11, '2023-04-07',
                11, '112(A) - 109(H)', 5)
    insertGames(connection, 1203, 12, 9, '2023-04-07',
                9, '122(A) - 115(H)', 12)
    insertGames(connection, 1204, 30, 16, '2023-04-07',
                30, '114(H) - 108(A)', 30)
    insertGames(connection, 1205, 1, 23, '2023-04-07',
                23, '136(A) - 131(H)', 1)
    insertGames(connection, 1206, 2, 28, '2023-04-07', 2, '121(H) - 102(A)', 2)
    insertGames(connection, 1207, 3, 22, '2023-04-07', 3, '101(H) - 84(A)', 3)
    insertGames(connection, 1208, 17, 15, '2023-04-07',
                15, '137(A) - 114(H)', 17)
    insertGames(connection, 1209, 19, 20, '2023-04-07',
                19, '113(H) - 105(A)', 19)
    insertGames(connection, 1210, 7, 4, '2023-04-07', 4, '115(A) - 112(H)', 7)
    insertGames(connection, 1211, 26, 10,
                '2023-04-07', 10, '119(A) - 97(H)', 26)
    insertGames(connection, 1212, 14, 24, '2023-04-07',
                14, '121(H) - 107(A)', 13)
    insertGames(connection, 1213, 29, 8, '2023-04-08',
                29, '118(H) - 114(A)', 29)
    insertGames(connection, 1214, 13, 25, '2023-04-08',
                13, '136(H) - 125(A)', 13)
    insertGames(connection, 1215, 27, 18, '2023-04-08',
                18, '151(A) - 131(H)', 27)
    insertGames(connection, 1216, 2, 1, '2023-04-09', 2, '120(H) - 114(A)', 2)
    insertGames(connection, 1217, 3, 23, '2023-04-09',
                23, '134(A) - 105(H)', 3)
    insertGames(connection, 1218, 4, 9, '2023-04-09', 4, '103(H) - 81(A)', 4)
    insertGames(connection, 1219, 6, 5, '2023-04-09', 5, '106(A) - 95(H)', 6)
    insertGames(connection, 1220, 16, 22, '2023-04-09',
                16, '123(H) - 110(A)', 16)
    insertGames(connection, 1221, 20, 12, '2023-04-09',
                12, '141(A) - 136(H)', 20)
    insertGames(connection, 1222, 28, 17, '2023-04-09',
                28, '121(H) - 105(A)', 28)
    insertGames(connection, 1223, 30, 11, '2023-04-09',
                11, '114(A) - 109(H)', 30)
    insertGames(connection, 1224, 7, 27, '2023-04-09',
                27, '138(A) - 117(H)', 7)
    insertGames(connection, 1225, 8, 26, '2023-04-09', 8, '109(H) - 95(A)', 8)
    insertGames(connection, 1226, 14, 29, '2023-04-09',
                14, '128(H) - 117(A)', 13)
    insertGames(connection, 1227, 18, 19, '2023-04-09',
                18, '113(H) - 108(A)', 18)
    insertGames(connection, 1228, 21, 15, '2023-04-09',
                21, '115(H) - 100(A)', 21)
    insertGames(connection, 1229, 24, 13, '2023-04-09',
                13, '119(A) - 114(H)', 24)
    insertGames(connection, 1230, 25, 10, '2023-04-09',
                10, '157(A) - 101(H)', 25)
    insertGames(connection, 1231, 16, 1, '2023-04-11',
                1, '116(A) - 105(H)', 16)
    insertGames(connection, 1232, 14, 18, '2023-04-11',
                14, '108(H) - 102(A)', 13)
    insertGames(connection, 1233, 28, 4, '2023-04-12',
                4, '109(A) - 105(H)', 28)
    insertGames(connection, 1234, 19, 21, '2023-04-12',
                21, '123(A) - 118(H)', 19)
    insertGames(connection, 1235, 16, 4, '2023-04-14',
                16, '102(H) - 91(A)', 16)
    insertGames(connection, 1236, 18, 21,
                '2023-04-14', 18, '120(H) - 95(A)', 18)
    insertGames(connection, 1237, 23, 3, '2023-04-15',
                23, '121(H) - 101(A)', 23)
    insertGames(connection, 1238, 2, 1, '2023-04-15', 2, '112(H) - 99(A)', 2)
    insertGames(connection, 1239, 6, 20, '2023-04-15', 20, '101(A) - 97(H)', 6)
    insertGames(connection, 1240, 26, 10, '2023-04-15',
                26, '126(H) - 123(A)', 26)
    insertGames(connection, 1241, 15, 14, '2023-04-16',
                14, '128(A) - 112(H)', 15)
    insertGames(connection, 1242, 17, 16, '2023-04-16',
                16, '130(A) - 117(H)', 17)
    insertGames(connection, 1243, 24, 13, '2023-04-16',
                13, '115(A) - 110(H)', 24)
    insertGames(connection, 1244, 8, 18, '2023-04-16', 8, '109(H) - 80(A)', 8)
    insertGames(connection, 1245, 23, 3, '2023-04-17', 23, '96(H) - 84(A)', 23)
    insertGames(connection, 1246, 26, 10, '2023-04-17',
                26, '114(H) - 106(A)', 26)
    insertGames(connection, 1247, 2, 1, '2023-04-18', 2, '119(H) - 106(A)', 2)
    insertGames(connection, 1248, 6, 20, '2023-04-18', 6, '107(H) - 90(A)', 6)
    insertGames(connection, 1249, 24, 13, '2023-04-18',
                24, '123(H) - 109(A)', 24)
    insertGames(connection, 1250, 15, 14,
                '2023-04-19', 15, '103(H) - 93(A)', 15)
    insertGames(connection, 1251, 17, 16, '2023-04-19',
                17, '138(H) - 122(A)', 17)
    insertGames(connection, 1252, 8, 18, '2023-04-19', 8, '122(H) - 113(A)', 8)
    insertGames(connection, 1253, 3, 23, '2023-04-20', 23, '102(A) - 97(H)', 3)
    insertGames(connection, 1254, 10, 26,
                '2023-04-20', 10, '114(H) - 97(A)', 10)
    insertGames(connection, 1255, 13, 24, '2023-04-20',
                24, '129(A) - 124(H)', 13)
    insertGames(connection, 1256, 1, 2, '2023-04-21', 1, '130(H) - 122(A)', 1)
    insertGames(connection, 1257, 20, 6, '2023-04-21', 20, '99(H) - 79(A)', 20)
    insertGames(connection, 1258, 18, 8, '2023-04-21',
                8, '120(A) - 111(H)', 18)
    insertGames(connection, 1259, 3, 23, '2023-04-22', 23, '96(A) - 88(H)', 3)
    insertGames(connection, 1260, 13, 24, '2023-04-22',
                24, '112(A) - 100(H)', 13)
    insertGames(connection, 1261, 16, 17,
                '2023-04-22', 16, '121(H) - 99(A)', 16)
    insertGames(connection, 1262, 14, 15, '2023-04-22',
                14, '111(H) - 101(A)', 13)
    insertGames(connection, 1263, 20, 6, '2023-04-23',
                20, '102(H) - 93(A)', 20)
    insertGames(connection, 1264, 10, 26, '2023-04-23',
                10, '126(H) - 125(A)', 10)
    insertGames(connection, 1265, 1, 2, '2023-04-23', 2, '129(A) - 121(H)', 1)
    insertGames(connection, 1266, 18, 8, '2023-04-23',
                18, '114(H) - 108(A)', 18)
    insertGames(connection, 1267, 16, 17, '2023-04-24',
                16, '119(H) - 114(A)', 16)
    insertGames(connection, 1268, 14, 15, '2023-04-24',
                14, '117(H) - 111(A)', 13)
    insertGames(connection, 1269, 2, 1, '2023-04-25', 1, '119(A) - 117(H)', 2)
    insertGames(connection, 1270, 8, 18, '2023-04-25', 8, '112(H) - 109(A)', 8)
    insertGames(connection, 1271, 24, 13, '2023-04-25',
                24, '136(H) - 130(A)', 24)
    insertGames(connection, 1272, 6, 20, '2023-04-26', 20, '106(A) - 95(H)', 6)
    insertGames(connection, 1273, 15, 14,
                '2023-04-26', 15, '116(H) - 99(A)', 15)
    insertGames(connection, 1274, 17, 16, '2023-04-26',
                16, '128(A) - 126(H)', 17)
    insertGames(connection, 1275, 26, 10, '2023-04-26',
                10, '123(A) - 116(H)', 26)
    insertGames(connection, 1276, 1, 2, '2023-04-27', 2, '128(A) - 120(H)', 1)
    insertGames(connection, 1277, 10, 26,
                '2023-04-28', 26, '118(A) - 99(H)', 10)
    insertGames(connection, 1278, 14, 15,
                '2023-04-28', 14, '125(H) - 85(A)', 13)
    insertGames(connection, 1279, 8, 24, '2023-04-29', 8, '125(H) - 107(A)', 8)
    insertGames(connection, 1280, 20, 16, '2023-04-30',
                16, '108(A) - 101(H)', 20)
    insertGames(connection, 1281, 26, 10, '2023-04-30',
                10, '120(A) - 100(H)', 26)
    insertGames(connection, 1282, 2, 23, '2023-05-01',
                23, '119(A) - 115(H)', 2)
    insertGames(connection, 1283, 8, 24, '2023-05-01', 8, '97(H) - 87(A)', 8)
    insertGames(connection, 1284, 20, 16, '2023-05-02',
                20, '111(H) - 105(A)', 20)
    insertGames(connection, 1285, 10, 14, '2023-05-02',
                14, '117(A) - 112(H)', 10)
    insertGames(connection, 1286, 2, 23, '2023-05-03', 2, '121(H) - 87(A)', 2)
    insertGames(connection, 1287, 10, 14, '2023-05-04',
                10, '127(H) - 100(A)', 10)
    insertGames(connection, 1288, 23, 2, '2023-05-05',
                2, '114(A) - 102(H)', 23)
    insertGames(connection, 1289, 24, 8, '2023-05-05',
                24, '121(H) - 114(A)', 24)
    insertGames(connection, 1290, 16, 20,
                '2023-05-06', 16, '105(H) - 86(A)', 16)
    insertGames(connection, 1291, 14, 10,
                '2023-05-06', 14, '127(H) - 97(A)', 13)
    insertGames(connection, 1292, 23, 2, '2023-05-07',
                23, '116(H) - 115(A)', 23)
    insertGames(connection, 1293, 24, 8, '2023-05-07',
                24, '129(H) - 124(A)', 24)
    insertGames(connection, 1294, 16, 20, '2023-05-08',
                16, '109(H) - 101(A)', 16)
    insertGames(connection, 1295, 14, 10, '2023-05-08',
                14, '104(H) - 101(A)', 13)
    insertGames(connection, 1296, 2, 23, '2023-05-09',
                23, '115(A) - 103(H)', 2)
    insertGames(connection, 1297, 8, 24, '2023-05-09', 8, '118(H) - 102(A)', 8)
    insertGames(connection, 1298, 20, 16, '2023-05-10',
                20, '112(H) - 103(A)', 20)
    insertGames(connection, 1299, 10, 14, '2023-05-10',
                10, '121(H) - 106(A)', 10)
    insertGames(connection, 1300, 23, 2, '2023-05-11', 2, '95(A) - 86(H)', 23)
    insertGames(connection, 1301, 24, 8, '2023-05-11',
                8, '125(A) - 100(H)', 24)
    insertGames(connection, 1302, 16, 20,
                '2023-05-12', 16, '96(H) - 92(A)', 16)
    insertGames(connection, 1303, 14, 10, '2023-05-12',
                14, '122(H) - 101(A)', 13)
    insertGames(connection, 1304, 2, 23, '2023-05-14', 2, '112(H) - 88(A)', 2)
    insertGames(connection, 1305, 8, 14, '2023-05-16', 8, '132(H) - 126(A)', 8)
    insertGames(connection, 1306, 2, 16, '2023-05-17',
                16, '123(A) - 116(H)', 2)
    insertGames(connection, 1307, 8, 14, '2023-05-18', 8, '108(H) - 103(A)', 8)
    insertGames(connection, 1308, 2, 16, '2023-05-19',
                16, '111(A) - 105(H)', 2)
    insertGames(connection, 1309, 14, 8, '2023-05-20',
                8, '119(A) - 108(H)', 13)
    insertGames(connection, 1310, 16, 2, '2023-05-21',
                16, '128(H) - 102(A)', 16)
    insertGames(connection, 1311, 14, 8, '2023-05-22',
                8, '113(A) - 111(H)', 13)
    insertGames(connection, 1312, 16, 2, '2023-05-23', 2, '116(A) - 99(H)', 16)
    insertGames(connection, 1313, 2, 16, '2023-05-25', 2, '110(H) - 97(A)', 2)
    insertGames(connection, 1314, 16, 2, '2023-05-27',
                2, '104(A) - 103(H)', 16)
    insertGames(connection, 1315, 2, 16, '2023-05-29', 16, '103(A) - 84(H)', 2)
    insertGames(connection, 1316, 8, 16, '2023-06-01', 8, '104(H) - 93(A)', 8)
    insertGames(connection, 1317, 8, 16, '2023-06-04',
                16, '111(A) - 108(H)', 8)
    insertGames(connection, 1318, 16, 8, '2023-06-07', 8, '109(A) - 94(H)', 16)
    insertGames(connection, 1319, 16, 8, '2023-06-09', 8, '108(A) - 95(H)', 16)
    insertGames(connection, 1320, 8, 16, '2023-06-12', 8, '94(H) - 89(A)', 8)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Coaches(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Coaches")

    insertCoaches(connection, 1, 'Quin Snyder', 1992, 0)
    insertCoaches(connection, 2, 'Joe Mazzulla', 2019, 0)
    insertCoaches(connection, 3, 'Jacque Vaughn', 2010, 0)
    insertCoaches(connection, 4, 'Billy Donovan', 2015, 0)
    insertCoaches(connection, 5, 'Steve Clifford', 2000, 0)
    insertCoaches(connection, 6, 'J.B. Bickerstaff', 2004, 0)
    insertCoaches(connection, 7, 'Jason Kidd', 2013, 0)
    insertCoaches(connection, 8, 'Michael Malone', 2003, 1)
    insertCoaches(connection, 9, 'Dwane Casey', 1994, 0)
    insertCoaches(connection, 10, 'Steve Kerr', 2014, 4)
    insertCoaches(connection, 11, 'Stephen Silas', 2000, 0)
    insertCoaches(connection, 12, 'Rick Carlisle', 1989, 1)
    insertCoaches(connection, 13, 'Tyronn Lue', 2011, 1)
    insertCoaches(connection, 14, 'Darvin Ham', 2011, 0)
    insertCoaches(connection, 15, 'Taylor Jenkins', 2013, 0)
    insertCoaches(connection, 16, 'Erik Spoelstra', 1997, 2)
    insertCoaches(connection, 17, 'Mike Budenholzer', 1996, 1)
    insertCoaches(connection, 18, 'Chris Finch', 2011, 0)
    insertCoaches(connection, 19, 'Willie Green', 2018, 9)
    insertCoaches(connection, 20, 'Tom Thibodeau', 1989, 0)
    insertCoaches(connection, 21, 'Mark Daigneault', 2019, 0)
    insertCoaches(connection, 22, 'Jamahl Mosley', 2006, 0)
    insertCoaches(connection, 23, 'Doc Rivers', 1999, 1)
    insertCoaches(connection, 24, 'Monty Williams', 2005, 0)
    insertCoaches(connection, 25, 'Chauncey Billups', 2020, 0)
    insertCoaches(connection, 26, 'Mike Brown', 1997, 0)
    insertCoaches(connection, 27, 'Gregg Popovich', 1988, 5)
    insertCoaches(connection, 28, 'Nick Nurse', 2013, 1)
    insertCoaches(connection, 29, 'Will Hardy', 2016, 0)
    insertCoaches(connection, 30, 'Wes Unseld', 2005, 0)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_News(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate News")

    insertNews(connection, 1, 'Signing', '2022-06-12',
               'Jalen Brunson signed a 4-year deal worth $104 million with the New York Knicks')
    insertNews(connection, 2, 'Trade', '2022-07-06',
               'The�Minnesota Timberwolves�traded�Malik Beasley,�Patrick Beverley,�Leandro Bolmaro,�Walker Kessler,�Jarred Vanderbilt, and five 1st round draft picks to the�Utah Jazz�for�Rudy Gobert.')
    insertNews(connection, 3, 'Trade', '2022-07-06',
               'The�Detroit Pistons�traded�Jerami Grant�and�Ismael Kamagate�to the�Portland Trail Blazers�for�Gabriele Procida, a 1st round draft pick, and two 2nd round draft picks.')
    insertNews(connection, 4, 'Trade', '2022-07-06',
               'The�Denver Nuggets�traded�Will Barton�and�Monte Morris�to the�Washington Wizards�for�Kentavious Caldwell-Pope�and�Ish Smith.')
    insertNews(connection, 5, 'Trade', '2022-07-06',
               'The�Atlanta Hawks�traded�Kevin Huerter�to the�Sacramento Kings�for�Maurice Harkless,�Justin Holiday�and a 2024 1st round draft pick')
    insertNews(connection, 6, 'Trade', '2022-07-06',
               'The�Detroit Pistons�traded a 1st round draft pick to the�New York Knicks�for�Jalen Duren�and�Kemba Walker')
    insertNews(connection, 7, 'Extension', '2022-07-06',
               'Bradley Beal signed a 5-year extension worth $251 million with the Washington Wizards')
    insertNews(connection, 8, 'Extension', '2022-07-06',
               'Anfernee Simons signed a 4-year extension worth $100 million with the Portland Trailblazers')
    insertNews(connection, 9, 'Signing', '2022-07-06',
               'Gary Payton ll signed a 3-year deal worth $28 million with the Portland Trailblazers')
    insertNews(connection, 10, 'Extension', '2022-07-06',
               'Jusuf Nurkic signed a 4-year extension worth $70 million with the Portland Trailblazers')
    insertNews(connection, 11, 'Extension', '2022-07-06',
               'Zion Williamson signed a 4-year extension worth $194 million with the New Orleans Pelicans')
    insertNews(connection, 12, 'Extension', '2022-07-06',
               'Devin Booker signed a 4-year extension worth $272 million with the Phoenix Suns')
    insertNews(connection, 13, 'Signing', '2022-07-06',
               'Tyus Jones signed a 2-year deal worth $30 million with the Memphis Grizzlies')
    insertNews(connection, 14, 'Signing', '2022-07-06',
               'P.J. Tucker signed a 3-year deal worth $33.2 million with the Philadelphia 76ers')
    insertNews(connection, 15, 'Signing', '2022-07-06',
               'Malik Monk signed a 2-year deal worth $19 million with the Sacramento Kings')
    insertNews(connection, 16, 'Signing', '2022-07-06',
               'Kevon Looney signed a 3-year deal worth $25.5 million with the Golden State Warriors')
    insertNews(connection, 17, 'Extension', '2022-07-07',
               'Zach LaVine signed a 5-year extension worth $215.2 million with the Chicago Bulls')
    insertNews(connection, 18, 'Signing', '2022-07-07',
               'Bruce Brown signed a 2-year deal worth $13 million with the Denver Nuggets')
    insertNews(connection, 19, 'Extension', '2022-07-07',
               'Karl-Anthony Towns signed a 4-year extension worth $224 million with the Minnesota Timberwolves')
    insertNews(connection, 20, 'Extension', '2022-07-08',
               'Nikola Jokic signed a 5-year extension worth $272 million with the Denver Nuggets ')
    insertNews(connection, 21, 'Trade', '2022-07-09',
               'The�Boston Celtics�traded�Malik Fitts,�Juwan Morgan,�Aaron Nesmith,�Nik Stauskas,�Daniel Theis, and a 1st round draft pick to the�Indiana Pacers�for�Malcolm Brogdon.')
    insertNews(connection, 22, 'Extension', '2022-07-09',
               'Damian Lillard signed a 2-year extension worth $106 million with the Portland Trailblazers')
    insertNews(connection, 23, 'Signing', '2022-07-15',
               'Deandre Ayton signed a 4-year deal worth $133 million with the Phoenix Suns')
    insertNews(connection, 24, 'Extension', '2022-07-27',
               'James Harden signed a 2-year extension worth $68.6 million with the Philadelphia 76ers')
    insertNews(connection, 25, 'Trade', '2022-09-03',
               'The�Cleveland Cavaliers�traded�Ochai Agbaji,�Lauri Markkanen,�Collin Sexton, and five 1st round draft picks to the�Utah Jazz�for�Donovan Mitchell.')
    insertNews(connection, 26, 'Trade', '2022-09-22',
               'The�Detroit Pistons�traded�Saben Lee�and�Kelly Olynyk�to the�Utah Jazz�for�Bojan Bogdanovic.')
    insertNews(connection, 27, 'Suspension', '2022-10-23',
               'Caleb Martin and Nikola Jovic were suspended for 1 game')
    insertNews(connection, 28, 'Extension', '2022-10-30',
               'Bojan Bogdanovic signed a 2-year extension worth $39 million with the Detroit Pistons')
    insertNews(connection, 29, 'Trade', '2023-01-23',
               'The�Los Angeles Lakers�traded�Kendrick Nunn, and three 2nd round draft picks to the�Washington Wizards�for�Rui Hachimura.')
    insertNews(connection, 30, 'Extension', '2023-01-30',
               'Myles Turner signed a 2-year extension worth $40 million with the Indiana Pacers')
    insertNews(connection, 31, 'Trade', '2023-02-06',
               'The�Brooklyn Nets�traded�Kyrie Irving�and�Markieff Morris�to the�Dallas Mavericks�for�Spencer Dinwiddie,�Dorian Finney-Smith, two 2nd round draft picks, and a 1st round draft pick ')
    insertNews(connection, 32, 'Trade', '2023-02-09',
               'The Charlotte Hornets traded Mason Plumlee to the Los Angeles Clippers for Reggie Jackson and a 2nd round draft pick')
    insertNews(connection, 33, 'Trade', '2023-02-09', 'Charlotte Hornets traded Jalen McDaniels and a 2nd round draft pick to the Philadelphia 76ers; the New York Knicks traded Sviatoslav Mykhailiuk to the Charlotte Hornets; the New York Knicks traded Ryan Arcidiacono, Cam Reddish, Ante Tomic, and a 1st round draft pick to the Portland Trail Blazers; the Philadelphia 76ers traded a 2023 2nd round draft pick to the Charlotte Hornets; the Philadelphia 76ers traded Matisse Thybulle to the Portland Trail Blazers; the Portland Trail Blazers traded a 2nd round draft pick to the Charlotte Hornets; the Portland Trail Blazers traded Dani Diez, Bojan Dubljevic and Josh Hart to the New York Knicks; and the Portland Trail Blazers traded a 2nd round draft pick to the Philadelphia 76ers. ')
    insertNews(connection, 34, 'Trade', '2023-02-09', 'The�Houston Rockets�traded�Eric Gordon�and a 1st round draft pick to the�Los Angeles Clippers; the�Los Angeles Clippers�traded�John Wall�and a 2023 1st round draft pick to the�Houston Rockets; the�Los Angeles Clippers�traded�Luke Kennard�and a 2nd round draft pick to the�Memphis Grizzlies; the�Memphis Grizzlies�traded�Danny Green�to the�Houston Rockets; and the�Memphis Grizzlies�traded a three 2nd round draft pick to the�Los Angeles Clippers.')
    insertNews(connection, 35, 'Trade', '2023-02-09',
               'The�Boston Celtics�traded�Justin Jackson, and two 2nd round draft picks to the�Oklahoma City Thunder�for�Mike Muscala.')
    insertNews(connection, 36, 'Trade', '2023-02-09',
               'The�New Orleans Pelicans�traded�Devonte Graham, and four 2nd round draft picks to the�San Antonio Spurs�for�Josh Richardson.')
    insertNews(connection, 37, 'Trade', '2023-02-09', 'In a 4-team trade, the�Atlanta Hawks�traded two 2nd round draft picks to the�Golden State Warriors; the�Atlanta Hawks�traded a three 2nd round draft picks to the�Portland Trail Blazers; the�Detroit Pistons�traded�Saddiq Bey�to the�Atlanta Hawks; the�Detroit Pistons�traded�Kevin Knox�to the�Portland Trail Blazers; the�Golden State Warriors�traded�James Wiseman�to the�Detroit Pistons; the�Golden State Warriors�traded two 2nd round draft picks to the�Portland Trail Blazers; and the�Portland Trail Blazers�traded�Gary Payton II�to the�Golden State Warriors.')
    insertNews(connection, 38, 'Trade', '2023-02-09', 'In a 4-team trade, the Brooklyn Nets traded Kevin Durant and T.J. Warren to the Phoenix Suns; the Indiana Pacers traded Juan Vaulet to the Brooklyn Nets; the Milwaukee Bucks traded two 2nd round draft picks to the Brooklyn Nets; the Milwaukee Bucks traded George Hill, Serge Ibaka, Jordan Nwora, and three 2nd round draft picks to the Indiana Pacers; the Phoenix Suns traded Mikal Bridges, Cameron Johnson, and five 1st round draft picks to the Brooklyn Nets; and the Phoenix Suns traded Jae Crowder to the Milwaukee Bucks.')
    insertNews(connection, 39, 'Trade', '2023-02-09', 'In a 4-team trade, the�Denver Nuggets�traded�Bones Hyland�to the�Los Angeles Clippers; the�Denver Nuggets�traded�Davon Reed�to the�Los Angeles Lakers; the�Denver Nuggets�traded a 2nd round draft pick to the�Orlando Magic; the�Los Angeles Clippers�traded two 2nd round draft picks to the�Los Angeles Lakers; the�Los Angeles Lakers�traded�Thomas Bryant�to the�Denver Nuggets; the�Los Angeles Lakers�traded Patrick Beverley�to the�Orlando Magic; and the�Orlando Magic�traded�Mo Bamba�to the�Los Angeles Lakers.')
    insertNews(connection, 40, 'Trade', '2023-02-09', 'In a 3-team trade, the�Los Angeles Lakers�traded a 2nd round draft pick to the�Minnesota Timberwolves; the�Los Angeles Lakers�traded�Damian Jones,�Juan Toscano-Anderson,�Russell Westbrook, and a 1st round draft pick to the�Utah Jazz; the�Minnesota Timberwolves�traded�D''Angelo Russell�to the�Los Angeles Lakers; the�Utah Jazz�traded�Malik Beasley�and�Jarred Vanderbilt�to the�Los Angeles Lakers; and the�Utah Jazz�traded�Nickeil Alexander-Walker,�Mike Conley, and two 2nd round draft picks to the�Minnesota Timberwolves.')
    insertNews(connection, 41, 'Trade', '2023-02-09',
               'The San Antonio Spurs traded Jakob Poeltl to the Toronto Raptors for Khem Birch, two  2nd round draft picks, and a 1st round draft pick.')
    insertNews(connection, 42, 'Signing', '2023-02-14',
               'The Denver Nuggets signed Reggie Jackson.')
    insertNews(connection, 43, 'Signing', '2023-02-14',
               'The Phoenix Suns signed Terrence Ross.')
    insertNews(connection, 44, 'Signing', '2023-02-20',
               'The Miami Heat signed Kevin Love and Cody Zeller')
    insertNews(connection, 45, 'Firing', '2023-02-21',
               'The Atlanta Hawks fired Nate McMillan as Head Coach')
    insertNews(connection, 46, 'Signing', '2023-02-22',
               'The Los Angeles Clippers signed Russell Westbrook.')
    insertNews(connection, 47, 'Hiring', '2023-02-26',
               'The Atlanta Hawks hired Quin Snyder.')
    insertNews(connection, 48, 'Suspension', '2023-03-15',
               'Trey Lyles was suspended for 1 game')
    insertNews(connection, 49, 'Suspension', '2023-03-15',
               'Ja Morant was suspended for 8 games')
    insertNews(connection, 50, 'Suspension', '2023-03-16',
               'Draymond Green was suspended for 1 game')
    insertNews(connection, 51, 'Suspension', '2023-03-21',
               'Dillon Brooks was suspended for 1 game')
    insertNews(connection, 52, 'Suspension', '2023-04-24',
               'Dejounte Murray was suspended for 1 game')

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Player(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Player")

    insertPlayer(connection, 1, 'Dejounte Murray', 'ATL-Hawks', 1, 2,
                 6.04, 180, 20.5, 5.3, 6.1, 1.5, 0.3, 0.464, 0.344, 2017, 16571120)
    insertPlayer(connection, 2, 'Trae Young', 'ATL-Hawks', 1, 1, 6.01,
                 164, 26.2, 3.0, 10.2, 1.1, 0.1, 0.429, 0.335, 2018, 37096500)
    insertPlayer(connection, 3, 'De''Andre Hunter', 'ATL-Hawks', 1, 3,
                 6.08, 225, 15.4, 4.2, 1.4, 0.5, 0.3, 0.461, 0.35, 2019, 9835881)
    insertPlayer(connection, 4, 'John Collins', 'ATL-Hawks', 1, 4, 6.09,
                 235, 13.1, 6.5, 1.2, 0.6, 1.0, 0.508, 0.292, 2017, 23500000)
    insertPlayer(connection, 5, 'Bogdan Bogdanovic', 'ATL-Hawks', 1, 2,
                 6.06, 220, 14.0, 3.1, 2.8, 0.8, 0.3, 0.447, 0.406, 2017, 18000000)
    insertPlayer(connection, 6, 'Clint Capela', 'ATL-Hawks', 1, 5,
                 6.1, 240, 12.0, 11.0, 0.9, 0.7, 1.2, 0.653, 0.0, 2014, 18706897)
    insertPlayer(connection, 7, 'Saddiq Bey', 'ATL-Hawks', 1, 3,
                 6.07, 215, 11.6, 4.8, 1.4, 0.8, 0.0, 0.47, 0.4, 2020, 2959080)
    insertPlayer(connection, 8, 'Onyeka Okongwu', 'ATL-Hawks', 1, 5,
                 6.08, 235, 9.9, 7.2, 1.0, 0.7, 1.3, 0.638, 0.308, 2020, 6395160)
    insertPlayer(connection, 9, 'AJ Griffin', 'ATL-Hawks', 1, 3,
                 6.06, 222, 8.9, 2.1, 1.0, 0.6, 0.2, 0.465, 0.39, 2022, 3536160)
    insertPlayer(connection, 10, 'Jalen Johnson', 'ATL-Hawks', 1, 3,
                 6.09, 220, 5.6, 4.0, 1.2, 0.5, 0.5, 0.491, 0.288, 2021, 2792640)
    insertPlayer(connection, 11, 'Jayson Tatum', 'BOS-Celtics', 2, 3,
                 6.08, 210, 30.1, 8.8, 4.6, 1.1, 0.7, 0.466, 0.35, 2017, 30351780)
    insertPlayer(connection, 12, 'Jaylen Brown', 'BOS-Celtics', 2, 2,
                 6.06, 223, 26.6, 6.9, 3.5, 1.1, 0.4, 0.491, 0.335, 2016, 28741071)
    insertPlayer(connection, 13, 'Marcus Smart', 'BOS-Celtics', 2, 1,
                 6.03, 220, 11.5, 3.1, 6.3, 1.5, 0.4, 0.415, 0.336, 2014, 17457142)
    insertPlayer(connection, 14, 'Al Horford', 'BOS-Celtics', 2, 4,
                 6.09, 240, 9.8, 6.2, 3.0, 0.5, 1.0, 0.476, 0.446, 2007, 26500000)
    insertPlayer(connection, 15, 'Derrick White', 'BOS-Celtics', 2, 2,
                 6.04, 190, 12.4, 3.6, 3.9, 0.7, 0.9, 0.462, 0.381, 2017, 16892857)
    insertPlayer(connection, 16, 'Malcolm Brogdon', 'BOS-Celtics', 2, 1,
                 6.05, 229, 14.9, 4.2, 3.7, 0.7, 0.3, 0.484, 0.444, 2016, 22600000)
    insertPlayer(connection, 17, 'Grant Williams', 'BOS-Celtics', 2, 4,
                 6.06, 236, 8.1, 4.6, 1.7, 0.5, 0.4, 0.454, 0.395, 2019, 4306281)
    insertPlayer(connection, 18, 'Robert Williams', 'BOS-Celtics', 2,
                 5, 6.09, 237, 8.0, 8.3, 1.4, 0.6, 1.4, 0.747, 0.0, 2018, 10937502)
    insertPlayer(connection, 19, 'Mike Muscala', 'BOS-Celtics', 2, 5,
                 6.1, 240, 5.9, 3.4, 0.6, 0.2, 0.3, 0.472, 0.385, 2013, 3500000)
    insertPlayer(connection, 20, 'Sam Hauser', 'BOS-Celtics', 2, 3,
                 6.08, 215, 6.4, 2.6, 0.9, 0.4, 0.3, 0.455, 0.418, 2021, 1637966)
    insertPlayer(connection, 21, 'Royce O''Neale', 'BKN-Nets', 3, 3,
                 6.04, 226, 8.8, 5.1, 3.7, 0.9, 0.6, 0.386, 0.389, 2017, 9200000)
    insertPlayer(connection, 22, 'Nic Claxton', 'BKN-Nets', 3, 5,
                 6.11, 215, 12.6, 9.2, 1.9, 0.9, 2.5, 0.705, 0.0, 2019, 8500000)
    insertPlayer(connection, 23, 'Joe Harris', 'BKN-Nets', 3, 3, 6.06,
                 220, 7.6, 2.2, 1.4, 0.5, 0.2, 0.457, 0.426, 2014, 18642857)
    insertPlayer(connection, 24, 'Seth Curry', 'BKN-Nets', 3, 2, 6.02,
                 185, 9.2, 1.6, 1.6, 0.6, 0.1, 0.463, 0.405, 2014, 8496653)
    insertPlayer(connection, 25, 'Cam Thomas', 'BKN-Nets', 3, 2, 6.04,
                 210, 10.6, 1.7, 1.4, 0.4, 0.1, 0.441, 0.383, 2021, 2138160)
    insertPlayer(connection, 26, 'Ben Simmons', 'BKN-Nets', 3, 1,
                 6.1, 240, 6.9, 6.3, 6.1, 1.3, 0.6, 0.566, 0.0, 2018, 35448672)
    insertPlayer(connection, 27, 'Mikal Bridges', 'BKN-Nets', 3, 2,
                 6.06, 209, 26.1, 4.5, 2.7, 1.0, 0.6, 0.475, 0.376, 2018, 20100000)
    insertPlayer(connection, 28, 'Spencer Dinwiddie', 'BKN-Nets', 3, 1,
                 6.05, 215, 16.5, 4.1, 9.1, 1.1, 0.3, 0.404, 0.289, 2014, 19500000)
    insertPlayer(connection, 29, 'Dorian Finney-Smith', 'BKN-Nets', 3, 4,
                 6.07, 220, 7.2, 4.9, 1.6, 0.7, 0.6, 0.351, 0.306, 2016, 12939848)
    insertPlayer(connection, 30, 'Cameron Johnson', 'BKN-Nets', 3, 4,
                 6.08, 210, 16.6, 4.8, 2.1, 1.4, 0.3, 0.468, 0.372, 2019, 5887899)
    insertPlayer(connection, 31, 'Terry Rozier', 'CHA-Hornets', 4, 2,
                 6.01, 190, 21.1, 4.1, 5.1, 1.2, 0.3, 0.415, 0.327, 2015, 21486316)
    insertPlayer(connection, 32, 'LaMelo Ball', 'CHA-Hornets', 4, 1,
                 6.07, 180, 23.3, 6.4, 8.4, 1.3, 0.3, 0.411, 0.376, 2020, 8623920)
    insertPlayer(connection, 33, 'P.J. Washington', 'CHA-Hornets', 4, 4,
                 6.07, 230, 15.7, 4.9, 2.4, 0.9, 1.1, 0.444, 0.348, 2019, 5808435)
    insertPlayer(connection, 34, 'Kelly Oubre Jr.', 'CHA-Hornets', 4, 3,
                 6.07, 203, 20.3, 5.2, 1.1, 1.4, 0.4, 0.431, 0.319, 2015, 12600000)
    insertPlayer(connection, 35, 'Gordon Hayward', 'CHA-Hornets', 4, 3,
                 6.07, 225, 14.7, 4.3, 4.1, 0.8, 0.2, 0.475, 0.325, 2010, 30075000)
    insertPlayer(connection, 36, 'Dennis Smith Jr.', 'CHA-Hornets', 4,
                 1, 6.02, 205, 8.8, 3.1, 4.8, 1.4, 0.5, 0.412, 0.216, 2017, 1836090)
    insertPlayer(connection, 37, 'Mark Williams', 'CHA-Hornets', 4, 5,
                 7.01, 241, 9.0, 7.1, 0.4, 0.7, 1.0, 0.637, 0.0, 2022, 3722000)
    insertPlayer(connection, 38, 'Cody Martin', 'CHA-Hornets', 4, 3,
                 6.05, 205, 5.0, 3.4, 1.6, 0.6, 0.1, 0.389, 0.214, 2019, 7000000)
    insertPlayer(connection, 39, 'Nick Richards', 'CHA-Hornets', 4,
                 5, 7.0, 245, 8.2, 6.4, 0.6, 0.2, 1.1, 0.629, 1.0, 2020, 1782621)
    insertPlayer(connection, 40, 'JT Thor', 'CHA-Hornets', 4, 4, 6.1,
                 205, 3.8, 2.2, 0.5, 0.3, 0.3, 0.399, 0.317, 2021, 1563518)
    insertPlayer(connection, 41, 'DeMar DeRozan', 'CHI-Bulls', 5, 3,
                 6.06, 220, 24.5, 4.6, 5.1, 1.1, 0.5, 0.504, 0.324, 2009, 27300000)
    insertPlayer(connection, 42, 'Zach LaVine', 'CHI-Bulls', 5, 2, 6.05,
                 200, 24.8, 4.5, 4.2, 0.9, 0.2, 0.485, 0.375, 2014, 37096500)
    insertPlayer(connection, 43, 'Nikola Vucevic', 'CHI-Bulls', 5, 5,
                 6.1, 260, 17.6, 11.0, 3.2, 0.7, 0.7, 0.52, 0.349, 2011, 22000000)
    insertPlayer(connection, 44, 'Patrick Williams', 'CHI-Bulls', 5, 4,
                 6.07, 215, 10.2, 4.0, 1.2, 0.9, 0.9, 0.464, 0.415, 2020, 7775400)
    insertPlayer(connection, 45, 'Ayo Dosunmu', 'CHI-Bulls', 5, 2,
                 6.05, 200, 8.6, 2.8, 2.6, 0.8, 0.3, 0.493, 0.312, 2021, 1563518)
    insertPlayer(connection, 46, 'Alex Caruso', 'CHI-Bulls', 5, 1,
                 6.04, 186, 5.6, 2.9, 2.9, 1.5, 0.7, 0.455, 0.364, 2017, 9030000)
    insertPlayer(connection, 47, 'Coby White', 'CHI-Bulls', 5, 2,
                 6.05, 195, 9.7, 2.9, 2.8, 0.7, 0.1, 0.443, 0.372, 2019, 7413955)
    insertPlayer(connection, 48, 'Goran Dragic', 'CHI-Bulls', 5, 1,
                 6.03, 190, 6.4, 1.4, 2.7, 0.2, 0.1, 0.425, 0.352, 2008, 1836090)
    insertPlayer(connection, 49, 'Javonte Green', 'CHI-Bulls', 5, 3,
                 6.04, 205, 5.2, 2.8, 0.7, 0.8, 0.7, 0.565, 0.371, 2019, 1815677)
    insertPlayer(connection, 50, 'Derrick Jones Jr.', 'CHI-Bulls', 5,
                 4, 6.05, 210, 5.0, 2.4, 0.5, 0.5, 0.6, 0.5, 0.338, 2016, 3200000)
    insertPlayer(connection, 51, 'Donovan Mitchell', 'CLE-Cavaliers', 6,
                 2, 6.01, 215, 28.3, 4.3, 4.4, 1.5, 0.4, 0.484, 0.386, 2017, 30913750)
    insertPlayer(connection, 52, 'Darius Garland', 'CLE-Cavaliers', 6,
                 1, 6.01, 192, 21.6, 2.7, 7.8, 1.2, 0.1, 0.462, 0.41, 2019, 8920795)
    insertPlayer(connection, 53, 'Evan Mobley', 'CLE-Cavaliers', 6, 4,
                 7.0, 215, 16.2, 9.0, 2.8, 0.8, 1.5, 0.554, 0.216, 2021, 8478720)
    insertPlayer(connection, 54, 'Jarrett Allen', 'CLE-Cavaliers', 6, 5,
                 6.11, 243, 14.3, 9.8, 1.7, 0.8, 1.2, 0.644, 0.1, 2017, 20000000)
    insertPlayer(connection, 55, 'Caris LeVert', 'CLE-Cavaliers', 6, 2,
                 6.06, 205, 12.1, 3.8, 3.9, 1.0, 0.3, 0.431, 0.392, 2016, 18796296)
    insertPlayer(connection, 56, 'Isaac Okoro', 'CLE-Cavaliers', 6, 3,
                 6.05, 225, 6.4, 2.5, 1.1, 0.7, 0.4, 0.494, 0.363, 2020, 7040880)
    insertPlayer(connection, 57, 'Dean Wade', 'CLE-Cavaliers', 6, 4,
                 6.09, 228, 4.7, 3.4, 0.8, 0.6, 0.5, 0.412, 0.354, 2019, 1930681)
    insertPlayer(connection, 58, 'Cedi Osman', 'CLE-Cavaliers', 6, 3,
                 6.07, 230, 8.7, 2.3, 1.5, 0.5, 0.1, 0.451, 0.372, 2017, 7426088)
    insertPlayer(connection, 59, 'Lamar Stevens', 'CLE-Cavaliers', 6, 3,
                 6.06, 230, 5.3, 3.3, 0.5, 0.4, 0.3, 0.448, 0.316, 2020, 1782621)
    insertPlayer(connection, 60, 'Ricky Rubio', 'CLE-Cavaliers', 6, 1,
                 6.02, 190, 5.2, 2.1, 3.5, 0.8, 0.2, 0.343, 0.256, 2011, 5853659)
    insertPlayer(connection, 61, 'Kyrie Irving', 'DAL-Mavericks', 7, 2,
                 6.02, 195, 27.0, 5.0, 6.0, 1.3, 0.6, 0.51, 0.392, 2011, 38917057)
    insertPlayer(connection, 62, 'Luka Doncic', 'DAL-Mavericks', 7, 1,
                 6.07, 230, 32.4, 8.6, 8.0, 1.4, 0.5, 0.496, 0.342, 2018, 37096500)
    insertPlayer(connection, 63, 'Reggie Bullock', 'DAL-Mavericks', 7,
                 3, 6.06, 205, 7.2, 3.6, 1.4, 0.7, 0.2, 0.409, 0.38, 2013, 10012800)
    insertPlayer(connection, 64, 'Tim Hardaway Jr.', 'DAL-Mavericks', 7,
                 3, 6.05, 205, 14.4, 3.5, 1.8, 0.7, 0.2, 0.401, 0.385, 2013, 19602273)
    insertPlayer(connection, 65, 'Christian Wood', 'DAL-Mavericks', 7, 5,
                 6.1, 214, 16.6, 7.3, 1.8, 0.4, 1.1, 0.515, 0.376, 2016, 14317459)
    insertPlayer(connection, 66, 'Josh Green', 'DAL-Mavericks', 7, 2,
                 6.05, 200, 9.1, 3.0, 1.7, 0.7, 0.1, 0.537, 0.402, 2020, 3098400)
    insertPlayer(connection, 67, 'Maxi Kleber', 'DAL-Mavericks', 7, 4,
                 6.1, 240, 5.9, 3.6, 1.4, 0.3, 0.8, 0.456, 0.348, 2017, 9000000)
    insertPlayer(connection, 68, 'Dwight Powell', 'DAL-Mavericks', 7,
                 5, 6.1, 240, 6.7, 4.1, 0.9, 0.6, 0.3, 0.732, 0.0, 2014, 11080125)
    insertPlayer(connection, 69, 'Justin Holiday', 'DAL-Mavericks', 7,
                 3, 6.06, 180, 4.4, 1.8, 0.9, 0.8, 0.5, 0.367, 0.286, 2013, 569821)
    insertPlayer(connection, 70, 'Jaden Hardy', 'DAL-Mavericks', 7, 2,
                 6.04, 198, 8.8, 1.9, 1.4, 0.4, 0.1, 0.438, 0.404, 2022, 1017781)
    insertPlayer(connection, 71, 'Nikola Jokic', 'DEN-Nuggets', 8, 5,
                 6.11, 184, 24.5, 11.8, 9.8, 1.3, 0.7, 0.632, 0.383, 2015, 33047803)
    insertPlayer(connection, 72, 'Jamal Murray', 'DEN-Nuggets', 8, 1,
                 6.04, 215, 20.0, 4.0, 6.2, 1.0, 0.2, 0.454, 0.398, 2017, 31650600)
    insertPlayer(connection, 73, 'Kentavious Caldwell-Pope', 'DEN-Nuggets',
                 8, 2, 6.05, 204, 10.8, 2.7, 2.4, 1.5, 0.5, 0.462, 0.423, 2013, 14004703)
    insertPlayer(connection, 74, 'Aaron Gordon', 'DEN-Nuggets', 8, 4,
                 6.08, 235, 16.3, 6.6, 3.0, 0.8, 0.8, 0.564, 0.347, 2014, 19690909)
    insertPlayer(connection, 75, 'Michael Porter Jr.', 'DEN-Nuggets', 8,
                 3, 6.1, 218, 17.4, 5.5, 1.0, 0.6, 0.5, 0.487, 0.414, 2019, 30913750)
    insertPlayer(connection, 76, 'Bruce Brown', 'DEN-Nuggets', 8, 3,
                 6.04, 202, 11.5, 4.1, 3.4, 1.1, 0.6, 0.483, 0.358, 2018, 6479000)
    insertPlayer(connection, 77, 'Reggie Jackson', 'DEN-Nuggets', 8, 1,
                 6.02, 208, 7.9, 1.8, 3.1, 0.6, 0.1, 0.383, 0.279, 2011, 580373)
    insertPlayer(connection, 78, 'Jeff Green', 'DEN-Nuggets', 8, 4,
                 6.08, 235, 7.8, 2.6, 1.2, 0.3, 0.3, 0.488, 0.288, 2008, 4500000)
    insertPlayer(connection, 79, 'Christian Braun', 'DEN-Nuggets', 8, 2,
                 6.07, 218, 4.7, 2.4, 0.8, 0.5, 0.2, 0.495, 0.354, 2022, 2808600)
    insertPlayer(connection, 80, 'DeAndre Jordan', 'DEN-Nuggets', 8,
                 5, 6.11, 265, 5.1, 5.2, 0.9, 0.3, 0.6, 0.765, 1.0, 2008, 1836090)
    insertPlayer(connection, 81, 'Cade Cunningham', 'DET-Pistons', 9, 1,
                 6.06, 220, 19.9, 6.2, 6.0, 0.8, 0.6, 0.415, 0.279, 2021, 10552800)
    insertPlayer(connection, 82, 'Bojan Bogdanovic', 'DET-Pistons', 9, 4,
                 6.07, 226, 21.6, 3.8, 2.6, 0.6, 0.1, 0.488, 0.411, 2014, 19550000)
    insertPlayer(connection, 83, 'Jaden Ivey', 'DET-Pistons', 9, 2,
                 6.04, 195, 16.3, 3.9, 5.2, 0.8, 0.2, 0.416, 0.343, 2022, 7252200)
    insertPlayer(connection, 84, 'Isaiah Stewart', 'DET-Pistons', 9, 5,
                 6.08, 250, 11.3, 8.1, 1.4, 0.4, 0.7, 0.442, 0.327, 2020, 3433320)
    insertPlayer(connection, 85, 'Killian Hayes', 'DET-Pistons', 9, 2,
                 6.05, 195, 10.3, 2.9, 6.2, 1.4, 0.4, 0.377, 0.28, 2020, 5837760)
    insertPlayer(connection, 86, 'James Wiseman', 'DET-Pistons', 9, 5,
                 7.0, 240, 12.7, 8.1, 0.7, 0.2, 0.8, 0.531, 0.167, 2021, 9603360)
    insertPlayer(connection, 87, 'Jalen Duren', 'DET-Pistons', 9, 5,
                 6.1, 250, 9.1, 8.9, 1.1, 0.7, 0.9, 0.648, 0.0, 2022, 4124280)
    insertPlayer(connection, 88, 'Marvin Bagley III', 'DET-Pistons', 9, 5,
                 6.11, 235, 12.0, 6.4, 0.9, 0.5, 0.7, 0.529, 0.288, 2018, 12500000)
    insertPlayer(connection, 89, 'Alec Burks', 'DET-Pistons', 9, 2,
                 6.06, 214, 12.8, 3.1, 2.2, 0.7, 0.2, 0.436, 0.414, 2011, 10012800)
    insertPlayer(connection, 90, 'Cory Joseph', 'DET-Pistons', 9, 1,
                 6.03, 200, 6.9, 1.7, 3.5, 0.5, 0.1, 0.427, 0.389, 2011, 5155500)
    insertPlayer(connection, 91, 'Stephen Curry', 'GSW-Warriors', 10, 1,
                 6.02, 185, 29.4, 6.1, 6.3, 0.9, 0.4, 0.493, 0.427, 2009, 48070014)
    insertPlayer(connection, 92, 'Klay Thompson', 'GSW-Warriors', 10, 3,
                 6.06, 215, 21.9, 4.1, 2.4, 0.7, 0.4, 0.436, 0.412, 2012, 40600080)
    insertPlayer(connection, 93, 'Andrew Wiggins', 'GSW-Warriors', 10, 3,
                 6.07, 197, 17.1, 5.0, 2.3, 1.2, 0.8, 0.473, 0.396, 2014, 33616770)
    insertPlayer(connection, 94, 'Draymond Green', 'GSW-Warriors', 10, 4,
                 6.06, 230, 8.5, 7.2, 6.8, 1.0, 0.8, 0.527, 0.305, 2012, 25806468)
    insertPlayer(connection, 95, 'Jordan Poole', 'GSW-Warriors', 10, 1,
                 6.04, 194, 20.4, 2.7, 4.5, 0.8, 0.3, 0.43, 0.336, 2019, 3901399)
    insertPlayer(connection, 96, 'Donte DiVincenzo', 'GSW-Warriors', 10,
                 2, 6.04, 203, 9.4, 4.5, 3.5, 1.3, 0.1, 0.435, 0.397, 2018, 4500000)
    insertPlayer(connection, 97, 'Kevon Looney', 'GSW-Warriors', 10,
                 5, 6.09, 222, 7.0, 9.3, 2.5, 0.6, 0.6, 0.63, 0.0, 2015, 8000000)
    insertPlayer(connection, 98, 'Jonathan Kuminga', 'GSW-Warriors', 10,
                 4, 6.08, 210, 9.9, 3.4, 1.9, 0.6, 0.5, 0.525, 0.37, 2021, 5739840)
    insertPlayer(connection, 99, 'Anthony Lamb', 'GSW-Warriors', 10, 3,
                 6.06, 227, 6.7, 3.5, 1.5, 0.5, 0.3, 0.471, 0.367, 2020, 253254)
    insertPlayer(connection, 100, 'Ty Jerome', 'GSW-Warriors', 10, 2,
                 6.05, 195, 6.9, 1.7, 3.0, 0.5, 0.1, 0.488, 0.389, 2019, 2439025)
    insertPlayer(connection, 101, 'Kevin Porter Jr.', 'HOU-Rockets', 11,
                 1, 6.04, 203, 19.2, 5.3, 5.7, 1.4, 0.3, 0.442, 0.366, 2019, 3217631)
    insertPlayer(connection, 102, 'Jalen Green', 'HOU-Rockets', 11, 2,
                 6.04, 178, 22.1, 3.7, 3.7, 0.8, 0.2, 0.416, 0.338, 2021, 9441840)
    insertPlayer(connection, 103, 'Jabari Smith Jr.', 'HOU-Rockets', 11,
                 4, 6.1, 220, 12.8, 7.2, 1.3, 0.5, 0.9, 0.408, 0.307, 2022, 8882640)
    insertPlayer(connection, 104, 'Alperen Seng�n', 'HOU-Rockets', 11, 5,
                 6.09, 235, 14.8, 9.0, 3.9, 0.9, 0.9, 0.553, 0.333, 2021, 3375360)
    insertPlayer(connection, 105, 'KJ Martin', 'HOU-Rockets', 11, 3,
                 6.06, 215, 12.7, 5.5, 1.5, 0.5, 0.4, 0.569, 0.315, 2020, 1782621)
    insertPlayer(connection, 106, 'Jae''Sean Tate', 'HOU-Rockets', 11,
                 3, 6.04, 230, 9.1, 3.8, 2.7, 0.7, 0.2, 0.48, 0.283, 2020, 7065217)
    insertPlayer(connection, 107, 'Tari Eason', 'HOU-Rockets', 11, 4,
                 6.08, 216, 9.3, 6.0, 1.1, 1.2, 0.6, 0.448, 0.343, 2022, 3359160)
    insertPlayer(connection, 108, 'Daishen Nix', 'HOU-Rockets', 11, 1,
                 6.05, 224, 4.0, 1.7, 2.3, 0.5, 0.1, 0.342, 0.286, 2021, 1563518)
    insertPlayer(connection, 109, 'TyTy Washington Jr.', 'HOU-Rockets', 11,
                 1, 6.03, 197, 4.7, 1.5, 1.5, 0.5, 0.1, 0.363, 0.238, 2022, 2210040)
    insertPlayer(connection, 110, 'Garrison Mathews', 'HOU-Rockets', 11,
                 2, 6.05, 215, 4.8, 1.4, 0.5, 0.5, 0.1, 0.353, 0.342, 2019, 2000000)
    insertPlayer(connection, 111, 'Tyrese Haliburton', 'IND-Pacers', 12,
                 1, 6.05, 185, 20.7, 3.7, 10.4, 1.6, 0.4, 0.49, 0.4, 2020, 4215120)
    insertPlayer(connection, 112, 'Buddy Hield', 'IND-Pacers', 12, 3,
                 6.04, 220, 16.8, 5.0, 2.8, 1.2, 0.3, 0.458, 0.425, 2016, 21177750)
    insertPlayer(connection, 113, 'Myles Turner', 'IND-Pacers', 12, 5,
                 6.11, 250, 18.0, 7.5, 1.4, 0.6, 2.3, 0.548, 0.373, 2015, 35069500)
    insertPlayer(connection, 114, 'Bennedict Mathurin', 'IND-Pacers', 12,
                 2, 6.06, 210, 16.7, 4.1, 1.5, 0.6, 0.2, 0.434, 0.323, 2022, 6586800)
    insertPlayer(connection, 115, 'Andrew Nembhard', 'IND-Pacers', 12,
                 2, 6.05, 193, 9.5, 2.7, 4.5, 0.9, 0.2, 0.441, 0.35, 2022, 2244111)
    insertPlayer(connection, 116, 'Aaron Nesmith', 'IND-Pacers', 12, 3,
                 6.05, 215, 10.1, 3.8, 1.3, 0.8, 0.5, 0.427, 0.366, 2020, 3804360)
    insertPlayer(connection, 117, 'Jordan Nwora', 'IND-Pacers', 12, 3,
                 6.08, 225, 13.0, 4.7, 2.1, 0.5, 0.3, 0.476, 0.422, 2020, 2800000)
    insertPlayer(connection, 118, 'T.J. McConnell', 'IND-Pacers', 12, 1,
                 6.01, 190, 8.7, 3.1, 5.3, 1.1, 0.1, 0.543, 0.441, 2015, 8100000)
    insertPlayer(connection, 119, 'Chris Duarte', 'IND-Pacers', 12, 3,
                 6.06, 190, 7.9, 2.5, 1.4, 0.5, 0.2, 0.369, 0.316, 2021, 3936960)
    insertPlayer(connection, 120, 'Jalen Smith', 'IND-Pacers', 12, 5,
                 6.1, 215, 9.4, 5.8, 1.0, 0.3, 0.9, 0.476, 0.283, 2020, 4670160)
    insertPlayer(connection, 121, 'Paul George', 'LAC-Clippers', 13, 3,
                 6.08, 220, 23.8, 6.1, 5.1, 1.5, 0.4, 0.457, 0.371, 0.871, 42492492)
    insertPlayer(connection, 122, 'Kawhi Leonard', 'LAC-Clippers', 13, 3,
                 6.07, 225, 23.8, 6.5, 3.9, 1.4, 0.5, 0.512, 0.416, 0.871, 42492492)
    insertPlayer(connection, 123, 'Russell Westbrook', 'LAC-Clippers', 13,
                 1, 6.03, 200, 15.8, 4.9, 7.6, 1.1, 0.5, 0.489, 0.356, 0.658, 495955)
    insertPlayer(connection, 124, 'Ivica Zubac', 'LAC-Clippers', 13, 5,
                 7.0, 240, 10.8, 9.9, 1.0, 0.4, 1.3, 0.634, 0.0, 0.697, 10123457)
    insertPlayer(connection, 125, 'Marcus Morris', 'LAC-Clippers', 13, 4,
                 6.08, 218, 11.2, 4.0, 1.8, 0.6, 0.3, 0.426, 0.364, 0.782, 16372093)
    insertPlayer(connection, 126, 'Norman Powell', 'LAC-Clippers', 13, 2,
                 6.03, 215, 17.0, 2.9, 1.8, 0.8, 0.3, 0.479, 0.397, 0.812, 16758621)
    insertPlayer(connection, 127, 'Eric Gordon', 'LAC-Clippers', 13, 2,
                 6.03, 215, 11.0, 1.7, 2.1, 0.6, 0.4, 0.463, 0.423, 0.842, 19568360)
    insertPlayer(connection, 128, 'Terance Mann', 'LAC-Clippers', 13, 2,
                 6.05, 215, 8.8, 3.4, 2.3, 0.5, 0.3, 0.519, 0.389, 0.78, 1930681)
    insertPlayer(connection, 129, 'Nicolas Batum', 'LAC-Clippers', 13, 4,
                 6.08, 230, 6.1, 3.8, 1.6, 0.7, 0.6, 0.42, 0.391, 0.708, 10843350)
    insertPlayer(connection, 130, 'Mason Plumlee', 'LAC-Clippers', 13,
                 5, 6.11, 254, 7.5, 6.9, 1.7, 0.5, 0.5, 0.727, 0.0, 0.772, 9080417)
    insertPlayer(connection, 131, 'LeBron James', 'LAL-Lakers', 14, 4,
                 6.09, 250, 28.9, 8.3, 6.8, 0.9, 0.6, 0.5, 0.321, 2003, 44474988)
    insertPlayer(connection, 132, 'Anthony Davis', 'LAL-Lakers', 14, 5,
                 6.1, 253, 25.9, 12.5, 2.6, 1.1, 2.0, 0.563, 0.257, 2012, 37980720)
    insertPlayer(connection, 133, 'D''Angelo Russell', 'LAL-Lakers', 14,
                 1, 6.04, 193, 17.4, 2.9, 6.1, 0.6, 0.5, 0.484, 0.414, 2015, 31377750)
    insertPlayer(connection, 134, 'Dennis Schr�der', 'LAL-Lakers', 14, 1,
                 6.03, 172, 12.6, 2.5, 4.5, 0.8, 0.2, 0.415, 0.329, 2013, 1836090)
    insertPlayer(connection, 135, 'Austin Reaves', 'LAL-Lakers', 14, 2,
                 6.05, 206, 13.0, 3.0, 3.4, 0.5, 0.3, 0.529, 0.398, 2021, 1563518)
    insertPlayer(connection, 136, 'Troy Brown Jr.', 'LAL-Lakers', 14,
                 3, 6.06, 215, 7.1, 4.1, 1.3, 0.8, 0.2, 0.43, 0.381, 2018, 1836090)
    insertPlayer(connection, 137, 'Jarred Vanderbilt', 'LAL-Lakers', 14,
                 4, 6.09, 214, 7.2, 6.7, 1.6, 1.2, 0.2, 0.529, 0.303, 2018, 4374000)
    insertPlayer(connection, 138, 'Malik Beasley', 'LAL-Lakers', 14, 2,
                 6.04, 187, 11.1, 3.3, 1.2, 0.8, 0.0, 0.392, 0.353, 2016, 15558035)
    insertPlayer(connection, 139, 'Lonnie Walker IV', 'LAL-Lakers', 14,
                 2, 6.04, 204, 11.7, 1.9, 1.1, 0.5, 0.3, 0.448, 0.365, 2018, 6479000)
    insertPlayer(connection, 140, 'Rui Hachimura', 'LAL-Lakers', 14, 4,
                 6.08, 230, 9.6, 4.7, 0.7, 0.2, 0.4, 0.485, 0.296, 2019, 6263188)
    insertPlayer(connection, 141, 'Ja Morant', 'MEM-Grizzlies', 15, 1,
                 6.01, 174, 26.2, 5.9, 8.1, 1.1, 0.3, 0.466, 0.307, 2019, 12119440)
    insertPlayer(connection, 142, 'Desmond Bane', 'MEM-Grizzlies', 15, 2,
                 6.05, 215, 21.5, 5.0, 4.4, 1.0, 0.4, 0.479, 0.408, 2020, 2130240)
    insertPlayer(connection, 143, 'Dillon Brooks', 'MEM-Grizzlies', 15, 3,
                 6.07, 225, 14.3, 3.3, 2.6, 0.9, 0.2, 0.396, 0.326, 2017, 11400000)
    insertPlayer(connection, 144, 'Jaren Jackson Jr.', 'MEM-Grizzlies', 15,
                 5, 6.11, 242, 18.6, 6.8, 1.0, 1.0, 3.0, 0.506, 0.355, 2019, 28946605)
    insertPlayer(connection, 145, 'Steven Adams', 'MEM-Grizzlies', 15,
                 5, 6.11, 265, 8.6, 11.5, 2.3, 0.9, 1.1, 0.597, 0.0, 2018, 17926829)
    insertPlayer(connection, 146, 'Luke Kennard', 'MEM-Grizzlies', 15, 2,
                 6.05, 206, 11.3, 3.1, 2.3, 0.5, 0.0, 0.526, 0.54, 2017, 14415545)
    insertPlayer(connection, 147, 'Tyus Jones', 'MEM-Grizzlies', 15, 1,
                 6.0, 196, 10.3, 2.5, 5.2, 1.0, 0.1, 0.438, 0.371, 2015, 15000000)
    insertPlayer(connection, 148, 'Santi Aldama', 'MEM-Grizzlies', 15,
                 4, 6.11, 224, 9.0, 4.8, 1.3, 0.6, 0.6, 0.47, 0.353, 2021, 28946605)
    insertPlayer(connection, 149, 'John Konchar', 'MEM-Grizzlies', 15,
                 3, 6.05, 210, 5.1, 4.3, 1.4, 1.1, 0.3, 0.431, 0.339, 2019, 2300000)
    insertPlayer(connection, 150, 'Brandon Clarke', 'MEM-Grizzlies', 15,
                 4, 6.08, 215, 10.0, 5.5, 1.3, 0.6, 0.7, 0.656, 0.167, 2019, 4343920)
    insertPlayer(connection, 151, 'Tyler Herro', 'MIA-Heat', 16, 2,
                 6.03, 195, 20.1, 5.4, 4.2, 0.8, 0.2, 0.439, 0.378, 2019, 5722116)
    insertPlayer(connection, 152, 'Bam Adebayo', 'MIA-Heat', 16, 5,
                 6.09, 255, 20.4, 9.2, 3.2, 1.2, 0.8, 0.54, 0.083, 2017, 30351780)
    insertPlayer(connection, 153, 'Jimmy Butler', 'MIA-Heat', 16, 4,
                 6.07, 230, 22.9, 5.9, 5.3, 1.8, 0.3, 0.539, 0.35, 2011, 37653300)
    insertPlayer(connection, 154, 'Kyle Lowry', 'MIA-Heat', 16, 1, 6.0,
                 196, 11.2, 4.1, 5.1, 1.0, 0.4, 0.404, 0.345, 2006, 28333334)
    insertPlayer(connection, 155, 'Caleb Martin', 'MIA-Heat', 16, 3,
                 6.05, 205, 9.6, 4.8, 1.6, 1.0, 0.4, 0.464, 0.356, 2019, 6479000)
    insertPlayer(connection, 156, 'Max Strus', 'MIA-Heat', 16, 3,
                 6.05, 215, 11.5, 3.2, 2.1, 0.5, 0.2, 0.41, 0.35, 2019, 1815677)
    insertPlayer(connection, 157, 'Victor Oladipo', 'MIA-Heat', 16, 2,
                 6.04, 213, 10.7, 3.0, 3.5, 1.4, 0.3, 0.397, 0.33, 2013, 8750000)
    insertPlayer(connection, 158, 'Gabe Vincent', 'MIA-Heat', 16, 1,
                 6.03, 195, 9.4, 2.1, 2.5, 0.9, 0.1, 0.402, 0.334, 2019, 1815677)
    insertPlayer(connection, 159, 'Kevin Love', 'MIA-Heat', 16, 4,
                 6.08, 251, 7.7, 5.7, 1.9, 0.4, 0.2, 0.388, 0.297, 2008, 3114138)
    insertPlayer(connection, 160, 'Haywood Highsmith', 'MIA-Heat', 16,
                 4, 6.07, 220, 4.4, 3.5, 0.8, 0.7, 0.3, 0.431, 0.339, 2020, 1752638)
    insertPlayer(connection, 161, 'Jrue Holiday', 'MIL-Bucks', 17, 1,
                 6.04, 205, 19.3, 5.1, 7.4, 1.2, 0.4, 0.479, 0.384, 2009, 33665040)
    insertPlayer(connection, 162, 'Giannis Antetokounmpo', 'MIL-Bucks', 17,
                 4, 7.0, 242, 31.1, 11.8, 5.7, 0.8, 0.8, 0.553, 0.275, 2013, 42492492)
    insertPlayer(connection, 163, 'Brook Lopez', 'MIL-Bucks', 17, 5,
                 7.0, 282, 15.9, 6.7, 1.3, 0.5, 2.5, 0.531, 0.374, 2008, 13906976)
    insertPlayer(connection, 164, 'Grayson Allen', 'MIL-Bucks', 17, 2,
                 6.04, 198, 10.4, 3.3, 2.3, 0.9, 0.2, 0.44, 0.399, 2018, 8500000)
    insertPlayer(connection, 165, 'Bobby Portis', 'MIL-Bucks', 17, 4,
                 6.1, 250, 14.1, 9.6, 1.5, 0.4, 0.2, 0.496, 0.37, 2015, 10843350)
    insertPlayer(connection, 166, 'Khris Middleton', 'MIL-Bucks', 17, 3,
                 6.07, 222, 15.1, 4.2, 4.9, 0.7, 0.2, 0.436, 0.315, 2012, 37948276)
    insertPlayer(connection, 167, 'Pat Connaughton', 'MIL-Bucks', 17, 3,
                 6.05, 209, 7.6, 4.6, 1.3, 0.6, 0.2, 0.392, 0.339, 2015, 5728393)
    insertPlayer(connection, 168, 'Joe Ingles', 'MIL-Bucks', 17, 3,
                 6.08, 220, 6.9, 2.8, 3.3, 0.7, 0.1, 0.435, 0.409, 2014, 6479000)
    insertPlayer(connection, 169, 'Jevon Carter', 'MIL-Bucks', 17, 1,
                 6.01, 200, 8.0, 2.5, 2.4, 0.8, 0.4, 0.423, 0.421, 2018, 2100000)
    insertPlayer(connection, 170, 'Jae Crowder', 'MIL-Bucks', 17, 4,
                 6.06, 235, 6.9, 3.8, 1.5, 0.7, 0.3, 0.479, 0.436, 2012, 10183800)
    insertPlayer(connection, 171, 'Anthony Edwards', 'MIN-Timberwolves', 18,
                 2, 6.04, 225, 24.6, 5.8, 4.4, 1.6, 0.7, 0.459, 0.369, 2020, 10733400)
    insertPlayer(connection, 172, 'Karl-Anthony Towns', 'MIN-Timberwolves',
                 18, 4, 6.11, 248, 20.8, 8.1, 4.8, 0.7, 0.6, 0.495, 0.366, 2015, 33833400)
    insertPlayer(connection, 173, 'Mike Conley', 'MIN-Timberwolves', 18,
                 1, 6.01, 175, 14.0, 3.1, 5.0, 1.2, 0.2, 0.46, 0.42, 2007, 22680000)
    insertPlayer(connection, 174, 'Rudy Gobert', 'MIN-Timberwolves', 18,
                 5, 7.01, 258, 13.4, 11.6, 1.2, 0.8, 1.4, 0.659, 0.0, 2013, 38172414)
    insertPlayer(connection, 175, 'Jaden McDaniels', 'MIN-Timberwolves', 18,
                 3, 6.09, 185, 12.1, 3.9, 1.9, 0.9, 1.0, 0.517, 0.398, 2020, 2161440)
    insertPlayer(connection, 176, 'Kyle Anderson', 'MIN-Timberwolves', 18,
                 4, 6.09, 230, 9.4, 5.3, 4.9, 1.1, 0.9, 0.509, 0.41, 2014, 8780488)
    insertPlayer(connection, 177, 'Taurean Prince', 'MIN-Timberwolves', 18,
                 4, 6.07, 218, 9.1, 2.4, 1.6, 0.5, 0.3, 0.467, 0.381, 2016, 7295000)
    insertPlayer(connection, 178, 'Austin Rivers', 'MIN-Timberwolves', 18,
                 2, 6.04, 200, 4.9, 1.6, 1.4, 0.5, 0.1, 0.435, 0.35, 2022, 1836090)
    insertPlayer(connection, 179, 'Jaylen Nowell', 'MIN-Timberwolves', 18,
                 2, 6.04, 201, 10.8, 2.6, 2.0, 0.6, 0.1, 0.448, 0.289, 2019, 1930681)
    insertPlayer(connection, 180, 'Naz Reid', 'MIN-Timberwolves', 18, 5,
                 6.09, 264, 11.5, 4.9, 1.1, 0.6, 0.8, 0.537, 0.346, 2019, 1930681)
    insertPlayer(connection, 181, 'CJ McCollum', 'NOP-Pelicans', 19, 1,
                 6.03, 190, 20.9, 4.4, 5.7, 0.9, 0.5, 0.437, 0.389, 2013, 33333333)
    insertPlayer(connection, 182, 'Brandon Ingram', 'NOP-Pelicans', 19,
                 3, 6.08, 190, 24.7, 5.5, 5.8, 0.7, 0.4, 0.484, 0.39, 2016, 31650600)
    insertPlayer(connection, 183, 'Zion Williamson', 'NOP-Pelicans', 19,
                 4, 6.06, 284, 26.0, 7.0, 4.6, 1.1, 0.6, 0.608, 0.368, 2020, 13534817)
    insertPlayer(connection, 184, 'Trey Murphy III', 'NOP-Pelicans', 19,
                 3, 6.09, 206, 14.5, 3.6, 1.4, 1.1, 0.5, 0.484, 0.406, 2021, 3206520)
    insertPlayer(connection, 185, 'Herbert Jones', 'NOP-Pelicans', 19,
                 4, 6.08, 210, 9.8, 4.1, 2.5, 1.6, 0.6, 0.469, 0.335, 2021, 1785000)
    insertPlayer(connection, 186, 'Jonas Valanciunas', 'NOP-Pelicans', 19,
                 5, 6.11, 265, 14.1, 10.2, 1.8, 0.3, 0.7, 0.547, 0.349, 2012, 14700000)
    insertPlayer(connection, 187, 'Naji Marshall', 'NOP-Pelicans', 19,
                 3, 6.07, 220, 9.1, 3.6, 2.5, 0.7, 0.2, 0.433, 0.303, 2020, 1782621)
    insertPlayer(connection, 188, 'Josh Richardson', 'NOP-Pelicans', 19,
                 2, 6.05, 200, 7.5, 2.4, 1.6, 1.3, 0.4, 0.419, 0.384, 2015, 12196094)
    insertPlayer(connection, 189, 'Jose Alvarado', 'NOP-Pelicans', 19,
                 1, 6.0, 179, 9.0, 2.3, 3.0, 1.1, 0.2, 0.411, 0.336, 2021, 1563518)
    insertPlayer(connection, 190, 'Larry Nance Jr.', 'NOP-Pelicans', 19,
                 5, 6.07, 245, 6.8, 5.4, 1.8, 0.9, 0.6, 0.61, 0.333, 2015, 9672727)
    insertPlayer(connection, 191, 'Julius Randle', 'NYK-Knicks', 20, 4,
                 6.08, 250, 25.1, 10.0, 4.1, 0.6, 0.3, 0.459, 0.343, 2014, 23760000)
    insertPlayer(connection, 192, 'Jalen Brunson', 'NYK-Knicks', 20, 1,
                 6.02, 190, 24.0, 3.5, 6.2, 0.9, 0.2, 0.491, 0.416, 2018, 27733332)
    insertPlayer(connection, 193, 'RJ Barrett', 'NYK-Knicks', 20, 2,
                 6.06, 214, 19.6, 5.0, 2.8, 0.4, 0.2, 0.434, 0.31, 2019, 10900635)
    insertPlayer(connection, 194, 'Josh Hart', 'NYK-Knicks', 20, 3,
                 6.05, 215, 10.2, 7.0, 3.6, 1.4, 0.5, 0.586, 0.519, 2017, 12960000)
    insertPlayer(connection, 195, 'Quentin Grimes', 'NYK-Knicks', 20, 2,
                 6.05, 205, 11.3, 3.2, 2.1, 0.7, 0.4, 0.468, 0.386, 2021, 2277000)
    insertPlayer(connection, 196, 'Immanuel Quickley', 'NYK-Knicks', 20,
                 2, 6.03, 190, 14.9, 4.2, 3.4, 1.0, 0.2, 0.448, 0.37, 2020, 2316240)
    insertPlayer(connection, 197, 'Mitchell Robinson', 'NYK-Knicks', 20,
                 5, 7.0, 240, 7.4, 9.4, 0.9, 0.9, 1.8, 0.671, 0.0, 2018, 17045454)
    insertPlayer(connection, 198, 'Derrick Rose', 'NYK-Knicks', 20, 3,
                 6.08, 218, 5.6, 1.5, 1.7, 0.3, 0.2, 0.384, 0.302, 2009, 14520730)
    insertPlayer(connection, 199, 'Isaiah Hartenstein', 'NYK-Knicks', 20,
                 5, 7.0, 250, 5.0, 6.5, 1.2, 0.6, 0.8, 0.535, 0.216, 2018, 7804879)
    insertPlayer(connection, 200, 'Obi Toppin', 'NYK-Knicks', 20, 4,
                 6.09, 220, 7.4, 2.8, 1.0, 0.3, 0.2, 0.446, 0.344, 2020, 5348280)
    insertPlayer(connection, 201, 'Shai Gilgeous-Alexander', 'OKC-Thunder',
                 21, 1, 6.06, 180, 31.4, 4.8, 5.5, 1.6, 1.0, 0.51, 0.345, 2018, 30913750)
    insertPlayer(connection, 202, 'Josh Giddey', 'OKC-Thunder', 21, 2,
                 6.08, 210, 16.6, 7.9, 6.2, 0.8, 0.4, 0.482, 0.325, 2021, 6287400)
    insertPlayer(connection, 203, 'Luguentz Dort', 'OKC-Thunder', 21, 3,
                 6.03, 215, 13.7, 4.6, 2.1, 1.0, 0.3, 0.388, 0.33, 0.772, 15277778)
    insertPlayer(connection, 204, 'Jalen Williams', 'OKC-Thunder', 21, 2,
                 6.06, 195, 14.1, 4.5, 3.3, 1.4, 0.5, 0.521, 0.356, 2022, 4341480)
    insertPlayer(connection, 205, 'Kenrich Williams', 'OKC-Thunder', 21,
                 4, 6.06, 210, 8.0, 4.9, 2.0, 0.8, 0.3, 0.517, 0.373, 2018, 2000000)
    insertPlayer(connection, 206, 'Aleksej Pokusevski', 'OKC-Thunder', 21,
                 4, 7.0, 190, 8.1, 4.7, 1.9, 0.6, 1.3, 0.434, 0.365, 2020, 3261480)
    insertPlayer(connection, 207, 'Isaiah Joe', 'OKC-Thunder', 21, 2,
                 6.04, 165, 9.5, 2.4, 1.2, 0.7, 0.1, 0.441, 0.409, 2020, 1836090)
    insertPlayer(connection, 208, 'Jeremiah Robinson-Earl', 'OKC-Thunder',
                 21, 4, 6.09, 230, 6.8, 4.2, 1.0, 0.6, 0.3, 0.444, 0.333, 2021, 2000000)
    insertPlayer(connection, 209, 'Jaylin Williams', 'OKC-Thunder', 21,
                 5, 6.1, 240, 5.9, 4.9, 1.6, 0.6, 0.2, 0.436, 0.407, 2022, 2000000)
    insertPlayer(connection, 210, 'Aaron Wiggins', 'OKC-Thunder', 21, 2,
                 6.06, 200, 6.8, 3.0, 1.1, 0.6, 0.2, 0.512, 0.393, 2021, 11055120)
    insertPlayer(connection, 211, 'Paolo Banchero', 'ORL-Magic', 22, 4,
                 6.1, 250, 20.0, 6.9, 3.7, 0.8, 0.5, 0.427, 0.298, 2022, 11055120)
    insertPlayer(connection, 212, 'Franz Wagner', 'ORL-Magic', 22, 3,
                 6.09, 225, 18.6, 4.1, 3.5, 1.0, 0.2, 0.485, 0.361, 2021, 5258280)
    insertPlayer(connection, 213, 'Wendell Carter Jr.', 'ORL-Magic', 22,
                 5, 6.1, 270, 15.2, 8.7, 2.3, 0.5, 0.6, 0.525, 0.356, 2018, 14150000)
    insertPlayer(connection, 214, 'Markelle Fultz', 'ORL-Magic', 22, 1,
                 6.03, 209, 14.0, 3.9, 5.7, 1.5, 0.4, 0.514, 0.31, 2017, 16500000)
    insertPlayer(connection, 215, 'Cole Anthony', 'ORL-Magic', 22, 1,
                 6.02, 185, 13.0, 4.8, 3.9, 0.6, 0.5, 0.454, 0.364, 2020, 3613680)
    insertPlayer(connection, 216, 'Gary Harris', 'ORL-Magic', 22, 2,
                 6.04, 210, 8.3, 2.0, 1.2, 0.9, 0.3, 0.45, 0.431, 2014, 13000000)
    insertPlayer(connection, 217, 'Jalen Suggs', 'ORL-Magic', 22, 2,
                 6.04, 205, 9.9, 3.0, 2.9, 1.3, 0.5, 0.419, 0.327, 2021, 6922320)
    insertPlayer(connection, 218, 'RJ Hampton', 'ORL-Magic', 22, 2,
                 6.04, 175, 5.7, 1.5, 1.3, 0.6, 0.2, 0.439, 0.34, 2020, 2412840)
    insertPlayer(connection, 219, 'Bol Bol', 'ORL-Magic', 22, 4, 7.02,
                 220, 9.1, 5.8, 1.0, 0.4, 1.2, 0.546, 0.265, 2019, 2200000)
    insertPlayer(connection, 220, 'Moritz Wagner', 'ORL-Magic', 22, 5,
                 6.11, 245, 10.5, 4.5, 1.5, 0.6, 0.2, 0.5, 0.313, 2018, 1878720)
    insertPlayer(connection, 221, 'James Harden', 'PHI-76ers', 23, 1,
                 6.05, 220, 21.0, 6.1, 10.7, 1.2, 0.5, 0.441, 0.385, 2009, 33000000)
    insertPlayer(connection, 222, 'Joel Embiid', 'PHI-76ers', 23, 5,
                 7.0, 280, 33.1, 10.2, 4.2, 1.0, 1.7, 0.548, 0.33, 2016, 33616770)
    insertPlayer(connection, 223, 'Tyrese Maxey', 'PHI-76ers', 23, 2,
                 6.02, 200, 20.3, 2.9, 3.5, 0.8, 0.1, 0.481, 0.434, 2020, 1997718)
    insertPlayer(connection, 224, 'Tobias Harris', 'PHI-76ers', 23, 3,
                 6.08, 226, 14.7, 5.7, 2.5, 0.9, 0.5, 0.501, 0.389, 2011, 37633050)
    insertPlayer(connection, 225, 'De''Anthony Melton', 'PHI-76ers', 23,
                 2, 6.02, 200, 10.1, 4.1, 2.6, 1.6, 0.5, 0.425, 0.39, 2018, 8250000)
    insertPlayer(connection, 226, 'P.J. Tucker', 'PHI-76ers', 23, 4,
                 6.05, 245, 3.5, 3.9, 0.8, 0.5, 0.2, 0.427, 0.393, 2011, 10490000)
    insertPlayer(connection, 227, 'Shake Milton', 'PHI-76ers', 23, 2,
                 6.05, 205, 8.4, 2.5, 3.2, 0.3, 0.2, 0.479, 0.378, 2018, 1997718)
    insertPlayer(connection, 228, 'Georges Niang', 'PHI-76ers', 23, 4,
                 6.07, 230, 8.2, 2.4, 1.0, 0.4, 0.2, 0.442, 0.401, 2016, 3465000)
    insertPlayer(connection, 229, 'Jalen McDaniels', 'PHI-76ers', 23,
                 3, 6.09, 205, 6.7, 3.2, 0.8, 0.7, 0.2, 0.488, 0.4, 2019, 1930681)
    insertPlayer(connection, 230, 'Danuel House Jr.', 'PHI-76ers', 23,
                 3, 6.06, 220, 4.8, 1.7, 0.8, 0.3, 0.2, 0.472, 0.336, 2016, 4105000)
    insertPlayer(connection, 231, 'Devin Booker', 'PHX-Suns', 24, 2,
                 6.05, 206, 27.8, 4.5, 5.5, 1.0, 0.3, 0.494, 0.351, 2015, 33833400)
    insertPlayer(connection, 232, 'Kevin Durant', 'PHX-Suns', 24, 4,
                 6.1, 240, 26.0, 6.4, 3.5, 0.3, 1.3, 0.57, 0.537, 2008, 44119845)
    insertPlayer(connection, 233, 'Chris Paul', 'PHX-Suns', 24, 1,
                 6.0, 175, 13.9, 4.3, 8.9, 1.5, 0.4, 0.44, 0.375, 2005, 28400000)
    insertPlayer(connection, 234, 'Deandre Ayton', 'PHX-Suns', 24, 5,
                 6.11, 250, 18.0, 10.0, 1.7, 0.6, 0.8, 0.589, 0.292, 2018, 30913750)
    insertPlayer(connection, 235, 'Torrey Craig', 'PHX-Suns', 24, 4,
                 6.07, 221, 7.4, 5.4, 1.5, 0.6, 0.8, 0.456, 0.395, 2017, 5121951)
    insertPlayer(connection, 236, 'Damion Lee', 'PHX-Suns', 24, 2,
                 6.05, 210, 8.2, 3.0, 1.3, 0.4, 0.1, 0.442, 0.445, 2017, 1836090)
    insertPlayer(connection, 237, 'Cameron Payne', 'PHX-Suns', 24, 1,
                 6.01, 183, 10.3, 2.2, 4.5, 0.7, 0.2, 0.415, 0.368, 2015, 6000000)
    insertPlayer(connection, 238, 'Landry Shamet', 'PHX-Suns', 24, 2,
                 6.04, 190, 8.7, 1.7, 2.3, 0.7, 0.1, 0.377, 0.377, 2018, 9500000)
    insertPlayer(connection, 239, 'Josh Okogie', 'PHX-Suns', 24, 2,
                 6.04, 213, 7.3, 3.5, 1.5, 0.8, 0.5, 0.391, 0.335, 2018, 1836090)
    insertPlayer(connection, 240, 'Terrence Ross', 'PHX-Suns', 24, 2,
                 6.06, 206, 9.0, 3.3, 2.0, 0.5, 0.1, 0.428, 0.347, 2012, 580373)
    insertPlayer(connection, 241, 'Damian Lillard', 'POR-TrailBlazers', 25,
                 1, 6.02, 205, 32.2, 4.8, 7.3, 0.9, 0.3, 0.463, 0.371, 2012, 42492492)
    insertPlayer(connection, 242, 'Jerami Grant', 'POR-TrailBlazers', 25,
                 4, 6.08, 210, 20.5, 4.5, 2.4, 0.8, 0.8, 0.475, 0.401, 2014, 20955000)
    insertPlayer(connection, 243, 'Anfernee Simons', 'POR-TrailBlazers', 25,
                 2, 6.03, 181, 21.1, 2.6, 4.1, 0.7, 0.2, 0.447, 0.377, 2018, 22321429)
    insertPlayer(connection, 244, 'Trendon Watford', 'POR-TrailBlazers',
                 25, 4, 6.09, 240, 7.4, 3.8, 2.1, 0.5, 0.2, 0.56, 0.391, 2021, 1563518)
    insertPlayer(connection, 245, 'Matisse Thybulle', 'POR-TrailBlazers',
                 25, 2, 6.05, 201, 7.4, 3.5, 1.4, 1.7, 0.8, 0.438, 0.388, 2019, 4379527)
    insertPlayer(connection, 246, 'Justise Winslow', 'POR-TrailBlazers', 25,
                 4, 6.06, 222, 6.8, 5.0, 3.4, 1.0, 0.4, 0.409, 0.311, 2015, 4097561)
    insertPlayer(connection, 247, 'Jusuf Nurkic', 'POR-TrailBlazers', 25,
                 5, 6.11, 290, 13.3, 9.1, 2.9, 0.8, 0.8, 0.519, 0.361, 2014, 15625000)
    insertPlayer(connection, 248, 'Nassir Little', 'POR-TrailBlazers', 25,
                 3, 6.05, 220, 6.6, 2.6, 0.9, 0.4, 0.4, 0.442, 0.367, 2019, 4171548)
    insertPlayer(connection, 249, 'Shaedon Sharpe', 'POR-TrailBlazers', 25,
                 2, 6.06, 200, 9.9, 3.0, 1.2, 0.5, 0.3, 0.472, 0.36, 2022, 6012960)
    insertPlayer(connection, 250, 'Drew Eubanks', 'POR-TrailBlazers', 25,
                 5, 6.09, 245, 6.6, 5.4, 1.3, 0.5, 1.3, 0.641, 0.389, 2018, 1836090)
    insertPlayer(connection, 251, 'Domantas Sabonis', 'SAC-Kings', 26, 5,
                 6.11, 240, 19.1, 12.3, 7.3, 0.8, 0.5, 0.615, 0.373, 2016, 18500000)
    insertPlayer(connection, 252, 'De''Aaron Fox', 'SAC-Kings', 26, 1,
                 6.03, 185, 25.0, 4.2, 6.1, 1.1, 0.3, 0.512, 0.324, 2017, 30351780)
    insertPlayer(connection, 253, 'Harrison Barnes', 'SAC-Kings', 26, 4,
                 6.08, 225, 15.0, 4.5, 1.6, 0.7, 0.1, 0.473, 0.374, 2012, 18352273)
    insertPlayer(connection, 254, 'Keegan Murray', 'SAC-Kings', 26, 3,
                 6.08, 215, 12.2, 4.6, 1.2, 0.8, 0.5, 0.453, 0.411, 2022, 8008440)
    insertPlayer(connection, 255, 'Kevin Huerter', 'SAC-Kings', 26, 2,
                 6.07, 190, 15.2, 3.3, 2.9, 1.1, 0.3, 0.485, 0.402, 2018, 14508929)
    insertPlayer(connection, 256, 'Malik Monk', 'SAC-Kings', 26, 2,
                 6.03, 200, 13.5, 2.6, 3.9, 0.6, 0.3, 0.448, 0.359, 2017, 9472219)
    insertPlayer(connection, 257, 'Davion Mitchell', 'SAC-Kings', 26,
                 1, 6.02, 205, 5.6, 1.3, 2.3, 0.6, 0.2, 0.454, 0.32, 2021, 4833600)
    insertPlayer(connection, 258, 'Trey Lyles', 'SAC-Kings', 26, 4,
                 6.09, 234, 7.6, 4.1, 0.9, 0.4, 0.4, 0.458, 0.363, 2015, 2625000)
    insertPlayer(connection, 259, 'Kessler Edwards', 'SAC-Kings', 26, 3,
                 6.08, 215, 3.9, 2.1, 1.0, 0.5, 0.2, 0.435, 0.349, 2021, 1637966)
    insertPlayer(connection, 260, 'Terence Davis', 'SAC-Kings', 26, 2,
                 6.04, 201, 6.7, 2.2, 1.0, 0.7, 0.2, 0.423, 0.366, 2019, 4000000)
    insertPlayer(connection, 261, 'Keldon Johnson', 'SAS-Spurs', 27, 3,
                 6.05, 220, 22.0, 5.0, 2.9, 0.7, 0.2, 0.452, 0.329, 2019, 3873025)
    insertPlayer(connection, 262, 'Devin Vassell', 'SAS-Spurs', 27, 2,
                 6.05, 200, 18.5, 3.9, 3.6, 1.1, 0.4, 0.439, 0.387, 2020, 4437000)
    insertPlayer(connection, 263, 'Tre Jones', 'SAS-Spurs', 27, 1,
                 6.01, 185, 12.9, 3.6, 6.6, 1.3, 0.1, 0.459, 0.285, 2020, 1782621)
    insertPlayer(connection, 264, 'Devonte'' Graham', 'SAS-Spurs', 27, 1,
                 6.01, 195, 13.0, 2.5, 4.0, 0.8, 0.3, 0.38, 0.358, 2018, 11550000)
    insertPlayer(connection, 265, 'Blake Wesley', 'SAS-Spurs', 27, 2,
                 6.05, 185, 5.0, 2.2, 2.7, 0.7, 0.1, 0.321, 0.385, 2022, 2385480)
    insertPlayer(connection, 266, 'Jeremy Sochan', 'SAS-Spurs', 27, 4,
                 6.09, 230, 11.0, 5.3, 2.5, 0.8, 0.4, 0.453, 0.246, 2022, 5063520)
    insertPlayer(connection, 267, 'Malaki Branham', 'SAS-Spurs', 27, 2,
                 6.05, 180, 10.2, 2.7, 1.9, 0.5, 0.1, 0.44, 0.302, 2022, 2925600)
    insertPlayer(connection, 268, 'Zach Collins', 'SAS-Spurs', 27, 5,
                 6.11, 250, 11.6, 6.4, 2.9, 0.6, 0.8, 0.518, 0.374, 2018, 7350000)
    insertPlayer(connection, 269, 'Keita Bates-Diop', 'SAS-Spurs', 27,
                 4, 6.08, 229, 9.7, 3.7, 1.5, 0.7, 0.3, 0.508, 0.394, 2018, 1878720)
    insertPlayer(connection, 270, 'Doug McDermott', 'SAS-Spurs', 27, 3,
                 6.07, 225, 10.2, 2.2, 1.4, 0.2, 0.1, 0.457, 0.413, 2014, 13750000)
    insertPlayer(connection, 271, 'Pascal Siakam', 'TOR-Raptors', 28, 4,
                 6.09, 230, 24.2, 7.8, 5.8, 0.9, 0.5, 0.48, 0.324, 2016, 35448672)
    insertPlayer(connection, 272, 'Fred VanVleet', 'TOR-Raptors', 28, 1,
                 6.01, 197, 19.3, 4.1, 7.2, 1.8, 0.6, 0.393, 0.342, 2016, 21250000)
    insertPlayer(connection, 273, 'OG Anunoby', 'TOR-Raptors', 28, 3,
                 6.07, 232, 16.8, 5.0, 2.0, 1.9, 0.7, 0.476, 0.387, 2017, 17357143)
    insertPlayer(connection, 274, 'Scottie Barnes', 'TOR-Raptors', 28, 3,
                 6.09, 227, 15.3, 6.6, 4.8, 1.1, 0.8, 0.456, 0.281, 2021, 7644600)
    insertPlayer(connection, 275, 'Gary Trent Jr.', 'TOR-Raptors', 28, 2,
                 6.05, 209, 17.4, 2.6, 1.6, 1.6, 0.2, 0.433, 0.369, 2018, 17505000)
    insertPlayer(connection, 276, 'Jakob Poeltl', 'TOR-Raptors', 28, 5,
                 7.01, 245, 13.1, 9.1, 2.2, 1.2, 1.3, 0.652, 0.0, 2016, 9398148)
    insertPlayer(connection, 277, 'Precious Achiuwa', 'TOR-Raptors', 28,
                 5, 6.08, 225, 9.2, 6.0, 0.9, 0.6, 0.5, 0.485, 0.269, 2020, 2840160)
    insertPlayer(connection, 278, 'Chris Boucher', 'TOR-Raptors', 28, 4,
                 6.09, 200, 9.4, 5.5, 0.4, 0.6, 0.8, 0.493, 0.328, 2017, 12690000)
    insertPlayer(connection, 279, 'Otto Porter Jr.', 'TOR-Raptors', 28,
                 3, 6.08, 198, 5.5, 2.4, 1.0, 1.4, 0.0, 0.5, 0.353, 2013, 6000000)
    insertPlayer(connection, 280, 'Thaddeus Young', 'TOR-Raptors', 28,
                 4, 6.08, 235, 4.4, 3.1, 1.4, 1.0, 0.1, 0.545, 0.176, 2007, 8000000)
    insertPlayer(connection, 281, 'Lauri Markkanen', 'UTA-Jazz', 29, 4,
                 7.0, 240, 25.6, 8.6, 1.9, 0.6, 0.6, 0.499, 0.391, 2017, 16475454)
    insertPlayer(connection, 282, 'Jordan Clarkson', 'UTA-Jazz', 29, 2,
                 6.04, 194, 20.8, 4.0, 4.4, 0.5, 0.2, 0.444, 0.338, 2014, 13340000)
    insertPlayer(connection, 283, 'Kelly Olynyk', 'UTA-Jazz', 29, 5,
                 6.11, 240, 12.5, 6.2, 3.7, 0.9, 0.5, 0.499, 0.394, 2013, 12804878)
    insertPlayer(connection, 284, 'Kris Dunn', 'UTA-Jazz', 29, 1,
                 6.03, 205, 13.2, 4.5, 5.6, 1.1, 0.5, 0.537, 0.472, 2016, 735819)
    insertPlayer(connection, 285, 'Collin Sexton', 'UTA-Jazz', 29, 1,
                 6.01, 190, 14.3, 2.2, 2.9, 0.6, 0.1, 0.506, 0.393, 2018, 16500000)
    insertPlayer(connection, 286, 'Walker Kessler', 'UTA-Jazz', 29, 5,
                 7.01, 245, 9.2, 8.4, 0.9, 0.4, 2.3, 0.72, 0.333, 2022, 2696400)
    insertPlayer(connection, 287, 'Ochai Agbaji', 'UTA-Jazz', 29, 2,
                 6.05, 215, 7.9, 2.1, 1.1, 0.3, 0.3, 0.427, 0.355, 2022, 3918360)
    insertPlayer(connection, 288, 'Talen Horton-Tucker', 'UTA-Jazz', 29,
                 2, 6.04, 234, 10.7, 3.2, 3.8, 0.6, 0.4, 0.419, 0.286, 2019, 10260000)
    insertPlayer(connection, 289, 'Nickeil Alexander-Walker', 'UTA-Jazz',
                 29, 2, 6.06, 205, 6.3, 1.6, 2.1, 0.7, 0.4, 0.488, 0.402, 2019, 5009633)
    insertPlayer(connection, 290, 'Rudy Gay', 'UTA-Jazz', 29, 4,
                 6.08, 250, 5.2, 2.9, 1.0, 0.3, 0.3, 0.38, 0.254, 2006, 6184500)
    insertPlayer(connection, 291, 'Kyle Kuzma', 'WAS-Wizards', 30, 4,
                 6.09, 221, 21.2, 7.2, 3.7, 0.6, 0.5, 0.448, 0.333, 2017, 13000000)
    insertPlayer(connection, 292, 'Bradley Beal', 'WAS-Wizards', 30, 2,
                 6.04, 207, 23.2, 3.9, 5.4, 0.9, 0.7, 0.506, 0.365, 2012, 43279250)
    insertPlayer(connection, 293, 'Kristaps Porzingis', 'WAS-Wizards', 30,
                 5, 7.03, 200, 23.2, 8.4, 2.7, 0.9, 1.5, 0.498, 0.385, 2016, 33833400)
    insertPlayer(connection, 294, 'Corey Kispert', 'WAS-Wizards', 30, 3,
                 6.07, 220, 11.1, 2.8, 1.2, 0.4, 0.1, 0.497, 0.424, 2021, 3552840)
    insertPlayer(connection, 295, 'Monte Morris', 'WAS-Wizards', 30, 1,
                 6.02, 183, 10.3, 3.4, 5.3, 0.7, 0.2, 0.48, 0.382, 2017, 9125000)
    insertPlayer(connection, 296, 'Deni Avdija', 'WAS-Wizards', 30, 3,
                 6.09, 210, 9.2, 6.4, 2.8, 0.9, 0.4, 0.437, 0.297, 2020, 4916160)
    insertPlayer(connection, 297, 'Delon Wright', 'WAS-Wizards', 30, 1,
                 6.05, 185, 7.4, 3.6, 3.9, 1.8, 0.3, 0.474, 0.345, 2015, 7804878)
    insertPlayer(connection, 298, 'Daniel Gafford', 'WAS-Wizards', 30,
                 5, 6.1, 234, 9.0, 5.6, 1.1, 0.4, 1.3, 0.732, 0.0, 2019, 1930681)
    insertPlayer(connection, 299, 'Will Barton', 'WAS-Wizards', 30, 2,
                 6.06, 181, 7.7, 2.8, 2.4, 0.4, 0.3, 0.386, 0.377, 2012, 14375000)
    insertPlayer(connection, 300, 'Jordan Goodwin', 'WAS-Wizards', 30,
                 1, 6.03, 200, 6.6, 3.3, 2.7, 0.9, 0.4, 0.448, 0.322, 2021, 900000)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Shots(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Shots")

    insertShots(connection, 1, 'Dejounte Murray', 8.3, 17.8, 0.464,
                1.8, 5.2, 0.344, 6.5, 12.6, 0.514, 0.514, 2.1, 2.6, 0.832)
    insertShots(connection, 2, 'Trae Young', 8.2, 19.0, 0.429, 2.1,
                6.3, 0.335, 6.1, 12.7, 0.476, 0.485, 7.8, 8.8, 0.886)
    insertShots(connection, 3, 'De''Andre Hunter', 5.7, 12.3, 0.461,
                1.5, 4.3, 0.35, 4.2, 8.0, 0.521, 0.522, 2.6, 3.1, 0.826)
    insertShots(connection, 4, 'John Collins', 5.1, 10.0, 0.508,
                1.0, 3.4, 0.292, 4.1, 6.6, 0.619, 0.557, 2.0, 2.5, 0.803)
    insertShots(connection, 5, 'Bogdan Bogdanovic', 5.1, 11.3, 0.447,
                2.7, 6.7, 0.406, 2.4, 4.6, 0.506, 0.566, 1.2, 1.4, 0.831)
    insertShots(connection, 6, 'Clint Capela', 5.4, 8.2, 0.653, 0.0,
                0.0, 0.0, 5.4, 8.2, 0.654, 0.653, 1.2, 2.0, 0.603)
    insertShots(connection, 7, 'Saddiq Bey', 4.3, 9.2, 0.47, 2.0,
                5.0, 0.4, 2.3, 4.2, 0.552, 0.578, 1.0, 1.2, 0.862)
    insertShots(connection, 8, 'Onyeka Okongwu', 4.0, 6.2, 0.638,
                0.1, 0.2, 0.308, 3.9, 6.1, 0.647, 0.642, 1.9, 2.5, 0.781)
    insertShots(connection, 9, 'AJ Griffin', 3.4, 7.4, 0.465, 1.4,
                3.6, 0.39, 2.0, 3.8, 0.536, 0.56, 0.6, 0.7, 0.894)
    insertShots(connection, 10, 'Jalen Johnson', 2.3, 4.6, 0.491,
                0.4, 1.5, 0.288, 1.8, 3.1, 0.587, 0.537, 0.7, 1.1, 0.628)
    insertShots(connection, 11, 'Jayson Tatum', 9.8, 21.1, 0.466,
                3.2, 9.3, 0.35, 6.6, 11.8, 0.558, 0.543, 7.2, 8.4, 0.854)
    insertShots(connection, 12, 'Jaylen Brown', 10.1, 20.6, 0.491,
                2.4, 7.3, 0.335, 7.7, 13.4, 0.576, 0.55, 3.9, 5.1, 0.765)
    insertShots(connection, 13, 'Marcus Smart', 4.1, 9.9, 0.415,
                1.9, 5.6, 0.336, 2.2, 4.3, 0.519, 0.511, 1.4, 1.9, 0.746)
    insertShots(connection, 14, 'Al Horford', 3.6, 7.6, 0.476, 2.3,
                5.2, 0.446, 1.3, 2.4, 0.539, 0.627, 0.2, 0.3, 0.714)
    insertShots(connection, 15, 'Derrick White', 4.3, 9.2, 0.462,
                1.8, 4.8, 0.381, 2.5, 4.5, 0.548, 0.56, 2.0, 2.3, 0.875)
    insertShots(connection, 16, 'Malcolm Brogdon', 5.3, 10.9, 0.484,
                2.0, 4.4, 0.444, 3.3, 6.5, 0.51, 0.574, 2.4, 2.7, 0.87)
    insertShots(connection, 17, 'Grant Williams', 2.7, 6.0, 0.454,
                1.5, 3.7, 0.395, 1.3, 2.3, 0.546, 0.575, 1.2, 1.5, 0.77)
    insertShots(connection, 18, 'Robert Williams', 3.6, 4.9, 0.747,
                0.0, 0.0, 0.0, 3.6, 4.8, 0.751, 0.747, 0.7, 1.2, 0.61)
    insertShots(connection, 19, 'Mike Muscala', 2.1, 4.5, 0.472,
                1.3, 3.3, 0.385, 0.9, 1.2, 0.708, 0.612, 0.5, 0.7, 0.692)
    insertShots(connection, 20, 'Sam Hauser', 2.3, 5.0, 0.455, 1.8,
                4.2, 0.418, 0.5, 0.8, 0.656, 0.631, 0.2, 0.2, 0.706)
    insertShots(connection, 21, 'Royce O''Neale', 3.0, 7.8, 0.386,
                2.1, 5.5, 0.389, 0.9, 2.3, 0.379, 0.524, 0.7, 0.9, 0.725)
    insertShots(connection, 22, 'Nic Claxton', 5.4, 7.7, 0.705, 0.0,
                0.0, 0.0, 5.4, 7.7, 0.708, 0.705, 1.8, 3.2, 0.541)
    insertShots(connection, 23, 'Joe Harris', 2.7, 5.9, 0.457, 1.9,
                4.5, 0.426, 0.8, 1.4, 0.551, 0.618, 0.2, 0.4, 0.643)
    insertShots(connection, 24, 'Seth Curry', 3.4, 7.4, 0.463, 1.5,
                3.8, 0.405, 1.9, 3.6, 0.525, 0.568, 0.8, 0.9, 0.927)
    insertShots(connection, 25, 'Cam Thomas', 3.5, 8.0, 0.441, 0.9,
                2.3, 0.383, 2.6, 5.7, 0.464, 0.497, 2.6, 3.1, 0.868)
    insertShots(connection, 26, 'Ben Simmons', 3.2, 5.6, 0.566, 0.0,
                0.0, 0.0, 3.2, 5.5, 0.571, 0.566, 0.6, 1.4, 0.439)
    insertShots(connection, 27, 'Mikal Bridges', 8.9, 18.6, 0.475,
                2.5, 6.7, 0.376, 6.3, 11.9, 0.531, 0.543, 5.9, 6.6, 0.894)
    insertShots(connection, 28, 'Spencer Dinwiddie', 5.5, 13.7, 0.404,
                1.7, 5.7, 0.289, 3.9, 8.0, 0.488, 0.465, 3.8, 4.7, 0.797)
    insertShots(connection, 29, 'Dorian Finney-Smith', 2.6, 7.3, 0.351,
                1.4, 4.7, 0.306, 1.2, 2.7, 0.429, 0.448, 0.6, 0.7, 0.789)
    insertShots(connection, 30, 'Cameron Johnson', 5.6, 12.0, 0.468,
                2.3, 6.2, 0.372, 3.3, 5.8, 0.572, 0.565, 3.0, 3.5, 0.851)
    insertShots(connection, 31, 'Terry Rozier', 7.8, 18.9, 0.415,
                2.6, 8.0, 0.327, 5.2, 10.8, 0.48, 0.484, 2.8, 3.5, 0.809)
    insertShots(connection, 32, 'LaMelo Ball', 8.2, 20.0, 0.411,
                4.0, 10.6, 0.376, 4.2, 9.4, 0.45, 0.51, 2.8, 3.4, 0.836)
    insertShots(connection, 33, 'P.J. Washington', 5.9, 13.4, 0.444,
                2.0, 5.9, 0.348, 3.9, 7.5, 0.518, 0.52, 1.7, 2.4, 0.73)
    insertShots(connection, 34, 'Kelly Oubre Jr.', 7.4, 17.1, 0.431,
                2.3, 7.1, 0.319, 5.1, 10.0, 0.51, 0.497, 3.3, 4.3, 0.76)
    insertShots(connection, 35, 'Gordon Hayward', 5.5, 11.6, 0.475,
                1.0, 3.2, 0.325, 4.5, 8.4, 0.532, 0.52, 2.6, 3.2, 0.811)
    insertShots(connection, 36, 'Dennis Smith Jr.', 3.4, 8.4, 0.412,
                0.4, 2.1, 0.216, 3.0, 6.3, 0.475, 0.438, 1.4, 2.0, 0.736)
    insertShots(connection, 37, 'Mark Williams', 3.7, 5.8, 0.637,
                0.0, 0.0, '', 3.7, 5.8, 0.637, 0.637, 1.6, 2.3, 0.691)
    insertShots(connection, 38, 'Cody Martin', 2.0, 5.1, 0.389, 0.4,
                2.0, 0.214, 1.6, 3.1, 0.5, 0.431, 0.6, 1.0, 0.571)
    insertShots(connection, 39, 'Nick Richards', 3.0, 4.8, 0.629,
                0.0, 0.0, 1.0, 3.0, 4.8, 0.628, 0.631, 2.1, 2.8, 0.749)
    insertShots(connection, 40, 'JT Thor', 1.4, 3.4, 0.399, 0.6,
                1.8, 0.317, 0.8, 1.7, 0.487, 0.481, 0.5, 0.7, 0.702)
    insertShots(connection, 41, 'DeMar DeRozan', 8.9, 17.6, 0.504,
                0.6, 1.9, 0.324, 8.3, 15.7, 0.526, 0.522, 6.2, 7.1, 0.872)
    insertShots(connection, 42, 'Zach LaVine', 8.7, 18.0, 0.485, 2.6,
                7.1, 0.375, 6.1, 11.0, 0.556, 0.558, 4.7, 5.6, 0.848)
    insertShots(connection, 43, 'Nikola Vucevic', 7.3, 14.0, 0.52,
                1.5, 4.2, 0.349, 5.8, 9.8, 0.594, 0.573, 1.6, 1.9, 0.835)
    insertShots(connection, 44, 'Patrick Williams', 3.8, 8.3, 0.464,
                1.4, 3.4, 0.415, 2.4, 4.9, 0.498, 0.549, 1.1, 1.3, 0.857)
    insertShots(connection, 45, 'Ayo Dosunmu', 3.5, 7.1, 0.493, 0.7,
                2.4, 0.312, 2.8, 4.8, 0.583, 0.545, 0.8, 1.0, 0.805)
    insertShots(connection, 46, 'Alex Caruso', 1.9, 4.3, 0.455, 0.8,
                2.3, 0.364, 1.1, 2.0, 0.556, 0.551, 0.9, 1.1, 0.808)
    insertShots(connection, 47, 'Coby White', 3.6, 8.0, 0.443, 1.7,
                4.6, 0.372, 1.8, 3.4, 0.54, 0.551, 0.8, 0.9, 0.871)
    insertShots(connection, 48, 'Goran Dragic', 2.5, 5.9, 0.425,
                0.9, 2.5, 0.352, 1.6, 3.4, 0.48, 0.5, 0.5, 0.8, 0.659)
    insertShots(connection, 49, 'Javonte Green', 1.9, 3.4, 0.565,
                0.4, 1.1, 0.371, 1.5, 2.3, 0.658, 0.625, 0.9, 1.4, 0.667)
    insertShots(connection, 50, 'Derrick Jones Jr.', 1.8, 3.6, 0.5,
                0.4, 1.3, 0.338, 1.4, 2.3, 0.587, 0.559, 1.0, 1.3, 0.738)
    insertShots(connection, 51, 'Donovan Mitchell', 10.0, 20.6, 0.484,
                3.6, 9.3, 0.386, 6.4, 11.3, 0.566, 0.572, 4.7, 5.4, 0.867)
    insertShots(connection, 52, 'Darius Garland', 7.6, 16.4, 0.462,
                2.4, 6.0, 0.41, 5.1, 10.4, 0.492, 0.537, 4.0, 4.7, 0.863)
    insertShots(connection, 53, 'Evan Mobley', 6.6, 12.0, 0.554, 0.3,
                1.3, 0.216, 6.4, 10.7, 0.595, 0.566, 2.6, 3.8, 0.674)
    insertShots(connection, 54, 'Jarrett Allen', 5.9, 9.2, 0.644,
                0.0, 0.1, 0.1, 5.9, 9.1, 0.653, 0.645, 2.4, 3.3, 0.733)
    insertShots(connection, 55, 'Caris LeVert', 4.3, 10.0, 0.431,
                1.7, 4.4, 0.392, 2.6, 5.6, 0.462, 0.517, 1.8, 2.4, 0.722)
    insertShots(connection, 56, 'Isaac Okoro', 2.3, 4.7, 0.494, 0.8,
                2.3, 0.363, 1.5, 2.4, 0.617, 0.582, 1.0, 1.4, 0.757)
    insertShots(connection, 57, 'Dean Wade', 1.7, 4.0, 0.412, 1.0,
                2.9, 0.354, 0.6, 1.1, 0.56, 0.54, 0.3, 0.5, 0.652)
    insertShots(connection, 58, 'Cedi Osman', 3.1, 6.9, 0.451, 1.5,
                4.1, 0.372, 1.6, 2.8, 0.564, 0.56, 1.0, 1.4, 0.694)
    insertShots(connection, 59, 'Lamar Stevens', 2.1, 4.6, 0.448,
                0.5, 1.5, 0.316, 1.6, 3.1, 0.513, 0.5, 0.6, 0.9, 0.702)
    insertShots(connection, 60, 'Ricky Rubio', 1.8, 5.4, 0.343, 0.6,
                2.5, 0.256, 1.2, 2.9, 0.417, 0.402, 0.8, 1.1, 0.8)
    insertShots(connection, 61, 'Kyrie Irving', 9.8, 19.2, 0.51, 2.9,
                7.4, 0.392, 6.9, 11.8, 0.585, 0.586, 4.5, 4.7, 0.947)
    insertShots(connection, 62, 'Luka Doncic', 10.9, 22.0, 0.496,
                2.8, 8.2, 0.342, 8.1, 13.8, 0.588, 0.56, 7.8, 10.5, 0.742)
    insertShots(connection, 63, 'Reggie Bullock', 2.5, 6.0, 0.409,
                1.9, 5.1, 0.38, 0.5, 0.9, 0.562, 0.569, 0.3, 0.5, 0.703)
    insertShots(connection, 64, 'Tim Hardaway Jr.', 4.8, 11.9, 0.401,
                3.0, 7.7, 0.385, 1.8, 4.2, 0.431, 0.527, 1.8, 2.3, 0.77)
    insertShots(connection, 65, 'Christian Wood', 5.9, 11.5, 0.515,
                1.6, 4.2, 0.376, 4.3, 7.3, 0.594, 0.583, 3.2, 4.2, 0.772)
    insertShots(connection, 66, 'Josh Green', 3.4, 6.4, 0.537, 1.1,
                2.8, 0.402, 2.3, 3.6, 0.643, 0.626, 1.1, 1.6, 0.723)
    insertShots(connection, 67, 'Maxi Kleber', 2.1, 4.6, 0.456, 1.1,
                3.0, 0.348, 1.0, 1.5, 0.667, 0.571, 0.7, 1.0, 0.711)
    insertShots(connection, 68, 'Dwight Powell', 2.6, 3.5, 0.732,
                0.0, 0.1, 0.0, 2.6, 3.5, 0.746, 0.732, 1.5, 2.2, 0.667)
    insertShots(connection, 69, 'Justin Holiday', 1.6, 4.4, 0.367,
                0.9, 3.1, 0.286, 0.7, 1.3, 0.565, 0.468, 0.3, 0.4, 0.625)
    insertShots(connection, 70, 'Jaden Hardy', 3.0, 6.9, 0.438, 1.3,
                3.3, 0.404, 1.7, 3.7, 0.469, 0.533, 1.4, 1.6, 0.823)
    insertShots(connection, 71, 'Nikola Jokic', 9.4, 14.8, 0.632,
                0.8, 2.2, 0.383, 8.5, 12.7, 0.675, 0.66, 4.9, 6.0, 0.822)
    insertShots(connection, 72, 'Jamal Murray', 7.3, 16.0, 0.454,
                2.6, 6.6, 0.398, 4.6, 9.4, 0.494, 0.537, 2.8, 3.3, 0.833)
    insertShots(connection, 73, 'Kentavious Caldwell-Pope', 3.8, 8.3,
                0.462, 1.8, 4.2, 0.423, 2.1, 4.1, 0.502, 0.569, 1.4, 1.6, 0.824)
    insertShots(connection, 74, 'Aaron Gordon', 6.3, 11.2, 0.564,
                0.9, 2.5, 0.347, 5.4, 8.6, 0.628, 0.603, 2.8, 4.6, 0.608)
    insertShots(connection, 75, 'Michael Porter Jr.', 6.4, 13.2,
                0.487, 3.0, 7.3, 0.414, 3.4, 5.9, 0.579, 0.602, 1.5, 1.9, 0.8)
    insertShots(connection, 76, 'Bruce Brown', 4.5, 9.3, 0.483, 1.1,
                3.2, 0.358, 3.3, 6.1, 0.548, 0.545, 1.5, 1.9, 0.758)
    insertShots(connection, 77, 'Reggie Jackson', 3.1, 8.0, 0.383,
                1.2, 4.3, 0.279, 1.9, 3.8, 0.5, 0.457, 0.6, 0.8, 0.833)
    insertShots(connection, 78, 'Jeff Green', 2.9, 5.9, 0.488, 0.5,
                1.9, 0.288, 2.3, 4.0, 0.58, 0.534, 1.6, 2.1, 0.744)
    insertShots(connection, 79, 'Christian Braun', 1.9, 3.8, 0.495,
                0.4, 1.3, 0.354, 1.4, 2.5, 0.565, 0.554, 0.5, 0.8, 0.625)
    insertShots(connection, 80, 'DeAndre Jordan', 2.3, 2.9, 0.765,
                0.0, 0.0, 1.0, 2.2, 2.9, 0.763, 0.77, 0.6, 1.2, 0.458)
    insertShots(connection, 81, 'Cade Cunningham', 7.8, 18.7, 0.415,
                1.4, 5.1, 0.279, 6.3, 13.6, 0.466, 0.453, 3.0, 3.6, 0.837)
    insertShots(connection, 82, 'Bojan Bogdanovic', 7.3, 14.9, 0.488,
                2.5, 6.0, 0.411, 4.8, 9.0, 0.539, 0.57, 4.5, 5.1, 0.884)
    insertShots(connection, 83, 'Jaden Ivey', 5.5, 13.3, 0.416, 1.6,
                4.7, 0.343, 3.9, 8.6, 0.457, 0.477, 3.6, 4.8, 0.747)
    insertShots(connection, 84, 'Isaiah Stewart', 3.9, 8.8, 0.442,
                1.3, 4.1, 0.327, 2.6, 4.7, 0.542, 0.518, 2.2, 3.0, 0.738)
    insertShots(connection, 85, 'Killian Hayes', 4.0, 10.7, 0.377,
                1.1, 3.8, 0.28, 3.0, 7.0, 0.429, 0.426, 1.2, 1.5, 0.821)
    insertShots(connection, 86, 'James Wiseman', 5.4, 10.2, 0.531,
                0.1, 0.8, 0.167, 5.3, 9.5, 0.559, 0.537, 1.8, 2.5, 0.712)
    insertShots(connection, 87, 'Jalen Duren', 3.9, 5.9, 0.648, 0.0,
                0.0, 0.0, 3.9, 5.9, 0.652, 0.648, 1.4, 2.3, 0.611)
    insertShots(connection, 88, 'Marvin Bagley III', 4.8, 9.1, 0.529,
                0.5, 1.6, 0.288, 4.4, 7.5, 0.579, 0.554, 1.9, 2.6, 0.75)
    insertShots(connection, 89, 'Alec Burks', 3.9, 9.0, 0.436, 1.9,
                4.7, 0.414, 2.0, 4.3, 0.459, 0.544, 3.0, 3.7, 0.814)
    insertShots(connection, 90, 'Cory Joseph', 2.4, 5.7, 0.427, 1.1,
                2.9, 0.389, 1.3, 2.8, 0.468, 0.527, 0.9, 1.2, 0.792)
    insertShots(connection, 91, 'Stephen Curry', 10.0, 20.2, 0.493,
                4.9, 11.4, 0.427, 5.1, 8.8, 0.579, 0.614, 4.6, 5.0, 0.915)
    insertShots(connection, 92, 'Klay Thompson', 7.9, 18.1, 0.436,
                4.4, 10.6, 0.412, 3.6, 7.6, 0.47, 0.556, 1.7, 1.9, 0.879)
    insertShots(connection, 93, 'Andrew Wiggins', 6.8, 14.3, 0.473,
                2.4, 6.1, 0.396, 4.4, 8.2, 0.53, 0.557, 1.2, 1.9, 0.611)
    insertShots(connection, 94, 'Draymond Green', 3.4, 6.5, 0.527,
                0.5, 1.8, 0.305, 2.9, 4.7, 0.612, 0.57, 1.1, 1.5, 0.713)
    insertShots(connection, 95, 'Jordan Poole', 6.7, 15.6, 0.43,
                2.6, 7.8, 0.336, 4.1, 7.8, 0.524, 0.514, 4.4, 5.1, 0.87)
    insertShots(connection, 96, 'Donte DiVincenzo', 3.3, 7.5, 0.435,
                2.1, 5.3, 0.397, 1.2, 2.3, 0.525, 0.574, 0.8, 1.0, 0.817)
    insertShots(connection, 97, 'Kevon Looney', 3.0, 4.7, 0.63,
                0.0, 0.0, 0.0, 3.0, 4.7, 0.632, 0.63, 1.1, 1.9, 0.606)
    insertShots(connection, 98, 'Jonathan Kuminga', 3.9, 7.4, 0.525,
                0.8, 2.2, 0.37, 3.1, 5.2, 0.59, 0.579, 1.3, 2.1, 0.652)
    insertShots(connection, 99, 'Anthony Lamb', 2.4, 5.1, 0.471,
                1.2, 3.2, 0.367, 1.2, 1.9, 0.652, 0.588, 0.7, 1.0, 0.767)
    insertShots(connection, 100, 'Ty Jerome', 2.6, 5.4, 0.488, 0.8,
                2.0, 0.389, 1.8, 3.4, 0.546, 0.56, 0.8, 0.9, 0.927)
    insertShots(connection, 101, 'Kevin Porter Jr.', 6.6, 15.0, 0.442,
                2.4, 6.5, 0.366, 4.2, 8.5, 0.501, 0.522, 3.5, 4.5, 0.784)
    insertShots(connection, 102, 'Jalen Green', 7.4, 17.9, 0.416,
                2.5, 7.3, 0.338, 5.0, 10.6, 0.471, 0.485, 4.8, 6.1, 0.786)
    insertShots(connection, 103, 'Jabari Smith Jr.', 4.6, 11.3, 0.408,
                1.5, 4.9, 0.307, 3.1, 6.3, 0.487, 0.475, 2.1, 2.6, 0.786)
    insertShots(connection, 104, 'Alperen Seng�n', 5.9, 10.7, 0.553,
                0.3, 0.8, 0.333, 5.6, 9.9, 0.57, 0.565, 2.7, 3.8, 0.715)
    insertShots(connection, 105, 'KJ Martin', 5.0, 8.8, 0.569, 0.8,
                2.6, 0.315, 4.2, 6.1, 0.679, 0.617, 1.8, 2.7, 0.68)
    insertShots(connection, 106, 'Jae''Sean Tate', 3.5, 7.4, 0.48,
                0.4, 1.5, 0.283, 3.1, 5.9, 0.53, 0.509, 1.6, 2.2, 0.725)
    insertShots(connection, 107, 'Tari Eason', 3.6, 8.0, 0.448, 0.7,
                2.1, 0.343, 2.9, 6.0, 0.486, 0.493, 1.3, 1.8, 0.752)
    insertShots(connection, 108, 'Daishen Nix', 1.4, 4.2, 0.342,
                0.7, 2.5, 0.286, 0.7, 1.7, 0.423, 0.426, 0.4, 0.6, 0.667)
    insertShots(connection, 109, 'TyTy Washington Jr.', 1.9, 5.2,
                0.363, 0.6, 2.6, 0.238, 1.3, 2.6, 0.488, 0.422, 0.3, 0.6, 0.556)
    insertShots(connection, 110, 'Garrison Mathews', 1.3, 3.8, 0.353,
                1.2, 3.4, 0.342, 0.2, 0.3, 0.467, 0.509, 0.9, 1.0, 0.911)
    insertShots(connection, 111, 'Tyrese Haliburton', 7.4, 15.0,
                0.49, 2.9, 7.2, 0.4, 4.5, 7.8, 0.572, 0.586, 3.1, 3.6, 0.871)
    insertShots(connection, 112, 'Buddy Hield', 5.9, 13.0, 0.458,
                3.6, 8.5, 0.425, 2.3, 4.5, 0.518, 0.596, 1.3, 1.6, 0.822)
    insertShots(connection, 113, 'Myles Turner', 6.5, 11.8, 0.548,
                1.5, 4.0, 0.373, 5.0, 7.8, 0.638, 0.612, 3.5, 4.5, 0.783)
    insertShots(connection, 114, 'Bennedict Mathurin', 5.3, 12.2,
                0.434, 1.3, 4.0, 0.323, 4.0, 8.2, 0.488, 0.487, 4.8, 5.8, 0.828)
    insertShots(connection, 115, 'Andrew Nembhard', 3.8, 8.6, 0.441,
                1.2, 3.5, 0.35, 2.6, 5.1, 0.504, 0.512, 0.7, 0.8, 0.79)
    insertShots(connection, 116, 'Aaron Nesmith', 3.5, 8.1, 0.427,
                1.6, 4.3, 0.366, 1.9, 3.8, 0.496, 0.525, 1.6, 1.9, 0.838)
    insertShots(connection, 117, 'Jordan Nwora', 4.9, 10.3, 0.476,
                1.9, 4.5, 0.422, 3.0, 5.8, 0.518, 0.569, 1.3, 1.8, 0.721)
    insertShots(connection, 118, 'T.J. McConnell', 3.8, 6.9, 0.543,
                0.3, 0.8, 0.441, 3.4, 6.2, 0.556, 0.568, 0.8, 0.9, 0.853)
    insertShots(connection, 119, 'Chris Duarte', 2.7, 7.2, 0.369,
                1.2, 3.8, 0.316, 1.5, 3.5, 0.428, 0.452, 1.3, 1.6, 0.847)
    insertShots(connection, 120, 'Jalen Smith', 3.6, 7.5, 0.476,
                0.8, 2.8, 0.283, 2.8, 4.7, 0.593, 0.53, 1.5, 2.0, 0.759)
    insertShots(connection, 121, 'Paul George', 8.2, 17.9, 0.457,
                2.8, 7.6, 0.371, 5.4, 10.3, 0.521, 0.536, 4.6, 5.3, 0.871)
    insertShots(connection, 122, 'Kawhi Leonard', 8.6, 16.8, 0.512,
                2.0, 4.8, 0.416, 6.6, 11.9, 0.551, 0.572, 4.7, 5.4, 0.871)
    insertShots(connection, 123, 'Russell Westbrook', 6.1, 12.5,
                0.489, 1.2, 3.5, 0.356, 4.9, 9.0, 0.54, 0.538, 2.4, 3.6, 0.658)
    insertShots(connection, 124, 'Ivica Zubac', 4.3, 6.8, 0.634,
                0.0, 0.0, 0.0, 4.3, 6.7, 0.637, 0.634, 2.2, 3.1, 0.697)
    insertShots(connection, 125, 'Marcus Morris', 4.2, 9.9, 0.426,
                1.7, 4.7, 0.364, 2.5, 5.2, 0.484, 0.513, 1.0, 1.3, 0.782)
    insertShots(connection, 126, 'Norman Powell', 5.7, 11.8, 0.479,
                1.9, 4.8, 0.397, 3.8, 7.1, 0.534, 0.559, 3.8, 4.6, 0.812)
    insertShots(connection, 127, 'Eric Gordon', 3.7, 8.0, 0.463,
                2.1, 5.0, 0.423, 1.5, 2.9, 0.531, 0.597, 1.5, 1.7, 0.842)
    insertShots(connection, 128, 'Terance Mann', 3.4, 6.5, 0.519,
                1.0, 2.4, 0.389, 2.4, 4.0, 0.598, 0.593, 1.1, 1.5, 0.78)
    insertShots(connection, 129, 'Nicolas Batum', 2.1, 4.9, 0.42,
                1.6, 4.1, 0.391, 0.5, 0.8, 0.563, 0.583, 0.4, 0.6, 0.708)
    insertShots(connection, 130, 'Mason Plumlee', 2.8, 3.8, 0.727,
                0.0, 0.0, 0.0, 2.8, 3.8, 0.727, 0.727, 1.9, 2.5, 0.772)
    insertShots(connection, 131, 'LeBron James', 11.1, 22.2, 0.5,
                2.2, 6.9, 0.321, 8.9, 15.3, 0.58, 0.549, 4.6, 5.9, 0.768)
    insertShots(connection, 132, 'Anthony Davis', 9.7, 17.2, 0.563,
                0.3, 1.3, 0.257, 9.3, 15.9, 0.589, 0.573, 6.2, 7.9, 0.784)
    insertShots(connection, 133, 'D''Angelo Russell', 6.3, 13.0, 0.484,
                2.7, 6.5, 0.414, 3.6, 6.5, 0.555, 0.588, 2.1, 2.9, 0.735)
    insertShots(connection, 134, 'Dennis Schr�der', 4.1, 9.8, 0.415,
                1.1, 3.4, 0.329, 3.0, 6.4, 0.461, 0.472, 3.3, 3.8, 0.857)
    insertShots(connection, 135, 'Austin Reaves', 4.0, 7.7, 0.529,
                1.3, 3.4, 0.398, 2.7, 4.3, 0.631, 0.616, 3.6, 4.1, 0.864)
    insertShots(connection, 136, 'Troy Brown Jr.', 2.6, 6.1, 0.43,
                1.4, 3.7, 0.381, 1.2, 2.4, 0.505, 0.545, 0.4, 0.5, 0.872)
    insertShots(connection, 137, 'Jarred Vanderbilt', 2.8, 5.4, 0.529,
                0.4, 1.3, 0.303, 2.5, 4.1, 0.598, 0.564, 1.1, 1.4, 0.784)
    insertShots(connection, 138, 'Malik Beasley', 4.0, 10.3, 0.392,
                2.5, 7.2, 0.353, 1.5, 3.1, 0.481, 0.515, 0.5, 0.8, 0.619)
    insertShots(connection, 139, 'Lonnie Walker IV', 4.2, 9.4, 0.448,
                1.6, 4.4, 0.365, 2.6, 5.0, 0.522, 0.534, 1.6, 1.9, 0.858)
    insertShots(connection, 140, 'Rui Hachimura', 3.8, 7.9, 0.485,
                0.6, 2.2, 0.296, 3.2, 5.7, 0.556, 0.525, 1.3, 1.8, 0.721)
    insertShots(connection, 141, 'Ja Morant', 9.3, 19.9, 0.466, 1.5,
                4.9, 0.307, 7.8, 15.0, 0.519, 0.504, 6.1, 8.1, 0.748)
    insertShots(connection, 142, 'Desmond Bane', 7.8, 16.2, 0.479,
                2.9, 7.0, 0.408, 4.9, 9.2, 0.534, 0.568, 3.1, 3.5, 0.883)
    insertShots(connection, 143, 'Dillon Brooks', 5.4, 13.6, 0.396,
                2.0, 6.0, 0.326, 3.4, 7.6, 0.451, 0.468, 1.6, 2.1, 0.779)
    insertShots(connection, 144, 'Jaren Jackson Jr.', 6.6, 13.0, 0.506,
                1.6, 4.5, 0.355, 5.0, 8.6, 0.585, 0.567, 3.8, 4.9, 0.788)
    insertShots(connection, 145, 'Steven Adams', 3.7, 6.3, 0.597,
                0.0, 0.0, 0.0, 3.7, 6.2, 0.599, 0.597, 1.1, 3.1, 0.364)
    insertShots(connection, 146, 'Luke Kennard', 3.8, 7.1, 0.526,
                3.1, 5.7, 0.54, 0.7, 1.4, 0.471, 0.743, 0.8, 0.8, 0.947)
    insertShots(connection, 147, 'Tyus Jones', 3.9, 8.9, 0.438, 1.5,
                4.1, 0.371, 2.4, 4.8, 0.495, 0.523, 1.0, 1.3, 0.8)
    insertShots(connection, 148, 'Santi Aldama', 3.2, 6.8, 0.47,
                1.2, 3.5, 0.353, 2.0, 3.4, 0.591, 0.56, 1.4, 1.9, 0.75)
    insertShots(connection, 149, 'John Konchar', 1.9, 4.4, 0.431,
                0.8, 2.5, 0.339, 1.1, 2.0, 0.545, 0.525, 0.4, 0.5, 0.778)
    insertShots(connection, 150, 'Brandon Clarke', 4.1, 6.2, 0.656,
                0.0, 0.1, 0.167, 4.1, 6.1, 0.665, 0.658, 1.8, 2.4, 0.723)
    insertShots(connection, 151, 'Tyler Herro', 7.3, 16.6, 0.439,
                3.0, 8.0, 0.378, 4.2, 8.5, 0.497, 0.531, 2.5, 2.7, 0.934)
    insertShots(connection, 152, 'Bam Adebayo', 8.0, 14.9, 0.54, 0.0,
                0.2, 0.083, 8.0, 14.7, 0.545, 0.541, 4.3, 5.4, 0.806)
    insertShots(connection, 153, 'Jimmy Butler', 7.5, 13.9, 0.539,
                0.6, 1.6, 0.35, 6.9, 12.3, 0.564, 0.56, 7.4, 8.7, 0.85)
    insertShots(connection, 154, 'Kyle Lowry', 3.6, 8.8, 0.404, 1.9,
                5.6, 0.345, 1.6, 3.2, 0.509, 0.514, 2.1, 2.5, 0.859)
    insertShots(connection, 155, 'Caleb Martin', 3.6, 7.7, 0.464,
                1.2, 3.3, 0.356, 2.4, 4.4, 0.545, 0.54, 1.3, 1.6, 0.805)
    insertShots(connection, 156, 'Max Strus', 4.1, 9.9, 0.41, 2.5,
                7.0, 0.35, 1.6, 2.8, 0.559, 0.535, 1.0, 1.1, 0.876)
    insertShots(connection, 157, 'Victor Oladipo', 3.8, 9.6, 0.397,
                1.7, 5.0, 0.33, 2.1, 4.5, 0.471, 0.484, 1.4, 1.9, 0.747)
    insertShots(connection, 158, 'Gabe Vincent', 3.4, 8.3, 0.402,
                1.7, 5.1, 0.334, 1.6, 3.2, 0.512, 0.505, 1.0, 1.1, 0.872)
    insertShots(connection, 159, 'Kevin Love', 2.6, 6.6, 0.388, 1.4,
                4.8, 0.297, 1.1, 1.8, 0.632, 0.496, 1.1, 1.3, 0.857)
    insertShots(connection, 160, 'Haywood Highsmith', 1.7, 4.0, 0.431,
                0.7, 2.0, 0.339, 1.0, 2.0, 0.523, 0.516, 0.2, 0.5, 0.464)
    insertShots(connection, 161, 'Jrue Holiday', 7.3, 15.3, 0.479,
                2.4, 6.1, 0.384, 5.0, 9.1, 0.542, 0.556, 2.3, 2.6, 0.859)
    insertShots(connection, 162, 'Giannis Antetokounmpo', 11.2, 20.3,
                0.553, 0.7, 2.7, 0.275, 10.5, 17.6, 0.596, 0.572, 7.9, 12.3, 0.645)
    insertShots(connection, 163, 'Brook Lopez', 6.1, 11.5, 0.531,
                1.7, 4.7, 0.374, 4.4, 6.9, 0.637, 0.606, 1.9, 2.4, 0.784)
    insertShots(connection, 164, 'Grayson Allen', 3.4, 7.7, 0.44,
                2.0, 5.1, 0.399, 1.4, 2.7, 0.518, 0.571, 1.6, 1.8, 0.905)
    insertShots(connection, 165, 'Bobby Portis', 5.7, 11.5, 0.496,
                1.4, 3.7, 0.37, 4.3, 7.8, 0.555, 0.555, 1.4, 1.8, 0.768)
    insertShots(connection, 166, 'Khris Middleton', 5.4, 12.3, 0.436,
                1.5, 4.9, 0.315, 3.8, 7.4, 0.516, 0.499, 2.8, 3.1, 0.902)
    insertShots(connection, 167, 'Pat Connaughton', 2.7, 6.9, 0.392,
                1.8, 5.3, 0.339, 0.9, 1.6, 0.566, 0.521, 0.4, 0.7, 0.659)
    insertShots(connection, 168, 'Joe Ingles', 2.3, 5.4, 0.435, 1.8,
                4.4, 0.409, 0.5, 1.0, 0.556, 0.603, 0.4, 0.5, 0.857)
    insertShots(connection, 169, 'Jevon Carter', 3.0, 7.0, 0.423,
                1.8, 4.2, 0.421, 1.2, 2.8, 0.425, 0.549, 0.4, 0.5, 0.816)
    insertShots(connection, 170, 'Jae Crowder', 2.5, 5.2, 0.479,
                1.3, 3.1, 0.436, 1.2, 2.2, 0.538, 0.606, 0.6, 0.7, 0.833)
    insertShots(connection, 171, 'Anthony Edwards', 8.9, 19.5, 0.459,
                2.7, 7.3, 0.369, 6.3, 12.2, 0.513, 0.528, 4.0, 5.3, 0.756)
    insertShots(connection, 172, 'Karl-Anthony Towns', 7.3, 14.8,
                0.495, 2.1, 5.7, 0.366, 5.2, 9.1, 0.576, 0.565, 4.1, 4.7, 0.874)
    insertShots(connection, 173, 'Mike Conley', 4.5, 9.8, 0.46, 2.4,
                5.8, 0.42, 2.1, 4.0, 0.515, 0.583, 2.6, 3.0, 0.863)
    insertShots(connection, 174, 'Rudy Gobert', 5.1, 7.8, 0.659,
                0.0, 0.0, 0.0, 5.1, 7.8, 0.663, 0.659, 3.1, 4.9, 0.644)
    insertShots(connection, 175, 'Jaden McDaniels', 4.7, 9.1, 0.517,
                1.4, 3.4, 0.398, 3.3, 5.7, 0.588, 0.591, 1.3, 1.8, 0.736)
    insertShots(connection, 176, 'Kyle Anderson', 3.7, 7.2, 0.509,
                0.6, 1.5, 0.41, 3.0, 5.7, 0.536, 0.553, 1.4, 2.0, 0.735)
    insertShots(connection, 177, 'Taurean Prince', 3.3, 7.0, 0.467,
                1.4, 3.6, 0.381, 1.9, 3.4, 0.557, 0.565, 1.2, 1.4, 0.844)
    insertShots(connection, 178, 'Austin Rivers', 1.8, 4.0, 0.435,
                0.8, 2.4, 0.35, 0.9, 1.7, 0.558, 0.538, 0.6, 0.8, 0.769)
    insertShots(connection, 179, 'Jaylen Nowell', 4.3, 9.6, 0.448,
                1.0, 3.6, 0.289, 3.3, 6.0, 0.542, 0.502, 1.2, 1.5, 0.778)
    insertShots(connection, 180, 'Naz Reid', 4.6, 8.5, 0.537, 1.1,
                3.2, 0.346, 3.5, 5.3, 0.653, 0.602, 1.3, 1.9, 0.677)
    insertShots(connection, 181, 'CJ McCollum', 7.8, 17.9, 0.437,
                2.8, 7.2, 0.389, 5.0, 10.7, 0.469, 0.515, 2.4, 3.2, 0.769)
    insertShots(connection, 182, 'Brandon Ingram', 9.0, 18.6, 0.484,
                1.4, 3.6, 0.39, 7.6, 14.9, 0.507, 0.522, 5.3, 6.0, 0.882)
    insertShots(connection, 183, 'Zion Williamson', 9.8, 16.2, 0.608,
                0.2, 0.7, 0.368, 9.6, 15.5, 0.618, 0.615, 6.1, 8.6, 0.714)
    insertShots(connection, 184, 'Trey Murphy III', 4.9, 10.1, 0.484,
                2.6, 6.3, 0.406, 2.3, 3.8, 0.611, 0.61, 2.2, 2.4, 0.905)
    insertShots(connection, 185, 'Herbert Jones', 3.6, 7.6, 0.469,
                0.8, 2.5, 0.335, 2.7, 5.1, 0.536, 0.525, 1.9, 2.4, 0.764)
    insertShots(connection, 186, 'Jonas Valanciunas', 5.6, 10.3,
                0.547, 0.5, 1.4, 0.349, 5.2, 8.9, 0.577, 0.57, 2.3, 2.8, 0.826)
    insertShots(connection, 187, 'Naji Marshall', 3.2, 7.4, 0.433,
                0.9, 2.8, 0.303, 2.4, 4.6, 0.513, 0.49, 1.8, 2.3, 0.789)
    insertShots(connection, 188, 'Josh Richardson', 2.7, 6.4, 0.419,
                1.4, 3.7, 0.384, 1.3, 2.7, 0.468, 0.53, 0.7, 0.9, 0.762)
    insertShots(connection, 189, 'Jose Alvarado', 3.3, 8.0, 0.411,
                1.4, 4.0, 0.336, 1.9, 4.0, 0.488, 0.496, 1.1, 1.3, 0.813)
    insertShots(connection, 190, 'Larry Nance Jr.', 2.9, 4.7, 0.61,
                0.2, 0.6, 0.333, 2.6, 4.0, 0.654, 0.633, 0.8, 1.2, 0.696)
    insertShots(connection, 191, 'Julius Randle', 8.5, 18.6, 0.459,
                2.8, 8.3, 0.343, 5.7, 10.3, 0.553, 0.536, 5.2, 6.9, 0.757)
    insertShots(connection, 192, 'Jalen Brunson', 8.6, 17.6, 0.491,
                2.0, 4.7, 0.416, 6.7, 12.8, 0.519, 0.547, 4.8, 5.8, 0.829)
    insertShots(connection, 193, 'RJ Barrett', 7.0, 16.1, 0.434,
                1.7, 5.3, 0.31, 5.3, 10.8, 0.495, 0.485, 4.0, 5.4, 0.74)
    insertShots(connection, 194, 'Josh Hart', 3.7, 6.3, 0.586, 1.1,
                2.1, 0.519, 2.6, 4.2, 0.619, 0.672, 1.8, 2.3, 0.789)
    insertShots(connection, 195, 'Quentin Grimes', 4.0, 8.5, 0.468,
                2.2, 5.7, 0.386, 1.8, 2.7, 0.641, 0.599, 1.1, 1.4, 0.796)
    insertShots(connection, 196, 'Immanuel Quickley', 5.2, 11.6,
                0.448, 2.1, 5.6, 0.37, 3.1, 6.0, 0.521, 0.537, 2.5, 3.1, 0.819)
    insertShots(connection, 197, 'Mitchell Robinson', 3.2, 4.7, 0.671,
                0.0, 0.0, 0.0, 3.2, 4.7, 0.671, 0.671, 1.0, 2.1, 0.484)
    insertShots(connection, 198, 'Cam Reddish', 3.1, 6.8, 0.449,
                0.9, 2.8, 0.304, 2.2, 4.0, 0.55, 0.511, 1.5, 1.7, 0.879)
    insertShots(connection, 199, 'Isaiah Hartenstein', 2.1, 4.0, 0.535,
                0.1, 0.5, 0.216, 2.0, 3.5, 0.576, 0.547, 0.6, 0.9, 0.676)
    insertShots(connection, 200, 'Obi Toppin', 2.8, 6.3, 0.446, 1.3,
                3.7, 0.344, 1.5, 2.6, 0.593, 0.548, 0.6, 0.7, 0.809)
    insertShots(connection, 201, 'Shai Gilgeous-Alexander', 10.4, 20.3,
                0.51, 0.9, 2.5, 0.345, 9.5, 17.8, 0.533, 0.531, 9.8, 10.9, 0.905)
    insertShots(connection, 202, 'Josh Giddey', 7.1, 14.7, 0.482,
                1.0, 3.1, 0.325, 6.1, 11.6, 0.524, 0.516, 1.4, 1.9, 0.731)
    insertShots(connection, 203, 'Luguentz Dort', 4.6, 11.8, 0.388,
                1.8, 5.5, 0.33, 2.8, 6.3, 0.44, 0.466, 2.7, 3.5, 0.772)
    insertShots(connection, 204, 'Jalen Williams', 5.5, 10.6, 0.521,
                1.0, 2.7, 0.356, 4.5, 7.9, 0.579, 0.567, 2.1, 2.5, 0.812)
    insertShots(connection, 205, 'Kenrich Williams', 3.4, 6.5, 0.517,
                0.9, 2.5, 0.373, 2.4, 4.0, 0.608, 0.59, 0.3, 0.7, 0.436)
    insertShots(connection, 206, 'Aleksej Pokusevski', 3.2, 7.3,
                0.434, 1.1, 3.1, 0.365, 2.1, 4.3, 0.483, 0.51, 0.6, 1.0, 0.629)
    insertShots(connection, 207, 'Isaiah Joe', 3.1, 7.0, 0.441, 2.2,
                5.4, 0.409, 0.9, 1.6, 0.553, 0.599, 1.1, 1.4, 0.82)
    insertShots(connection, 208, 'Jeremiah Robinson-Earl', 2.6, 5.8,
                0.444, 0.9, 2.6, 0.333, 1.7, 3.2, 0.533, 0.518, 0.8, 1.0, 0.833)
    insertShots(connection, 209, 'Jaylin Williams', 2.1, 4.8, 0.436,
                0.9, 2.3, 0.407, 1.1, 2.5, 0.463, 0.534, 0.8, 1.1, 0.704)
    insertShots(connection, 210, 'Aaron Wiggins', 2.7, 5.2, 0.512,
                0.7, 1.7, 0.393, 2.0, 3.4, 0.573, 0.579, 0.8, 1.0, 0.831)
    insertShots(connection, 211, 'Paolo Banchero', 6.7, 15.6, 0.427,
                1.2, 4.0, 0.298, 5.5, 11.6, 0.471, 0.465, 5.5, 7.4, 0.738)
    insertShots(connection, 212, 'Franz Wagner', 6.8, 14.0, 0.485,
                1.6, 4.5, 0.361, 5.2, 9.5, 0.544, 0.543, 3.4, 4.0, 0.842)
    insertShots(connection, 213, 'Wendell Carter Jr.', 5.6, 10.8,
                0.525, 1.4, 3.9, 0.356, 4.2, 6.8, 0.624, 0.591, 2.5, 3.4, 0.738)
    insertShots(connection, 214, 'Markelle Fultz', 5.8, 11.3, 0.514,
                0.5, 1.5, 0.31, 5.4, 9.9, 0.544, 0.534, 1.9, 2.4, 0.783)
    insertShots(connection, 215, 'Cole Anthony', 4.6, 10.2, 0.454,
                1.3, 3.4, 0.364, 3.4, 6.7, 0.5, 0.516, 2.5, 2.8, 0.894)
    insertShots(connection, 216, 'Gary Harris', 2.9, 6.4, 0.45, 2.0,
                4.5, 0.431, 0.9, 1.9, 0.494, 0.603, 0.6, 0.6, 0.9)
    insertShots(connection, 217, 'Jalen Suggs', 3.5, 8.4, 0.419,
                1.2, 3.8, 0.327, 2.3, 4.6, 0.496, 0.493, 1.6, 2.2, 0.723)
    insertShots(connection, 218, 'Terrence Ross', 3.1, 7.1, 0.431,
                1.5, 3.8, 0.381, 1.6, 3.3, 0.489, 0.533, 0.4, 0.5, 0.75)
    insertShots(connection, 219, 'Bol Bol', 3.7, 6.8, 0.546, 0.4,
                1.6, 0.265, 3.3, 5.2, 0.633, 0.577, 1.2, 1.5, 0.759)
    insertShots(connection, 220, 'Moritz Wagner', 3.5, 6.9, 0.5,
                0.9, 2.9, 0.313, 2.6, 4.1, 0.631, 0.564, 2.7, 3.2, 0.841)
    insertShots(connection, 221, 'James Harden', 6.4, 14.5, 0.441,
                2.8, 7.2, 0.385, 3.6, 7.3, 0.495, 0.536, 5.4, 6.2, 0.867)
    insertShots(connection, 222, 'Joel Embiid', 11.0, 20.1, 0.548,
                1.0, 3.0, 0.33, 10.0, 17.1, 0.587, 0.573, 10.0, 11.7, 0.857)
    insertShots(connection, 223, 'Tyrese Maxey', 7.3, 15.2, 0.481,
                2.7, 6.2, 0.434, 4.7, 9.1, 0.513, 0.568, 3.0, 3.6, 0.845)
    insertShots(connection, 224, 'Tobias Harris', 5.7, 11.4, 0.501,
                1.7, 4.4, 0.389, 4.0, 7.0, 0.57, 0.575, 1.5, 1.7, 0.876)
    insertShots(connection, 225, 'De''Anthony Melton', 3.6, 8.5,
                0.425, 2.0, 5.2, 0.39, 1.6, 3.2, 0.484, 0.546, 0.9, 1.1, 0.793)
    insertShots(connection, 226, 'P.J. Tucker', 1.3, 3.0, 0.427,
                0.7, 1.9, 0.393, 0.5, 1.1, 0.482, 0.549, 0.3, 0.3, 0.826)
    insertShots(connection, 227, 'Shake Milton', 3.2, 6.6, 0.479,
                0.7, 1.9, 0.378, 2.4, 4.7, 0.521, 0.535, 1.3, 1.5, 0.853)
    insertShots(connection, 228, 'Georges Niang', 2.8, 6.4, 0.442,
                2.0, 4.9, 0.401, 0.9, 1.5, 0.576, 0.596, 0.5, 0.6, 0.867)
    insertShots(connection, 229, 'Jalen McDaniels', 2.5, 5.1, 0.488,
                0.5, 1.3, 0.4, 2.0, 3.9, 0.516, 0.537, 1.2, 1.4, 0.824)
    insertShots(connection, 230, 'Danuel House Jr.', 1.7, 3.5, 0.472,
                0.7, 2.0, 0.336, 1.0, 1.6, 0.644, 0.566, 0.8, 1.1, 0.75)
    insertShots(connection, 231, 'Devin Booker', 9.9, 20.1, 0.494,
                2.1, 6.0, 0.351, 7.8, 14.2, 0.554, 0.546, 5.8, 6.8, 0.855)
    insertShots(connection, 232, 'Kevin Durant', 9.1, 16.0, 0.57,
                2.8, 5.1, 0.537, 6.4, 10.9, 0.586, 0.656, 5.0, 6.0, 0.833)
    insertShots(connection, 233, 'Chris Paul', 5.0, 11.3, 0.44, 1.7,
                4.4, 0.375, 3.3, 6.9, 0.482, 0.513, 2.3, 2.7, 0.831)
    insertShots(connection, 234, 'Deandre Ayton', 7.8, 13.2, 0.589,
                0.1, 0.4, 0.292, 7.7, 12.9, 0.597, 0.592, 2.3, 3.0, 0.76)
    insertShots(connection, 235, 'Torrey Craig', 2.9, 6.3, 0.456,
                1.3, 3.2, 0.395, 1.6, 3.1, 0.518, 0.556, 0.4, 0.6, 0.711)
    insertShots(connection, 236, 'Damion Lee', 2.7, 6.1, 0.442, 1.5,
                3.3, 0.445, 1.2, 2.8, 0.439, 0.564, 1.3, 1.4, 0.904)
    insertShots(connection, 237, 'Cameron Payne', 3.9, 9.4, 0.415,
                1.4, 3.9, 0.368, 2.5, 5.6, 0.448, 0.49, 1.0, 1.3, 0.766)
    insertShots(connection, 238, 'Landry Shamet', 2.8, 7.5, 0.377,
                1.9, 5.0, 0.377, 1.0, 2.5, 0.376, 0.502, 1.1, 1.3, 0.882)
    insertShots(connection, 239, 'Josh Okogie', 2.3, 5.8, 0.391,
                0.9, 2.7, 0.335, 1.3, 3.0, 0.442, 0.471, 1.9, 2.7, 0.724)
    insertShots(connection, 240, 'Terrence Ross', 3.4, 7.9, 0.428,
                1.6, 4.7, 0.347, 1.8, 3.2, 0.544, 0.53, 0.6, 0.7, 0.857)
    insertShots(connection, 241, 'Damian Lillard', 9.6, 20.7, 0.463,
                4.2, 11.3, 0.371, 5.4, 9.4, 0.574, 0.564, 8.8, 9.6, 0.914)
    insertShots(connection, 242, 'Jerami Grant', 6.9, 14.5, 0.475,
                2.3, 5.7, 0.401, 4.6, 8.8, 0.523, 0.554, 4.4, 5.4, 0.813)
    insertShots(connection, 243, 'Anfernee Simons', 7.5, 16.9, 0.447,
                3.4, 9.1, 0.377, 4.1, 7.8, 0.528, 0.548, 2.6, 2.9, 0.894)
    insertShots(connection, 244, 'Trendon Watford', 2.9, 5.2, 0.56,
                0.4, 1.0, 0.391, 2.5, 4.2, 0.602, 0.599, 1.2, 1.6, 0.72)
    insertShots(connection, 245, 'Matisse Thybulle', 2.7, 6.2, 0.438,
                1.5, 3.9, 0.388, 1.2, 2.4, 0.519, 0.558, 0.5, 0.7, 0.625)
    insertShots(connection, 246, 'Justise Winslow', 2.8, 6.8, 0.409,
                0.5, 1.6, 0.311, 2.3, 5.3, 0.438, 0.444, 0.7, 1.0, 0.714)
    insertShots(connection, 247, 'Jusuf Nurkic', 5.0, 9.7, 0.519,
                0.8, 2.3, 0.361, 4.2, 7.4, 0.567, 0.561, 2.4, 3.7, 0.661)
    insertShots(connection, 248, 'Nassir Little', 2.5, 5.6, 0.442,
                1.1, 2.9, 0.367, 1.4, 2.7, 0.524, 0.538, 0.6, 0.9, 0.717)
    insertShots(connection, 249, 'Shaedon Sharpe', 3.8, 8.1, 0.472,
                1.3, 3.5, 0.36, 2.6, 4.6, 0.559, 0.551, 0.9, 1.3, 0.714)
    insertShots(connection, 250, 'Drew Eubanks', 2.7, 4.3, 0.641,
                0.1, 0.2, 0.389, 2.7, 4.1, 0.655, 0.651, 1.1, 1.6, 0.664)
    insertShots(connection, 251, 'Domantas Sabonis', 7.3, 11.9, 0.615,
                0.4, 1.1, 0.373, 6.9, 10.8, 0.639, 0.632, 4.1, 5.5, 0.742)
    insertShots(connection, 252, 'De''Aaron Fox', 9.3, 18.2, 0.512,
                1.6, 5.0, 0.324, 7.7, 13.2, 0.584, 0.557, 4.7, 6.0, 0.78)
    insertShots(connection, 253, 'Harrison Barnes', 4.6, 9.6, 0.473,
                1.6, 4.3, 0.374, 3.0, 5.3, 0.553, 0.556, 4.3, 5.0, 0.847)
    insertShots(connection, 254, 'Keegan Murray', 4.4, 9.8, 0.453,
                2.6, 6.3, 0.411, 1.9, 3.5, 0.527, 0.584, 0.8, 1.0, 0.765)
    insertShots(connection, 255, 'Kevin Huerter', 5.6, 11.5, 0.485,
                2.7, 6.8, 0.402, 2.9, 4.7, 0.604, 0.603, 1.3, 1.7, 0.725)
    insertShots(connection, 256, 'Malik Monk', 4.6, 10.3, 0.448,
                1.9, 5.2, 0.359, 2.8, 5.2, 0.538, 0.538, 2.4, 2.7, 0.889)
    insertShots(connection, 257, 'Davion Mitchell', 2.3, 5.0, 0.454,
                0.8, 2.5, 0.32, 1.5, 2.5, 0.584, 0.533, 0.3, 0.4, 0.806)
    insertShots(connection, 258, 'Trey Lyles', 2.5, 5.5, 0.458, 1.2,
                3.2, 0.363, 1.4, 2.3, 0.595, 0.565, 1.4, 1.7, 0.815)
    insertShots(connection, 259, 'Kessler Edwards', 1.4, 3.1, 0.435,
                0.7, 2.0, 0.349, 0.7, 1.2, 0.577, 0.543, 0.5, 0.6, 0.769)
    insertShots(connection, 260, 'Terence Davis', 2.4, 5.7, 0.423,
                1.4, 3.8, 0.366, 1.0, 1.9, 0.537, 0.545, 0.5, 0.7, 0.791)
    insertShots(connection, 261, 'Keldon Johnson', 8.0, 17.7, 0.452,
                2.1, 6.5, 0.329, 5.9, 11.2, 0.523, 0.512, 3.9, 5.2, 0.749)
    insertShots(connection, 262, 'Devin Vassell', 6.9, 15.7, 0.439,
                2.7, 7.0, 0.387, 4.2, 8.7, 0.48, 0.525, 2.1, 2.6, 0.78)
    insertShots(connection, 263, 'Tre Jones', 5.0, 10.9, 0.459, 0.7,
                2.3, 0.285, 4.4, 8.6, 0.506, 0.489, 2.2, 2.5, 0.86)
    insertShots(connection, 264, 'Devonte'' Graham', 3.8, 10.0, 0.38,
                2.7, 7.4, 0.358, 1.2, 2.6, 0.442, 0.513, 2.7, 3.6, 0.75)
    insertShots(connection, 265, 'Jakob Poeltl', 5.2, 8.4, 0.616,
                0.0, 0.0, 0.0, 5.2, 8.4, 0.618, 0.616, 1.7, 2.8, 0.605)
    insertShots(connection, 266, 'Jeremy Sochan', 4.5, 9.9, 0.453,
                0.6, 2.4, 0.246, 3.9, 7.5, 0.519, 0.483, 1.4, 2.1, 0.698)
    insertShots(connection, 267, 'Malaki Branham', 4.1, 9.3, 0.44,
                1.2, 3.9, 0.302, 2.9, 5.4, 0.539, 0.503, 0.9, 1.1, 0.829)
    insertShots(connection, 268, 'Zach Collins', 4.5, 8.7, 0.518,
                0.9, 2.3, 0.374, 3.6, 6.4, 0.571, 0.568, 1.7, 2.3, 0.761)
    insertShots(connection, 269, 'Keita Bates-Diop', 3.5, 6.9, 0.508,
                0.8, 2.1, 0.394, 2.7, 4.8, 0.557, 0.568, 1.8, 2.2, 0.793)
    insertShots(connection, 270, 'Doug McDermott', 3.7, 8.2, 0.457,
                1.9, 4.7, 0.413, 1.8, 3.5, 0.516, 0.575, 0.8, 1.1, 0.757)
    insertShots(connection, 271, 'Pascal Siakam', 8.9, 18.5, 0.48,
                1.3, 4.0, 0.324, 7.6, 14.5, 0.523, 0.515, 5.2, 6.7, 0.774)
    insertShots(connection, 272, 'Fred VanVleet', 6.3, 16.1, 0.393,
                3.0, 8.8, 0.342, 3.3, 7.3, 0.455, 0.486, 3.7, 4.1, 0.898)
    insertShots(connection, 273, 'OG Anunoby', 6.3, 13.2, 0.476,
                2.1, 5.5, 0.387, 4.2, 7.7, 0.539, 0.556, 2.1, 2.5, 0.838)
    insertShots(connection, 274, 'Scottie Barnes', 6.0, 13.2, 0.456,
                0.8, 2.9, 0.281, 5.2, 10.3, 0.505, 0.487, 2.5, 3.2, 0.772)
    insertShots(connection, 275, 'Gary Trent Jr.', 6.1, 14.2, 0.433,
                2.5, 6.8, 0.369, 3.6, 7.3, 0.493, 0.522, 2.6, 3.1, 0.839)
    insertShots(connection, 276, 'Jakob Poeltl', 5.8, 8.8, 0.652,
                0.0, 0.0, 0.0, 5.8, 8.8, 0.652, 0.652, 1.6, 2.8, 0.569)
    insertShots(connection, 277, 'Precious Achiuwa', 3.6, 7.3, 0.485,
                0.5, 2.0, 0.269, 3.0, 5.4, 0.564, 0.521, 1.6, 2.3, 0.702)
    insertShots(connection, 278, 'Chris Boucher', 3.4, 7.0, 0.493,
                0.8, 2.5, 0.328, 2.6, 4.5, 0.585, 0.552, 1.7, 2.2, 0.762)
    insertShots(connection, 279, 'Otto Porter Jr.', 1.9, 3.8, 0.5,
                0.8, 2.1, 0.353, 1.1, 1.6, 0.692, 0.6, 1.0, 1.0, 1.0)
    insertShots(connection, 280, 'Thaddeus Young', 2.0, 3.7, 0.545,
                0.1, 0.6, 0.176, 1.9, 3.0, 0.622, 0.561, 0.3, 0.5, 0.692)
    insertShots(connection, 281, 'Lauri Markkanen', 8.7, 17.3, 0.499,
                3.0, 7.7, 0.391, 5.6, 9.6, 0.585, 0.586, 5.3, 6.0, 0.875)
    insertShots(connection, 282, 'Jordan Clarkson', 7.5, 16.9, 0.444,
                2.5, 7.5, 0.338, 5.0, 9.4, 0.53, 0.519, 3.3, 4.0, 0.816)
    insertShots(connection, 283, 'Kelly Olynyk', 4.1, 8.2, 0.499,
                1.4, 3.5, 0.394, 2.7, 4.7, 0.576, 0.583, 2.9, 3.4, 0.853)
    insertShots(connection, 284, 'Kris Dunn', 5.3, 9.8, 0.537, 0.8,
                1.6, 0.472, 4.5, 8.2, 0.55, 0.576, 1.9, 2.4, 0.774)
    insertShots(connection, 285, 'Collin Sexton', 4.9, 9.8, 0.506,
                1.0, 2.5, 0.393, 3.9, 7.2, 0.546, 0.558, 3.4, 4.1, 0.819)
    insertShots(connection, 286, 'Walker Kessler', 4.0, 5.6, 0.72,
                0.0, 0.0, 0.333, 4.0, 5.6, 0.723, 0.721, 1.1, 2.1, 0.516)
    insertShots(connection, 287, 'Ochai Agbaji', 2.8, 6.5, 0.427,
                1.4, 3.9, 0.355, 1.4, 2.7, 0.532, 0.532, 0.9, 1.2, 0.812)
    insertShots(connection, 288, 'Talen Horton-Tucker', 4.0, 9.4,
                0.419, 0.9, 3.1, 0.286, 3.1, 6.3, 0.485, 0.467, 1.9, 2.6, 0.75)
    insertShots(connection, 289, 'Nickeil Alexander-Walker', 2.3, 4.7,
                0.488, 1.0, 2.4, 0.402, 1.3, 2.3, 0.578, 0.591, 0.8, 1.1, 0.692)
    insertShots(connection, 290, 'Rudy Gay', 1.9, 5.1, 0.38, 0.6,
                2.3, 0.254, 1.4, 2.8, 0.484, 0.437, 0.8, 0.9, 0.857)
    insertShots(connection, 291, 'Kyle Kuzma', 8.0, 17.8, 0.448,
                2.5, 7.5, 0.333, 5.5, 10.3, 0.533, 0.518, 2.7, 3.7, 0.73)
    insertShots(connection, 292, 'Bradley Beal', 8.9, 17.6, 0.506,
                1.6, 4.4, 0.365, 7.3, 13.2, 0.552, 0.551, 3.8, 4.6, 0.842)
    insertShots(connection, 293, 'Kristaps Porzingis', 7.8, 15.7, 0.498,
                2.1, 5.5, 0.385, 5.7, 10.2, 0.559, 0.565, 5.4, 6.4, 0.851)
    insertShots(connection, 294, 'Corey Kispert', 3.9, 7.9, 0.497,
                2.2, 5.2, 0.424, 1.7, 2.7, 0.637, 0.637, 1.0, 1.2, 0.852)
    insertShots(connection, 295, 'Monte Morris', 4.0, 8.3, 0.48,
                1.3, 3.3, 0.382, 2.7, 5.0, 0.543, 0.555, 1.0, 1.2, 0.831)
    insertShots(connection, 296, 'Deni Avdija', 3.3, 7.6, 0.437,
                0.9, 3.1, 0.297, 2.4, 4.6, 0.53, 0.497, 1.6, 2.2, 0.739)
    insertShots(connection, 297, 'Delon Wright', 2.8, 5.8, 0.474,
                0.8, 2.4, 0.345, 1.9, 3.4, 0.564, 0.545, 1.0, 1.2, 0.867)
    insertShots(connection, 298, 'Daniel Gafford', 3.7, 5.1, 0.732,
                0.0, 0.0, 0.0, 3.7, 5.1, 0.732, 0.732, 1.6, 2.4, 0.679)
    insertShots(connection, 299, 'Will Barton', 2.8, 7.1, 0.386,
                1.3, 3.5, 0.377, 1.5, 3.7, 0.395, 0.477, 0.9, 1.1, 0.778)
    insertShots(connection, 300, 'Jordan Goodwin', 2.5, 5.7, 0.448,
                0.6, 1.9, 0.322, 1.9, 3.8, 0.511, 0.501, 0.9, 1.1, 0.768)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Stadium(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Stadium")

    insertStadium(connection, 26, 'Golden 1 Center', 17608, 'Sacramento')
    insertStadium(connection, 10, 'Chase Center', 18064, 'San Francisco')
    insertStadium(connection, 1, 'State Farm Arena', 16600, 'Atlanta')
    insertStadium(connection, 2, 'TD Garden', 19156, 'Boston')
    insertStadium(connection, 21, 'Paycom Center', 18203, 'Oklahoma CIty')
    insertStadium(connection, 29, 'Vivint Arena', 18306, 'Salt Lake City')
    insertStadium(connection, 15, 'FedExForum', 17794, 'Memphis')
    insertStadium(connection, 17, 'Fiserv Forum', 17385, 'Milwaukee')
    insertStadium(connection, 12, 'Gainbridge Fieldhouse',
                  17274, 'Indianapolis')
    insertStadium(connection, 20, 'Madison Square Garden', 19812, 'New York')
    insertStadium(connection, 8, 'Ball Arena', 19520, 'Denver')
    insertStadium(connection, 18, 'Target Center', 18798, 'Minneapolis')
    insertStadium(connection, 23, 'Wells Fargo Center', 21000, 'Philadelphia')
    insertStadium(connection, 19, 'Smoothie King Center', 16867, 'New Orleans')
    insertStadium(connection, 7, 'American Airlines Center', 21146, 'Dallas')
    insertStadium(connection, 24, 'Footprint Center', 17071, 'Phoenix')
    insertStadium(connection, 13, 'Crypto.com Arena', 19079, 'Los Angeles')
    insertStadium(connection, 25, 'Moda Center', 19393, 'Portland')
    insertStadium(connection, 3, 'Barclays Center', 17732, 'Brooklyn')
    insertStadium(connection, 30, 'Capital One Arena', 20356, 'Washington')
    insertStadium(connection, 4, 'United Center', 20917, 'Chicago')
    insertStadium(connection, 27, 'Frost Bank Center', 18418, 'San Antonio')
    insertStadium(connection, 28, 'Scotiabank Arena', 20511, 'Toronto')
    insertStadium(connection, 6, 'Rocket Mortgage Fieldhouse',
                  19432, 'Cleveland')
    insertStadium(connection, 22, 'Amway Center', 18846, 'Orlando')
    insertStadium(connection, 5, 'Spectrum Center', 20200, 'Charlotte')
    insertStadium(connection, 11, 'Toyota Center', 18104, 'Houston')
    insertStadium(connection, 9, 'Little Caesars Arena', 20332, 'Detroit')
    insertStadium(connection, 16, 'Kaseya Center', 19600, 'Miami')

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Team(connection):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Teams")

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

    print("++++++++++++++++++++++++++++++++++")


def populateTables(connection):
    populateTable_Coaches(connection)
    populateTable_Games(connection)
    populateTable_News(connection)
    populateTable_Player(connection)
    populateTable_Shots(connection)
    populateTable_Stadium(connection)
    populateTable_Team(connection)


def main():
    database = r"Project_Database.sqlite"
    connection = openConnection(database)
    cursor = connection.cursor()

    with connection:
        #createTables(connection)
        #populateTables(connection)

        closeConnection(connection, database)


if __name__ == '__main__':
    main()
