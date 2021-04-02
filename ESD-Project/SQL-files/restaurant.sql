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
CREATE DATABASE IF NOT EXISTS `restaurant` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `restaurant`;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurant`
--

-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
CREATE TABLE IF NOT EXISTS `restaurant` (
  `restaurantID` varchar(64) NOT NULL,
  `name` varchar(64) NOT NULL,
  `branch` varchar(8) NOT NULL,
  `category` varchar(64) NOT NULL,
  `location` varchar(64) NOT NULL,
  `description` varchar(10000) NOT NULL,
  `rating` double NOT NULL,
  `ratingCount` double NOT NULL,
  `image` varchar(500) DEFAULT NULL,
  `email` varchar(500) NOT NULL,
  PRIMARY KEY (`restaurantID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` (`restaurantID`, `name`, `branch`, `category`, `location`, `description`, `rating`, `ratingCount`,`image`,`email`) VALUES
('EighteenChefz', '18 Chefs', 'Novena S', 'Western Cuisine', 'Novena Square #03-12', '18 Chef is a fine dining restaurant for cheap teenagers', 4.1,55, 'EighteenChefz.jpg','toktzekiat@gmail.com'),
('Mala123', 'Watashiwa Mala', 'Lot 1', 'Chinese Cuisine', 'Lot 1 #01-11', 'Super hot mala for insecure teens', 3.7,12, 'Mala123.jpg','toktzekiat@gmail.com'),
('Weizhi', 'Wei Zhi China Wine', 'Yew Tee ', 'Wine', 'Yew Tee #B0-01', 'Wei Zhi`s china wine has orginated back from the bodoh dynstasty....', 4.8,33, 'WeiZhi.jpg','toktzekiat@gmail.com'),
('XJWangz', 'Wang`s and Wank`s', 'Tekong', 'Chinese Cuisine', 'Tekong Ferry', 'Eat some tekong boys like xing jie', 1, 21 ,'XJWangz.jpg','toktzekiat@gmail.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

