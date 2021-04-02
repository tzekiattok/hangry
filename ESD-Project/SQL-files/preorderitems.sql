-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 06, 2021 at 08:45 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
CREATE DATABASE IF NOT EXISTS `preorderitems` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `preorderitems`;



DROP TABLE IF EXISTS `preorderitems`;
CREATE TABLE IF NOT EXISTS `preorderitems` (
  `itemID` int AUTO_INCREMENT NOT NULL ,
  `orderID` int NOT NULL ,
  `itemName` varchar(64) NOT NULL,
  `price` decimal NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`itemID`,`orderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
--

INSERT INTO `preorderitems` (`orderID`, `itemName`, `quantity`) VALUES
(1, 'Chicken Nuggets', 2),
(1, 'Popcorn Chicken', 6),
(1, 'Striploin', 3),
(2, 'BBQ Chicken', 5),
(2, 'Teriyaki Salmon', 2),
(3, 'Fish & Chips', 1),
(4, 'Salted Egg Prawn Pasta', 2),
(5, 'BBQ Chicken', 2),
(5, 'Chicken Nuggets', 4),
(6, 'Classic Fish Burger', 2),
(6, 'Fish & Chips', 3),
(7, 'Popcorn Chicken', 1),
(8, 'Ribeye', 1),
(8, 'Beef Burger', 1),
(9, 'Striploin', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;