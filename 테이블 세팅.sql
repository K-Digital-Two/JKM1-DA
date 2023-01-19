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
-- Table `ship`.`schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ship`.`schedule` (
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
  `schedule_ship_shipId` INT NOT NULL,
  `insertTime` DATETIME NULL DEFAULT NULL,
  `shipLat` DOUBLE NULL DEFAULT NULL,
  `shipLon` DOUBLE NULL DEFAULT NULL,
  `speed` DOUBLE NULL DEFAULT NULL,
  `arrivalTime` DATETIME NULL DEFAULT NULL,
  `takeTime` INT NULL DEFAULT NULL,
  `accuracy` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`schedule_ship_shipId`),
  INDEX `fk_info_schedule1_idx` (`schedule_ship_shipId` ASC) VISIBLE,
  CONSTRAINT `fk_info_schedule1`
    FOREIGN KEY (`schedule_ship_shipId`)
    REFERENCES `ship`.`schedule` (`ship_shipId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `ship`.`summary`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ship`.`summary` (
  `mmsi` INT NOT NULL,
  `shipName` VARCHAR(20) NULL DEFAULT NULL,
  `destination` VARCHAR(10) NULL DEFAULT NULL,
  `predTime` INT NULL DEFAULT NULL,
  `percentage` INT NULL DEFAULT NULL,
  PRIMARY KEY (`mmsi`))
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
  `flowMeter` INT NULL DEFAULT NULL,
  `flowRate` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`obsId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;