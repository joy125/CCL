-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2020-05-14 08:28:18
-- 伺服器版本： 10.4.11-MariaDB
-- PHP 版本： 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `ass`
--

-- --------------------------------------------------------

--
-- 資料表結構 `a123`
--

CREATE TABLE `a123` (
  `c_ID` int(11) NOT NULL DEFAULT 0,
  `Name` varchar(255) DEFAULT '未知',
  `Phone` varchar(20) DEFAULT NULL,
  `Address` varchar(10) NOT NULL,
  `intt` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `a123`
--

INSERT INTO `a123` (`c_ID`, `Name`, `Phone`, `Address`, `intt`) VALUES
(1, 'a', '0900', '', NULL),
(2, 'b', '0800', '', NULL),
(3, 'c', '0222', '', NULL),
(4, 'd', NULL, '', NULL),
(5, '未知', NULL, '', 1),
(6, '未知', NULL, '', 1),
(7, '未知', NULL, '', 1),
(8, '未知', NULL, '', 1),
(9, '未知', NULL, '', 2),
(10, '未知', NULL, '', 1),
(11, '未知', NULL, '', 1),
(12, '未知', NULL, '', 1),
(13, '未知', NULL, '', 1),
(14, '未知', NULL, '', 2);

-- --------------------------------------------------------

--
-- 資料表結構 `customers`
--

CREATE TABLE `customers` (
  `c_ID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT '未知',
  `Phone` varchar(20) DEFAULT NULL,
  `Address` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `customers`
--

INSERT INTO `customers` (`c_ID`, `Name`, `Phone`, `Address`) VALUES
(1, 'a', '0900', ''),
(2, 'b', '0800', ''),
(3, 'c', '0222', ''),
(4, 'd', NULL, ''),
(5, '未知', NULL, ''),
(6, '未知', NULL, ''),
(7, '未知', NULL, ''),
(8, '未知', NULL, ''),
(9, '未知', NULL, ''),
(10, '未知', NULL, ''),
(11, '未知', NULL, ''),
(12, '未知', NULL, ''),
(13, '未知', NULL, ''),
(14, '未知', NULL, '');

-- --------------------------------------------------------

--
-- 資料表結構 `orders`
--

CREATE TABLE `orders` (
  `C_id` int(11) NOT NULL,
  `O_id` int(11) NOT NULL,
  `order_NO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `orders`
--

INSERT INTO `orders` (`C_id`, `O_id`, `order_NO`) VALUES
(3, 0, 9),
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(4, 5, 5),
(4, 6, 6),
(3, 10, 10);

-- --------------------------------------------------------

--
-- 資料表結構 `user2`
--

CREATE TABLE `user2` (
  `C_id` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 替換檢視表以便查看 `v`
-- (請參考以下實際畫面)
--
CREATE TABLE `v` (
`ID` int(11)
,`Name` varchar(255)
);

-- --------------------------------------------------------

--
-- 檢視表結構 `v`
--
DROP TABLE IF EXISTS `v`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v`  AS  select `customers`.`c_ID` AS `ID`,`customers`.`Name` AS `Name` from `customers` group by `customers`.`c_ID` ;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`c_ID`);

--
-- 資料表索引 `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`O_id`),
  ADD KEY `C_id` (`C_id`);

--
-- 資料表索引 `user2`
--
ALTER TABLE `user2`
  ADD PRIMARY KEY (`C_id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `customers`
--
ALTER TABLE `customers`
  MODIFY `c_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `C_id` FOREIGN KEY (`C_id`) REFERENCES `customers` (`c_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
