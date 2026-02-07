CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(255),
    date_naissance DATE,
    pays VARCHAR(255),
    ville VARCHAR(255),
    code_postal VARCHAR(5)
);

INSERT INTO users (nom, prenom, email, date_naissance, pays, ville, code_postal)
VALUES ('John', 'Doe', 'john@example.com', '1990-01-01', 'France', 'Paris', '75001');