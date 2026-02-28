1.
SELECT COUNT(DISTINCT customer_id)
FROM customers;

2. 
SELECT COUNT(DISTINCT account_no)
FROM accounts;

3.
SELECT COUNT(DISTINCT tran_id)
FROM transactions;

-- I used the count & distinct funtion instead of count(*) so, the result doesnt contain duplicates records or null value
4.
SELECT COUNT(*)
FROM fx_rates;

5. 
SELECT customer_id, full_name, phone, email
FROM customers
WHERE created_at = '2025-01-01';

6.
SELECT*
FROM customers
WHERE phone = '0803499078';

7.
SELECT*
FROM customers
WHERE email IN ('customer10850@bank.com', 'customer50306500@bank.com');

-- Decides to use the 'IN' operator instead of 'AND' because our findings is limited to 'email'.
8.
SELECT*
FROM accounts
WHERE status = 'ACTIVE'
AND account_type = 'CURRENT'
LIMIT 100;
-- I used 'AND' here because our finidings is both connected to 'status', and 'account_type'.

9.
SELECT*
FROM accounts
WHERE balance > '500000'
AND account_type = 'SAVINGS'
LIMIT 100;
--similar explanation as no 8.

10.
SELECT DISTINCT account_type
FROM accounts;

11. 
SELECT*
FROM transactions
LIMIT 100;

12.
SELECT*
FROM transactions
WHERE amount > '100000'
LIMIT 500;

13.
SELECT *
FROM transactions
WHERE tran_type = 'DEBIT'
AND tran_date BETWEEN '2025-12-01' AND '2025-12-31';

14.
SELECT
	c.customer_id,
	c.full_name,
	c.email,
	c.phone,
	a.opened_date,
	a.status,
	a.account_type
FROM customers c
JOIN accounts a
	ON c.customer_id = a.customer_id
WHERE a.account_no = 'ACC5273';

15.
SELECT*
FROM transactions
WHERE a.account_no = 'ACC733869'
AND tran_date BETWEEN '2025-10-01' AND '2025-12-31';

16.
SELECT
	c.customer_id,
	c.full_name,
	c.email,
	c.phone,
	a.opened_date,
	a.status,
	a.account_type, 
	t.tran_id, 
	t.tran_type,
	t.amount,
	t.tran_date,
	t.narrative
FROM customers c
JOIN accounts a
	ON c.customer_id = a.customer_id
JOIN transactions t
	ON a.account_no = t.account_no
WHERE a.account_no = 'ACC733869'
AND tran_date BETWEEN '2025-10-01' AND '2025-12-31';

17. 
SELECT *
FROM transactions
WHERE account_no = 'ACC2558028186' 
AND narrative LIKE 'ATM%'
AND tran_date BETWEEN '2025-06-01' AND '2025-06-30';

18.
SELECT 
	c.customer_id,
	c.full_name,
	a.account_no
FROM customers c
LEFT JOIN accounts a
	ON c.customer_id = a.customer_id
WHERE a.account_no IS NULL
LIMIT 329;

19.
SELECT 
   t.tran_id, 
   a.account_type,
   t.amount
FROM transactions t
JOIN accounts a
	ON t.customer_id = a.customer_id
WHERE customer_id = '1247'
AND tran_date IN ('2025-10-12', '2025-10-20');

20. 
SELECT
    c.customer_id,
    c.full_name,
    COUNT(a.account_no) AS account_count
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.full_name
HAVING COUNT(a.account_no) > 1
LIMIT 10;

21.
SELECT 
	t.tran_id,
	t.account_no,
	t.customer_id,
	t.amount,
	t.tran_type,
	a.account_type
FROM transactions t
JOIN accounts a
	ON t.account_no = a.account_no
WHERE a.account_type = 'CURRENT'
AND tran_date BETWEEN '2025-06-01' AND '2025-06-30';

22.
SELECT 
	c.customer_id,
	c.full_name,
	a.account_no,
	a.balance
FROM customers c
LEFT JOIN accounts a
	ON c.customer_id = a.customer_id
WHERE a.balance	> '1000000'

23.
SELECT
	t.tran_id,
	t.account_no,
	t.customer_id,
	t.amount,
	f.ccy,
	f.rate
FROM transactions t
JOIN fx_rates f
	ON t.tran_date = f.business_date
WHERE t.account_no = 'ACC5055287'  
AND ccy = 'USD'
AND tran_date = '2026-01-07';

25.
SELECT
	account_no,
	SUM(amount) AS total_tran_amount
FROM transactions
WHERE tran_date BETWEEN '2026-01-01' AND '2026-01-31'
GROUP BY account_no;


26.

SELECT
	customer_id,
	COUNT(tran_id) AS total_tran
FROM transactions
WHERE tran_date BETWEEN '2026-01-01' AND '2026-01-31'
GROUP BY customer_id;

27.
SELECT
	account_no,
	SUM(amount) AS total_tran_value
FROM transactions
WHERE tran_date BETWEEN '2025-12-01' AND '2025-12-31'
GROUP BY account_no
ORDER BY total_tran_value  DESC
LIMIT 5;

28.
SELECT
	customer_id,
	AVG(amount) AS average_amount
FROM transactions
WHERE tran_date BETWEEN '2025-10-01' AND '2025-12-31'
GROUP BY customer_id;

29.
SELECT
	tran_id
	customer_id,
	account_no,
	amount
FROM transactions
WHERE account_no = ' ACC5055287'
ORDER BY amount DESC
LIMIT 1;

30.
SELECT 
	SUM(t.amount) AS credit_turnover
FROM transactions t
JOIN accounts a
	ON t.account_no = a.account_no
WHERE a.account_type = 'SAVINGS'
AND tran_type = 'CREDIT'
AND tran_date BETWEEN '2025-01-01' AND '2025-12-31';

31.
SELECT 
	SUM(t.amount) AS debit_turnover
FROM transactions t
JOIN accounts a
	ON t.account_no = a.account_no
WHERE a.account_type = 'CURRENT'
AND tran_type = 'DEBIT'
AND tran_date BETWEEN '2025-01-01' AND '2025-12-31';

