-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2022 at 03:46 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pollution_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `readings`
--

CREATE TABLE `readings` (
  `readingid` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `nox` float DEFAULT NULL,
  `no2` float DEFAULT NULL,
  `no` float DEFAULT NULL,
  `pm10` float DEFAULT NULL,
  `nvpm10` float DEFAULT NULL,
  `vpm` float DEFAULT NULL,
  `mvpm` float DEFAULT NULL,
  `pm2.5` float DEFAULT NULL,
  `vpm2.5` float DEFAULT NULL,
  `co` float DEFAULT NULL,
  `o3` float DEFAULT NULL,
  `so2` float DEFAULT NULL,
  `temperature` double DEFAULT NULL,
  `rh` int(11) DEFAULT NULL,
  `airpressure` int(11) DEFAULT NULL,
  `datestart` datetime DEFAULT NULL,
  `dateend` datetime DEFAULT NULL,
  `current` text DEFAULT NULL,
  `instrumenttype` varchar(32) DEFAULT NULL,
  `stationid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `schema`
--

CREATE TABLE `schema` (
  `measure` varchar(32) NOT NULL,
  `description` varchar(64) NOT NULL,
  `unit` varchar(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `stations`
--

CREATE TABLE `stations` (
  `stationid` int(11) NOT NULL,
  `location` varchar(48) NOT NULL,
  `geo_point_2d` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `readings`
--
ALTER TABLE `readings`
  ADD PRIMARY KEY (`readingid`),
  ADD KEY `stationid` (`stationid`);

--
-- Indexes for table `schema`
--
ALTER TABLE `schema`
  ADD PRIMARY KEY (`measure`);

--
-- Indexes for table `stations`
--
ALTER TABLE `stations`
  ADD PRIMARY KEY (`stationid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `readings`
--
ALTER TABLE `readings`
  ADD CONSTRAINT `stationid` FOREIGN KEY (`stationid`) REFERENCES `stations` (`stationid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
