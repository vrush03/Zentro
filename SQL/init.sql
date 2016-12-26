create database zentro;
use zentro;

--Order

CREATE TABLE `Order1` (
`Detail` VARCHAR(255) NULL,
`MobileNo` INT not NULL,
`PINCODE` INT NULL,
`Landmark` VARCHAR(255) NULL,
`Society` VARCHAR(255) NULL,
`Flat` VARCHAR(255) NULL, 
`Place` VARCHAR(255) NULL,
`FirstName` VARCHAR(255) NULL,
`LastName` VARCHAR(255) NULL,
`Useremail` VARCHAR(255) NULL,
PRIMARY KEY (`MobileNo`));


CREATE TABLE `Feedback` (
`Detail` VARCHAR(255),
`MobileNo` INT ,
`FirstName` VARCHAR(255) NULL,
PRIMARY KEY (`MobileNo`));


-- Order Procedure

DROP procedure IF EXISTS `sp_addStat`;
DELIMITER $$
CREATE PROCEDURE `sp_addStat`(
    IN p_detail VARCHAR(255),
    IN p_mob INT,
    IN p_pin INT,
    IN p_land VARCHAR(255),
    IN p_society VARCHAR(255),
    IN p_flat VARCHAR(255),
    IN p_place VARCHAR(255),
    IN p_first VARCHAR(255),
    IN p_last VARCHAR(255),
    IN p_email VARCHAR(255)
    
)
BEGIN
    insert into Order1 (
        Detail,
        MobileNo,
        PINCODE,
        Landmark,
        Society,
        Flat,
        Place,
        FirstName,
        LastName,
        Useremail
        
    )
    values
    (
        p_detail,
        p_mob,
        p_pin,
        p_land,
        p_society,
        p_flat,
        p_place,
        p_first,
        p_last,
        p_email
        
    );
END$$

DELIMITER ;
;


