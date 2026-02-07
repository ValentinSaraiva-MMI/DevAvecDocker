CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(255),
    promo VARCHAR(50)
);

INSERT INTO students (nom, prenom, email, promo)
VALUES ('Alice', 'Smith', 'alice@example.com', 'M2 Info');