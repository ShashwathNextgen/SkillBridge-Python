-- Remove MySQL-specific settings
-- SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
-- SET AUTOCOMMIT = 0;
-- SET time_zone = "+00:00";
-- /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
-- /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
-- /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;

-- Start the transaction
BEGIN;

-- Creating the tables in PostgreSQL syntax
CREATE TABLE admin (
    id serial PRIMARY KEY,
    email varchar(255) NOT NULL,
    password varchar(1000) NOT NULL
);

CREATE TABLE books (
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL,
    description text NOT NULL,
    author varchar(255) NOT NULL,
    availability boolean NOT NULL,
    edition varchar(255) NOT NULL,
    count integer NOT NULL
);

CREATE TABLE reserve (
    id serial PRIMARY KEY,
    user_id integer NOT NULL,
    book_id integer NOT NULL
);

CREATE TABLE users (
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(1000) NOT NULL,
    bio text,
    mob varchar(255),
    locked boolean,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO admin (email, password) VALUES
('hamza@gmail.com', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8');

INSERT INTO books (name, description, author, availability, edition, count) VALUES
('101 Ways To Be A Software Engineer', 'Description text here', 'Mr. Johnny Test', true, '1', 3),
('JAVA For Absolute Beginners', 'Basic description here', '', true, '1', 5);

INSERT INTO reserve (user_id, book_id) VALUES
(1, 1),
(6, 1);

INSERT INTO users (name, email, password, bio, mob, locked, created_at) VALUES
('Hamza', 'hamza@gmail.com', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Bio text here', '', false, '2021-11-09 00:00:00'),
('Naveed Ali', 'naveed@gmail.com', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', 'Another bio text', '', false, '2021-11-18 23:07:53');

-- Commit the transaction
COMMIT;
