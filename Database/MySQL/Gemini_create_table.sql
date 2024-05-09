CREATE TABLE Typ (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) UNIQUE
);

CREATE TABLE Pokemon (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) UNIQUE,
  primary_type_id INT NOT NULL,
  secondary_type_id INT DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (primary_type_id) REFERENCES Typ(id),
  FOREIGN KEY (secondary_type_id) REFERENCES Typ(id)
);
CREATE TABLE Skill (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) UNIQUE,
  strength INT,
  type_id INT NOT NULL,  
  PRIMARY KEY (id),
  FOREIGN KEY (type_id) REFERENCES Typ(id)
);
CREATE TABLE Pokemon_Skill (
  pokemon_id INT NOT NULL,
  skill_id INT NOT NULL,
  is_boosted BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
  FOREIGN KEY (skill_id) REFERENCES Skill(id),
  PRIMARY KEY (pokemon_id, skill_id)
);