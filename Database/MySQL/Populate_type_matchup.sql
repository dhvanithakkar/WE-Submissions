drop table type_matchup;

CREATE TABLE type_matchup (
  attacking_type_id INT NOT NULL,
  defending_type_id INT NOT NULL,
  multiplier DECIMAL(2,1) NOT NULL,
  FOREIGN KEY (attacking_type_id) REFERENCES typ(id),
  FOREIGN KEY (defending_type_id) REFERENCES typ(id),
  PRIMARY KEY (attacking_type_id, defending_type_id)
);
-- Fire super effective against Grass
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Fire"), (SELECT id FROM typ WHERE name = "Grass"), 2.0);

-- Fire weak against Water
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Fire"), (SELECT id FROM typ WHERE name = "Water"), 0.5);

-- Similar inserts for other type matchups (Grass, Water, Normal, Flying)
-- Grass super effective against Water
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Grass"), (SELECT id FROM typ WHERE name = "Water"), 2.0);

-- Grass weak against Fire
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Grass"), (SELECT id FROM typ WHERE name = "Fire"), 0.5);

-- Grass weak against Flying
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Grass"), (SELECT id FROM typ WHERE name = "Flying"), 0.5);

-- Water super effective against Fire
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Water"), (SELECT id FROM typ WHERE name = "Fire"), 2.0);

-- Water weak against Grass
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Water"), (SELECT id FROM typ WHERE name = "Grass"), 0.5);

-- Normal has no effectiveness multipliers
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES 
((SELECT id FROM typ WHERE name = "Normal"), (SELECT id FROM typ WHERE name = "Fire"), 1.0),
((SELECT id FROM typ WHERE name = "Normal"), (SELECT id FROM typ WHERE name = "Flying"), 1.0),
((SELECT id FROM typ WHERE name = "Normal"), (SELECT id FROM typ WHERE name = "Grass"), 1.0),
((SELECT id FROM typ WHERE name = "Normal"), (SELECT id FROM typ WHERE name = "Normal"), 1.0),
((SELECT id FROM typ WHERE name = "Normal"), (SELECT id FROM typ WHERE name = "Water"), 1.0),

((SELECT id FROM typ WHERE name = "Fire"), (SELECT id FROM typ WHERE name = "Normal"), 1.0),
((SELECT id FROM typ WHERE name = "Flying"), (SELECT id FROM typ WHERE name = "Normal"), 1.0),
((SELECT id FROM typ WHERE name = "Grass"), (SELECT id FROM typ WHERE name = "Normal"), 1.0),
((SELECT id FROM typ WHERE name = "Water"), (SELECT id FROM typ WHERE name = "Normal"), 1.0);


-- Flying super effective against Grass
INSERT INTO type_matchup (attacking_type_id, defending_type_id, multiplier)
VALUES ((SELECT id FROM typ WHERE name = "Flying"), (SELECT id FROM typ WHERE name = "Grass"), 2.0);
