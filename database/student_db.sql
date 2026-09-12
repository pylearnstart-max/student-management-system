CREATE DATABASE student_db;
GO

USE student_db;
GO

CREATE TABLE Students (
    StudentID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Course VARCHAR(100),
    Age INT,
    Status VARCHAR(20)
);
GO