-- Creating a table

-- Constraints -> Data integrity

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    student_id TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    gender TEXT,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at DATE
);

-- CRON jobs - background jobs that run repeatedly

-- modify
ALTER TABLE students ADD COLUMN nationality TEXT; -- adds a column

ALTER TABLE students DROP COLUMN nationality; -- works in sqlite above 3.37
-- Parameter binding - sqlalchemy
-- delete a table
DROP TABLE students;


-- CRUD operations

-- CREATE
INSERT INTO students (name, student_id, email, age, gender) VALUES ("Jane", 32423, "jane@student.com", 20, "Female")

INSERT INTO students (name, student_id, email, age) VALUES ("John", 32321, "john@student.com", 25)

-- READ -> query modifiers
SELECT * FROM students;

-- Updating
UPDATE students SET gender = "Male"; -- updates all rows

UPDATE students SET gender = "Female" WHERE id = 1; -- update specific rows

-- DELETE
-- Soft deleting using what we call flags
DELETE FROM students; --deletes all records

DELETE FROM students WHERE id = 4;

UPDATE students SET is_deleted = TRUE WHERE id = 8;
UPDATE students SET deleted_at = "date provided by the backend" WHERE id = 8;

SELECT * FROM students WHERE is_deleted = FALSE;
SELECT * FROM students WHERE deleted_at IS NULL;

INSERT INTO students (name, student_id, email, age) VALUES ("Haji", 3242, "haji@student.com", 26)

SELECT count(id), avg(age), sum(age), max(age), min(age) FROM students;


SELECT sqlite_version();
