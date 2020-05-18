-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2020-05-07 09:53:52
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
-- 資料庫： `test`
--

-- --------------------------------------------------------

--
-- 資料表結構 `frinend`
--

CREATE TABLE `frinend` (
  `no` smallint(6) NOT NULL,
  `name` varchar(5) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `sex` char(1) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `age` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `star_signs` varchar(3) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `height` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `weight` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `career` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `frinend`
--

INSERT INTO `frinend` (`no`, `name`, `sex`, `age`, `star_signs`, `height`, `weight`, `career`) VALUES
(1, '小燕子', '女', '20~25', '牡羊座', '155~160', '45~50', '上班族'),
(2, '雲翔', '男', '20~25', '天蠍座', '175~180', '65~70', 'SOHO族'),
(3, '莫昭奴', '男', '25~30', '天秤座', '175~180', '65~70', '上班族'),
(4, '葉小釵', '男', '30~35', '摩羯座', '165~170', '60~65', '老師'),
(5, '流川楓', '女', '15~20', '射手座', '160~165', '45~50', '上班族');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `frinend`
--
ALTER TABLE `frinend`
  ADD PRIMARY KEY (`no`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `frinend`
--
ALTER TABLE `frinend`
  MODIFY `no` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
