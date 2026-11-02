CREATE TABLE students(
    id INTEGER  PRIMARY KEY, 
    name TEXT,
    mark REAL,
    age INTEGER);
INSERT INTO students(name, mark, age) VALUES('Иванов', 41, 19)
SELECT * FROM students WHERE age>18
UPDATE students SET age=20 WHERE name='Иванов'
DELETE FROM students WHERE id=1 
