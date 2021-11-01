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
-- Table structure for table `cantrip`
--

DROP TABLE IF EXISTS `cantrip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cantrip` (
  `name` varchar(255) NOT NULL,
  `text` text,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cantrip`
--

LOCK TABLES `cantrip` WRITE;
/*!40000 ALTER TABLE `cantrip` DISABLE KEYS */;
INSERT INTO `cantrip` VALUES ('acid_splash','{name} hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.\n\nSpell save DC = {spell_save_dc}\nDamage = {xd6}'),('chill_touch','{name} create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can’t regain hit points until the start of your next turn. Until then, the hand clings to the target. If {name} hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.\n\nSpell attack = {spell_attack}\nAdvantage/Disadvantage = {spell_attack}\nDamage = {xd8}'),('eldritch_blast','A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage.\n\nSpell attack = {spell_attack}\nAdvantage/Disadvantage = {spell_attack}\nDamage = {xd10}'),('fire_bolt','{name} hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn’t being worn or carried.\n\nSpell attack = {spell_attack}\nAdvantage/Disadvantage = {spell_attack}\nDamage = {xd10}'),('poison_spray','{name} extend his hand toward a creature he can see within range and project a puff of noxious gas from his palm. The creature must succeed on a Constitution saving throw or take 1d12 poison damage.\n\nSpell save DC = {spell_save_dc}\nDamage = {xd12}'),('produce_flame','A flickering flame appears in {name}\'s hand. The flame remains there for the duration and harms neither you nor your equipment. The flame sheds bright light in a 10-foot radius and dim light for an additional 10 feet. The spell ends if you dismiss it as an action or if you cast it again.\n\nYou can also attack with the flame, although doing so ends the spell. When you cast this spell, or as an action on a later turn, you can hurl the flame at a creature within 30 feet of you. Make a ranged spell attack. On a hit, the target takes 1d8 fire damage.\n\nSpell attack = {spell_attack}\nAdvantage/Disadvantage = {spell_attack}\nDamage = {xd8}'),('ray_of_frost','A frigid beam of blue-white light streaks toward a creature within range. {name} make a ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by 10 feet until the start of your next turn.\n\nSpell attack = {spell_attack}\nAdvantage/Disadvantage = {spell_attack}\nDamage = {xd8}'),('sacred_flame','Flame-like radiance descends on a creature that {name} can see within range. The target must succeed on a Dexterity saving throw or take 1d8 radiant damage. The target gains no benefit from cover for this saving throw.\n\nSpell save DC = {spell_save_dc}\nDamage = {xd8}'),('shocking_grasp','Lightning springs from {name}\'s hand to deliver a shock to a creature he try to touch. Make a melee spell attack against the target. You have advantage on the attack roll if the target is wearing armor made of metal. On a hit, the target takes 1d8 lightning damage, and it can’t take reactions until the start of its next turn.\n\nSpell attack = {spell_attack}\nAdvantage/Disadvantage = {spell_attack}\nDamage = {xd8}'),('thorn_whip','{name} create a long, vine-like whip covered in thorns that lashes out at your command toward a creature in range. Make a melee spell attack against the target. If the attack hits, the creature takes 1d6 piercing damage, and if the creature is Large or smaller, you pull the creature up to 10 feet closer to you.\n\nSpell attack = {spell_attack}\nAdvantage/Disadvantage = {spell_attack}\nDamage = {xd6}'),('vicious_mockery','{name} unleash a string of insults laced with subtle enchantments at a creature you can see within range. If the target can hear you (though it need not understand you), it must succeed on a Wisdom saving throw or take 1d4 psychic damage and have disadvantage on the next attack roll it makes before the end of its next turn.\n\nSpell save DC = {spell_save_dc}\nDamage = {xd4}');
/*!40000 ALTER TABLE `cantrip` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-01 16:55:56
