-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS `menu` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `menu`;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `menu`;
CREATE TABLE IF NOT EXISTS `menu`(
	`menuid` int NOT NULL,
    `itemid` int NOT NULL,
    `restaurantid` varchar(64) NOT NULL,
    `category` varchar(64) NOT NULL,
    `itemname` varchar(64) NOT NULL,
    `description` varchar(64) NOT NULL,
    `price` decimal(10,2) NOT NULL,
    `image` varchar(1024) NOT NULL,
    PRIMARY KEY(`menuid`,`itemid`, `restaurantid`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`menuid`, `itemid`, `restaurantid`, `category`, `itemname`, `description`, `price`, `image`) VALUES
( 1, 1, 'EighteenChefz', 'Mains', 'Chicken Rice', 'A plate of chicken with rice', 24.99, 'static/menuImage/chickenrice.jpg' ),
( 1, 2, 'EighteenChefz', 'Mains', 'Laksa', 'A bowl of curry noodles', 1.99, 'static/menuImage/laksa.jpg' ),

( 2, 1, 'Mala123', 'Mains', 'Mala Bowl', 'A bowl of mala things', 17.99, 'static/menuImags/malabowl.jpg' ),
( 2, 2, 'Mala123', 'Drinks', 'Mala Drink', 'A drink of mala sauce', 120.99, 'static/menuImage/maladrink.jpg' ),


( 3, 1, 'Weizhi', 'Mains', 'Duck Rice', 'A plate of duck with rice', 6.99, 'static/menuImage/duckrice.jpg' ),
( 3, 2, 'Weizhi', 'Mains', 'Yong Tao Foo', 'A bowl of healthy goodness', 5.99, 'static/menuImage/yongtaofoo.jpg' ),

( 4, 1, 'XJWangz', 'Mains', 'Wang Specialty', 'Order to find out', 24.99, 'static/menuImage/wangspecialty.jpg' ),
( 4, 2, 'XJWangz', 'Sides', 'Chicken Wang', 'A plate of wang wangs', 54.99, 'static/menuImage/chickenwang.jpg' );


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
