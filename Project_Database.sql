--
-- File generated with SQLiteStudio v3.4.4 on Tue Nov 7 13:02:28 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: coaches
CREATE TABLE IF NOT EXISTS coaches (
    c_coachid identity(1, 1) primary key,
    c_name varchar(50),
    c_startyear date not null,
    c_numofchamp int
);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (1, 'Quin Snyder', 1992, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (2, 'Joe Mazzulla', 2019, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (3, 'Jacque Vaughn', 2010, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (4, 'Billy Donovan', 2015, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (5, 'Steve Clifford', 2000, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (6, 'J.B. Bickerstaff', 2004, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (7, 'Jason Kidd', 2013, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (8, 'Michael Malone', 2003, 1);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (9, 'Dwane Casey', 1994, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (10, 'Steve Kerr', 2014, 4);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (11, 'Stephen Silas', 2000, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (12, 'Rick Carlisle', 1989, 1);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (13, 'Tyronn Lue', 2011, 1);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (14, 'Darvin Ham', 2011, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (15, 'Taylor Jenkins', 2013, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (16, 'Erik Spoelstra', 1997, 2);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (17, 'Mike Budenholzer', 1996, 1);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (18, 'Chris Finch', 2011, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (19, 'Willie Green', 2018, 9);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (20, 'Tom Thibodeau', 1989, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (21, 'Mark Daigneault', 2019, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (22, 'Jamahl Mosley', 2006, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (23, 'Doc Rivers', 1999, 1);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (24, 'Monty Williams', 2005, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (25, 'Chauncey Billups', 2020, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (26, 'Mike Brown', 1997, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (27, 'Gregg Popovich', 1988, 5);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (28, 'Nick Nurse', 2013, 1);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (29, 'Will Hardy', 2016, 0);
INSERT INTO coaches (c_coachid, c_name, c_startyear, c_numofchamp) VALUES (30, 'Wes Unseld', 2005, 0);

-- Table: Player
CREATE TABLE IF NOT EXISTS Player (player_id INTEGER PRIMARY KEY, p_name TEXT, p_teamname TEXT, p_position INTEGER, p_height TEXT, p_weight INTEGER, p_ppg REAL, p_rpg REAL, p_apg REAL, p_spg REAL, p_bpg REAL, "p_FG%" REAL, "p_3point%" REAL, p_startyear INTEGER, p_salary INTEGER);

-- Table: stadium
CREATE TABLE IF NOT EXISTS stadium (
    st_stadiumid identity(1, 1) primary key,
    st_name varchar(50),
    st_size int,
    st_location varchar(50)
);
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (26, 'Golden 1 Center', 17608, 'Sacramento');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (10, 'Chase Center', 18064, 'San Francisco');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (1, 'State Farm Arena', 16600, 'Atlanta');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (2, 'TD Garden', 19156, 'Boston');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (21, 'Paycom Center', 18203, 'Oklahoma CIty');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (29, 'Vivint Arena', 18306, 'Salt Lake City');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (15, 'FedExForum', 17794, 'Memphis');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (17, 'Fiserv Forum', 17385, 'Milwaukee');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (12, 'Gainbridge Fieldhouse', 17274, 'Indianapolis');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (20, 'Madison Square Garden', 19812, 'New York');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (8, 'Ball Arena', 19520, 'Denver');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (18, 'Target Center', 18798, 'Minneapolis');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (23, 'Wells Fargo Center', 21000, 'Philadelphia');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (19, 'Smoothie King Center', 16867, 'New Orleans');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (7, 'American Airlines Center', 21146, 'Dallas');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (24, 'Footprint Center', 17071, 'Phoenix');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (13, 'Crypto.com Arena', 19079, 'Los Angeles');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (25, 'Moda Center', 19393, 'Portland');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (3, 'Barclays Center', 17732, 'Brooklyn');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (30, 'Capital One Arena', 20356, 'Washington');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (4, 'United Center', 20917, 'Chicago');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (27, 'Frost Bank Center', 18418, 'San Antonio');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (28, 'Scotiabank Arena', 20511, 'Toronto');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (6, 'Rocket Mortgage Fieldhouse', 19432, 'Cleveland');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (22, 'Amway Center', 18846, 'Orlando');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (5, 'Spectrum Center', 20200, 'Charlotte');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (11, 'Toyota Center', 18104, 'Houston');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (9, 'Little Caesars Arena', 20332, 'Detroit');
INSERT INTO stadium (st_stadiumid, st_name, st_size, st_location) VALUES (16, 'Kaseya Center', 19600, 'Miami');

-- Table: team
CREATE TABLE IF NOT EXISTS team (t_teamid identity (1, 1) PRIMARY KEY, t_tname varchar (50), t_foundyear date NOT NULL, t_city varchar (50), t_coachid int, t_stadiumid int);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (26, 'Sacramento Kings', 1985, 'Sacramento', 26, 26);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (10, 'Golden State Warriors', 1971, 'San Francisco', 10, 10);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (1, 'Atlanta Hawks', 1968, 'Atlanta', 1, 1);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (2, 'Boston Celtics', 1946, 'Boston', 2, 2);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (21, 'Oklahoma City Thunder', 2008, 'Oklahoma City', 21, 21);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (14, 'Los Angeles Lakers', 1960, 'Los Angeles', 14, 13);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (29, 'Utah Jazz', 1979, 'Salt Lake City', 29, 29);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (15, 'Memphis Grizzlies', 2001, 'Memphis', 15, 15);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (17, 'Milwaukee Bucks', 1968, 'Milwaukee', 17, 17);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (12, 'Indiana Pacers', 1976, 'Indianapolis', 12, 12);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (20, 'New York Knicks', 1946, 'New York', 20, 20);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (8, 'Denver Nuggets', 1976, 'Denver', 8, 8);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (18, 'Minnesota Timberwolves', 1989, 'Minneapolis', 18, 18);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (23, 'Philadelphia 76ers', 1963, 'Philadelphia', 23, 23);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (19, 'New Orleans Pelicans', 2013, 'New Orleans', 19, 19);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (7, 'Dallas Mavericks', 1980, 'Dallas', 7, 7);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (24, 'Phoenix Suns', 1968, 'Phoenix', 24, 24);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (13, 'Los Angeles Clippers', 1984, 'Los Angeles', 13, 13);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (25, 'Portland Trail Blazers', 1970, 'Portland', 25, 25);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (3, 'Brooklyn Nets', 2012, 'Brooklyn', 3, 3);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (30, 'Washington Wizards', 1997, 'Washington', 30, 30);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (4, 'Chicago Bulls', 1966, 'Chicago', 4, 4);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (27, 'San Antonio Spurs', 1976, 'San Antonio', 27, 27);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (28, 'Toronto Raptors', 1995, 'Toronto', 28, 28);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (6, 'Cleveland Cavaliers', 1970, 'Cleveland', 6, 6);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (22, 'Orlando Magic', 1989, 'Orlando', 22, 22);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (5, 'Charlotte Hornets', 1988, 'Charlotte', 5, 5);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (11, 'Houston Rockets', 1971, 'Houston', 11, 11);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (9, 'Detroit Pistons', 1957, 'Detroit', 9, 9);
INSERT INTO team (t_teamid, t_tname, t_foundyear, t_city, t_coachid, t_stadiumid) VALUES (16, 'Miami Heat', 1988, 'Miami', 16, 16);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
