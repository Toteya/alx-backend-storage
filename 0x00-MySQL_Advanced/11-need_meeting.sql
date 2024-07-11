-- Creates a view that lists students that have a score under 80 and no last
-- meeting or last meeting longer than a month ago
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH)
OR last_meeting IS NULL);
