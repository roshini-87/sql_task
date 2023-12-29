-- a) Write a SQL query for the provided table to retrieve the first five unique salespeople IDs 
-- in order based on higher purchase amounts, where each salesperson's purchase amount should not exceed 2000.
SELECT salesman_id, MAX(purch_amt) AS max_purchase
FROM orders
WHERE purch_amt <= 2000
GROUP BY salesman_id
ORDER BY max_purchase DESC
LIMIT 5;

 salesman_id | max_purchase
-------------+--------------
        5006 |      1983.43
        5002 |        948.5
        5005 |       270.65
        5003 |        110.5
        5007 |        75.29
        
-- b) Write a SQL query for the provided table to retrieve the first five unique salespeople IDs
--  in order based on lower purchase amounts, where each salesperson's purchase amount should exceed 100.
SELECT salesman_id, MAX(purch_amt) AS max_purchase
FROM orders
WHERE purch_amt > 100
GROUP BY salesman_id
ORDER BY max_purchase ASC
LIMIT 5;

 salesman_id | max_purchase
-------------+--------------
        5005 |       270.65
        5002 |        948.5
        5006 |      1983.43
        5003 |       2480.4
        5001 |         5760