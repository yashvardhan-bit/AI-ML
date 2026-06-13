CREATE DATABASE IF NOT EXISTS college;
USE college;
CREATE TABLE teacher(
id int PRIMARY KEY,
name varchar(25),
subject varchar(30),
salary float);
INSERT INTO teacher VALUES
(23,"Ajay","Math",50000),
(47,"Bharat","English",60000),
(18,"Chetan","Chemistry",45000),
(9,"Divya","Physics",75000);
select * from teacher;

SELECT * FROM teacher
WHERE salary>55000;

ALTER TABLE teacher
CHANGE COLUMN salary ctc INT;

UPDATE teacher
SET ctc=ctc*1.25;

ALTER TABLE teacher
ADD COLUMN city VARCHAR(50) DEFAULT "Gurgaon";

ALTER TABLE teacher
DROP COLUMN CTC;

CREATE TABLE student(
rollno INT PRIMARY KEY,
name VARCHAR(30),
city VARCHAR(30),
marks INT);

INSERT INTO student
(rollno,name,city,marks)
VALUES
(110,"Adam","Delhi",76),
(108,"Bob","Mumbai",65),
(124,"Casey","Pune",94),
(112,"Duke","Pune",80);

SELECT * FROM student;
 
SELECT *
FROM student
WHERE marks>75;

SELECT DISTINCT city
FROM student;

SELECT city
FROM student
GROUP BY city;

SELECT city, max(marks)
FROM student
GROUP BY city;

SELECT avg(marks)
FROM student;

ALTER TABLE student
ADD COLUMN grade VARCHAR(5);

UPDATE student
SET grade ="O"
WHERE marks>=80;

UPDATE student
SET grade ="A"
WHERE marks>70 AND marks<80;

UPDATE student
SET grade ="B"
WHERE marks>60 AND marks<70;

select * FROM student;
