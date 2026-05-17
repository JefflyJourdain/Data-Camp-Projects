
select count(*) as missing_year
from products
where  year_added is null;


-- Write your query for task 2 in this cell
with clean_data as (select product_id,coalesce(product_type,'Unknown') as product_type ,coalesce(replace(brand,'-','Unknown'),'Unknown') as brand,
	round(coalesce(replace(weight,'grams','')::numeric,(select avg(replace(weight,'grams','')::numeric) from products)),2) as weight 
	,round(coalesce(price::numeric,(select avg(price::numeric) from products)),2) as price,coalesce(average_units_sold::int,0) as average_units_sold,coalesce(year_added,'2022') as year_added ,coalesce(upper(stock_location),'Unknown') as stock_location
from products)
select *
from clean_data;

#  finding out how the range varies for each product type  

-- Write your query for task 3 in this cell
select product_type,min(price) as min_price ,max(price) as max_price
from products
group by product_type;

# 
#  more detail look at meat and dairy products where the average units sold was greater than ten. 
# 
-- Write your query for task 4 in this cell
with meat_dairy as (select * 
	from products 
	where product_type = 'Dairy' or product_type = 'Meat')
select product_id,price,average_units_sold
from meat_dairy 
	--group by product_id,price
where average_units_sold > 10;

