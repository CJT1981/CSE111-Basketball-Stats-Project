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
        g_home INTEGER, 
        g_away INTEGER, 
        g_date TEXT, 
        g_winner INTEGER, 
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


def main():
    database = r"Project_Database.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTables(conn)
        mainMenu(conn)

    closeConnection(conn, database)


def mainMenu(_conn):
    while True:
        print("\nMain Menu")
        print("1. Coaches")
        print("2. Game")
        print("3. News")
        print("4. Player")
        print("5. Shots")
        print("6. Stadium")
        print("7. Team")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            coachesMenu(_conn)
        elif choice == "2":
            gameMenu(_conn)
        elif choice == "3":
            newsMenu(_conn)
        elif choice == "4":
            playerMenu(_conn)
        if choice == "5":
            shotsMenu(_conn)
        elif choice == "6":
            stadiumMenu(_conn)
        elif choice == "7":
            teamMenu(_conn)
        elif choice == "8":
            break
        else:
            print("Invalid choice, please try again.")


def coachesMenu(_conn):
    while True:
        print("\nCoaches Menu")
        print("1. Back to main menu.")
        print("2. Find the number of coaches that have won at least 1 championship in their career.")
        print("3. ")
        print("4. ")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT count(*) as coach_cnt
            FROM coaches
            WHERE c_numofchamp > 0;
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"The number of coaches who won at least 1 championship is {result[0]}.")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":

            pass
        elif choice == "4":
            pass
        else:
            print("Invalid choice, please try again.")


def gameMenu(_conn):
    while True:
        print("\nGame Menu")
        print("1. Back to main menu.")
        print("2. Show the details of the games that were played on October 21, 2022.")
        print("3. ")
        print("4. ")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT 
                g.g_gameid,
                ht.t_name AS Home_Team,
                at.t_name AS Away_Team,
                g.g_date,
                wt.t_name AS Winning_Team,
                g.g_score,
                st.st_name AS Stadium
            FROM 
                games g
                LEFT JOIN team ht ON g.g_home = ht.t_teamid
                LEFT JOIN team at ON g.g_away = at.t_teamid
                LEFT JOIN team wt ON g.g_winner = wt.t_teamid
                LEFT JOIN stadium st ON g.g_stadium = st.st_stadiumid
            WHERE 
                g.g_date = '2022-10-21';
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(
                    "Game ID | Home Team | Away Team | Date | Winner Team | Score | Stadium")
                for row in result:
                    print(
                        f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")

            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":

            pass
        elif choice == "4":
            pass
        else:
            print("Invalid choice, please try again.")


def newsMenu(_conn):
    while True:
        print("\nNews Menu")
        print("1. Back to main menu.")
        print("2. Out of all the transactions happened on July 6, 2022, how many of them were 'Trade' type.")
        print("3. ")
        print("4. ")

        choice = input("Enter your choice: ")

        if choice == 1:
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT n_date, n_type, count(*) as n_cnt
            FROM news
            WHERE n_type = 'Trade'
            AND n_date = '2022-07-06';
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"{result[2]} {result[1]} type transactions happened on {result[0]}.")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":

            pass
        elif choice == "4":
            pass
        else:
            print("Invalid choice, please try again.")


def playerMenu(_conn):
    while True:
        print("\nPlayer Menu")
        print("1. Back to main menu.")
        print("2. Who is the tallest player?")
        print("3. Find top 5 players that have the highest field goal percentage and which teams they play for.")
        print("4. What is the salary of a player who has the lowest 2 pointer percentage, compared to the highest 2 pointer percentage player.")
        print("5. Which players have a higher 3-point percentage than 2-point percentage?")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT p_name, p_height
            FROM player
            ORDER BY p_height DESC
            LIMIT 1;
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"The tallest player is {result[0]} with a height of {result[1]} ft.")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":
            cursor = _conn.cursor()

            query = """
            SELECT p_name, p_fgpercent, t_name
            FROM player, team
            WHERE p_teamid = t_teamid
            ORDER BY p_fgpercent DESC
            LIMIT 5;
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(f"Player Name | FG % | Team Name")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "4":
            cursor = _conn.cursor()

            query = """
            SELECT * FROM (
                SELECT p_name AS PlayerName, s_2PPCT AS TwoPointPercentage, p_salary AS Salary
                FROM player, shots
                WHERE p_playerid = s_playerid
                ORDER BY s_2PPCT ASC
                LIMIT 1
            )

            UNION ALL

            SELECT * FROM (
                SELECT p_name AS PlayerName, s_2PPCT AS TwoPointPercentage, p_salary AS Salary
                FROM player, shots
                WHERE p_playerid = s_playerid
                ORDER BY s_2PPCT DESC
                LIMIT 1
            );
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(f"Player Name | 2 Point % | Salary")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "5":
            cursor = _conn.cursor()

            query = """
            SELECT p_name, p_3Ppercent, s_2Ppct
            FROM player, shots
            WHERE s_playerid = p_playerid
            AND p_3Ppercent > s_2Ppct;
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(f"Player Name | 3 Point % | 2 Point %")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")

            cursor.close()
        else:
            print("Invalid choice, please try again.")


def shotsMenu(_conn):
    while True:
        print("\nShots Menu")
        print("1. Back to main menu.")
        print("2. ")
        print("3. ")
        print("4. ")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":

            pass
        elif choice == "3":

            pass
        elif choice == "4":
            pass
        else:
            print("Invalid choice, please try again.")


def stadiumMenu(_conn):
    while True:
        print("\nStadium Menu")
        print("1. Back to main menu.")
        print("2. Which stadium was used the most during the entire 2022 - 2023 basketball season?")
        print("3. ")
        print("4. ")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT st_name as stadium, count(*) as num_games
            FROM games, stadium
            WHERE g_stadium = st_stadiumid
            GROUP BY stadium
            ORDER BY num_games DESC
            LIMIT 1;
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"The {result[0]} stadium was used the most - {result[1]} times.")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":

            pass
        elif choice == "4":
            pass
        else:
            print("Invalid choice, please try again.")


def teamMenu(_conn):
    while True:
        print("\nTeam Menu")
        print("1. Back to main menu.")
        print("2. Find out how many games did the youngest team founded won during the 2022 - 2023 season.")
        print("3. Which team won the championship during the 2022 - 2023 season?")
        print("4. ")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT 
                t_name as team, 
                t_foundyear as found_year, 
                (   
                    SELECT count(*)
                    FROM games
                    WHERE g_winner = t_teamid
                ) as games_won
            FROM team 
            WHERE t_foundyear = (SELECT MAX(t_foundyear) from team);
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"The {result[0]} team was founded in {result[1]} and won {result[2]} games during the 2022 - 2023 championship.")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":
            cursor = _conn.cursor()

            query = """
            SELECT t1.t_name as winner, g_score as score, t2.t_name as runnerup
            FROM games, team t1, team t2
            WHERE g_winner = t1.t_teamid
            AND (g_home = t2.t_teamid OR g_away = t2.t_teamid)
            AND t2.t_teamid <> g_winner
            ORDER BY g_date DESC
            LIMIT 1;
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"{result[0]} entered finals with {result[2]} and won with the score {result[1]}.")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "4":
            pass
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
