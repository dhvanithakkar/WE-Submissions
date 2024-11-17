INSERT INTO Typ (name) VALUES 
('Grass'), 
('Fire'), 
('Water'), 
('Normal'), 
('Flying');

INSERT INTO Pokemon (name, primary_type_id) VALUES
  ("Bulbasaur", (SELECT id FROM Typ WHERE name = "Grass")),
  ("Charmander", (SELECT id FROM Typ WHERE name = "Fire")),
  ("Squirtle", (SELECT id FROM Typ WHERE name = "Water")),
  ("Eevee", (SELECT id FROM Typ WHERE name = "Normal")),
  ("Pidgey", (SELECT id FROM Typ WHERE name = "Normal"));

INSERT INTO Skill (name, strength, type_id) VALUES
  ("Tackle", 35, (SELECT id FROM Typ WHERE name = "Normal")),
  ("Water Gun", 40, (SELECT id FROM Typ WHERE name = "Water")),
  ("Ember", 40, (SELECT id FROM Typ WHERE name = "Fire")),
  ("Vine Whip", 40, (SELECT id FROM Typ WHERE name = "Grass")),
  ("Wing Attack", 65, (SELECT id FROM Typ WHERE name = "Flying")),
  ("Headbutt", 70, (SELECT id FROM Typ WHERE name = "Normal")),
  ("Return", 100, (SELECT id FROM Typ WHERE name = "Normal"));

