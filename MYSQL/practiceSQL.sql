show databases;

# Creating Database
CREATE DATABASE college;

# Select The Database
USE college;

# Creating Table students
CREATE TABLE IF NOT EXISTS students(name varchar(50),age int,address varchar(100),marks int);

# Structure Of Table
DESC students;

# INSERTING VALUES IN TABLE
INSERT INTO students VALUES ('Abir',22,'Assam',100);
INSERT INTO students(name,age,address,marks) VALUES ('Amisha',20,'Assam',100);
INSERT INTO students VALUES ('Vikas',21,'Haryana',95),('Mukund',20,'Rajasthan',90),('Anam',21,'Telengana',98);

# Viewing The Data Of Table
SELECT * FROM students;

# View Students From Assam
SELECT * FROM students where address like 'Assam';

# Display students whose marks are greater than 75.
SELECT * FROM students WHERE marks>=95;

# Display students whose age is less than 21.
SELECT * FROM students WHERE marks<95;

# Display students who belong to Mumbai and scored more than 95
SELECT * FROM students WHERE marks>90 and address like 'Assam';

# Display students whose marks are between 60 and 90.
SELECT * FROM students WHERE marks between 95 and 100;

# Display students who belong to Delhi OR Pune.
SELECT * FROM students WHERE address like 'Assam' or address like 'Haryana';

# Display students whose age is NOT 22.
SELECT * FROM students WHERE age <> 22;

# Display students whose name starts with 'A'.
SELECT * FROM students WHERE name like 'A%';

# Display students whose name ends with 'n'.
SELECT * FROM students WHERE name like '%m'; # m -> M and m both

# Display students whose city is in (Delhi, Mumbai, Chandigarh).
SELECT * FROM students WHERE address like 'Assam' or address like 'Haryana';

# Display first 3 students from table
SELECT * FROM students LIMIT 3;

# Display top 3 student who scored highest marks
SELECT * FROM students ORDER BY marks DESC LIMIT 3;

# Display 2 students after skipping first 2 records.
SELECT * FROM students LIMIT 2 OFFSET 2;

# Display only 1 student with lowest marks.
SELECT * FROM students order by marks LIMIT 1;

# Display first 4 students from Mumbai.
SELECT * FROM students WHERE address like 'ASSAM' LIMIT 1;

# Display all students sorted by marks ascending
SELECT * FROM students ORDER BY marks;

# Display all students sorted by marks descending
SELECT * FROM students ORDER BY marks DESC;

# Display studynts sorted by name alphabeticålly.
SELECT * FROM students ORDER BY name;

# Display students sorted by city then marks descending
SELECT * FROM students ORDER BY address ASC, marks DESC;

# Display students sorted by age descending
SELECT * FROM students ORDER BY age DESC;

# Find the total number of students.
SELECT COUNT(*) FROM students;

# Find the maximum marks scored.
SELECT MAX(marks) FROM students;

# Find the minimum marks scored.
SELECT MIN(marks) FROM students;

# Find the average marks of students.
SELECT AVG(marks) FROM students;

# Find the sum of all marks.
SELECT SUM(marks) FROM students;


