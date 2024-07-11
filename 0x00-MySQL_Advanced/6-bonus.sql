-- Creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    SET @project_id = (SELECT id from projects WHERE name = project_name);
    IF @project_id IS NULL THEN
        INSERT projects (name) VALUES (project_name);
        SET @project_id = (SELECT id from projects WHERE name = project_name);
    END IF;
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id from projects WHERE name = project_name), score);
END $$
DELIMITER ;
