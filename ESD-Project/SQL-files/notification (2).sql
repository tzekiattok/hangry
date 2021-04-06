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
CREATE DATABASE IF NOT EXISTS `notification` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `notification`;


DROP TABLE IF EXISTS `notification`;
CREATE TABLE IF NOT EXISTS `notification` (
  `notificationNum` int AUTO_INCREMENT NOT NULL,
  `reservationID` int NOT NULL,
  `receiverId` varchar(64) NOT NULL,
  `customerId` varchar(64) NOT NULL,
  `restaurantId` varchar(64) NOT NULL,
  `reservationDate` varchar(64) NOT NULL,
  `reservationTime` varchar(64) DEFAULT NULL,
  `duration` varchar(64) NOT NULL,
  `status` varchar(64) NOT NULL,
  PRIMARY KEY (`notificationNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
