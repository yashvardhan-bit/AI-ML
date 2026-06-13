#JOINS
CREATE DATABASE joins;
USE joins;
CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
amount INT

);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104,5,700);

SELECT * FROM customers;
SELECT * FROM orders;

#inner join
SELECT *
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id;

SELECT c.customer_id,o.order_id,c.name
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id;

#LEFT JOIN /LEFT OUTTER JOIN
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id;

#RIGHT JOIN
SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id=o.customer_id;

#OUTTER JOIN
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id
UNION
SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id=o.customer_id;

#CROSS JOIN
SELECT *
FROM customers
CROSS JOIN orders;

# SELF JOIN (ON SAME TABLE)
SELECT *
FROM customers as A
JOIN customers as B
ON A.customer_id=B.customer_id;

#EXCLUSIVE JOINS
SELECT *
FROM customers A
LEFT JOIN orders B
ON A.customer_id=B.customer_id
WHERE B.customer_id IS NULL;

SELECT *
FROM customers A
RIGHT JOIN orders B
ON A.customer_id=B.customer_id
WHERE A.customer_id IS NULL;
