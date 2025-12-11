CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(255),
    classe VARCHAR(50)
);

INSERT INTO students (nom, prenom, email, classe)
VALUES ('Alice', 'Smith', 'alice@example.com', 'M2 Info');