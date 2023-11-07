CREATE TABLE coaches (
    c_coachid identity(1, 1) primary key,
    c_name varchar(50),
    c_startyear date not null,
    c_numofchamp int
)

CREATE TABLE stadium (
    st_stadiumid identity(1, 1) primary key,
    st_name varchar(50),
    st_size int,
    st_location varchar(50)
)

CREATE TABLE team (
    t_teamid identity(1, 1) primary key,
    t_tname varchar(50),
    t_foundyear date not null,
    t_city varchar(50),
    t_cid int, 
    t_stid int
)
