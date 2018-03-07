-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 13, 2014 at 05:07 PM
-- Server version: 5.6.17
-- PHP Version: 5.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bitcoin`
--

-- --------------------------------------------------------

--
-- Table structure for table `blocks`
--

CREATE TABLE IF NOT EXISTS `blocks` (
  `dbindex` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `block_index` int(11) NOT NULL,
  `block_date` datetime NOT NULL,
  `block_received_time` datetime NOT NULL,
  `height` int(11) NOT NULL,
  `hash` char(64) NOT NULL,
  `bits` bigint(20) NOT NULL,
  `n_tx` int(11) NOT NULL,
  `fee` bigint(20) NOT NULL,
  `size` bigint(20) NOT NULL,
  `main_chain` tinyint(1) NOT NULL,
  `relayed_by` varchar(15) NOT NULL,
  PRIMARY KEY (`dbindex`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Informació dels blocs' AUTO_INCREMENT=3671 ;

--
-- Table structure for table `transaccions`
--

CREATE TABLE IF NOT EXISTS `transaccions` (
  `dbindex` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `block_index` int(11) NOT NULL,
  `block_date` datetime NOT NULL,
  `Altura` int(11) NOT NULL,
  `hash` char(64) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `tx_hash` char(64) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `tx_index` int(11) NOT NULL,
  `relayed_by` varchar(15) NOT NULL,
  `tx_date` datetime NOT NULL,
  `n_inputs` int(11) NOT NULL,
  `input` bigint(20) NOT NULL,
  `n_outputs` int(11) NOT NULL,
  `output` bigint(20) NOT NULL,
  `fee` bigint(20) NOT NULL,
  `temps` int(11) NOT NULL,
  PRIMARY KEY (`dbindex`),
  UNIQUE KEY `dbindex` (`dbindex`),
  KEY `block_index` (`block_index`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1415235 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

