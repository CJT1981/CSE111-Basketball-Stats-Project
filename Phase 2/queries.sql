/*
1. Find the number of coaches that have won at least 1 championship in their career.
*/

SELECT count(*) as coach_cnt
FROM coaches
WHERE c_numofchamp > 0;



/*
2. Find the name and the height of the tallest basketball player.
*/

SELECT p_name, MAX(p_height)
FROM player;



/*
3. Show the details of the games that were played on October 21, 2022.
*/

SELECT *
FROM games
WHERE g_date = '2022-10-21';



/*
4. Which stadium was used the most during the entire 2022 - 2023 basketball season? 
Show the name and number of games it held. 
*/

SELECT st_name as stadium, count(*) as num_games
FROM games, stadium
WHERE g_stadium = st_stadiumid
GROUP BY stadium
ORDER BY num_games DESC
LIMIT 1;



/*
5. Find top 5 players that have the highest field goal percentage and which teams they play for.  
*/

SELECT p_name, p_fgpercent, t_name
FROM player, team
WHERE p_teamid = t_teamid
ORDER BY p_fgpercent DESC
LIMIT 5;



/*
6. Find out how many games did the youngest team founded won during the 2022 - 2023 season. 
Output team name, found year, and how many games they won.
*/

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



/*
7. Find which team won the championship during the 2022 - 2023 season. 
Output the team that won first, then the score, and then the opponent.
*/

SELECT t1.t_name as winner, g_score as score, t2.t_name as runnerup
FROM games, team t1, team t2
WHERE g_winner = t1.t_teamid
AND (g_home = t2.t_teamid OR g_away = t2.t_teamid)
AND t2.t_teamid <> g_winner
ORDER BY g_date DESC
LIMIT 1;



/*
8. Out of all the transactions happened on July 6, 2022, how many of them were "Trade" type. 
*/

SELECT n_type, n_date, count(*) as n_cnt
FROM "player news"
WHERE n_type = 'Trade'
AND n_date = '2022-07-06';



/*
9. What is the salary of a player who has the lowest 2 pointer percentage, compared to the highest 2 pointer percentage player.
Output lowest player name, 2P%, his salary, and then the same for the higest player's.
*/

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



/*
10. Which players have a higher 3-point percentage than 2-point percentage?
*/

SELECT p_name, p_3Ppercent, s_2Ppct
FROM player, shots
WHERE s_playerid = p_playerid
AND p_3Ppercent > s_2Ppct;



/*
11. For each team, list the number of players in each position.
*/

SELECT t_name, p_position, COUNT(*) AS number_of_players
FROM team, player
WHERE t_teamid = p_teamid
GROUP BY t_name, p_position;



/*
12. Which team has the highest total salary for their players?
*/

SELECT t_name, SUM(p_salary) AS total_salary
FROM team, player
WHERE t_teamid = p_teamid
GROUP BY t_name
ORDER BY total_salary DESC;



/*
13. What are the five most common final scores in the database? 
Show the score and the number of games that ended with that score.
*/

SELECT g_score, COUNT(*) AS NumberOfGames
FROM games
GROUP BY g_score
ORDER BY NumberOfGames DESC
LIMIT 5;



/*
14. Does the average height of players on a team correlate with the number of wins? 
Show team names along with average height and win count.
*/

SELECT t_name, AVG(p_height) AS AverageHeight, SUM(CASE WHEN g_winner = t_teamid THEN 1 ELSE 0 END) AS Wins
FROM team, player, games
WHERE t_teamid = p_teamid
AND t_teamid IN (g_home, g_away)
GROUP BY t_name;


/*
15. Which team has the best win-to-salary ratio, indicating efficient budget spending? 
List the team name and the calculated ratio.
*/

SELECT
  t_name, 
  SUM(p_salary) AS TotalSalary, 
  SUM(CASE WHEN g_winner = t_teamid THEN 1 ELSE 0 END) AS Wins,
  (SUM(CASE WHEN g_winner = t_teamid THEN 1 ELSE 0 END) * 1.0 / SUM(p_salary)) AS EfficiencyRatio
FROM 
  team, player, games
WHERE t_teamid = p_teamid
AND t_teamid IN (g_home, g_away)
GROUP BY t_name
ORDER BY EfficiencyRatio DESC
LIMIT 1;


