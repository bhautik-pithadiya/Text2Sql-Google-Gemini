-- SQLite
SELECT E.Name
FROM Employees AS E
JOIN Tasks AS T ON E.EmployeeID = T.AssigneeID
JOIN Projects AS P ON T.ProjectID = P.ProjectID
WHERE P.Name = 'Website Development';