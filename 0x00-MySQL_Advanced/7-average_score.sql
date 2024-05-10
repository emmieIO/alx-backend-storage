-- Stored procedure to compute and store the average score for a user
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE user_total_score FLOAT;
    DECLARE user_total_projects INT;
    DECLARE user_avg_score FLOAT;

    -- Calculate the total score for the user
    SELECT SUM(score)
    INTO user_total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the total number of projects for the user
    SELECT COUNT(*)
    INTO user_total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score for the user
    IF user_total_projects > 0 THEN
        SET user_avg_score = user_total_score / user_total_projects;
    ELSE
        SET user_avg_score = 0;
    END IF;

    -- Update the users table with the average score
    UPDATE users
    SET average_score = user_avg_score
    WHERE id = user_id;
END //

DELIMITER ;
