CREATE TABLE coaches (
    c_cid identity(1, 1) primary key,
    c_name varchar(50),
    c_startyear date not null,
    c_numofchamp int
)

CREATE TABLE stadium (
    st_stname identity(1, 1) primary key,
    st_size int,
    st_location varchar(50)
)

CREATE TABLE team (
    t_tname identity(1, 1) primary key,
    t_foundyear date not null,
    t_city varchar(50),
    t_cid int, 
    t_manager varchar(50),
    t_stname int
)