# https://www.kaggle.com/datasets/knightbearr/sales-product-data
import numpy as np
import statistics as st
import math as m
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter
import datetime as dt
# load data from C drive
import pandas as pd
df_sp = pd.read_csv(r"C:\Users\Master\Documents\data_analytics\Kaggle\Ecommerce\sales_2019_silver_complete.csv")
# print(df_sp.head(10))
# df_sp.info()
# print(df_sp.shape)
# print(df_sp.isnull())
# rename some columns and assign as a new df
df_sp1 = df_sp.rename(columns={'revenue': 'sales', 'quantity': 'units_sold'})
# change order date to datetime format
df_sp1['order_date'] = pd.to_datetime(df_sp1['order_date'])
# create and add minute and month column
df_sp1['min'] = df_sp1['order_date'].dt.minute
df_sp1['month'] = df_sp1['order_date'].dt.month
print(df_sp1.head(3))
# print(df_sp1.head(5))
df_sp1.info()
# print(df_sp1[['order_date', 'month']])
# print(df_sp1.groupby('month').sum()['sales'].sort_values(ascending=False).head(1))

# plt.title('sales by month', fontweight="bold", color='darkslategray')
results_month = df_sp1.groupby('month').sum()['sales']
plt.bar(results_month.index, results_month)
for x,y in zip(results_month.index, results_month):
    label = "{:.0f}".format(y) # no decimal point
    plt.text(x, y, label, ha='center', va='bottom')
plt.xticks(results_month.index)
plt.title('sales by month', fontweight="bold", color='darkslategray')
plt.legend()
plt.show()

# plt.title('sales by city', fontweight="bold", color='darkslategray')
results_city = df_sp1.groupby('city').sum()['sales']
plt.bar(results_city.index, results_city)
for x,y in zip(results_city.index, results_city):
    label = "{:.0f}".format(y) # no decimal point
    plt.text(x, y, label, ha='center', va='bottom')
plt.xticks(results_city.index)
plt.title('sales by city', fontweight="bold", color='darkslategray')
plt.legend()
plt.show()

# plt.title('unique order counts by hour', fontweight="bold", color='darkslategray')
results_hour = df_sp1.groupby('hour')['order_id'].nunique() # unique counts of order_id
hours = [hour for hour, df in df_sp1.groupby('hour')]
plt.bar(results_hour.index, results_hour)  
for x,y in zip(results_hour.index, results_hour):
    label = "{:.0f}".format(y) # no decimal point
    plt.text(x, y, label, ha='center', va='bottom')
plt.xticks(results_hour.index)
plt.title('unique order counts by hour', fontweight="bold", color='darkslategray')
plt.legend()
plt.show()


# df_sp1.to_csv(r"C:\Users\Master\Documents\data_analytics\Kaggle\Ecommerce\df_sp1.csv", index=True)

# we have multiple rows for the same order id as some orders are combos of multiple producs. 
# Use Keep=False to keep all repeats as True by  boolean operator Duplicated(). Non-repeat order ids are removed by default as the boolean will return false for all nopn repeats
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html 
df_combobase = df_sp1[df_sp1['order_id'].duplicated(keep=False)]
# join all the product attributes with comma ',' using transform join x
df_combobase['product_combo'] = df_combobase.groupby('order_id')['product'].transform(lambda x: ', '.join(x))
# now drop the duplicated rows of order_id and product combo
df_combofinal = df_combobase[['order_id','product_combo']].drop_duplicates()
print(df_combofinal.head(20))

# export to csv
df_combofinal.to_csv(r"C:\Users\Master\Documents\data_analytics\Kaggle\Ecommerce\order_combo.csv", index=False)

from itertools import combinations
from collections import Counter

results_combo = df_combofinal.groupby('product_combo').count()['order_id'].sort_values(ascending=False)
print(results_combo)
results_combo.to_csv(r"C:\Users\Master\Documents\data_analytics\Kaggle\Ecommerce\results_combo.csv", index=True)