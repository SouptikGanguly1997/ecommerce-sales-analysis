--  1: Total revenue
SELECT SUM(amount) AS total_revenue
FROM sales;
-- 2: Top customer
select name, Sum(amount) as total_spent
from sales
group by name
order by total_spent desc
limit 1;
-- 3: City with highest revenue
select city, Sum(amount) as city_with_highest_revenue
from sales
group by city
order by city_with_highest_revenue desc
limit 1;
-- 4: Customer Segmentation: 60000=>"VIP",30000-60000=>"Regular",else=>"Low"
select name, Sum(amount) as total_spent, 
case 
	when Sum(amount) >= 60000 then 'VIP'
    when 60000> Sum(amount) >30000  then 'Regular'
    else 'Low'
end as Category
from sales
group by name;
-- 5. Revenue distibution by city
SELECT city,
SUM(amount) AS revenue,
(SUM(amount) * 100.0 / SUM(SUM(amount)) OVER()) AS percentage
FROM sales
GROUP BY city
order by percentage desc;