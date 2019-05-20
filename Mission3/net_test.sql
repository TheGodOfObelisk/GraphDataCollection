-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: net_test
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Addresscontent` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Adjacent_attack`
--

DROP TABLE IF EXISTS `Adjacent_attack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Adjacent_attack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Attack`
--

DROP TABLE IF EXISTS `Attack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Attack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AttackInfo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Attacker`
--

DROP TABLE IF EXISTS `Attacker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Attacker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AttackerInfo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `DNSName`
--

DROP TABLE IF EXISTS `DNSName`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DNSName` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DNSNameContent` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Edges`
--

DROP TABLE IF EXISTS `Edges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Edges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) DEFAULT NULL,
  `in_vertex_id` int(11) DEFAULT NULL,
  `out_vertex_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `edge_unique` (`type`,`in_vertex_id`,`out_vertex_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1115 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Hardware`
--

DROP TABLE IF EXISTS `Hardware`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Hardware` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `IP`
--

DROP TABLE IF EXISTS `IP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `IP` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Local_attack`
--

DROP TABLE IF EXISTS `Local_attack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Local_attack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Malicious Domains`
--

DROP TABLE IF EXISTS `Malicious Domains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Malicious Domains` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `ip_address` int(20) DEFAULT NULL,
  `MaliciousDomains` varchar(255) DEFAULT NULL,
  `describe` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Malware`
--

DROP TABLE IF EXISTS `Malware`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Malware` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  `Risk_Impact` varchar(10) DEFAULT NULL,
  `Updated` varchar(45) DEFAULT NULL,
  `pubDate` varchar(15) DEFAULT NULL,
  `Version` varchar(30) DEFAULT NULL,
  `Publisher` varchar(60) DEFAULT NULL,
  `File_Names` varchar(110) DEFAULT NULL,
  `Discovered` varchar(20) DEFAULT NULL,
  `Also_Known_As` varchar(35) DEFAULT NULL,
  `Characteristics` varchar(65) DEFAULT NULL,
  `Region_Reported` varchar(30) DEFAULT NULL,
  `Area_of_infection` varchar(65) DEFAULT NULL,
  `Likelihood` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `origin_id` int(11) DEFAULT '-1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1173 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `OS`
--

DROP TABLE IF EXISTS `OS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Name_UNIQUE` (`Name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Physical_attack`
--

DROP TABLE IF EXISTS `Physical_attack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Physical_attack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Remote_attack`
--

DROP TABLE IF EXISTS `Remote_attack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Remote_attack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `application`
--

DROP TABLE IF EXISTS `application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bid`
--

DROP TABLE IF EXISTS `bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bid` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `bidNumber` varchar(2000) DEFAULT NULL,
  `bidUrl` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `number` (`number`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=29800 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cnvd`
--

DROP TABLE IF EXISTS `cnvd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cnvd` (
  `id` int(20) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `serverity` varchar(255) DEFAULT NULL,
  `isEvent` varchar(2000) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  `submitTime` varchar(255) DEFAULT NULL,
  `openTime` varchar(255) DEFAULT NULL,
  `discovererName` varchar(2000) DEFAULT NULL,
  `referenceLink` varchar(2000) DEFAULT NULL,
  `formalWay` varchar(2000) DEFAULT NULL,
  `patchName` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `number_bid` (`number`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=122387 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cve`
--

DROP TABLE IF EXISTS `cve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cve` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `cveNumber` varchar(255) DEFAULT NULL,
  `cveUrl` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `number` (`number`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=84100 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cvssBaseMetrics`
--

DROP TABLE IF EXISTS `cvssBaseMetrics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cvssBaseMetrics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) DEFAULT NULL,
  `score` varchar(255) DEFAULT NULL,
  `accessVector` varchar(255) DEFAULT NULL,
  `accessComplexity` varchar(255) DEFAULT NULL,
  `authentication` varchar(255) DEFAULT NULL,
  `confidentialityImpact` varchar(255) DEFAULT NULL,
  `integrityImpact` varchar(255) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `generatedOnDatetime` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=110495 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `entry`
--

DROP TABLE IF EXISTS `entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) DEFAULT NULL,
  `publishedDatetime` varchar(255) DEFAULT NULL,
  `lastModifiedDatetime` varchar(255) DEFAULT NULL,
  `cweId` varchar(255) DEFAULT NULL,
  `summary` text,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=538732 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `product` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `number` (`number`) USING BTREE,
  KEY `product` (`product`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=88022 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reference`
--

DROP TABLE IF EXISTS `reference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reference` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) DEFAULT NULL,
  `cweId` varchar(255) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `referenceHref` text,
  `lang` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=116745 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `solution`
--

DROP TABLE IF EXISTS `solution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `solution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `solutionInfo` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `symantec`
--

DROP TABLE IF EXISTS `symantec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `symantec` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `x_description` varchar(45) DEFAULT NULL,
  `x_link` varchar(100) DEFAULT NULL,
  `x_title` varchar(45) DEFAULT NULL,
  `Updated` varchar(45) DEFAULT NULL,
  `Risk_Impact` varchar(10) DEFAULT NULL,
  `Infection_Length` varchar(45) DEFAULT NULL,
  `x_pubDate` varchar(15) DEFAULT NULL,
  `Type` varchar(45) DEFAULT NULL,
  `System_Affected` varchar(100) DEFAULT NULL,
  `Name` varchar(75) DEFAULT NULL,
  `Writeup_By` varchar(55) DEFAULT NULL,
  `Version` varchar(30) DEFAULT NULL,
  `Publisher` varchar(60) DEFAULT NULL,
  `File_Names` varchar(110) DEFAULT NULL,
  `Discovered` varchar(20) DEFAULT NULL,
  `Also_Known_As` varchar(110) DEFAULT NULL,
  `Target_Platform` varchar(35) DEFAULT NULL,
  `Characteristics` varchar(65) DEFAULT NULL,
  `Region_Reported` varchar(30) DEFAULT NULL,
  `Area_of_infection` varchar(65) DEFAULT NULL,
  `Likelihood` varchar(45) DEFAULT NULL,
  `Package_name` varchar(25) DEFAULT NULL,
  `CVE_References` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1186 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vertex`
--

DROP TABLE IF EXISTS `vertex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vertex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(11) DEFAULT NULL,
  `id_search` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idvertex_UNIQUE` (`id`),
  UNIQUE KEY `vertex_unique` (`type`,`id_search`)
) ENGINE=InnoDB AUTO_INCREMENT=2229 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vulnerableSoftwareList`
--

DROP TABLE IF EXISTS `vulnerableSoftwareList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vulnerableSoftwareList` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(255) DEFAULT NULL,
  `product` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=260918 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-20 16:20:31
