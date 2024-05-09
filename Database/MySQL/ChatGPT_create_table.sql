CREATE TABLE Pokemon (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE
);

CREATE TABLE Type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE
);

CREATE TABLE Skill (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    type_id INT,
    strength DECIMAL(5, 2),
    FOREIGN KEY (type_id) REFERENCES Type(id)
);

CREATE TABLE Pokemon_Type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pokemon_id INT,
    type_id INT,
    is_primary BOOLEAN,
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
    FOREIGN KEY (type_id) REFERENCES Type(id)
);

CREATE TABLE Pokemon_Skill (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pokemon_id INT,
    skill_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
    FOREIGN KEY (skill_id) REFERENCES Skill(id)
);

CREATE TABLE Type_Interaction (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type_id1 INT,
    type_id2 INT,
    multiplier DECIMAL(3, 2),
    FOREIGN KEY (type_id1) REFERENCES Type(id),
    FOREIGN KEY (type_id2) REFERENCES Type(id)
);
