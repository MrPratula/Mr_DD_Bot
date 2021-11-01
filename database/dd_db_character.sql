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
-- Table structure for table `character`
--

DROP TABLE IF EXISTS `character`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character` (
  `char_id` int NOT NULL AUTO_INCREMENT,
  `char_name` varchar(255) NOT NULL,
  `strength` int DEFAULT NULL,
  `strength_saving_throw` bit(1) DEFAULT b'0',
  `athletics` bit(1) DEFAULT b'0',
  `dexterity` int DEFAULT NULL,
  `dexterity_saving_throw` bit(1) DEFAULT b'0',
  `acrobatics` bit(1) DEFAULT b'0',
  `sleight_of_hand` bit(1) DEFAULT b'0',
  `stealth` bit(1) DEFAULT b'0',
  `constitution` int DEFAULT NULL,
  `constitution_saving_throw` bit(1) DEFAULT b'0',
  `intelligence` int DEFAULT NULL,
  `intelligence_saving_throw` bit(1) DEFAULT b'0',
  `arcana` bit(1) DEFAULT b'0',
  `history` bit(1) DEFAULT b'0',
  `investigation` bit(1) DEFAULT b'0',
  `nature` bit(1) DEFAULT b'0',
  `religion` bit(1) DEFAULT b'0',
  `wisdom` int DEFAULT NULL,
  `wisdom_saving_throw` bit(1) DEFAULT b'0',
  `animal_handling` bit(1) DEFAULT b'0',
  `insight` bit(1) DEFAULT b'0',
  `medicine` bit(1) DEFAULT b'0',
  `perception` bit(1) DEFAULT b'0',
  `survival` bit(1) DEFAULT b'0',
  `charisma` int DEFAULT NULL,
  `charisma_saving_throw` bit(1) DEFAULT b'0',
  `deception` bit(1) DEFAULT b'0',
  `intimidation` bit(1) DEFAULT b'0',
  `performance` bit(1) DEFAULT b'0',
  `persuasion` bit(1) DEFAULT b'0',
  `proficiency` int DEFAULT NULL,
  `class` varchar(255) DEFAULT NULL,
  `life` int NOT NULL DEFAULT '10',
  `level` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`char_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character`
--

LOCK TABLES `character` WRITE;
/*!40000 ALTER TABLE `character` DISABLE KEYS */;
/*!40000 ALTER TABLE `character` ENABLE KEYS */;
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
