USE task7_db;

CREATE TABLE IF NOT EXISTS demo_enrollments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id VARCHAR(20) NOT NULL,
  student_name VARCHAR(50) NOT NULL,
  course_code VARCHAR(20) NOT NULL,
  course_name VARCHAR(80) NOT NULL,
  score INT NOT NULL,
  semester VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 清空旧数据（方便重复演示）
TRUNCATE TABLE demo_enrollments;

INSERT INTO demo_enrollments (student_id, student_name, course_code, course_name, score, semester) VALUES
('S2025001','Student_A','CS101','Web Development Basics',88,'2025-Fall'),
('S2025002','Student_B','CS101','Web Development Basics',91,'2025-Fall'),
('S2025003','Student_C','CS101','Web Development Basics',85,'2025-Fall'),
('S2025004','Student_D','CS101','Web Development Basics',93,'2025-Fall'),
('S2025005','Student_E','CS101','Web Development Basics',87,'2025-Fall'),
('S2025006','Student_F','CS101','Web Development Basics',79,'2025-Fall'),

('S2025001','Student_A','DB201','Database Systems',90,'2025-Fall'),
('S2025002','Student_B','DB201','Database Systems',86,'2025-Fall'),
('S2025003','Student_C','DB201','Database Systems',92,'2025-Fall'),
('S2025004','Student_D','DB201','Database Systems',84,'2025-Fall'),
('S2025005','Student_E','DB201','Database Systems',89,'2025-Fall'),
('S2025006','Student_F','DB201','Database Systems',81,'2025-Fall'),

('S2025001','Student_A','DC301','Cloud Computing Fundamentals',95,'2025-Fall'),
('S2025002','Student_B','DC301','Cloud Computing Fundamentals',88,'2025-Fall'),
('S2025003','Student_C','DC301','Cloud Computing Fundamentals',90,'2025-Fall'),
('S2025004','Student_D','DC301','Cloud Computing Fundamentals',82,'2025-Fall'),
('S2025005','Student_E','DC301','Cloud Computing Fundamentals',85,'2025-Fall'),
('S2025006','Student_F','DC301','Cloud Computing Fundamentals',87,'2025-Fall'),

('S2025007','Student_G','SE210','Software Engineering',80,'2025-Fall'),
('S2025008','Student_H','SE210','Software Engineering',86,'2025-Fall'),
('S2025009','Student_I','NW220','Computer Networks',83,'2025-Fall'),
('S2025010','Student_J','NW220','Computer Networks',92,'2025-Fall'),
('S2025011','Student_K','AI330','Intro to AI',89,'2025-Fall'),
('S2025012','Student_L','AI330','Intro to AI',78,'2025-Fall');
