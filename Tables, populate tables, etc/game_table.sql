CREATE TABLE game (
    g_gameid identity(1, 1) primary key,
    g_home int,
    g_away int,
    g_date date not null,
    g_winner int,
    g_score varchar(50),
    g_stadiumid int
);

INSERT INTO game (g_gameid, g_home, g_away, g_date, g_winner, g_score, g_stadium)

VALUES

(1, 2, 23, '2022-10-18', 2, '126(H) - 117(A)', 2),
(2, 10, 14, '2022-10-18', 10, '123(H) - 109(A)', 10),

(3, 9, 22, '2022-10-19', 9, '113(H) - 109(A)', 9),
(4, 12, 30, '2022-10-19', 30, '114(A) - 107(H)', 12),
(5, 1, 11, '2022-10-19', 1, '117(H) - 107(A)', 1),
(6, 3, 19, '2022-10-19', 19, '130(A) - 108(H)', 3),
(7, 15, 20, '2022-10-19', 15, '115(H) - 112(A)', 15),
(8, 16, 4, '2022-10-19', 4, '116(A) - 108(H)', 16),
(9, 28, 6, '2022-10-19', 28, '108(H) - 105(A)', 28),
(10, 18, 21, '2022-10-19', 18, '115(H) - 108(A)', 18),
(11, , , '2022-10-19', , '', ),
(12, , , '2022-10-19', , '', ),
(13, , , '2022-10-19', , '', ),
(14, , , '2022-10-19', , '', ),

(15, , , '2022-10-20', , '', ),
(16, , , '2022-10-20', , '', ),

(17, , , '2022-10-21', , '', ),
(18, , , '2022-10-21', , '', ),
(19, , , '2022-10-21', , '', ),
(20, , , '2022-10-21', , '', ),
(21, , , '2022-10-21', , '', ),
(22, , , '2022-10-21', , '', ),
(23, , , '2022-10-21', , '', ),
(24, , , '2022-10-21', , '', ),
(25, , , '2022-10-21', , '', ),
(26, , , '2022-10-21', , '', ),
(27, , , '2022-10-21', , '', ),

(28, , , '2022-10-22', , '', ),
(29, , , '2022-10-22', , '', ),
(30, , , '2022-10-22', , '', ),
(31, , , '2022-10-22', , '', ),
(32, , , '2022-10-22', , '', ),
(33, , , '2022-10-22', , '', ),
(34, , , '2022-10-22', , '', ),
(35, , , '2022-10-22', , '', ),
(36, , , '2022-10-22', , '', ),

(37, , , '2022-10-23', , '', ),
(38, , , '2022-10-23', , '', ),
(39, , , '2022-10-23', , '', ),
(40, , , '2022-10-23', , '', ),
(41, , , '2022-10-23', , '', ),
(42, , , '2022-10-23', , '', ),
(43, , , '2022-10-23', , '', ),

(44, , , '2022-10-24', , '', ),
(45, , , '2022-10-24', , '', ),
(46, , , '2022-10-24', , '', ),
(47, , , '2022-10-24', , '', ),
(48, , , '2022-10-24', , '', ),
(49, , , '2022-10-24', , '', ),
(50, , , '2022-10-24', , '', ),
(51, , , '2022-10-24', , '', ),

(52, , , '2022-10-25', , '', ),
(53, , , '2022-10-25', , '', ),
(54, , , '2022-10-25', , '', ),
(55, , , '2022-10-25', , '', ),

(56, , , '2022-10-26', , '', ),
(57, , , '2022-10-26', , '', ),
(58, , , '2022-10-26', , '', ),
(59, , , '2022-10-26', , '', ),
(60, , , '2022-10-26', , '', ),
(61, , , '2022-10-26', , '', ),
(62, , , '2022-10-26', , '', ),
(63, , , '2022-10-26', , '', ),
(64, , , '2022-10-26', , '', ),
(65, , , '2022-10-26', , '', ),

(66, , , '2022-10-27', , '', ),
(67, , , '2022-10-27', , '', ),
(68, , , '2022-10-27', , '', ),
(69, , , '2022-10-27', , '', ),

(70, , , '2022-10-28', , '', ),
(71, , , '2022-10-28', , '', ),
(72, , , '2022-10-28', , '', ),
(73, , , '2022-10-28', , '', ),
(74, , , '2022-10-28', , '', ),
(75, , , '2022-10-28', , '', ),
(76, , , '2022-10-28', , '', ),
(77, , , '2022-10-28', , '', ),
(78, , , '2022-10-28', , '', ),
(79, , , '2022-10-28', , '', ),
(80, , , '2022-10-28', , '', ),

(81, , , '2022-10-29', , '', ),
(82, , , '2022-10-29', , '', ),
(83, , , '2022-10-29', , '', ),
(84, , , '2022-10-29', , '', ),
(85, , , '2022-10-29', , '', ),
(86, , , '2022-10-29', , '', ),
(87, , , '2022-10-29', , '', ),

(88, , , '2022-10-30', , '', ),
(89, , , '2022-10-30', , '', ),
(90, , , '2022-10-30', , '', ),
(91, , , '2022-10-30', , '', ),
(92, , , '2022-10-30', , '', ),
(93, , , '2022-10-30', , '', ),
(94, , , '2022-10-30', , '', ),
(95, , , '2022-10-30', , '', ),

(96, , , '2022-10-31', , '', ),
(97, , , '2022-10-31', , '', ),
(98, , , '2022-10-31', , '', ),
(99, , , '2022-10-31', , '', ),
(100, , , '2022-10-31', , '', ),
(101, , , '2022-10-31', , '', ),
(102, , , '2022-10-31', , '', ),