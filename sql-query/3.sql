-- 3. From the following table, write a SQL query to find those employees who 
-- worked more than or equal to  two jobs in the past. Return employee id. 

SELECT employee_id
FROM employee_history
GROUP BY employee_id
HAVING COUNT(DISTINCT job_id) >= 2;


employee_id
-------------
         101
         176
         200