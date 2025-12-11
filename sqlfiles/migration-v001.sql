CREATE DATABASE mydb;

\c mydb;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO users (username, email)
VALUES ('john', 'john@example.com');

-- Student TABLE