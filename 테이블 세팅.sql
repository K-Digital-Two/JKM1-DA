-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ship
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ship
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ship` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `ship` ;

-- -----------------------------------------------------
-- Table `ship`.`arrivalport`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ship`.`arrivalport` (
  `arrivalName` VARCHAR(10) NOT NULL,
  `arrivalLat` DOUBLE NULL DEFAULT NULL,
  `arrivalLon` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`arrivalName`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `ship`.`ship`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ship`.`ship` (
  `shipId` INT NOT NULL,
  `shipCode` VARCHAR(10) NOT NULL,
  `shipName` VARCHAR(20) NOT NULL,
  `shipUse` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`shipId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `ship`.`schedules`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ship`.`schedules` (
  `ship_shipId` INT NOT NULL,
  `arrivalPort_arrivalName` VARCHAR(10) NOT NULL,
  `departure` VARCHAR(10) NULL DEFAULT NULL,
  `departTime` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`ship_shipId`),
  INDEX `fk_schedule_ship_idx` (`ship_shipId` ASC) VISIBLE,
  INDEX `fk_schedule_arrivalPort1_idx` (`arrivalPort_arrivalName` ASC) VISIBLE,
  CONSTRAINT `fk_schedule_arrivalPort1`
    FOREIGN KEY (`arrivalPort_arrivalName`)
    REFERENCES `ship`.`arrivalport` (`arrivalName`),
  CONSTRAINT `fk_schedule_ship`
    FOREIGN KEY (`ship_shipId`)
    REFERENCES `ship`.`ship` (`shipId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `ship`.`info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ship`.`info` (
  `schedules_ship_shipId` INT NOT NULL,
  `insertTime` DATETIME NULL DEFAULT NULL,
  `shipLat` DOUBLE NULL DEFAULT NULL,
  `shipLon` DOUBLE NULL DEFAULT NULL,
  `speed` DOUBLE NULL DEFAULT NULL,
  `arrivalTime` DATETIME NULL DEFAULT NULL,
  `takeTime` INT NULL DEFAULT NULL,
  `accuracy` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`schedules_ship_shipId`),
  INDEX `fk_info_schedule1_idx` (`schedules_ship_shipId` ASC) VISIBLE,
  CONSTRAINT `fk_info_schedule1`
    FOREIGN KEY (`schedules_ship_shipId`)
    REFERENCES `ship`.`schedules` (`ship_shipId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `ship`.`weather`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ship`.`weather` (
  `obsId` VARCHAR(10) NOT NULL,
  `time` DATETIME NULL DEFAULT NULL,
  `temp` DOUBLE NULL DEFAULT NULL,
  `pressure` INT NULL DEFAULT NULL,
  `windDirec` INT NULL DEFAULT NULL,
  `windSpeed` DOUBLE NULL DEFAULT NULL,
  `obsLat` DOUBLE NULL DEFAULT NULL,
  `obsLon` DOUBLE NULL DEFAULT NULL,
  `titdeLevel` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`obsId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
