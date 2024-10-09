# Full name: Darshan Wadekar 
# Student ID: 8934575 
# Class number: Fall Section 1 - Cloud DevOps

-- Create the 'departments' table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

-- Insert sample data into the 'departments' table
INSERT INTO departments (department_name, location) VALUES 
('Human Resources', 'New York'),
('Finance', 'Toronto'),
('Engineering', 'San Francisco');

-- Create the 'employees' table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Update the 'departments' table to modify a column
ALTER TABLE departments MODIFY location VARCHAR(500);

-- Delete a specific row from the departments table
DELETE FROM departments WHERE department_id = 1;
