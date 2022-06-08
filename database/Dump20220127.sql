CREATE DATABASE  IF NOT EXISTS `laboratory_department` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `laboratory_department`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: hospital-lab.mysql.database.azure.com    Database: laboratory_department
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `conducts`
--

DROP TABLE IF EXISTS `conducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conducts` (
  `LabTechSSn` varchar(255) NOT NULL,
  `TestID` int NOT NULL,
  PRIMARY KEY (`LabTechSSn`,`TestID`),
  KEY `TestID` (`TestID`),
  CONSTRAINT `conducts_ibfk_1` FOREIGN KEY (`LabTechSSn`) REFERENCES `lab_technician` (`SSN`),
  CONSTRAINT `conducts_ibfk_2` FOREIGN KEY (`TestID`) REFERENCES `test` (`Test_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conducts`
--

LOCK TABLES `conducts` WRITE;
/*!40000 ALTER TABLE `conducts` DISABLE KEYS */;
INSERT INTO `conducts` VALUES ('067',1),('002',6),('002',323),('002',542),('002',562),('002',8776),('002',45454545);
/*!40000 ALTER TABLE `conducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumables`
--

DROP TABLE IF EXISTS `consumables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumables` (
  `Name` varchar(255) NOT NULL,
  `Stock` int NOT NULL,
  `SupplierContact` text NOT NULL,
  `InventoryID` varchar(255) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumables`
--

LOCK TABLES `consumables` WRITE;
/*!40000 ALTER TABLE `consumables` DISABLE KEYS */;
INSERT INTO `consumables` VALUES ('bgfbfdh',4,'5435634624','454542523'),('fhgfhf',5,'4535532','234345345'),('gloves',40,'0109581508','0885'),('hfsdkjfd',4,'5435634624','454542523'),('hgjhj',2,'756465','788687'),('jhkjklm',5,'7999','8786898'),('jjjn',6,'67656465','67878'),('masks',200,'0109581508','1'),('Microscope Slides',6,'0107744995','421'),('Pencil',10,'018484275','482'),('pipe',4,'0109581508','8008'),('syringe',4,'010','3333'),('tube',4,'0109581508','09067');
/*!40000 ALTER TABLE `consumables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contains`
--

DROP TABLE IF EXISTS `contains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contains` (
  `LabNumber` int NOT NULL,
  `EquipmentSerialNumber` varchar(255) NOT NULL,
  PRIMARY KEY (`LabNumber`,`EquipmentSerialNumber`),
  KEY `EquipmentSerialNumber` (`EquipmentSerialNumber`),
  CONSTRAINT `contains_ibfk_1` FOREIGN KEY (`LabNumber`) REFERENCES `lab` (`Lab_Number`),
  CONSTRAINT `contains_ibfk_2` FOREIGN KEY (`EquipmentSerialNumber`) REFERENCES `equipment` (`Serial_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contains`
--

LOCK TABLES `contains` WRITE;
/*!40000 ALTER TABLE `contains` DISABLE KEYS */;
/*!40000 ALTER TABLE `contains` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dependents_employee`
--

DROP TABLE IF EXISTS `dependents_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dependents_employee` (
  `Dependent_SSN` varchar(255) NOT NULL,
  `ESSN` varchar(255) NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Middle_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `SEX` enum('male','female') NOT NULL,
  `Birthdate` date NOT NULL,
  `Address` text NOT NULL,
  `Relationship` varchar(255) NOT NULL,
  PRIMARY KEY (`Dependent_SSN`,`ESSN`),
  KEY `ESSN` (`ESSN`),
  CONSTRAINT `dependents_employee_ibfk_1` FOREIGN KEY (`ESSN`) REFERENCES `employee` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependents_employee`
--

LOCK TABLES `dependents_employee` WRITE;
/*!40000 ALTER TABLE `dependents_employee` DISABLE KEYS */;
INSERT INTO `dependents_employee` VALUES ('009900','099','Shafie','Muhammad','Mahmoud','male','2002-02-02','brother','cairo'),('090302','099','john','nasser','mohamed','female','2022-02-03','brother','maadi '),('10221','099','abdullah','yasser','mmm','male','2002-02-02','sheikh zayed','brother'),('133033','122022','no','i\'m','not','female','3003-03-03','sister','moqatam'),('4464464','099','farida','muhammad','youssef','female','2002-01-01','daughter','sheikh zayed'),('464644','099','Farida','Muhammad','Youssef','female','2002-02-02','daughter','sheikh zayed'),('6077','099','toqa','saeed','Mahmoud','female','2002-02-02','maadi','sister'),('67493','048','Mahmoud','Ahmed','Mohamed','male','2002-01-05','maadi','brother');
/*!40000 ALTER TABLE `dependents_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dependents_labtech`
--

DROP TABLE IF EXISTS `dependents_labtech`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dependents_labtech` (
  `Dependent_SSN` varchar(255) NOT NULL,
  `Lab_Tech_SSN` varchar(255) NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Middle_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `SEX` enum('male','female') NOT NULL,
  `Birthdate` date NOT NULL,
  `Address` text NOT NULL,
  `Relationship` varchar(255) NOT NULL,
  PRIMARY KEY (`Dependent_SSN`,`Lab_Tech_SSN`),
  KEY `Lab_Tech_SSN` (`Lab_Tech_SSN`),
  CONSTRAINT `dependents_labtech_ibfk_1` FOREIGN KEY (`Lab_Tech_SSN`) REFERENCES `lab_technician` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependents_labtech`
--

LOCK TABLES `dependents_labtech` WRITE;
/*!40000 ALTER TABLE `dependents_labtech` DISABLE KEYS */;
INSERT INTO `dependents_labtech` VALUES ('0020002','002','abdullah','yasser','mohammed','male','2002-02-02','maadi','father'),('03357889','002','yasser','nasser','amir','male','2001-09-12','old maadi','son'),('0666','002','reem','yasser','youssef','female','2002-02-02','moqatam','sister'),('06789','067','Amr','Ahmad','Nabeel','male','2000-02-03','Sheikh Zayed','Brother'),('087333','002','abdullah','saeed','mmm','male','2002-01-01','cairo','mother'),('09030405','002','yhhj','bgfds','gfds','female','1969-11-23','cairo','mother'),('147965','067','Hazem','Ahmad','Nabeel','male','2009-06-09','Sheikh Zayed','Brother'),('222022','002','Zendaya','3ashan','Maryam','female','2002-02-02','sheikh zayed','sister'),('234512','5555','Nour','Ahmad','Aly','female','2009-06-09','Sheikh Zayed','Daughter'),('304040','002','Wael','Muhammad','Mansour','male','2002-02-01','moqatam','father'),('46789','002','Malak','Ahmad','Sayed','female','2009-06-09','Maadi','sister'),('4747','002','Roba','Ehab','Amin','female','1998-09-07','sister','Maadi'),('47474','002','Roba','Ehab','Amin','female','1989-04-05','Maadi','sister'),('6644557','5555','Roba','Yasser','Sayed','female','2009-06-09','Maadi','Brother'),('667799','5555','Nour','Ehab','Amin','female','2000-02-03','mearaj','sister'),('74743','002','Mohamed','Gaafar','Gaafar','male','2001-05-05','old maadi','son'),('846541651684','067','Roba','Yasser','Amin','female','2000-02-03','B99','Daughter'),('93092','002','basboosa','mohamed','nasser','female','2014-03-12','new maadi','pet'),('9456','0897','Wael','Ahmad','Aly','male','1989-04-16','Sheikh Zayed','Husband');
/*!40000 ALTER TABLE `dependents_labtech` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `SSN` varchar(255) NOT NULL,
  `ID` int NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Middle_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `SEX` enum('male','female') NOT NULL,
  `Birthdate` date NOT NULL,
  `Salary` int NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Address` text NOT NULL,
  `Supervisor_SSN` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SSN`),
  UNIQUE KEY `Email` (`Email`),
  KEY `Supervisor_SSN` (`Supervisor_SSN`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Supervisor_SSN`) REFERENCES `employee` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('00050',504,'mohamed','omar','doe','female','2022-02-01',300,'mshnasser@gmail.com','maadi cairo',NULL),('0155',324,'Mohamed','Ahmed','Nasser','male','2001-01-01',33300,'sampleemail@gmail.com','abcde',NULL),('040234',8365,'toaa','ehab','mmm','female','2002-01-01',20000,'po@gmail.com','moqatam',NULL),('048',8,'Ameer','Mohammed','Amin','male','2009-06-09',3000,'ameer@gmail.com','Maadi','1212121212121'),('066',9,'Hassan','Ahmad','Sayed','male','1989-04-05',6000,'hassan@gmail.com','Sheikh Zayed','1212121212121'),('099',55,'reem','yasser','youssef','female','2002-02-02',20000,'reem@gmail.com','sheikh zayed',NULL),('119',239,'Yasser','Youssef','Gamal','male','1969-11-23',20000,'yasser23@gmail.com','sheikh zayed',NULL),('1190456',456789,'omar','yasser','youssef','female','2002-02-02',20000,'omar@mail.com','sheikh zayed','099'),('1212121212121',99999,'Dalia','Ahmad','Sayed','female','1973-04-04',30000,'Dalia@gmail.com','mearaj',NULL),('122022',1390,'uuuu','rrrrrr','high','female','2002-02-02',20000,'uuu@gmail.com','moqatam',NULL),('1234255674',10,'Mohamed','Nasser','Gaafar','male','2021-12-01',100000,'mohamednasser2001@hotmail.com','maadi',NULL),('344444',87777,'decgyhn',' bnjm','cvgbnm','male','2002-02-02',20000,'xffthj@gmail.com','sheikh zayed',NULL),('4555',4666,'ro\'aa','ehab','mohammed','female','2002-02-02',20000,'roaa@gmail.com','maadi',NULL),('455999',4666999,'ro\'aa','ehab','mohammed','female','2002-02-02',20000,'rrrrrr@gmail.com','maadi',NULL),('790',7809,'reem','saeed','mohammed','female','2002-01-01',20000,'rm@gmail.com','maadi',NULL);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employeephonenumber`
--

DROP TABLE IF EXISTS `employeephonenumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employeephonenumber` (
  `EmployeeSSN` varchar(255) NOT NULL,
  `PhoneNumber` varchar(255) NOT NULL,
  PRIMARY KEY (`EmployeeSSN`,`PhoneNumber`),
  CONSTRAINT `employeephonenumber_ibfk_1` FOREIGN KEY (`EmployeeSSN`) REFERENCES `employee` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employeephonenumber`
--

LOCK TABLES `employeephonenumber` WRITE;
/*!40000 ALTER TABLE `employeephonenumber` DISABLE KEYS */;
INSERT INTO `employeephonenumber` VALUES ('00050','0111222991'),('0155','0118867442'),('040234','010000'),('048','01068414816'),('066','010878454964'),('099','010'),('119','010000'),('1190456','011'),('1212121212121','086516164651'),('122022','012'),('1234255674','01234567901'),('344444','010'),('4555','012'),('455999','012'),('790','010000');
/*!40000 ALTER TABLE `employeephonenumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employeequalifications`
--

DROP TABLE IF EXISTS `employeequalifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employeequalifications` (
  `EmployeeSSN` varchar(255) NOT NULL,
  `CV` blob NOT NULL,
  PRIMARY KEY (`EmployeeSSN`),
  CONSTRAINT `employeequalifications_ibfk_1` FOREIGN KEY (`EmployeeSSN`) REFERENCES `employee` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employeequalifications`
--

LOCK TABLES `employeequalifications` WRITE;
/*!40000 ALTER TABLE `employeequalifications` DISABLE KEYS */;
INSERT INTO `employeequalifications` VALUES ('00050',_binary 'servodatasheet.pdf'),('0155',_binary 'servodatasheet.pdf'),('040234',_binary 'Group 5_ReemYasser_Ass1.pdf'),('048',_binary '2. GENN224_Lecture _9.pdf'),('066',_binary 'Task#4-SBEN213.pdf'),('099',_binary 'ReemYasserYoussef_190433_VideoCritique.pdf'),('119',_binary 'P_S_scale_riskmatrix.docx'),('1190456',_binary 'Poster1.png'),('1212121212121',_binary '2. GENN224_Lecture _9.pdf'),('122022',_binary 'collapse.png'),('1234255674',''),('344444',_binary 'collapse.png'),('4555',_binary 'collapse.png'),('455999',_binary 'collapse.png'),('790',_binary 'PRA_Project.docx');
/*!40000 ALTER TABLE `employeequalifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `Serial_Number` varchar(255) NOT NULL,
  `Inventory_ID` int NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Device_Name` varchar(255) NOT NULL,
  `Test_Name` varchar(255) NOT NULL,
  `Test_Type` varchar(255) NOT NULL,
  `Status` enum('Available','Busy') NOT NULL,
  `IPMMaintenance` varchar(255) NOT NULL,
  `Manufacturer_ID` varchar(255) NOT NULL,
  `Model` varchar(255) NOT NULL,
  `ManufacturerName` varchar(255) NOT NULL,
  `ManufacturingDate` date NOT NULL,
  PRIMARY KEY (`Serial_Number`),
  UNIQUE KEY `Inventory_ID` (`Inventory_ID`),
  UNIQUE KEY `Device_Name` (`Device_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES ('0555',9770,'rfdhyc','fgfvghb','98','tree','Available','xtgstgfcdsg','04388','ghygfvgh','cghjkl','2006-05-09'),('07905',665,'rfdhyc','uhygfd','8','zeft','Available','xtgstgfcdsg','0987658','pokjhg','jhbghjk','2006-05-09'),('5464623',6738,'3','kjdfkjd','2','1','Available','sssss','6754353','jkkldflsd44','fhegjdfs','2008-01-03'),('55536',56543,'2','djfdjfd','','','Available','ffdgfsd','2321','jjkfdkf','jdfjfd','2008-01-03'),('567893',84,'53','Spectroscopy','Urea','urine','Available','None','6443','GM 0X10','General Electric','2001-01-02'),('62345',2222224,'1','hjsfdhjfsd','7','3','Available','ttt','734783','kfdkjsfkjfsdkjdk','jsjfdjk','2008-01-03'),('643734',2123,'3','fgdaddas','Test_Type','','Available','DFDS','31242','gdrfs','safsF','2008-01-01'),('68473',12,'Laboratory','Sample Analyzer','DNA ','SEQUENCING','Available','None','3948','AHD 39','Philips','2012-01-02'),('74388943',89832823,'2','jsfkjfd','12','3','Busy','yyyyyy','237823892398','kfdjkdf3','hdfhfdfdkjfd','2008-01-01');
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab`
--

DROP TABLE IF EXISTS `lab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab` (
  `Lab_Number` int NOT NULL,
  `Lab_Name` varchar(255) NOT NULL,
  `Lab_Type` varchar(255) NOT NULL,
  `Lab_Location` text NOT NULL,
  PRIMARY KEY (`Lab_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab`
--

LOCK TABLES `lab` WRITE;
/*!40000 ALTER TABLE `lab` DISABLE KEYS */;
INSERT INTO `lab` VALUES (1,'B','Blood Analysis','Floor 2'),(2,'Clinical_A','Clinical','2nd floor'),(3,'Research_A','Research','1st floor'),(4,'Research_B','Research','3rd floor'),(5,'Clinical_B','Clinical Lab','Second Floor Room 50'),(8,'Research_C','Research','4th floor'),(55,'Virology','Genetic Sequencing','third floor room 4');
/*!40000 ALTER TABLE `lab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_technician`
--

DROP TABLE IF EXISTS `lab_technician`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_technician` (
  `SSN` varchar(255) NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Middle_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `SEX` enum('male','female') NOT NULL,
  `Birthdate` date NOT NULL,
  `Salary` int NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Address` text NOT NULL,
  `Manager_SSN` varchar(255) NOT NULL,
  PRIMARY KEY (`SSN`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Email_2` (`Email`),
  UNIQUE KEY `Email_3` (`Email`),
  UNIQUE KEY `Email_4` (`Email`),
  KEY `Manager_SSN` (`Manager_SSN`),
  CONSTRAINT `lab_technician_ibfk_1` FOREIGN KEY (`Manager_SSN`) REFERENCES `employee` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_technician`
--

LOCK TABLES `lab_technician` WRITE;
/*!40000 ALTER TABLE `lab_technician` DISABLE KEYS */;
INSERT INTO `lab_technician` VALUES ('002','Roaa','Ehab','Amin','female','2002-01-01',10000,'roaa@gmail.com','Maadi','099'),('00338','Muhammad','Khaled','Ahmed','male','2002-02-01',20000,'Muhammad@gmail.com','sheikh zayed','099'),('0102','Tamer','Basha','msh 3arfa','male','2002-02-02',20000,'tamer@eng.com','cairo','099'),('030356','John','Max','Krasinski','male','2002-02-02',20000,'johnk@gmail.com','sheikh zayed','099'),('03111','reem','yasser','youssef','female','2002-02-02',20000,'re@gmail.com','sheikh zayed','099'),('0350','Pamila','Beasley','Halpert','female','2002-02-02',20000,'Pam@gmail.com','maadi','099'),('067','Farah','Mohammed','Nabeel','female','2000-02-03',6000,'farah@gmail.com','zayed','00050'),('06903','Micheal','k','scott','male','2002-02-02',20000,'michael@mail.com','cairo','099'),('0897','Ola','Ahmad','Ahmad','female','1989-04-05',8000,'ola@gmail.com','Sheikh Zayed','048'),('12329','Hany','Gaafar','Mohamed','male','2002-12-01',100,'techlabnasser@gmail.com','dokki','066'),('3002','Khaled','Zeyad','Mansour','male','2001-01-02',56743,'khaled@gmail.com','street 1','066'),('30392','reem','momtaz','moataz','female','2022-01-05',100,'lab@technician.com','maadi ','099'),('500500','vbewrb','hnyynyne','bgbyrbtw','male','2002-02-01',20000,'fhkugo@gmail.com','sheikh zayed','099'),('533690','toaa','saeed','Mahmoud','male','2002-02-02',20000,'ojhg@gmail.com','moqatam','099'),('54932','Maryam','Moataz','Momtaz','female','2001-05-05',392,'maryam@gmail.com','madinet nasr','048'),('5555','Eman','Ahmad','Sayed','female','2009-06-09',20000,'eman@gmail.com','Sheikh Zayed','099'),('744709','ro\'aa','Muhammad','Mahmoud','female','2002-02-02',20000,'pooh@mail.com','moqatam','099'),('89572','Zeyad','Mohamed','Nasser','male','2001-01-05',5000,'zeyad@gmail.com','alooooo','048');
/*!40000 ALTER TABLE `lab_technician` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `labtechphonenumber`
--

DROP TABLE IF EXISTS `labtechphonenumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `labtechphonenumber` (
  `LabTechSSN` varchar(255) NOT NULL,
  `PhoneNumber` varchar(255) NOT NULL,
  PRIMARY KEY (`LabTechSSN`,`PhoneNumber`),
  CONSTRAINT `labtechphonenumber_ibfk_1` FOREIGN KEY (`LabTechSSN`) REFERENCES `lab_technician` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `labtechphonenumber`
--

LOCK TABLES `labtechphonenumber` WRITE;
/*!40000 ALTER TABLE `labtechphonenumber` DISABLE KEYS */;
INSERT INTO `labtechphonenumber` VALUES ('002','00112233445'),('00338','011'),('0102','010000'),('030356','010'),('03111','011'),('0350','010000'),('067','086516164651'),('06903','010'),('0897','01068414816'),('12329','0118856762'),('3002','01144877336'),('30392','01203451935'),('500500','012'),('533690','010000'),('54932','011884729'),('5555','0101848485'),('744709','010000'),('89572','01144833778');
/*!40000 ALTER TABLE `labtechphonenumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `labtechqualifications`
--

DROP TABLE IF EXISTS `labtechqualifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `labtechqualifications` (
  `LabTechSSN` varchar(255) NOT NULL,
  `Qualifications` blob NOT NULL,
  PRIMARY KEY (`LabTechSSN`),
  CONSTRAINT `labtechqualifications_ibfk_1` FOREIGN KEY (`LabTechSSN`) REFERENCES `lab_technician` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `labtechqualifications`
--

LOCK TABLES `labtechqualifications` WRITE;
/*!40000 ALTER TABLE `labtechqualifications` DISABLE KEYS */;
INSERT INTO `labtechqualifications` VALUES ('002',''),('00338',_binary 'GENN210 - Fall 2021 - Lecture 1 - Introduction.pdf'),('0102',_binary 'Project_Risk.docx'),('030356',_binary 'PRA_Project.docx'),('03111',_binary 'P_S_scale_riskmatrix.docx'),('0350',_binary 'GENN210 - Fall 2021 - Lecture 1 - Introduction.pdf'),('067',_binary 'GENN224_Class_Activity_4.pdf'),('06903',_binary 'Group 5_ReemYasser_Ass1.pdf'),('0897',_binary '05 Environmental Impact Assessment 2021.pptx'),('12329',_binary 'servodatasheet.pdf'),('3002',_binary 'servodatasheet.pdf'),('30392',_binary 'servodatasheet.pdf'),('500500',_binary 'Reem_Yasser_Assignment2_GENN210.pdf'),('533690',_binary 'P_S_scale_riskmatrix.docx'),('54932',_binary 'servodatasheet.pdf'),('5555',_binary '2. GENN224_Lecture _9.pdf'),('744709',_binary 'P_S_scale_riskmatrix.docx'),('89572',_binary 'servodatasheet.pdf');
/*!40000 ALTER TABLE `labtechqualifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `SSN` varchar(255) NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Middle_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `SEX` enum('male','female') NOT NULL,
  `Birthdate` date NOT NULL,
  `Insurance` varchar(255) DEFAULT NULL,
  `Address` text NOT NULL,
  `Email` varchar(255) NOT NULL,
  PRIMARY KEY (`SSN`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES ('0004045','Ahmed','Mohammed','Mahmoud','male','2002-02-02','AXA','sheikh zayed','Ahmed@mail.com'),('0101','yehia','ahmed','mohammed','male','2001-03-04','GIG','Cairo','yehiahmed@gmail.com'),('0909','Aly','Yasser','Ehab','male','1999-04-15','Deraya','Giza','aly@gmail.com'),('147892422','Nabeel','Ahmad','Mohammed','male','2000-02-03','Lockton','Maadi','nabeel@gmail.com'),('3449','Mark','Mario','Mohamed','male','2003-09-02','Misr Insurance','new cairo','mark@gmail.com'),('4558585858','amr','ahmad','aly','male','1989-04-05','GIG','Maadi','amr@gmail.com'),('8560','Malak','Ahmad','Aly','female','2002-02-02','GIG','maadi','malak@mail.com');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientmedicalhistory`
--

DROP TABLE IF EXISTS `patientmedicalhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patientmedicalhistory` (
  `PatientSSN` varchar(255) NOT NULL,
  `MedicalHistory` varchar(255) NOT NULL,
  PRIMARY KEY (`PatientSSN`,`MedicalHistory`),
  CONSTRAINT `patientmedicalhistory_ibfk_1` FOREIGN KEY (`PatientSSN`) REFERENCES `patient` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientmedicalhistory`
--

LOCK TABLES `patientmedicalhistory` WRITE;
/*!40000 ALTER TABLE `patientmedicalhistory` DISABLE KEYS */;
INSERT INTO `patientmedicalhistory` VALUES ('0004045','Covid-19'),('0101','Diabetes'),('0909','none'),('147892422','none'),('3449','Asthma'),('4558585858','none'),('8560','Covid-19');
/*!40000 ALTER TABLE `patientmedicalhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientphonenumber`
--

DROP TABLE IF EXISTS `patientphonenumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patientphonenumber` (
  `PatientSSN` varchar(255) NOT NULL,
  `PhoneNumber` varchar(255) NOT NULL,
  PRIMARY KEY (`PatientSSN`,`PhoneNumber`),
  CONSTRAINT `patientphonenumber_ibfk_1` FOREIGN KEY (`PatientSSN`) REFERENCES `patient` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientphonenumber`
--

LOCK TABLES `patientphonenumber` WRITE;
/*!40000 ALTER TABLE `patientphonenumber` DISABLE KEYS */;
INSERT INTO `patientphonenumber` VALUES ('0004045','01045687595'),('0101','01045987452'),('0909','01236987452'),('147892422','01035971268'),('3449','01188755669'),('4558585858','01165874954'),('8560','01147778962');
/*!40000 ALTER TABLE `patientphonenumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `ReportID` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Publish_Date` date NOT NULL,
  `Referred_By` varchar(255) NOT NULL,
  `Comments` text,
  `Patient_SSN` varchar(255) NOT NULL,
  PRIMARY KEY (`ReportID`),
  KEY `Patient_SSN` (`Patient_SSN`),
  CONSTRAINT `report_ibfk_1` FOREIGN KEY (`Patient_SSN`) REFERENCES `patient` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES (1,'CBC','2022-07-01','Dr. Roaa','none','0909'),(2,'CBC','2022-05-01','Dr. Roaa','none','0909'),(3,'Urine Analysis','2021-07-03','Dr. Ahmed','high urea levels','0101'),(4,'Urine Analysis','2021-05-03','Dr. Mohammed','low urea levels','0909'),(7,'rep1','2021-05-08','dr.reem','none','0101'),(8,'rep8','2021-05-08','dr.reem','none','0101'),(9,'rep3','2021-05-08','dr.reem','none','0101'),(10,'rep10','2021-05-08','dr.reem','dfghjk','0101'),(11,'rep11','2021-05-08','dr.reem','dfghjk','147892422'),(34,'Urine Analysis','2021-07-03','Dr. Mohammed','high urea levels','0101'),(44,'CBC','2022-01-01','dr Nasser','no comment','147892422'),(55,'NKT Photonics','2022-01-01','aloo','no comment','0909'),(111,'testreport','2021-01-08','doctor','no comments','0909'),(213,'Report','2021-12-10','Doctor','no comments','0101'),(216,'Report2','2021-12-16','Doctor','no comments','0101'),(332,'CBC','2021-05-03','Dr. Mohammed','no comments','0909'),(683,'retdfg','2021-05-03','Dr. Ahmed','none','0909'),(765,'Blood Test','2021-12-09','Dr Ahmed','very bad condition','8560'),(809,'CBC','2021-07-03','Dr. Ahmed','none','0909'),(978,'Urine Analysis','2021-05-03','Dr. Ahmed','low urea levels','0909'),(998,'kjhgvfx','2021-07-03','Dr. Ahmed','none','0909'),(1000,'rep1000','2021-05-08','dr.reem','dfghjk','147892422'),(5555,'testreport','2021-03-03','doctor','no comments','0909'),(11111,'testreport','2021-04-01','doctor','no comments','0909'),(89898,'report45','2021-05-08','dr.reem','dfghjk','0101');
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `Test_ID` int NOT NULL,
  `Test_Name` varchar(255) NOT NULL,
  `Category` varchar(255) NOT NULL,
  `Value` int NOT NULL,
  `Reference_Range` varchar(255) NOT NULL,
  `Cost` int NOT NULL,
  `Patient_SSN` varchar(255) NOT NULL,
  `Report_ID` int NOT NULL,
  `Lab_No` int NOT NULL,
  PRIMARY KEY (`Test_ID`),
  KEY `Patient_SSN` (`Patient_SSN`),
  KEY `Report_ID` (`Report_ID`),
  KEY `Lab_No` (`Lab_No`),
  CONSTRAINT `test_ibfk_1` FOREIGN KEY (`Patient_SSN`) REFERENCES `patient` (`SSN`),
  CONSTRAINT `test_ibfk_2` FOREIGN KEY (`Report_ID`) REFERENCES `report` (`ReportID`),
  CONSTRAINT `test_ibfk_3` FOREIGN KEY (`Lab_No`) REFERENCES `lab` (`Lab_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES (1,'test1','CBC',5,'10',500,'0004045',9,1),(2,'test2','CBC',5,'10',500,'0101',55,1),(5,'test5','CBC',5,'10',500,'0101',55,1),(6,'Hemoglobin','CBC',10,'5 - 30',20,'0004045',1,1),(11,'RBC','CBC',1,'2',10,'0909',1,1),(22,'Hemoglobin','CBC',10,'30',20,'8560',2,3),(43,'Neutrophils','White Blood Cells',10,'40 - 60',700,'0909',1,1),(66,'test66','CBC',5,'10',500,'0004045',55,1),(76,'mohamed msh nasser','cbc',10,'20',1000000,'0004045',55,1),(77,'test77','CBC',5,'10',500,'0101',55,1),(88,'test88','CBC',5,'10',500,'0101',55,1),(323,'Urea','Urine Analysis',42,'30-70',600,'0101',3,1),(449,'Hemoglobin','CBC',10,'30',20,'0909',2,3),(542,'Test2','Rapid PCR',1,'0 - 1',800,'8560',7,4),(562,'Covid-19','PCR',1,'1 - 0',600,'0909',1,1),(8776,'hgfx','nbvcx',10,'5 - 30',20,'147892422',1,1),(45454545,'dggr','gergerg',5,'10',500,'147892422',34,1);
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `User_SSN` varchar(255) NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Permission_Level` enum('admin','employee','labtechnician','patient') NOT NULL,
  `Email` varchar(255) NOT NULL,
  `PatientSSN` varchar(255) DEFAULT NULL,
  `LabTechSSN` varchar(255) DEFAULT NULL,
  `EmpSSN` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`User_SSN`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Username` (`Username`),
  UNIQUE KEY `Password` (`Password`),
  KEY `PatientSSN` (`PatientSSN`),
  KEY `LabTechSSN` (`LabTechSSN`),
  KEY `EmpSSN` (`EmpSSN`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`PatientSSN`) REFERENCES `patient` (`SSN`),
  CONSTRAINT `user_ibfk_2` FOREIGN KEY (`LabTechSSN`) REFERENCES `lab_technician` (`SSN`),
  CONSTRAINT `user_ibfk_3` FOREIGN KEY (`EmpSSN`) REFERENCES `employee` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('0004045','Ahmed2','2323','patient','Ahmed@mail.com','0004045',NULL,NULL),('00050','monaser123','1245','employee','mshnasser@gmail.com',NULL,NULL,'00050'),('002','roaa','roaa22','labtechnician','roaa@gmail.com',NULL,'002',NULL),('00338','Muhammad','Muhammad22','labtechnician','Muhammad@gmail.com',NULL,'00338',NULL),('0102','Tamer24','tamerr','labtechnician','tamer@eng.com',NULL,'0102',NULL),('0155','Naaser4','sample4','employee','sampleemail@gmail.com',NULL,NULL,'0155'),('030356','johnk','john123k','labtechnician','johnk@gmail.com',NULL,'030356',NULL),('03111','re33','re33ee','labtechnician','re@gmail.com',NULL,'03111',NULL),('0350','Pambea','pam123','labtechnician','Pam@gmail.com',NULL,'0350',NULL),('040234','po2','2233','employee','po@gmail.com',NULL,NULL,'040234'),('048','Ameer','ameer34','employee','ameer@gmail.com',NULL,NULL,'048'),('066','Hassan','hassan55','employee','hassan@gmail.com',NULL,NULL,'066'),('067','Farah','farah44','labtechnician','farah@gmail.com',NULL,'067',NULL),('06903','michaels','thatswhatshesaid','labtechnician','michael@mail.com',NULL,'06903',NULL),('0897','Ola','ola25','labtechnician','ola@gmail.com',NULL,'0897',NULL),('0909','Aly','aly1234','patient','aly@gmail.com','0909',NULL,NULL),('099','reemy22','123@REEM','employee','reem@gmail.com',NULL,NULL,'099'),('119','yaserr23','yas2311','admin','yasser23@gmail.com',NULL,NULL,'119'),('1190456','omarrrrr','23456789','employee','omar@mail.com',NULL,NULL,'1190456'),('1212121212121','Dalia','1234','admin','Dalia@gmail.com',NULL,NULL,'1212121212121'),('122022','uuuu','uuu123','employee','uuu@gmail.com',NULL,NULL,'122022'),('12329','nassertech','stronkpass','labtechnician','techlabnasser@gmail.com',NULL,'12329',NULL),('1234255674','mohamed123','','employee','mohamednasser2001@hotmail.com',NULL,NULL,'1234255674'),('147892422','Nabeel','nabeel44','patient','nabeel@gmail.com','147892422',NULL,NULL),('3002','khaled','khaledgamed','labtechnician','khaled@gmail.com',NULL,'3002',NULL),('30392','labnasser','2345678','labtechnician','lab@technician.com',NULL,'30392',NULL),('344444','werfsfg','45678ertyu','employee','xffthj@gmail.com',NULL,NULL,'344444'),('3449','mark1','mark23','patient','mark@gmail.com','3449',NULL,NULL),('4558585858','amr','amr22','patient','amr@gmail.com','4558585858',NULL,NULL),('455999','roaa22','123@Roaa','employee','rrrrrr@gmail.com',NULL,NULL,'455999'),('500500','rtyy','frbrtrbb','labtechnician','fhkugo@gmail.com',NULL,'500500',NULL),('533690','omarrrr90','gf456ef43','labtechnician','ojhg@gmail.com',NULL,'533690',NULL),('54932','maryammoataz','maryam123','labtechnician','maryam@gmail.com',NULL,'54932',NULL),('5555','Eman','eman25','labtechnician','eman@gmail.com',NULL,'5555',NULL),('744709','pooh','0093','labtechnician','pooh@mail.com',NULL,'744709',NULL),('790','05683','rm45','employee','rm@gmail.com',NULL,NULL,'790'),('8560','6yhtnh','6tyhbgbf','patient','65r@mail.com','8560',NULL,NULL),('89572','zeyad','z1234','labtechnician','zeyad@gmail.com',NULL,'89572',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uses`
--

DROP TABLE IF EXISTS `uses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uses` (
  `Consumables_Name` varchar(255) NOT NULL,
  `EquipmentSerialNumber` varchar(255) NOT NULL,
  PRIMARY KEY (`Consumables_Name`,`EquipmentSerialNumber`),
  KEY `EquipmentSerialNumber` (`EquipmentSerialNumber`),
  CONSTRAINT `uses_ibfk_1` FOREIGN KEY (`Consumables_Name`) REFERENCES `consumables` (`Name`),
  CONSTRAINT `uses_ibfk_2` FOREIGN KEY (`EquipmentSerialNumber`) REFERENCES `equipment` (`Serial_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uses`
--

LOCK TABLES `uses` WRITE;
/*!40000 ALTER TABLE `uses` DISABLE KEYS */;
INSERT INTO `uses` VALUES ('Microscope Slides','0555'),('Pencil','07905'),('bgfbfdh','5464623'),('masks','55536'),('pipe','55536');
/*!40000 ALTER TABLE `uses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_on` (
  `LabTechSSN` varchar(255) NOT NULL,
  `Hours` int NOT NULL,
  `EquipmentSerialNumber` varchar(255) NOT NULL,
  PRIMARY KEY (`LabTechSSN`,`EquipmentSerialNumber`),
  KEY `EquipmentSerialNumber` (`EquipmentSerialNumber`),
  CONSTRAINT `works_on_ibfk_1` FOREIGN KEY (`LabTechSSN`) REFERENCES `lab_technician` (`SSN`),
  CONSTRAINT `works_on_ibfk_2` FOREIGN KEY (`EquipmentSerialNumber`) REFERENCES `equipment` (`Serial_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
/*!40000 ALTER TABLE `works_on` DISABLE KEYS */;
/*!40000 ALTER TABLE `works_on` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-27 10:09:59
