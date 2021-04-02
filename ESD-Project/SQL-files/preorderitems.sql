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
  `orderID` varchar(64) NOT NULL ,
  `itemName` varchar(64) NOT NULL,
  `price` decimal NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`itemID`,`orderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
--

INSERT INTO `preorderitems` (`orderID`, `itemName`, `price`, `quantity`) VALUES
('1', 'Chicken Nuggets', 4.50, 2),
('1', 'Popcorn Chicken', 5.50, 6),
('1', 'Striploin', 13.80, 3),
('2', 'BBQ Chicken', 15.00, 5),
('2', 'Teriyaki Salmon', 7.50, 2),
('3', 'Fish & Chips', 8.50, 1),
('4', 'Salted Egg Prawn Pasta', 9.00, 2),
('5', 'BBQ Chicken', 15.00, 2),
('5', 'Chicken Nuggets', 4.50, 4),
('6', 'Classic Fish Burger', 7.00, 2),
('6', 'Fish & Chips', 8.50, 3),
('7', 'Popcorn Chicken', 5.50, 1),
('8', 'Ribeye', 17.30, 1),
('8', 'Beef Burger', 9.50, 1),
('9', 'Striploin', 13.80, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;