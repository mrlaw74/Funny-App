-- MySQL dump for login table

CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

-- Table structure for table `login`

DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `username` varchar(15) NOT NULL,
  `password` varchar(10) NOT NULL,
  `sec_que` varchar(100) NULL,
  `sec_ans` varchar(30) NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table `login`

LOCK TABLES `login` WRITE;
INSERT INTO `login` VALUES 
('username','password', NULL, NULL,'2021-08-13 01:34:25');
INSERT INTO `login` VALUES 
('mrlaw','123123123', NULL, NULL,'2024-09-20 11:34:25');
UNLOCK TABLES;
