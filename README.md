# Sales_Product_Data
An attempt to identify potential marketing decision that can be explored through the analysis of the dataset of ecommerce electronics orders fulfiled a few select US cities. 

## Project summary of the empirical, methodical and teleological findings by coderedstorage
* Six-field dataset for fulfilled e-commerce orders (incl. quantities, selling prices etc) of premium and low-ASP/consumable electronic devices. Details for purchase times/locations (across a few US cities) is also included.
* MySQL/Python(Pandas) needed to faciliate enablement of useful datasets for Tableau Public. Enablement activity comprises creating derived fields on original ones for analysis. This includes cleansing (including detection/elimination of small numbers of duplication) and data type conversions into realistically analyzable formats. Python/MySQL scripts provided for reference.
* Generated insights:
  * Behavioral patterns such as monthly seasonality, performance over space(city) and time (weeks/months) and hourly purchase patterns. 
  * Product taxonomy based on product species and economicssuch, lower lifetime consumables vs non-consumables, and overlaying premium versus low ASP.
  * Orders are categorized based on basket complexity such as one type product vs multiple products. Economic density (revenue per order) shown in parallel. 
  * Estimated probabilities of the next purchase by product type.
* Limitations and blindspots:
  * There is limited 2020 data, hence analysis is restricted to 2019 only, and covers only a narrow slice of the ecommerce market, making it unrepresentative of the deterministic features of the market. Therefore, adjusting for outliers may not be necessary for enablement. 
  * Further investigation for joint probacilities of complementary multiple product purchases may be educational. While multiple product purchases carry greater economic density, such orders are likley anchored by the major premium/high-value product in the basket, thus reverting to single product type analytics, assuming the one-way etiological flow. Joint probabilities were not examined. 
  * It may be useful to analyze the data further based on bespoke sets created to align with proper etiological assessment. For now this consideration serves as a placeholder.
  * Lack of unit cost of inventory data, proportionate SG&A cost allocation to units, returns (and cost of returns) and rebates result in poor resolution on the effective per unit margins, which may challenge the economic presupposition made on advertising decisions (for short-term predictable conversions), made based on hourly purchase patterns.
  - The data is inherently lacking the property to explain potential indeterministic possibilities for esoteric brand-building and advertising efforts, and as  

## About Dataset (from ther source Kaggle link https://public.tableau.com/views/sales_2019/StorySalesProductData?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link) 
# Context
Sales analytics is the practice of generating insights from sales data, trends, and metrics to set targets and forecast future sales performance. Sales analysis is mining your data to evaluate the performance of your sales team against its goals. It provides insights about the top performing and underperforming products/services, the problems in selling and market opportunities, sales forecasting, and sales activities that generate revenue.
# Content
Order ID - An Order ID is the number system that Amazon uses exclusively to keep track of orders. Each order receives its own Order ID that will not be duplicated. This number can be useful to the seller when attempting to find out certain details about an order such as shipment date or status.
Product - The product that have been sold.
Quantity Ordered - Ordered Quantity is the total item quantity ordered in the initial order (without any changes).
Price Each - The price of each products.
Order Date - This is the date the customer is requesting the order be shipped.
Purchase Address - The purchase order is prepared by the buyer, often through a purchasing department. The purchase order, or PO, usually includes a PO number, which is useful in matching shipments with purchases; a shipping date; billing address; shipping address; and the request items, quantities and price.
# Target
A target market analysis is an assessment of how your product or service fits into a specific market and where it will gain the most.
# Task:
Q: What was the best Year for sales? How much was earned that Year?
Q: What was the best month for sales? How much was earned that month?
Q: What City had the highest number of sales?
Q: What time should we display adverstisement to maximize likelihood of customer's buying product?
Q: What products are most often sold together?
Q: What product sold the most? Why do you think it sold the most?
# How Much Probability?
How much probability for next people will ordered USB-C Charging Cable?
How much probability for next people will ordered iPhone?
How much probability for next people will ordered Google Phone?
How much probability other peoples will ordered Wired Headphones?
