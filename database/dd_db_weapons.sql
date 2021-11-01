CREATE DATABASE  IF NOT EXISTS `dd_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dd_db`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: dd_db
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `weapons`
--

DROP TABLE IF EXISTS `weapons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weapons` (
  `name` varchar(255) NOT NULL,
  `damage` varchar(4) NOT NULL,
  `type` varchar(255) NOT NULL,
  `versatile_dmg` varchar(4) DEFAULT NULL,
  `mod` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weapons`
--

LOCK TABLES `weapons` WRITE;
/*!40000 ALTER TABLE `weapons` DISABLE KEYS */;
INSERT INTO `weapons` VALUES ('battleaxe','1d8','martial','1d10','strength'),('blowgun','1','martial_ranged',NULL,'dexterity'),('club','1d4','simple',NULL,'strength'),('crossbow_hand','1d6','martial_ranged',NULL,'dexterity'),('crossbow_heavy','1d10','martial_ranged',NULL,'dexterity'),('crossbow_light','1d8','simple_ranged',NULL,'dexterity'),('dagger','1d4','simple',NULL,'finesse'),('dart','1d4','simple_ranged',NULL,'finesse'),('flail','1d8','martial',NULL,'strength'),('glaive','1d10','martial',NULL,'strength'),('great_club','1d8','simple',NULL,'strength'),('great_sword','2d6','martial',NULL,'strength'),('greataxe','1d12','martial',NULL,'strength'),('halberd','1d10','martial',NULL,'strength'),('hand_axe','1d6','simple',NULL,'strength'),('javelin','1d6','simple',NULL,'strength'),('lance','1d12','martial',NULL,'strength'),('light_hammer','1d4','simple',NULL,'strength'),('long_sword','1d8','martial','1d10','strength'),('longbow','1d8','martial_ranged',NULL,'dexterity'),('mace','1d6','simple',NULL,'strength'),('maul','2d6','martial',NULL,'strength'),('morning_star','1d8','martial',NULL,'strength'),('pike','1d10','martial',NULL,'strength'),('quarterstaff','1d6','simple','1d8','strength'),('rapier','1d8','martial',NULL,'finesse'),('scimmitar','1d6','martial',NULL,'finesse'),('short_bow','1d6','simple_ranged',NULL,'dexterity'),('short_sword','1d6','martial',NULL,'finesse'),('sickle','1d4','simple',NULL,'strength'),('sling','1d4','simple_ranged',NULL,'dexterity'),('spear','1d6','simple','1d8','strength'),('trident','1d6','martial','1d8','strength'),('war_hammer','1d8','martial','1d10','strength'),('war_pick','1d8','martial',NULL,'strength'),('whip','1d4','martial',NULL,'finesse');
/*!40000 ALTER TABLE `weapons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-01 16:55:55
