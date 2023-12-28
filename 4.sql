-- a)a) Write a SQL statement to generate a list of salesmen who either serve one or 
-- more customers or have not joined any customer yet. The customers may have placed one or 
-- more orders with an order amount equal to or exceeding 2000, and they must have a grade. 
-- Alternatively, customers may not have placed any order with the associated supplier.(Use joins)
-- Return cust_name, cust city, grade, Salesman name, ord_no, ord_date, purch_amt

SELECT c.cust_name,c.city,c.grade,s.name,o.ord_no,o.ord_date,o.purch_amt
FROM customer c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN salesman s ON c.salesman_id = s.salesman_id
WHERE(o.purch_amt >= 2000 AND c.grade IS NOT NULL);
    -- OR(o.customer_id IS NULL AND c.grade IS NOT NULL);

-- b) Write a SQL statement to generate a report with the customer name, city, order number, order date, 
-- and purchase amount for customers on the list who must have a grade and placed one or more orders. 
-- Additionally, include orders placed by customers who are neither on the list nor have a grade.(Use joins)

SELECT c.cust_name, c.city, o.ord_no,
       o.ord_date, o.purch_amt
FROM customer c 
FULL OUTER JOIN orders o 
ON c.customer_id = o.customer_id 
WHERE c.grade IS NOT NULL AND o.customer_id IS NOT NULL;


