-- Active: 1734301207878@@127.0.0.1@3306@Quiz_DB

-- Quiz Application Database Design

-- Table: Users
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role ENUM('student', 'teacher') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: Quizzes
CREATE TABLE Quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    teacher_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Table: Questions
CREATE TABLE Questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id INT NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES Quizzes(id) ON DELETE CASCADE
);

-- Table: Options
CREATE TABLE Options (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    FOREIGN KEY (question_id) REFERENCES Questions(id) ON DELETE CASCADE
);

-- Table: Student_Answers
CREATE TABLE Student_Answers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    quiz_id INT NOT NULL,
    question_id INT NOT NULL,
    option_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (quiz_id) REFERENCES Quizzes(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES Questions(id) ON DELETE CASCADE,
    FOREIGN KEY (option_id) REFERENCES Options(id) ON DELETE CASCADE,
    UNIQUE(student_id, quiz_id, question_id) -- Ensure one attempt per question per quiz
);


-- Insert into Users
INSERT INTO Users (id, name, role, created_at) VALUES
(1, 'Alice Smith', 'teacher', '2024-01-01 10:00:00'),
(2, 'Bob Johnson', 'teacher', '2024-01-02 11:00:00'),
(3, 'Charlie Davis', 'student', '2024-01-03 12:00:00'),
(4, 'Dana Lee', 'student', '2024-01-04 13:00:00');

-- Insert into Quizzes
INSERT INTO Quizzes (id, title, teacher_id, created_at) VALUES
(1, 'Math Quiz', 1, '2024-01-05 14:00:00'),
(2, 'Science Quiz', 2, '2024-01-06 15:00:00');

-- Insert into Questions
INSERT INTO Questions (id, quiz_id, text) VALUES
(1, 1, 'What is 2 + 2?'),
(2, 1, 'What is the square root of 16?'),
(3, 2, 'What planet is known as the Red Planet?'),
(4, 2, 'What is the chemical symbol for water?');

-- Insert into Options
INSERT INTO Options (id, question_id, text, is_correct) VALUES
(1, 1, '3', FALSE),
(2, 1, '4', TRUE),
(3, 1, '5', FALSE),
(4, 2, '2', FALSE),
(5, 2, '4', TRUE),
(6, 2, '8', FALSE),
(7, 3, 'Earth', FALSE),
(8, 3, 'Mars', TRUE),
(9, 3, 'Jupiter', FALSE),
(10, 4, 'H2O', TRUE),
(11, 4, 'O2', FALSE),
(12, 4, 'CO2', FALSE);

-- Insert into Student_Answers
INSERT INTO Student_Answers (id, student_id, quiz_id, question_id, option_id) VALUES
(1, 3, 1, 1, 2),
(2, 3, 1, 2, 5),
(3, 4, 2, 3, 8),
(4, 4, 2, 4, 10);
