-- a)From the following tables write a SQL query to find those employees who work for the department 
-- where the departmental allotment amount is more than Rs. 50000. Return emp_fname and emp_lname.

SELECT e.emp_fname, e.emp_lname
FROM employee e
INNER JOIN department d ON e.emp_dept = d.dpt_code
WHERE d.dpt_allotment > 50000;

--  write a SQL query to find the departments with the second lowest sanction amount. Return emp_fname and emp_lname.

SELECT employee.emp_fname, employee.emp_lname
FROM employee
WHERE emp_dept =(
    SELECT dpt_code
    FROM department
    ORDER BY dpt_allotment 
    LIMIT 1 OFFSET 1
);



