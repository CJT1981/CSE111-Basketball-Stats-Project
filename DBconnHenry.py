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
        print("3. Find how many championship(s) did a certain coach win.")
        print("4. Find when did a certain coach start his career.")
        print(
            "5. Find what team did a certain coach coach during the 2022 - 2023 NBA season.")

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
            c_name_input = input("Enter the full name of the coach: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT c_name, c_startyear
            FROM coaches
            WHERE LOWER(c_name) = ?;
            """
            cursor.execute(query, (c_name_input,))
            result = cursor.fetchone()

            if result:
                print(f"{result[0]} started coaching in {result[1]}.")
            else:
                print("No data available or coach not found.")

            cursor.close()
        elif choice == "5":
            c_name_input = input(
                "Enter the full name of the coach: ").strip().lower()

            cursor = _conn.cursor()

            query = """
            SELECT c.c_name, t.t_name
            FROM coaches c
            JOIN team t ON c.c_coachid = t.t_coachid
            WHERE LOWER(c.c_name) = ?;
            """
            cursor.execute(query, (c_name_input,))
            result = cursor.fetchone()

            if result:
                print(
                    f"{result[0]} was a head coach for {result[1]} team during the 2022 - 2023 season.")
            else:
                print("No data available or coach not found.")

            cursor.close()
        else:
            print("Invalid choice, please try again.")


def gameMenu(_conn):
    while True:
        print("\nGame Menu")
        print("1. Back to main menu.")
        print("2. Display the info of a highest scoring game.")
        print("3. Find history of games played between two teams.")
        print("4. Show the details of the games that were played on a certain date.")
        print("5. Show the details of the games that were played during a certain month.")
        print("6. Find how many home games did a certain team win.")
        print("7. Find how many away games did a certain team win.")
        print("8. Find how many games did a certain team win and lose.")
        print("9. Find a certain team's overall ranking.")
        print("10. ")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT 
                g.g_date,
                ht.t_name AS Home_Team,
                g.g_score,
                at.t_name AS Away_Team,
                wt.t_name AS Winning_Team
            FROM 
                game g
                LEFT JOIN team ht ON g.g_home = ht.t_teamid
                LEFT JOIN team at ON g.g_away = at.t_teamid
                LEFT JOIN team wt ON g.g_winner = wt.t_teamid
            ORDER BY 
                (
                    CAST(SUBSTR(g.g_score, 1, INSTR(g.g_score, '(') - 1) AS INTEGER) +
                    CAST(SUBSTR(g.g_score, INSTR(g.g_score, '-') + 1, 
                    INSTR(g.g_score, '(') - INSTR(g.g_score, '-') - 2) AS INTEGER)
                ) DESC
            LIMIT 1;
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"On {result[0]}, {result[1]} played against {result[3]}, and {result[4]} won with the highest score of {result[2]} throughtout the enitire season!")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":
            team1 = input("Enter the first team's name: ").strip().lower()
            team2 = input("Enter the second team's name: ").strip().lower()

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
                game g
                LEFT JOIN team ht ON g.g_home = ht.t_teamid
                LEFT JOIN team at ON g.g_away = at.t_teamid
                LEFT JOIN team wt ON g.g_winner = wt.t_teamid
                LEFT JOIN stadium st ON g.g_stadium = st.st_stadiumid
            WHERE 
                (LOWER(ht.t_name) = ? AND LOWER(at.t_name) = ?) OR 
                (LOWER(ht.t_name) = ? AND LOWER(at.t_name) = ?)
            ORDER BY 
                g.g_date;
            """
            cursor.execute(query, (team1, team2, team2, team1))
            result = cursor.fetchall()

            if result:
                print(
                    "Game ID | Home Team | Away Team | Date | Winner Team | Score | Stadium")
                for row in result:
                    print(
                        f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
            else:
                print("No games found between these two teams.")

            cursor.close()
        elif choice == "4":
            date_input = input(
                "Enter the date you are looking for in the following format YYYY-MM-DD: ")

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
                game g
                LEFT JOIN team ht ON g.g_home = ht.t_teamid
                LEFT JOIN team at ON g.g_away = at.t_teamid
                LEFT JOIN team wt ON g.g_winner = wt.t_teamid
                LEFT JOIN stadium st ON g.g_stadium = st.st_stadiumid
            WHERE 
                g.g_date = ?;
            """
            cursor.execute(query, (date_input,))
            result = cursor.fetchall()

            if result:
                print(
                    "Game ID | Home Team | Away Team | Date | Winner Team | Score | Stadium")
                for row in result:
                    print(
                        f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")

            else:
                print("No data available or the date is incorrect.")

            cursor.close()
        elif choice == "5":
            month_input = input(
                "Enter the year and month you are looking for in the following format YYYY-MM: ")
            month_input = month_input + '%'

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
                game g
                LEFT JOIN team ht ON g.g_home = ht.t_teamid
                LEFT JOIN team at ON g.g_away = at.t_teamid
                LEFT JOIN team wt ON g.g_winner = wt.t_teamid
                LEFT JOIN stadium st ON g.g_stadium = st.st_stadiumid
            WHERE 
                g.g_date LIKE ?;
            """
            cursor.execute(query, (month_input,))
            result = cursor.fetchall()

            if result:
                print(
                    "Game ID | Home Team | Away Team | Date | Winner Team | Score | Stadium")
                for row in result:
                    print(
                        f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")

            else:
                print("No data available or the date is incorrect.")

            cursor.close()
        elif choice == "6":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT 
                t_name, 
                COUNT(*) AS total_home_games,
                SUM(CASE WHEN g_winner = t_teamid THEN 1 ELSE 0 END) AS home_wins
            FROM game, team
            WHERE g_home = t_teamid
            AND LOWER(t_name) = ?;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result and result[1] > 0:
                print(
                    f"{result[0]} has won {result[2]} home game(s) out of {result[1]}.")
            else:
                print(
                    f"{team_name} has not won any home games or the team name is incorrect.")

            cursor.close()
        elif choice == "7":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT 
                t_name, 
                COUNT(*) AS total_away_games,
                SUM(CASE WHEN g_winner = t_teamid THEN 1 ELSE 0 END) AS away_wins
            FROM game, team
            WHERE g_away = t_teamid
            AND LOWER(t_name) = ?;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result and result[1] > 0:
                print(
                    f"{result[0]} has won {result[2]} away game(s) out of {result[1]}.")
            else:
                print(
                    f"{team_name} has not won any home games or the team name is incorrect.")

            cursor.close()
        elif choice == "8":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT 
                t_name,
                (SELECT COUNT(*) FROM game WHERE g_winner = t_teamid) AS total_wins,
                (SELECT COUNT(*) FROM game WHERE (g_home = t_teamid OR g_away = t_teamid) AND g_winner != t_teamid) AS total_losses
            FROM team
            WHERE LOWER(t_name) = ?;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result:
                print(f"{result[0]} has a record of {result[1]}-{result[2]}.")
            else:
                print(
                    f"{team_name} has not won any home games or the team name is incorrect.")

            cursor.close()
        elif choice == "9":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT 
                t.t_name,
                COUNT(CASE WHEN g.g_winner = t.t_teamid THEN 1 END) AS Wins,
                COUNT(CASE WHEN g.g_winner != t.t_teamid AND (g.g_home = t.t_teamid OR g.g_away = t.t_teamid) THEN 1 END) AS Losses
            FROM 
                team t
                LEFT JOIN game g ON (g.g_home = t.t_teamid OR g.g_away = t.t_teamid)
            WHERE 
                t.t_name = ?
            GROUP BY 
                t.t_teamid, t.t_name;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result:
                print(f"{result[0]} - Wins: {result[1]}, Losses: {result[2]}")
            else:
                print(
                    f"No data found for {team_name} or the team name is incorrect.")

            cursor.close()
        else:
            print("Invalid choice, please try again.")


def newsMenu(_conn):
    while True:
        print("\nNews Menu")
        print("1. Back to main menu.")
        print("2. See all the news that occurred")
        print("3. Input a type of news to only see specific news:")
        print("4. Input a date to see what news occurred on this date:")
        print("5. Input a date and type of news to only see specific news on that date:")

        choice = input("Enter your choice: ")
        tradeTypes = "The news types are: Extension, Firing, Hiring, Signing, Suspension, Trade"

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()
            query = """
            SELECT 
                n_date, 
                n_type, 
                n_news
            FROM news
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(f"News Type | Date | News")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")
            cursor.close()

        elif choice == "3":
            print(tradeTypes)
            newsType = input(
                "What news would you be interested in looking into: ")

            cursor = _conn.cursor()
            query = """
            SELECT 
                n_date, 
                n_type, 
                n_news
            FROM news
            WHERE 
                n_type = ?
            """
            cursor.execute(query, (newsType,))
            result = cursor.fetchall()

            if result:
                print(f"Date | News Type | News")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")
            cursor.close()
        elif choice == "4":
            date = input(
                "Enter a date to see the news in YYYY-MM-DD format: ")

            cursor = _conn.cursor()
            query = """
            SELECT 
                n_date, 
                n_type, 
                n_news
            FROM news
            WHERE 
                n_date = ?
            """
            cursor.execute(query, (date,))
            result = cursor.fetchall()

            if result:
                print(f"Date | News Type | News")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")
        elif choice == "5":
            print(tradeTypes)
            newsType = input(
                "What news would you be interested in looking into: ")
            date = input(
                "Enter a date to see the news in YYYY-MM-DD format: ")

            cursor = _conn.cursor()
            query = """
            SELECT 
                n_date, 
                n_type, 
                n_news
            FROM news
            WHERE 
                n_type = ? AND
                n_date = ?
            """
            args = [newsType, date]
            cursor.execute(query, args)
            result = cursor.fetchall()

            if result:
                print(f"Date | News Type | News")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")
        elif choice != "1" or choice != "2" or choice != "3" or choice != "4" or choice != "5":
            print("Invalid choice, please try again.")


def playerMenu(_conn):
    while True:
        print("\nPlayer Menu")
        print("1. Back to main menu.")
        print("2. Show a player's biography")
        print("3. Find a stat for a player")
        print("4. Show top 10 players for a stat: ")
        print("5. Find the top 10 players for a stat based on a position: ")

        choice = input("Enter your choice: ")
        playerStats = "Per game statistics, you can look into are:\nppg = Points\nrpg = Rebounds\napg = Assists\nspg = Steals\nbpg = Blocks\nFGpercent = FG%\n3ppercent = 3PT%"
        playerPosition = "1 = Point Guard\n2 = Shooting Guard\n3 = Small Forward\n4 = Point Forward\n5 = Center"

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            name = input("Enter a player, who you want to see: ")
            playerName = name.lower()

            query = """
            SELECT 
                p_name,
                p_teamname, 
                p_position, 
                p_height, 
                p_weight, 
                p_startyear, 
                p_salary
            FROM player
            WHERE
                LOWER(p_name) = ?
            """
            cursor.execute(query, (playerName,))
            result = cursor.fetchone()

            if result:
                print(f"Name | Team | Position | Height | Weight | Start Year | Salary")
                print(
                    f"{result[0]} | {result[1]} | {result[2]} | {result[3]} | {result[4]} | {result[5]} | {result[6]}")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "3":
            cursor = _conn.cursor()

            playerName = input("What player do you want to look into: ")
            name = playerName.lower()
            print(playerStats)
            stat = input("What statistic do you want to look at: ")
            stats = "p_" + stat

            query = """
            SELECT 
                p_name, """ + stats + """
            FROM player
            WHERE 
                LOWER(p_name) = ?
            """
            cursor.execute(query, (name,))
            result = cursor.fetchone()

            if result:
                print(f"Player Name | {stat}")
                print(f"{result[0]} | {result[1]}")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "4":
            cursor = _conn.cursor()

            print(playerStats)
            stat = input("What statistic would you like to see: ")
            stats = "p_" + stat

            query = """
            SELECT 
                p_name,""" + stats + """
            FROM player
            ORDER BY """ + stats + """ DESC
            LIMIT 10
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(f"Player Name | {stat}")
                for row in result:
                    print(f"{row[0]} | {row[1]}")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "5":
            cursor = _conn.cursor()

            print(playerStats)
            stat = input("What statistic would you like to see: ")
            stats = "p_" + stat
            print(playerPosition)
            position = input("Select a position: ")

            query = """
            SELECT 
                p_name,""" + stats + """
            FROM player
            WHERE 
                p_position = ? 
            ORDER BY """ + stats + """ DESC
            LIMIT 10
            """
            cursor.execute(query, (position,))
            result = cursor.fetchall()

            if result:
                print(f"Player Name | {stat}")
                for row in result:
                    print(f"{row[0]} | {row[1]}")
            else:
                print("No data available.")

            cursor.close()
        else:
            print("Invalid choice, please try again.")


def shotsMenu(_conn):
    while True:
        print("\nShots Menu")
        print("1. Back to main menu.")
        print("2. League average for every advance statistic:")
        print("3. Show the top 10 players in a advanced stat:")
        print("4. Show a player's efficiency stats:")
        print("5. Show a player's per game shot frequency:")
        print("5. Compare two players efficiency:")
        print("6. Show all players with an advance stat above a threshold:")
        print("7. Show the top 10 players in an advance stat:")

        choice = input("Enter your choice: ")
        advPlayerStats = "FG = Field Goals Made\nFGA = Field Goals Attempted\nFGPCT\n3P - 3-Pointer Made\n3PA = 3-Pointer Attempts\n3PPCT = 3-Point %\n2P = 2-Pointer Made\n2PA = 2-Pointer Attempts\n2PPCT = 2-Point %\neFGPCT = Effective Field Goal %\nFT = Free Throws Made \nFTA = Free Throw Attempts\nFTPCT = Free Throw %"

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT 
                SUM(s_FG)/300, 
                SUM(s_FGA)/300, 
                SUM(s_FGPCT)/300, 
                SUM(s_3P)/300, 
                SUM(s_3PA)/300, 
                SUM(s_3PPCT)/300, 
                SUM(s_2P)/300, 
                SUM(s_2PA)/300, 
                SUM(s_2PPCT)/300, 
                SUM(s_eFGPCT)/300, 
                SUM(s_FT)/300, 
                SUM(s_FTA)/300, 
                SUM(s_FTPCT)/300
            FROM shots
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(
                    f"FGM | FGA | FG% | 3PM | 3PA | 3P% | 2PM | 2PA | 2P% | eFG% | FTM | FTA | FT%")
                print(f"{result[0]} | {result[1]} | {result[2]} | {result[3]} | {result[4]} | {result[5]} | {result[6]} | {result[7]} | {result[8]} | {result[9]} | {result[10]} | {result[11]} | {result[12]}")
        elif choice == "3":
            cursor = _conn.cursor()

            print(advPlayerStats)
            advStat = input("Enter an advance stat to see: ")
            stats = "s_" + advStat

            query = """
            SELECT 
                s_playername, """ + stats + """
            FROM shots
            ORDER BY """ + stats + """ DESC
            LIMIT 10
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(f"Player Name | {advStat}")
                for row in result:
                    print(f"{row[0]} | {row[1]}")
            else:
                print("No Data Available")

            cursor.close()
        elif choice == "4":
            cursor = _conn.cursor()

            player = input("Enter a player's name: ")
            playerName = player.lower()

            query = """
            SELECT 
                s_playername, 
                s_FGPCT,
                s_3PPCT,
                s_2PPCT,
                s_eFGPCT,
                s_FTPCT
            FROM shots
            WHERE
                LOWER(s_playername) = ?
            """
            cursor.execute(query, (playerName,))
            result = cursor.fetchone()

            if result:
                print(f"Player Name | FG% | 3PT% | 2PT% | eFG% | FT%")
                print(
                    f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
            else:
                print("No Data Available")

            cursor.close()
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
        print("4. For each team, list the number of players in each position.")
        print("5.  Which team has the highest total salary for their players?")

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
            cursor = _conn.cursor()

            query = """
            SELECT t_name, p_position, COUNT(*) AS number_of_players
            FROM team, player
            WHERE t_teamid = p_teamid
            GROUP BY t_name, p_position;
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(f"Team Name | Player Position | Number of Players")
                for row in result:
                    print(f"{row[0]} | {row[1]} | {row[2]}")
            else:
                print("No data available.")

            cursor.close()
        elif choice == "5":
            cursor = _conn.cursor()

            query = """
            SELECT t_name, SUM(p_salary) AS total_salary
            FROM team, player
            WHERE t_teamid = p_teamid
            GROUP BY t_name
            ORDER BY total_salary DESC;
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(
                    f"{result[0]} has the total highest salary of ${result[1]} for their players.")
            else:
                print("No data available.")

            cursor.close()
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
