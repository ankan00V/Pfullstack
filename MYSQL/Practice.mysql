mysql> use college;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

mysql> CREATE TABLE stud (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(50),
    ->     city VARCHAR(50),
    ->     marks INT,
    ->     age INT
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> INSERT INTO stud (name, city, marks, age) VALUES
    -> ('Aman', 'Delhi', 82, 20),
    -> ('Rohan', 'Mumbai', 76, 22),
    -> ('Anita', 'Pune', 91, 19),
    -> ('Karan', 'Delhi', 67, 21),
    -> ('Arjun', 'Mumbai', 88, 20),
    -> ('Neha', 'Chennai', 73, 23),
    -> ('Anil', 'Delhi', 95, 18),
    -> ('Sonia', 'Pune', 60, 22),
    -> ('Varun', 'Mumbai', 79, 20),
    -> ('Aditi', 'Delhi', 85, 21);
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM stud;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
|  1 | Aman  | Delhi   |    82 |   20 |
|  2 | Rohan | Mumbai  |    76 |   22 |
|  3 | Anita | Pune    |    91 |   19 |
|  4 | Karan | Delhi   |    67 |   21 |
|  5 | Arjun | Mumbai  |    88 |   20 |
|  6 | Neha  | Chennai |    73 |   23 |
|  7 | Anil  | Delhi   |    95 |   18 |
|  8 | Sonia | Pune    |    60 |   22 |
|  9 | Varun | Mumbai  |    79 |   20 |
| 10 | Aditi | Delhi   |    85 |   21 |
+----+-------+---------+-------+------+
10 rows in set (0.01 sec)

mysql> SELECT * FROM stud WHERE city = 'Delhi';
+----+-------+-------+-------+------+
| id | name  | city  | marks | age  |
+----+-------+-------+-------+------+
|  1 | Aman  | Delhi |    82 |   20 |
|  4 | Karan | Delhi |    67 |   21 |
|  7 | Anil  | Delhi |    95 |   18 |
| 10 | Aditi | Delhi |    85 |   21 |
+----+-------+-------+-------+------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE marks > 75;
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  1 | Aman  | Delhi  |    82 |   20 |
|  2 | Rohan | Mumbai |    76 |   22 |
|  3 | Anita | Pune   |    91 |   19 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  7 | Anil  | Delhi  |    95 |   18 |
|  9 | Varun | Mumbai |    79 |   20 |
| 10 | Aditi | Delhi  |    85 |   21 |
+----+-------+--------+-------+------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE age < 21;
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  1 | Aman  | Delhi  |    82 |   20 |
|  3 | Anita | Pune   |    91 |   19 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  7 | Anil  | Delhi  |    95 |   18 |
|  9 | Varun | Mumbai |    79 |   20 |
+----+-------+--------+-------+------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE city = 'Mumbai' AND marks > 75;
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  2 | Rohan | Mumbai |    76 |   22 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  9 | Varun | Mumbai |    79 |   20 |
+----+-------+--------+-------+------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE marks BETWEEN 60 AND 90;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
|  1 | Aman  | Delhi   |    82 |   20 |
|  2 | Rohan | Mumbai  |    76 |   22 |
|  4 | Karan | Delhi   |    67 |   21 |
|  5 | Arjun | Mumbai  |    88 |   20 |
|  6 | Neha  | Chennai |    73 |   23 |
|  8 | Sonia | Pune    |    60 |   22 |
|  9 | Varun | Mumbai  |    79 |   20 |
| 10 | Aditi | Delhi   |    85 |   21 |
+----+-------+---------+-------+------+
8 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE city = 'Delhi' OR city = 'Pune';
+----+-------+-------+-------+------+
| id | name  | city  | marks | age  |
+----+-------+-------+-------+------+
|  1 | Aman  | Delhi |    82 |   20 |
|  3 | Anita | Pune  |    91 |   19 |
|  4 | Karan | Delhi |    67 |   21 |
|  7 | Anil  | Delhi |    95 |   18 |
|  8 | Sonia | Pune  |    60 |   22 |
| 10 | Aditi | Delhi |    85 |   21 |
+----+-------+-------+-------+------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE age <> 22;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
|  1 | Aman  | Delhi   |    82 |   20 |
|  3 | Anita | Pune    |    91 |   19 |
|  4 | Karan | Delhi   |    67 |   21 |
|  5 | Arjun | Mumbai  |    88 |   20 |
|  6 | Neha  | Chennai |    73 |   23 |
|  7 | Anil  | Delhi   |    95 |   18 |
|  9 | Varun | Mumbai  |    79 |   20 |
| 10 | Aditi | Delhi   |    85 |   21 |
+----+-------+---------+-------+------+
8 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE name LIKE 'A%';
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  1 | Aman  | Delhi  |    82 |   20 |
|  3 | Anita | Pune   |    91 |   19 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  7 | Anil  | Delhi  |    95 |   18 |
| 10 | Aditi | Delhi  |    85 |   21 |
+----+-------+--------+-------+------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE name LIKE '%n';
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  1 | Aman  | Delhi  |    82 |   20 |
|  2 | Rohan | Mumbai |    76 |   22 |
|  4 | Karan | Delhi  |    67 |   21 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  9 | Varun | Mumbai |    79 |   20 |
+----+-------+--------+-------+------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE name LIKE '%n';
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  1 | Aman  | Delhi  |    82 |   20 |
|  2 | Rohan | Mumbai |    76 |   22 |
|  4 | Karan | Delhi  |    67 |   21 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  9 | Varun | Mumbai |    79 |   20 |
+----+-------+--------+-------+------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM stud WHERE city IN ('Delhi', 'Mumbai', 'Chandigarh');
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  1 | Aman  | Delhi  |    82 |   20 |
|  2 | Rohan | Mumbai |    76 |   22 |
|  4 | Karan | Delhi  |    67 |   21 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  7 | Anil  | Delhi  |    95 |   18 |
|  9 | Varun | Mumbai |    79 |   20 |
| 10 | Aditi | Delhi  |    85 |   21 |
+----+-------+--------+-------+------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM stud LIMIT 3;
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  1 | Aman  | Delhi  |    82 |   20 |
|  2 | Rohan | Mumbai |    76 |   22 |
|  3 | Anita | Pune   |    91 |   19 |
+----+-------+--------+-------+------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM stud ORDER BY marks DESC LIMIT 5;
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  7 | Anil  | Delhi  |    95 |   18 |
|  3 | Anita | Pune   |    91 |   19 |
|  5 | Arjun | Mumbai |    88 |   20 |
| 10 | Aditi | Delhi  |    85 |   21 |
|  1 | Aman  | Delhi  |    82 |   20 |
+----+-------+--------+-------+------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM stud LIMIT 2 OFFSET 2;
+----+-------+-------+-------+------+
| id | name  | city  | marks | age  |
+----+-------+-------+-------+------+
|  3 | Anita | Pune  |    91 |   19 |
|  4 | Karan | Delhi |    67 |   21 |
+----+-------+-------+-------+------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM stud ORDER BY marks ASC LIMIT 1;
+----+-------+------+-------+------+
| id | name  | city | marks | age  |
+----+-------+------+-------+------+
|  8 | Sonia | Pune |    60 |   22 |
+----+-------+------+-------+------+
1 row in set (0.00 sec)

mysql> 
mysql> SELECT * FROM stud WHERE city = 'Mumbai' LIMIT 4;
+----+-------+--------+-------+------+
| id | name  | city   | marks | age  |
+----+-------+--------+-------+------+
|  2 | Rohan | Mumbai |    76 |   22 |
|  5 | Arjun | Mumbai |    88 |   20 |
|  9 | Varun | Mumbai |    79 |   20 |
+----+-------+--------+-------+------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM stud ORDER BY marks ASC;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
|  8 | Sonia | Pune    |    60 |   22 |
|  4 | Karan | Delhi   |    67 |   21 |
|  6 | Neha  | Chennai |    73 |   23 |
|  2 | Rohan | Mumbai  |    76 |   22 |
|  9 | Varun | Mumbai  |    79 |   20 |
|  1 | Aman  | Delhi   |    82 |   20 |
| 10 | Aditi | Delhi   |    85 |   21 |
|  5 | Arjun | Mumbai  |    88 |   20 |
|  3 | Anita | Pune    |    91 |   19 |
|  7 | Anil  | Delhi   |    95 |   18 |
+----+-------+---------+-------+------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM stud ORDER BY marks DESC;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
|  7 | Anil  | Delhi   |    95 |   18 |
|  3 | Anita | Pune    |    91 |   19 |
|  5 | Arjun | Mumbai  |    88 |   20 |
| 10 | Aditi | Delhi   |    85 |   21 |
|  1 | Aman  | Delhi   |    82 |   20 |
|  9 | Varun | Mumbai  |    79 |   20 |
|  2 | Rohan | Mumbai  |    76 |   22 |
|  6 | Neha  | Chennai |    73 |   23 |
|  4 | Karan | Delhi   |    67 |   21 |
|  8 | Sonia | Pune    |    60 |   22 |
+----+-------+---------+-------+------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM stud ORDER BY name ASC;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
| 10 | Aditi | Delhi   |    85 |   21 |
|  1 | Aman  | Delhi   |    82 |   20 |
|  7 | Anil  | Delhi   |    95 |   18 |
|  3 | Anita | Pune    |    91 |   19 |
|  5 | Arjun | Mumbai  |    88 |   20 |
|  4 | Karan | Delhi   |    67 |   21 |
|  6 | Neha  | Chennai |    73 |   23 |
|  2 | Rohan | Mumbai  |    76 |   22 |
|  8 | Sonia | Pune    |    60 |   22 |
|  9 | Varun | Mumbai  |    79 |   20 |
+----+-------+---------+-------+------+
10 rows in set (0.01 sec)

mysql> SELECT * FROM stud ORDER BY city ASC, marks DESC;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
|  6 | Neha  | Chennai |    73 |   23 |
|  7 | Anil  | Delhi   |    95 |   18 |
| 10 | Aditi | Delhi   |    85 |   21 |
|  1 | Aman  | Delhi   |    82 |   20 |
|  4 | Karan | Delhi   |    67 |   21 |
|  5 | Arjun | Mumbai  |    88 |   20 |
|  9 | Varun | Mumbai  |    79 |   20 |
|  2 | Rohan | Mumbai  |    76 |   22 |
|  3 | Anita | Pune    |    91 |   19 |
|  8 | Sonia | Pune    |    60 |   22 |
+----+-------+---------+-------+------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM stud ORDER BY age DESC;
+----+-------+---------+-------+------+
| id | name  | city    | marks | age  |
+----+-------+---------+-------+------+
|  6 | Neha  | Chennai |    73 |   23 |
|  2 | Rohan | Mumbai  |    76 |   22 |
|  8 | Sonia | Pune    |    60 |   22 |
|  4 | Karan | Delhi   |    67 |   21 |
| 10 | Aditi | Delhi   |    85 |   21 |
|  1 | Aman  | Delhi   |    82 |   20 |
|  5 | Arjun | Mumbai  |    88 |   20 |
|  9 | Varun | Mumbai  |    79 |   20 |
|  3 | Anita | Pune    |    91 |   19 |
|  7 | Anil  | Delhi   |    95 |   18 |
+----+-------+---------+-------+------+
10 rows in set (0.01 sec)

mysql> 
