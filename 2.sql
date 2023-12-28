-- a) Write a SQL query for the given table to retrieve details of salespeople with commissions ranging from 0.10 to 0.12.
-- (Begin and end values are included.) Return salesman_id, name, city, and commission
SELECT salesman_id, name, city, commission
FROM salesman
WHERE commission BETWEEN 0.10 AND 0.12;

 salesman_id |    name    |   city   | commission
-------------+------------+----------+------------
        5005 | Pit Alex   | London   |       0.11
        5003 | Lauson Hen | San Jose |       0.12


--b) Write a SQL query for the given table to retrieve avg details of commissions
--  ranging from 0.12 to 0.14.(Begin and end values are included.)
SELECT AVG(commission) AS average
FROM salesman
WHERE commission BETWEEN 0.12 AND 0.14;

 average
---------
    0.13
