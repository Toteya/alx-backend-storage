-- Creates a user-defined function SafeDiv that divides the first number
-- by the second number and returns the result, or zwero if the second number
-- is zero.
DELIMITER $$
CREATE FUNCTION SafeDiv(
    num1 INT,
    num2 INT
)
RETURNS FLOAT
BEGIN
    IF num2 = 0 THEN
        RETURN 0;
    ELSE
        RETURN num1 / num2;
    END IF;
END $$
DELIMITER ;
