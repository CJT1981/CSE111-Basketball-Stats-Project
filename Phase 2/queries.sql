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
4. Which stadium was used the most during the entire 2022 - 2023 basketball season? Show the name and number of games it held. 
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
6. Find out how many games did the youngest team founded won during the 2022 - 2023 season. Outout team name, found year, and how many games they won.
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
7. Find which team won the championship during the 2022 - 2023 season. Output the team that won first, then the score, and then the opponent.
*/

SELECT t1.t_name as winner, g_score as score, t2.t_name as runnerup
FROM games, team t1, team t2
WHERE g_winner = t1.t_teamid
AND (g_home = t2.t_teamid OR g_away = t2.t_teamid)
AND t2.t_teamid <> g_winner
ORDER BY g_date DESC
LIMIT 1;



/*
8. 
*/

