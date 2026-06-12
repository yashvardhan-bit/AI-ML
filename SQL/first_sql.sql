create database college;
CREATE DATABASE IF NOT EXISTS instagram;
DROP DATABASE IF EXISTS college;
SHOW DATABASES;
USE instagram;
CREATE TABLE IF NOT EXISTS user(
Id INT,
Age INT,
Name VARCHAR(30) NOT NULL,
Email VARCHAR(30) UNIQUE,
Followers INT DEFAULT 0,
Following INT,
CONSTRAINT CHECK(Age>=13),
PRIMARY KEY(Id)
);
INSERT INTO user
(Id,Age,Name,Email,Followers,Following)
VALUES
(1,14,"yash","yash@gmail.com",121,223),
(2,19,"oscar","badmoshi.com",89,2233),
(3,33,"bob","laadle@yaahoo",121,223),
(4,67,"cameraman","meow@123.in",123,23);
SELECT * FROM user;



CREATE TABLE post(
id INT PRIMARY KEY,
content VARCHAR(100),
user_id INT,
FOREIGN KEY (user_id) REFERENCES user(Id)
);
INSERT INTO post VALUES
(101,"Badmashi matt kariye mittar",3),
(102,"Ki haal ne tere we",1),
(103,"Ni pehla naalo farak bda",3);



SELECT * FROM post;
SELECT DISTINCT user_id FROM post;

SELECT Name,Age
FROM user
WHERE Age>=14
LIMIT 2;

SELECT name,age,followers
FROM user
ORDER BY followers DESC;

SELECT name,age,followers
FROM user
ORDER BY followers;

#Aggregate function
SELECT count(followers)
FROM user
WHERE AGE>14;

#group by
SELECT age, max(followers)
FROM user
GROUP BY age;