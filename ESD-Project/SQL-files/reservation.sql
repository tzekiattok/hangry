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
CREATE DATABASE IF NOT EXISTS `reservation` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `reservation`;



DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `reservationID` int AUTO_INCREMENT NOT NULL ,
  `restaurantID` varchar(64) NOT NULL,
  `customerID` varchar(64) DEFAULT NULL,
  `capacity` int NOT NULL,
  `date` Date NOT NULL,
  `time` time NOT NULL,
  `status` varchar(64) NOT NULL,
  `duration` float NOT NULL,
  PRIMARY KEY (`reservationID`,`restaurantID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
--

INSERT INTO `reservation` (`restaurantID`, `capacity`, `date`, `time`,`duration`, `status`,`customerID`) VALUES
('EighteenChefz', 4, '2021-04-01', '12:00:00', 2.00, 'pending', 'cornyho123'),
('EighteenChefz', 4, '2021-04-01', '14:00:00', 2.00, 'pending','cornyho123'),
('EighteenChefz', 4, '2021-04-01', '16:00:00', 2.00, 'pending','Bartok'),
('EighteenChefz', 2, '2021-04-01', '18:00', 2.00, 'pending', 'cornyho123'),
('EighteenChefz', 4, '2021-04-01', '20:00', 2.00, 'open',NULL),
('EighteenChefz', 6, '2021-04-02', '12:00', 2.00, 'open',NULL),
('EighteenChefz', 6, '2021-04-02', '14:00', 2.00, 'open',NULL),
('EighteenChefz', 6, '2021-04-02', '16:00', 2.00, 'open',NULL),
('EighteenChefz', 6, '2021-04-02', '18:00', 2.00, 'open',NULL),
('EighteenChefz', 6, '2021-04-02', '20:00', 2.00, 'open',NULL),
('Mala123', 4, '2021-04-01', '11:00', 1.00, 'open',NULL),
('Mala123', 5, '2021-04-02', '12:00', 1.00, 'open',NULL),
('Mala123', 6, '2021-04-02', '13:00', 1.00, 'open',NULL),
('Mala123', 6, '2021-04-03', '14:00', 1.00, 'open',NULL),
('Weizhi', 6, '2021-04-03', '14:00', 3.00, 'open',NULL),
('Weizhi', 4, '2021-04-03', '14:00', 1.00, 'open',NULL),
('Weizhi', 4, '2021-04-03', '15:00', 1.00, 'open',NULL),
('Weizhi', 2, '2021-04-03', '16:00', 1.00, 'open',NULL),
('XJWangz', 8,'2021-04-04', '13:00', 1.00, 'open',NULL),
('XJWangz', 12, '2021-04-04', '14:00', 1.00, 'open',NULL),
('XJWangz', 5, '2021-04-04', '18:00', 1.00, 'open',NULL),
('XJWangz', 4, '2021-04-04', '18:00', 1.00, 'open',NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
