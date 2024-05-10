-- This script creates a stored procedure 'ComputeAverageScoreForUser'
-- to calculate and store the average score for a user (supports decimals).

CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INT
)
BEGIN

  DECLARE total_score DECIMAL(10,2);  -- Variable to hold total score (decimal)

  -- Calculate total score for the user
  SELECT SUM(score) INTO total_score
  FROM scores  -- Replace 'scores' with your actual score table name
  WHERE user_id = user_id;

  -- Handle division by zero
  IF total_score IS NULL THEN
    SET total_score = 0;
  END IF;
  DECLARE avg_score DECIMAL(10,2);
  SET avg_score = total_score / (SELECT COUNT(*) FROM scores WHERE user_id = user_id);

  -- Update user table (replace 'users' with your actual user table name)
  UPDATE users
  SET average_score = avg_score
  WHERE id = user_id;

END;
