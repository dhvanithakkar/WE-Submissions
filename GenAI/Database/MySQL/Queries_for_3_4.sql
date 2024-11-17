-- Write a query that returns all the pokemon who can learn ‘Return’. (5)

SELECT p.name AS pokemon
FROM Pokemon p
INNER JOIN Pokemon_Skill ps ON ps.pokemon_id = p.id
INNER JOIN Skill s ON ps.skill_id = s.id
WHERE s.name = "Return";

-- Write a query that returns all the moves in the game that are powerful against Grass. (5)

SELECT s.id, s.name
FROM skill s
WHERE type_id IN
(SELECT attacking_type_id 
FROM type_matchup 
WHERE defending_type_id = (SELECT id FROM typ WHERE name = "Grass")
AND multiplier = 2);