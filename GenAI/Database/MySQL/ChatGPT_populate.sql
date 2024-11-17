show tables;
INSERT INTO Type (name) VALUES ('Grass'), ('Fire'), ('Water'), ('Normal'), ('Flying');

-- Inserting Pokemon
INSERT INTO Pokemon (name) VALUES ('Bulbasaur'), ('Charmander'), ('Squirtle'), ('Eevee'), ('Pidgey');

-- Inserting Pokemon Types
INSERT INTO Pokemon_Type (pokemon_id, type_id, is_primary) VALUES
(1, 1, TRUE), -- Bulbasaur: Grass
(2, 2, TRUE), -- Charmander: Fire
(3, 3, TRUE), -- Squirtle: Water
(4, 4, TRUE), -- Eevee: Normal
(5, 4, TRUE), -- Pidgey: Normal
(5, 5, FALSE); -- Pidgey: Flying

-- Inserting Skills
INSERT INTO Skill (name, type_id, strength) VALUES
('Tackle', 4, 35),   -- Normal
('Vine Whip', 1, 40), -- Grass
('Ember', 2, 40),     -- Fire
('Water Gun', 3, 40), -- Water
('Wing Attack', 5, 65), -- Flying
('Headbutt', 4, 70),  -- Normal
('Return', 4, 100);   -- Normal

-- Inserting Pokemon Skills
INSERT INTO Pokemon_Skill (pokemon_id, skill_id) VALUES
(1, 1), -- Bulbasaur: Tackle
(1, 2), -- Bulbasaur: Vine Whip
(1, 7), -- Bulbasaur: Return
(2, 1), -- Charmander: Tackle
(2, 3), -- Charmander: Ember
(2, 7), -- Charmander: Return
(3, 1), -- Squirtle: Tackle
(3, 4), -- Squirtle: Water Gun
(3, 7), -- Squirtle: Return
(4, 1), -- Eevee: Tackle
(4, 6), -- Eevee: Headbutt
(4, 7), -- Eevee: Return
(5, 1), -- Pidgey: Tackle
(5, 5), -- Pidgey: Wing Attack
(5, 7); -- Pidgey: Return

-- Inserting Type Interactions
INSERT INTO Type_Interaction (type_id1, type_id2, multiplier) VALUES
(1, 2, 2), -- Grass is powerful against Fire
(1, 3, 0.5), -- Grass is weak against Water
(1, 5, 0.5), -- Grass is weak against Flying
(2, 1, 0.5), -- Fire is weak against Grass
(2, 3, 2), -- Fire is powerful against Water
(3, 1, 2), -- Water is powerful against Grass
(3, 2, 0.5), -- Water is weak against Fire
(5, 1, 2); -- Flying is powerful against Grass
