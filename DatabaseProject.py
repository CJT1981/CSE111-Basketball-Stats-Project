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
        s_teamid INTEGER REFERENCES Team (t_teamid),
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

    _conn = openConnection(database)
    with _conn:
        dropTable(_conn)
        createTable(_conn)
        populateTables(_conn)
        mainMenu(_conn)

    closeConnection(_conn, database)


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
            c_name_input = input("Enter the full name of the coach: ").lower()

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
        print("10. Find a certain team's longest winning streak.")

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
            team1 = input("Enter the first team's name: ").lower()
            team2 = input("Enter the second team's name: ").lower()

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
        elif choice == "10":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            WITH OrderedGames AS (
                SELECT 
                    g.g_date,
                    t.t_teamid,
                    t.t_name,
                    CASE WHEN g.g_winner = t.t_teamid THEN 1 ELSE 0 END AS IsWin,
                    ROW_NUMBER() OVER (PARTITION BY t.t_teamid ORDER BY g.g_date) AS RowNum
                FROM 
                    game g
                    JOIN team t ON (g.g_home = t.t_teamid OR g.g_away = t.t_teamid)
                WHERE 
                    LOWER(t.t_name) = ? AND g.g_date < '2023-04-11'
            ),
            Streaks AS (
                SELECT 
                    og.t_teamid,
                    og.t_name,
                    og.IsWin,
                    og.RowNum - ROW_NUMBER() OVER (PARTITION BY og.t_teamid, og.IsWin ORDER BY og.g_date) AS StreakGroup
                FROM 
                    OrderedGames og
                WHERE 
                    og.IsWin = 1
            )
            SELECT 
                s.t_name,
                MAX(COUNT(*)) OVER (PARTITION BY s.t_teamid) AS LongestWinStreak
            FROM 
                Streaks s
            GROUP BY 
                StreakGroup, s.t_teamid, s.t_name;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result:
                print(
                    f"The longest winning streak for {result[0]} is {result[1]} games.")
            else:
                print(f"No winning streak data found or the team name is incorrect.")

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
        print("2. Show a player's biography:")
        print("3. Show a particular performance stat for a player:")
        print("4. Show top 10 players for a particular performance stat:")
        print("5. Show top 10 players based on a particular player position and performance stat:")
        print("6. Compare two players' performance statistics.")
        print("7. Show all players based on a particular performance stat threshold:")

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
        elif choice == "6":
            cursor = _conn.cursor()

            player = input("Enter the first of two players: ")
            playerOne = player.lower()
            player = input("Enter the second of two players: ")
            playerTwo = player.lower()

            query = """
            SELECT 
                p_name, 
                p_ppg,
                p_rpg,
                p_apg,
                p_spg,
                p_bpg
            FROM player
            WHERE
                LOWER(p_name) = ?
            """
            cursor.execute(query, (playerOne,))
            resultOne = cursor.fetchone()
            cursor.execute(query, (playerTwo,))
            resultTwo = cursor.fetchone()

            if resultOne and resultTwo:
                print(f"Player Name | PPG | RPG | APG | SPG | BPG")
                print(
                    f"{resultOne[0]} | {resultOne[1]} | {resultOne[2]} | {resultOne[3]} | {resultOne[4]} | {resultOne[5]}")
                print(
                    f"{resultTwo[0]} | {resultTwo[1]} | {resultTwo[2]} | {resultTwo[3]} | {resultTwo[4]} | {resultTwo[5]}")
            else:
                print("No Data Available")

            cursor.close()
        elif choice == "7":
            cursor = _conn.cursor()

            print(playerStats)
            stat = input("Enter a stat: ")
            stat_input = "p_" + stat
            threshold = input(
                "What is the minimum threshold you want to place: ")

            query = """
            SELECT 
                p_name, """ + stat_input + """
            FROM player
            WHERE
            """ + stat_input + """ >= ?
            ORDER BY """ + stat_input + """ DESC
            """
            cursor.execute(query, (threshold,))
            result = cursor.fetchall()

            if result:
                print(f"Player Name | {stat_input} ")
                for row in result:
                    print(
                        f"{row[0]} | {row[1]} ")
        else:
            print("Invalid choice, please try again.")


def shotsMenu(_conn):
    while True:
        print("\nShots Menu")
        print("1. Back to main menu.")
        print("2. League Average for each advanced statistic:")
        print("3. Find a player's specific advanced statistic:")
        print("4. Find a player's efficency statistics:")
        print("5. Find a player's made-attempt statistics:")
        print("6. Compare two players efficiency:")
        print("7. Show 10 best players for statistic:")
        print("8. Show all players with a statistic above a threshold:")

        choice = input("Enter your choice: ")
        advPlayerStats = "FG = Field Goals Made\nFGA = Field Goals Attempted\nFGPCT = Field Goal %\n3P - 3-Pointer Made\n3PA = 3-Pointer Attempts\n3PPCT = 3-Point %\n2P = 2-Pointer Made\n2PA = 2-Pointer Attempts\n2PPCT = 2-Point %\neFGPCT = Effective Field Goal %\nFT = Free Throws Made \nFTA = Free Throw Attempts\nFTPCT = Free Throw %"
        playerPosition = "1 = Point Guard\n2 = Shooting Guard\n3 = Small Forward\n4 = Point Forward\n5 = Center"

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
                row = result[0]
                print(
                    f"FGM | FGA | FG% | 3PM | 3PA | 3P% | 2PM | 2PA | 2P% | eFG% | FTM | FTA | FT%")
                print(f"{row[0]} | {row[1]:.2f} | {row[2]:.2f} | {row[3]:.2f} | {row[4]:.2f} | {row[5]:.2f} | {row[6]:.2f} | {row[7]:.2f} | {row[8]:.2f} | {row[9]:.2f} | {row[10]:.2f} | {row[11]:.2f} | {row[12]:.2f}")
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
                    f"{result[0]} | {result[1]} | {result[2]} | {result[3]} | {result[4]} | {result[5]}")
            else:
                print("No Data Available")

            cursor.close()
        elif choice == "5":
            cursor = _conn.cursor()

            player = input("Enter a player's name: ")
            playerName = player.lower()

            query = """
            SELECT 
                s_playername, 
                s_FG, 
                s_FGA,
                s_3P, 
                s_3PA,
                s_2P, 
                s_2PA,
                s_FT, 
                s_FTA
            FROM shots
            WHERE
                LOWER(s_playername) = ?
            """
            cursor.execute(query, (playerName,))
            result = cursor.fetchall()

            if result:
                row = result[0]
                print(f"Player Name | FGM | FGA | 3PM | 3PA% | 2PM | 2PA | FTM | FTA")
                print(
                    f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]}")
            else:
                print("No Data Available")

            cursor.close()
        elif choice == "6":
            cursor = _conn.cursor()

            player = input("Enter the first of two players: ")
            playerOne = player.lower()
            player = input("Enter the second of two players: ")
            playerTwo = player.lower()

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
            cursor.execute(query, (playerOne,))
            resultOne = cursor.fetchone()
            cursor.execute(query, (playerTwo,))
            resultTwo = cursor.fetchone()

            if resultOne and resultTwo:
                print(f"Player Name | FG% | 3PT% | 2PT% | eFG% | FT%")
                print(
                    f"{resultOne[0]} | {resultOne[1]} | {resultOne[2]} | {resultOne[3]} | {resultOne[4]} | {resultOne[5]}")
                print(
                    f"{resultTwo[0]} | {resultTwo[1]} | {resultTwo[2]} | {resultTwo[3]} | {resultTwo[4]} | {resultTwo[5]}")
            else:
                print("No Data Available")

            cursor.close()
        elif choice == "7":
            cursor = _conn.cursor()

            print(playerPosition)
            position = input("Enter a position: ")
            print(advPlayerStats)
            advStat = input("Enter a stat: ")
            statInput = "s_" + advStat

            query = """
            SELECT 
                s_playername, """ + statInput + """
            FROM shots, player
            WHERE
                s_playername = p_name AND
                p_position = ?
            ORDER BY """ + statInput + """ DESC
            LIMIT 10
            """
            cursor.execute(query, (position,))
            result = cursor.fetchall()

            if result:
                print(f"Player Name | {advStat} ")
                for row in result:
                    print(
                        f"{row[0]} | {row[1]} ")
            else:
                print("No Data Available")

            cursor.close()
        elif choice == "8":
            cursor = _conn.cursor()

            print(advPlayerStats)
            stat = input("Enter a stat: ")
            stat_input = "s_" + stat
            threshold = input(
                "What is the minimum threshold you want to place: ")

            query = """
            SELECT 
                s_playername, """ + stat_input + """
            FROM shots
            WHERE
            """ + stat_input + """ >= ?
            ORDER BY """ + stat_input + """ DESC
            """
            cursor.execute(query, (threshold,))
            result = cursor.fetchall()

            if result:
                print(f"Player Name | {stat_input} ")
                for row in result:
                    print(
                        f"{row[0]} | {row[1]} ")
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
        print("3. Find the capacity of a certain stadium.")
        print("4. Find the location of a certain stadium.")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cursor = _conn.cursor()

            query = """
            SELECT st_name as stadium, count(*) as num_games
            FROM game, stadium
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
                print("No data available or the stadium name is incorrect.")

            cursor.close()
        elif choice == "3":
            stadium_name = input("Enter the stadium's name: ")

            cursor = _conn.cursor()

            query = """
            SELECT st_name as stadium, st_size
            FROM stadium
            WHERE LOWER(st_name) = ?;
            """
            cursor.execute(query, (stadium_name,))
            result = cursor.fetchone()

            if result:
                print(
                    f"The {result[0]} stadium has a capacity of {result[1]} seats.")
            else:
                print("No data available or the stadium name is incorrect.")

            cursor.close()
        elif choice == "4":
            stadium_name = input("Enter the stadium's name: ")

            cursor = _conn.cursor()

            query = """
            SELECT st_name as stadium, st_location
            FROM stadium
            WHERE LOWER(st_name) = ?;
            """
            cursor.execute(query, (stadium_name,))
            result = cursor.fetchone()

            if result:
                print(
                    f"The {result[0]} stadium is located in {result[1]}.")
            else:
                print("No data available or the stadium name is incorrect.")

            cursor.close()
        else:
            print("Invalid choice, please try again.")


def teamMenu(_conn):
    while True:
        print("\nTeam Menu")
        print("1. Back to main menu.")
        print("2. Display a certain team's basic information.")
        print("3. Display a certain team's roster.")
        print("4. Display a certain team's payroll.")
        print("5. Display average statistics a certain team. (PPG, RPG, APG, SPG, BPG)")
        print("6. Display average advanced statistics a certain team. (FG, FGA, FG%, 3P, 3PA, 3P%, 2P, 2PA, 2P%, eFG%, FT, FTA, FT%)")
        print(
            "7. Display top 5 top performers in a certain team. (PPG, RPG, APG, SPG, BPG)")
        print("8. Display a certain player's average statistics against a certain team's average statistics.")

        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            team_name = input("Enter the team name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT t_name, t_foundyear, t_city, c_name, st_name
            FROM team, coaches, stadium
            WHERE LOWER(t_name) = ?
            AND t_coachid = c_coachid
            AND t_stadiumid = st_stadiumid;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result:
                print("Team Name | Found Year | City | Head Coach | Home Stadium")
                print(
                    f"{result[0]} | {result[1]} | {result[2]} | {result[3]} | {result[4]}")
            else:
                print("No data available or team name is incorrect.")

            cursor.close()
        elif choice == "3":
            team_name = input("Enter the team name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT p_name, p_position
            FROM team, player
            WHERE LOWER(t_name) = ?
            AND t_teamid = p_teamid;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchall()

            if result:
                print("Position | Player Name")
                for row in result:
                    print(f"{row[1]} | {row[0]}")
            else:
                print("No data available or team name is incorrect.")

            cursor.close()
        elif choice == "4":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT p_name, p_salary
            FROM player, team
            WHERE p_teamid = t_teamid
            AND LOWER(t_name) = ?;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchall()

            if result:
                print("Player Name | Salary")
                for row in result:
                    print(f"{row[0]} | {row[1]}")

                query = """
                SELECT t_name, SUM(p_salary) AS Total_Payroll
                FROM player, team
                WHERE p_teamid = t_teamid
                AND LOWER(t_name) = ?;
                """
                cursor.execute(query, (team_name,))
                result = cursor.fetchone()

                if result:
                    print(f"Total Payroll: {result[0]}: {result[1]}")
                else:
                    print("Unable to calculate the total payroll.")
            else:
                print("No players or team found with the given name.")

            cursor.close()
        elif choice == "5":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT AVG(p_ppg), AVG(p_rpg), AVG(p_apg), AVG(p_spg), AVG(p_bpg)
            FROM player, team 
            WHERE p_teamid = t_teamid
            AND LOWER(t_name) = ?;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result:
                print("PPG | RPG | APG | SPG | BPG")
                print(
                    f"{result[0]:.2f} | {result[1]:.2f} | {result[2]:.2f} | {result[3]:.2f} | {result[4]:.2f}")
            else:
                print("No data available or team name is incorrect.")

            cursor.close()
        elif choice == "6":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT 
                AVG(s_FG), AVG(s_FGA), AVG(s_FGPCT), AVG(s_3P), AVG(s_3PA), AVG(s_3PPCT), AVG(s_2P),
                AVG(s_2PA), AVG(s_2PPCT), AVG(s_eFGPCT), AVG(s_FT), AVG(s_FTA), AVG(s_FTPCT)
            FROM shots, player, team
            WHERE s_playerid = p_playerid
            AND p_teamid = t_teamid
            AND LOWER(t_name) = ?;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchone()

            if result:
                print(
                    "FG | FGA | FG% | 3P | 3PA | 3P% | 2P | 2PA | 2P% | eFG% | FT | FTA | FT%")
                print(
                    f"{result[0]:.2f} | {result[1]:.2f} | {result[2]:.2f}% | "
                    f"{result[3]:.2f} | {result[4]:.2f} | {result[5]:.2f}% | "
                    f"{result[6]:.2f} | {result[7]:.2f} | {result[8]:.2f}% | "
                    f"{result[9]:.2f}% | {result[10]:.2f} | {result[11]:.2f} | {result[12]:.2f}%"
                )

            else:
                print("No data available or team name is incorrect.")

            cursor.close()
        elif choice == "7":
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT 
                p_name,
                p_ppg,
                p_rpg,
                p_apg,
                p_spg,
                p_bpg
            FROM player, team 
            WHERE p_teamid = t_teamid
            AND LOWER(t_name) = ?
            ORDER BY p_ppg DESC
            LIMIT 5;
            """
            cursor.execute(query, (team_name,))
            result = cursor.fetchall()

            if result:
                print("Player Name | PPG | RPG | APG | SPG | BPG")
                for row in result:
                    ppg = float(row[1]) if row[1] else 0
                    rpg = float(row[2]) if row[2] else 0
                    apg = float(row[3]) if row[3] else 0
                    spg = float(row[4]) if row[4] else 0
                    bpg = float(row[5]) if row[5] else 0

                    print(
                        f"{row[0]} | {ppg:.2f} | {rpg:.2f} | {apg:.2f} | {spg:.2f} | {bpg:.2f}")
            else:
                print("No data available or team name is incorrect.")

            cursor.close()
        elif choice == "8":
            player_name = input("Enter player's name: ").lower()
            team_name = input("Enter the team's name: ").lower()

            cursor = _conn.cursor()

            query = """
            SELECT 
                (SELECT AVG(p_ppg) FROM player WHERE LOWER(p_name) = ?) AS Player_PPG,
                (SELECT AVG(p_rpg) FROM player WHERE LOWER(p_name) = ?) AS Player_RPG,
                (SELECT AVG(p_apg) FROM player WHERE LOWER(p_name) = ?) AS Player_APG,
                (SELECT AVG(p_spg) FROM player WHERE LOWER(p_name) = ?) AS Player_SPG,
                (SELECT AVG(p_bpg) FROM player WHERE LOWER(p_name) = ?) AS Player_BPG,
                (SELECT AVG(p_ppg) FROM player p JOIN team t ON p.p_teamid = t.t_teamid WHERE LOWER(t.t_name) = ?) AS Team_PPG,
                (SELECT AVG(p_rpg) FROM player p JOIN team t ON p.p_teamid = t.t_teamid WHERE LOWER(t.t_name) = ?) AS Team_RPG,
                (SELECT AVG(p_apg) FROM player p JOIN team t ON p.p_teamid = t.t_teamid WHERE LOWER(t.t_name) = ?) AS Team_APG,
                (SELECT AVG(p_spg) FROM player p JOIN team t ON p.p_teamid = t.t_teamid WHERE LOWER(t.t_name) = ?) AS Team_SPG,
                (SELECT AVG(p_bpg) FROM player p JOIN team t ON p.p_teamid = t.t_teamid WHERE LOWER(t.t_name) = ?) AS Team_BPG;

            """
            cursor.execute(query, (player_name, player_name, player_name, player_name,
                           player_name, team_name, team_name, team_name, team_name, team_name,))
            result = cursor.fetchone()

            if result:
                print("PPG | RPG | APG | SPG | BPG")
                print(
                    f"{result[0]:.2f} | {result[1]:.2f} | {result[2]:.2f} | {result[3]:.2f} | {result[4]:.2f}")
                print(
                    f"{result[5]:.2f} | {result[6]:.2f} | {result[7]:.2f} | {result[8]:.2f} | {result[9]:.2f}")
            else:
                print("No data available or team name is incorrect.")

            cursor.close()
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
