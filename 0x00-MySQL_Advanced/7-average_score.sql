-- Stored procedure to compute and store the average score for a user
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE user_avg FLOAT;

    -- Compute average score
    SELECT AVG(score) INTO user_avg
    FROM corrections
    WHERE user_id = user_id;

    -- Update average score in users table
    UPDATE users
    SET average_score = user_avg
    WHERE id = user_id;
END //

DELIMITER ;
