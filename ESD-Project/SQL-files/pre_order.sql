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

-- Database: `book`
CREATE DATABASE IF NOT EXISTS `pre_order` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pre_order`;
-- --------------------------------------------------------

DROP TABLE IF EXISTS `pre_order`;
CREATE TABLE IF NOT EXISTS `pre_order` (
  orderID varchar (64) NOT NULL ,
  customerID varchar(64) NOT NULL,
  status varchar(30) NOT NULL,

  PRIMARY KEY (`orderID`,`customerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- DROP TABLE IF EXISTS `pre_order_items`;
-- CREATE TABLE IF NOT EXISTS `pre_order_items` (
--   `itemID` varchar(64) NOT NULL,
--   `itemName` varchar(64) NOT NULL,
--   `orderID` varchar(64) NOT NULL,
--   `price` int NOT NULL,
--   `quantity` int NOT NULL,

--   PRIMARY KEY (`orderID`)    
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `pre_order`
INSERT INTO `pre_order`(`customerID`,`orderID`, `status`) VALUES
('bhorbee', 'Order1', 'Confirmed'),
('Alvinng', 'Order2', 'Confirmed'),
('starsis', 'Order3', 'Confirmed'),
('sherry', 'Order4', 'Confirmed'),
('kelppy', 'Order5', 'Confirmed'),
('IMDYING', 'Order6', 'Confirmed')
;


COMMIT;
