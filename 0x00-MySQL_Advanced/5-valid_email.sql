-- Creates a trigger that resets the valid_email attribute
DELIMITER $$
DROP TRIGGER IF EXISTS reset_valid_email;
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;
