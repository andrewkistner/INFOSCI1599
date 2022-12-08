-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ank243
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ank243
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ank243` DEFAULT CHARACTER SET utf8 ;
USE `ank243` ;

-- -----------------------------------------------------
-- Table `ank243`.`locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`locations` (
  `pk_locations_id` INT NOT NULL,
  PRIMARY KEY (`pk_locations_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`customers` (
  `pk_customers_id` VARCHAR(36) NOT NULL,
  `customer_name` VARCHAR(45) NULL,
  `customer_address` VARCHAR(45) NULL,
  `customer_phone` VARCHAR(45) NULL,
  PRIMARY KEY (`pk_customers_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`toppings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`toppings` (
  `pk_toppings_id` VARCHAR(36) NOT NULL,
  `topping_name` VARCHAR(45) NULL,
  PRIMARY KEY (`pk_toppings_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`sizes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`sizes` (
  `pk_sizes_id` VARCHAR(36) NOT NULL,
  `sizes_name` VARCHAR(45) NULL,
  `sizes_price` VARCHAR(45) NULL,
  PRIMARY KEY (`pk_sizes_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`pizzas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`pizzas` (
  `pk_pizzas_id` VARCHAR(36) NOT NULL,
  `fk_pizzas_size` VARCHAR(36) NULL,
  `fk_pizzas_topping1` VARCHAR(36) NULL,
  `fk_pizzas_topping2` VARCHAR(36) NULL,
  `pizzas_name` VARCHAR(45) NULL,
  PRIMARY KEY (`pk_pizzas_id`),
  INDEX `size_fk_idx` (`fk_pizzas_size` ASC) VISIBLE,
  INDEX `topping1_fk_idx` (`fk_pizzas_topping1` ASC) VISIBLE,
  INDEX `topping2_fk_idx` (`fk_pizzas_topping2` ASC) VISIBLE,
  CONSTRAINT `size_fk`
    FOREIGN KEY (`fk_pizzas_size`)
    REFERENCES `ank243`.`sizes` (`pk_sizes_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `topping1_fk`
    FOREIGN KEY (`fk_pizzas_topping1`)
    REFERENCES `ank243`.`toppings` (`pk_toppings_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `topping2_fk`
    FOREIGN KEY (`fk_pizzas_topping2`)
    REFERENCES `ank243`.`toppings` (`pk_toppings_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`credit_card`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`credit_card` (
  `pk_creditcard_id` VARCHAR(36) NOT NULL,
  `credit_name` VARCHAR(45) NULL,
  `credit_number` VARCHAR(45) NULL,
  `credit_expiration` VARCHAR(45) NULL,
  PRIMARY KEY (`pk_creditcard_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`customer_order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`customer_order` (
  `pk_cusomerorder_id` VARCHAR(36) NOT NULL,
  `total_price` VARCHAR(45) NULL,
  `fk_customer_id` VARCHAR(36) NULL,
  `fk_creditcard_id` VARCHAR(36) NULL,
  PRIMARY KEY (`pk_cusomerorder_id`),
  INDEX `customer_fk_idx` (`fk_customer_id` ASC) VISIBLE,
  INDEX `creditcard_fk_idx` (`fk_creditcard_id` ASC) VISIBLE,
  CONSTRAINT `customer_fk`
    FOREIGN KEY (`fk_customer_id`)
    REFERENCES `ank243`.`customers` (`pk_customers_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `creditcard_fk`
    FOREIGN KEY (`fk_creditcard_id`)
    REFERENCES `ank243`.`credit_card` (`pk_creditcard_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`customer_pizzas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`customer_pizzas` (
  `fk_customer_order_id` VARCHAR(36) NULL,
  `fk_pizza_id` VARCHAR(36) NULL,
  INDEX `customerorder_fk_idx` (`fk_customer_order_id` ASC) VISIBLE,
  INDEX `pizza_fk_idx` (`fk_pizza_id` ASC) VISIBLE,
  CONSTRAINT `customerorder_fk`
    FOREIGN KEY (`fk_customer_order_id`)
    REFERENCES `ank243`.`customer_order` (`pk_cusomerorder_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `pizza_fk`
    FOREIGN KEY (`fk_pizza_id`)
    REFERENCES `ank243`.`pizzas` (`pk_pizzas_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`customer_credit_card`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`customer_credit_card` (
  `fk_customer_id` VARCHAR(36) NULL,
  `fk_creditcard_id` VARCHAR(36) NULL,
  INDEX `cust_fk_idx` (`fk_customer_id` ASC) VISIBLE,
  INDEX `credit_fk_idx` (`fk_creditcard_id` ASC) VISIBLE,
  CONSTRAINT `cust_fk`
    FOREIGN KEY (`fk_customer_id`)
    REFERENCES `ank243`.`customers` (`pk_customers_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `credit_fk`
    FOREIGN KEY (`fk_creditcard_id`)
    REFERENCES `ank243`.`credit_card` (`pk_creditcard_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`customer_order_preference`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`customer_order_preference` (
  `fk_customer_id` VARCHAR(36) NULL,
  `fk_customer_order_id` VARCHAR(36) NULL,
  INDEX `customerpref_fk_idx` (`fk_customer_id` ASC) VISIBLE,
  INDEX `customer_order_fk_idx` (`fk_customer_order_id` ASC) VISIBLE,
  CONSTRAINT `customerpref_fk`
    FOREIGN KEY (`fk_customer_id`)
    REFERENCES `ank243`.`customers` (`pk_customers_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `customer_order_fk`
    FOREIGN KEY (`fk_customer_order_id`)
    REFERENCES `ank243`.`customer_order` (`pk_cusomerorder_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`drinks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`drinks` (
  `pk_drinks_id` VARCHAR(36) NOT NULL,
  `drink_name` VARCHAR(45) NULL,
  `drink_price` VARCHAR(45) NULL,
  PRIMARY KEY (`pk_drinks_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ank243`.`customer_drinks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ank243`.`customer_drinks` (
  `fk_customer_order_id` VARCHAR(36) NULL,
  `fk_drink_id` VARCHAR(36) NULL,
  INDEX `fk_cust_order_idx` (`fk_customer_order_id` ASC) VISIBLE,
  INDEX `fk_drinks_idx` (`fk_drink_id` ASC) VISIBLE,
  CONSTRAINT `fk_cust_order`
    FOREIGN KEY (`fk_customer_order_id`)
    REFERENCES `ank243`.`customer_order` (`pk_cusomerorder_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_drinks`
    FOREIGN KEY (`fk_drink_id`)
    REFERENCES `ank243`.`drinks` (`pk_drinks_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
