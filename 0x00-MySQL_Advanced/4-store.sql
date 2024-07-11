-- Creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER decrease_quantities
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - new.number WHERE name = new.item_name;
END$$
DELIMITER ;
