CREATE OR REPLACE VIEW ecommerce.sales_2019_silver AS
WITH base AS (
SELECT
		DISTINCT CONCAT(order_id,'-',product,'-',quantity,'-',price,'-',order_date_txt,'-',customer_address) keyword_id,
        order_id,
        product,
        quantity,
        price,
        STR_TO_DATE(order_date_txt, '%m/%d/%y %H:%i') AS order_date,
        customer_address
FROM ecommerce.raw_table)
SELECT
		order_id,
		product,
		quantity,
		price,
		quantity*price AS revenue,
		order_date,
		customer_address,
		DAY(order_date) AS day_no,
		MONTH(order_date) AS month_no,
		YEAR(order_date) AS year_no,
		HOUR(order_date) AS hour,
		WEEKDAY(order_date) AS week_day_no,
		DAYNAME(order_date) AS day_name,
        CASE 
			WHEN WEEKDAY(order_date) IN (5,6) THEN 'Y' 
            ELSE 'N' 
        END AS is_weekend,
SUBSTRING_INDEX(customer_address, ', ', 1) street_address, 
SUBSTRING_INDEX(SUBSTRING_INDEX(customer_address, ', ', -2), ', ',1) city,
SUBSTRING_INDEX(SUBSTRING_INDEX(customer_address, ', ', - 1),' ',1) state_code,
SUBSTRING_INDEX(SUBSTRING_INDEX(customer_address, ', ', - 1),' ',-1) zipcode
FROM base
WHERE YEAR(order_date) = 2019;