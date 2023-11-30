# Sales Product Data Analysis
An attempt to identify potential marketing decision that can be explored through the analysis of the dataset of ecommerce electronics orders fulfilled in a few select US cities. 

## 1. Project description
Generate insights from sales data, trends, activities and relevant metrics which can be used to set targets and forecast dales performance, and execute decisions such as advertising.

## 2. Submission & Feedback
* Self-directed project.
* Submitted to Masterschool schoolmaster and received commendation, and subsequently presented to Masterschool class.

## 3. Insights
* Please see dashboard [(Tableau Story)](https://public.tableau.com/views/Sales_Product_Data/StorySalesProductData?:language=en-US&:display_count=n&:origin=viz_share_link)
* Types of insights shown:
  * Global and local financial metrics.
  * Behavioral patterns or trends: monthly seasonality, performance over space (city) and time (weeks/months) and hourly purchase patterns. 
  * Product taxonomy: overlay product species and economics, with considerations on lower lifespan consumables vs. non-consumables, and premium vs. low ASP (average selling price).
  * Orders are categorized based on basket complexity, such as one type of product vs. multiple products. Economic density (revenue per order) shown in parallel. 
  * Estimated probabilities of the next purchase by product type.

## 4. Resources:
* Dashboard [(Tableau Story)](https://public.tableau.com/views/Sales_Product_Data/StorySalesProductData?:language=en-US&:display_count=n&:origin=viz_share_link)
* [Github](https://github.com/coderedstorage/Sales_Product_Data)
   * [Sales_Product_Data.twbx](https://github.com/coderedstorage/Sales_Product_Data/blob/main/Sales_Product_Data.twbx)
   * [archive.zip](https://github.com/coderedstorage/Sales_Product_Data/blob/main/archive.zip) (original data obtained from [Kaggle](https://www.kaggle.com/datasets/knightbearr/sales-product-data?resource=download)). Imported into MySQL table ecommerce.raw_table.
   * [ecommerce.sales_2019_silver.sql](https://github.com/coderedstorage/Sales_Product_Data/blob/main/ecommerce.sales_2019_silver.sql) MySQL script to generate MySQL view ecommerce.sales_2019_silver.
   * [sales_2019_silver_complete.zip](https://github.com/coderedstorage/Sales_Product_Data/blob/main/sales_2019_silver_complete.zip) (final dataset committed to Tableau) exported from MySQL view ecommerce.sales_2019_silver.
   * [Sales_Product_Analysis.ipynb](https://github.com/coderedstorage/Sales_Product_Data/blob/main/Sales_Product_Analysis.ipynb) python notebook to generate combo product analysis (order_combo.csv).
   * [order_combo.csv](https://github.com/coderedstorage/Sales_Product_Data/blob/main/order_combo.csv) (data additionally committed to Tableau).

## 5. Tools used
* MySQL/Python(Pandas) to facilitate enablement of useful derived datasets
* Tableau Public to create visualization (requires final dataset sales_2019_silver_complete.csv zipped in sales_2019_silver_complete.zip, and order_combo.csv to be committed to Tableau Public)
* Enablement comprises:
   * Create derived fields on original ones for analysis.
   * Data cleansing (detection/elimination of small numbers of duplication).
   * Data type conversions to analyzable formats (e.g. text date to datetime).
   * Python/MySQL scripts in repository for reference.

## 6. Condition of dataset
* Six-field dataset for fulfilled e-commerce orders (incl. quantities, selling prices etc) of premium and low-ASP/consumable electronics. 
* Details for purchase times/locations (across a few US cities) is also included.
* Minimal duplications found.
* Lacks proper indexing in the form of sub-order ids etc, though not essesntial. 
* More details, see Appendix.

## 7. Limitations and blind spots:
* Only full year 2019 information is available in the dataset. Thus the analysis is restricted to 2019, and on a narrow slice of the ecommerce market in a handful of US cities. Thus, dataset may not be representative of the deterministic features of the addressable market. Thus, adjusting for outliers may not be necessary for enablement. 
* Further investigation for joint probabilities of complementary multiple product purchases may be educational for now:
  * While multiple product purchases carry greater economic density, such orders are likely anchored by the major premium/high-value product component in the basket. 
  * Reverting to single product-type analytics on units sold regardless of basket type (single product or blended) may be sufficient for probabilistic assessments on next sale by product, assuming one-way etiological flow in blended baskets. 
  * Also, blended baskets are a small slice of the overall order counts. Joint probabilities thus are not examined.
  * Still, it may be useful to analyze the data further for probabilistic assessments based on some segmentation of orders that make sense with proper etiological assessment. This consideration serves as a placeholder for future enhancement. 
* Poor resolution on unit economics (i.e. effective per unit margins) is limiting the intelligence needed to plan and forecast the business. If issues exist with respect adverse unit economics, there may be material challenge to the soundness of the economic presupposition on the proposed advertising decision (based on hourly purchase patterns). What drives poor resolution? Drivers on costs such as unit cost of inventory, proportionate SG&A cost allocation, returns (+ cost), platform charges, rebates and others are missing from the dataset.
* The data by nature, lacks useful property to divine potential indeterminate possibilities for transformational brand-building and advertising efforts. As such, it is insufficient to capture Mr. AD-man Rory Sutherland's notion of 'magic'.

# Appendix: About the dataset
Copied from [Kaggle](https://www.kaggle.com/datasets/knightbearr/sales-product-data?resource=download).
## Context
Sales analytics is the practice of generating insights from sales data, trends, and metrics to set targets and forecast future sales performance. Sales analysis is mining your data to evaluate the performance of your sales team against its goals. It provides insights about the top performing and underperforming products/services, the problems in selling and market opportunities, sales forecasting, and sales activities that generate revenue.
## Content
* Order ID - An Order ID is the number system that Amazon uses exclusively to keep track of orders. Each order receives its own Order ID that will not be duplicated. This number can be useful to the seller when attempting to find out certain details about an order such as shipment date or status.
* Product - The product that have been sold.
* Quantity Ordered - Ordered Quantity is the total item quantity ordered in the initial order (without any changes).
* Price Each - The price of each products.
* Order Date - This is the date the customer is requesting the order be shipped.
* Purchase Address - The purchase order is prepared by the buyer, often through a purchasing department. The purchase order, or PO, usually includes a PO number, which is useful in matching shipments with purchases; a shipping date; billing address; shipping address; and the request items, quantities and price.
## Target
A target market analysis is an assessment of how your product or service fits into a specific market and where it will gain the most.
## Task:
* Q: What was the best Year for sales? How much was earned that Year? - [dataset insufficient to answer this]
* Q: What was the best month for sales? How much was earned that month?
* Q: What City had the highest number of sales?
* Q: What time should we display adverstisement to maximize likelihood of customer's buying product?
* Q: What products are most often sold together?
* Q: What product sold the most? Why do you think it sold the most?
## How Much Probability?
* How much probability for next people will ordered USB-C Charging Cable?
* How much probability for next people will ordered iPhone?
* How much probability for next people will ordered Google Phone?
* How much probability other peoples will ordered Wired Headphones?
