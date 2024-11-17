INSERT INTO Pokemon_Skill (pokemon_id, skill_id) VALUES
  ((SELECT id FROM Pokemon WHERE name = "Bulbasaur"), (SELECT id FROM Skill WHERE name = "Tackle")),
  ((SELECT id FROM Pokemon WHERE name = "Bulbasaur"), (SELECT id FROM Skill WHERE name = "Vine Whip")),
  ((SELECT id FROM Pokemon WHERE name = "Bulbasaur"), (SELECT id FROM Skill WHERE name = "Return"));

-- Charmander
INSERT INTO Pokemon_Skill (pokemon_id, skill_id) VALUES
  ((SELECT id FROM Pokemon WHERE name = "Charmander"), (SELECT id FROM Skill WHERE name = "Tackle")),
  ((SELECT id FROM Pokemon WHERE name = "Charmander"), (SELECT id FROM Skill WHERE name = "Ember")),
  ((SELECT id FROM Pokemon WHERE name = "Charmander"), (SELECT id FROM Skill WHERE name = "Return"));

-- Squirtle
INSERT INTO Pokemon_Skill (pokemon_id, skill_id) VALUES
  ((SELECT id FROM Pokemon WHERE name = "Squirtle"), (SELECT id FROM Skill WHERE name = "Tackle")),
  ((SELECT id FROM Pokemon WHERE name = "Squirtle"), (SELECT id FROM Skill WHERE name = "Water Gun")),
  ((SELECT id FROM Pokemon WHERE name = "Squirtle"), (SELECT id FROM Skill WHERE name = "Return"));

-- Eevee
INSERT INTO Pokemon_Skill (pokemon_id, skill_id) VALUES
  ((SELECT id FROM Pokemon WHERE name = "Eevee"), (SELECT id FROM Skill WHERE name = "Tackle")),
  ((SELECT id FROM Pokemon WHERE name = "Eevee"), (SELECT id FROM Skill WHERE name = "Headbutt")),
  ((SELECT id FROM Pokemon WHERE name = "Eevee"), (SELECT id FROM Skill WHERE name = "Return"));

-- Pidgey
INSERT INTO Pokemon_Skill (pokemon_id, skill_id) VALUES
  ((SELECT id FROM Pokemon WHERE name = "Pidgey"), (SELECT id FROM Skill WHERE name = "Tackle")),
  ((SELECT id FROM Pokemon WHERE name = "Pidgey"), (SELECT id FROM Skill WHERE name = "Wing Attack")),
  ((SELECT id FROM Pokemon WHERE name = "Pidgey"), (SELECT id FROM Skill WHERE name = "Return"));
