import sqlite3


## connect to sqlite 
connection = sqlite3.connect("test.db")

## Create a cursor object to insert record, create table , retrieve
cursor = connection.cursor()

## Create the table
table_info = [["""
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    JobTitle VARCHAR(100),
    DepartmentID INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
"""
],["""
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    Name VARCHAR(100),
    ManagerID INT,
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
);
"""
],["""CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    Name VARCHAR(100),
    DepartmentID INT,
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

"""],[
    """
CREATE TABLE Tasks (
    TaskID INT PRIMARY KEY,
    Description VARCHAR(255),
    ProjectID INT,
    AssigneeID INT,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (AssigneeID) REFERENCES Employees(EmployeeID)
);"""
]]

for table in table_info:
    cursor.execute(table[0])
    print('\n')

## Insert some more records
queries = [['''
INSERT INTO Employees (EmployeeID, Name, JobTitle, DepartmentID, Salary) VALUES
(1, 'John Doe', 'Software Engineer', 1, 70000.00),
(2, 'Jane Smith', 'Data Analyst', 2, 60000.00),
(3, 'Michael Johnson', 'Project Manager', 3, 80000.00),
(4, 'Emily Brown', 'HR Specialist', 4, 55000.00),
(5, 'David Wilson', 'Marketing Manager', 5, 75000.00);
'''],[
'''INSERT INTO Departments (DepartmentID, Name, ManagerID) VALUES
(1, 'Engineering', 1),
(2, 'Data Science', 2),
(3, 'Project Management', 3),
(4, 'Human Resources', 4),
(5, 'Marketing', 5);'''
],[
'''
INSERT INTO Projects (ProjectID, Name, DepartmentID, StartDate, EndDate) VALUES
(101, 'Website Development', 1, '2024-01-01', '2024-06-30'),
(102, 'Data Analysis Project', 2, '2024-02-15', '2024-08-31'),
(103, 'Product Launch', 3, '2024-03-10', '2024-10-31'),
(104, 'Employee Training Program', 4, '2024-04-01', '2024-05-31'),
(105, 'Marketing Campaign', 5, '2024-05-01', '2024-07-31');'''
],[
    """
-- Tasks
INSERT INTO Tasks (TaskID, Description, ProjectID, AssigneeID) VALUES
(1, 'Design website layout', 101, 1),
(2, 'Write backend code', 101, 1),
(3, 'Analyze user data', 102, 2),
(4, 'Prepare project report', 102, 2),
(5, 'Coordinate team meetings', 103, 3),
(6, 'Conduct training sessions', 103, 3),
(7, 'Recruit new employees', 104, 4),
(8, 'Handle employee grievances', 104, 4),
(9, 'Design marketing materials', 105, 5),
(10, 'Run social media campaigns', 105, 5);
"""
]]

for i in queries:
    cursor.execute(i[0])
## Display all the records 
print('The inserted records are')

data = cursor.execute('''SELECT e.Name AS EmployeeName, e.JobTitle, d.Name AS DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID;''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close()