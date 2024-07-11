-- Creates a stored procedure ComputerAverageScoreForUser that computes and
-- stores the average score for a student
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN u_id INT
)
BEGIN
    SET @avg_score =
    (SELECT AVG(score)
    FROM corrections
    WHERE user_id = u_id
    GROUP BY user_id);
    UPDATE users SET average_score = @avg_score WHERE id = u_id;
END $$
DELIMITER ;
