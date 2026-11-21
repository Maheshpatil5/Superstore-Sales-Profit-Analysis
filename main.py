
import pandas as pd

# Load Superstore Dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())













# Step 9: Data Understanding

print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())



















# Step 10: Data Cleaning

# Create a copy of original dataset
df_clean = df.copy()

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()

# Check missing values
print("\nMissing Values:")
print(df_clean.isnull().sum())

# Remove rows with missing values
df_clean = df_clean.dropna()

# Convert date columns
df_clean["Order Date"] = pd.to_datetime(
    df_clean["Order Date"], format="%m/%d/%Y"
)

df_clean["Ship Date"] = pd.to_datetime(
    df_clean["Ship Date"], format="%m/%d/%Y"
)

# Display cleaned dataset shape
print("\nCleaned Dataset Shape:")
print(df_clean.shape)

# Save cleaned dataset
df_clean.to_csv(
    "data/superstore_cleaned.csv",
    index=False
)

print("\nData Cleaning Completed Successfully!")












# Step 11: Sales & Profit Analysis

# Calculate Total Sales
total_sales = df_clean["Sales"].sum()

# Calculate Total Profit
total_profit = df_clean["Profit"].sum()

# Calculate Profit Margin
profit_margin = (total_profit / total_sales) * 100

# Display Results
print("\n===== SALES & PROFIT ANALYSIS =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")


















# Step 12: Category-wise Sales Analysis

# Calculate total sales by category
category_sales = df_clean.groupby("Category")["Sales"].sum()

# Sort sales from highest to lowest
category_sales = category_sales.sort_values(
    ascending=False
)

# Display results
print("\n===== CATEGORY-WISE SALES =====")
print(category_sales)

# Find highest-selling category
top_category = category_sales.idxmax()

print("\nHighest Selling Category:", top_category)























# Step 13: Sub-Category Performance Analysis

# Calculate sales and profit by sub-category
subcategory_analysis = df_clean.groupby(
    "Sub-Category"
)[["Sales", "Profit"]].sum()

# Sort by highest sales
subcategory_analysis = subcategory_analysis.sort_values(
    by="Sales",
    ascending=False
)

# Display results
print("\n===== SUB-CATEGORY PERFORMANCE =====")
print(subcategory_analysis)

# Find highest selling sub-category
top_subcategory = subcategory_analysis["Sales"].idxmax()

# Find most profitable sub-category
most_profitable = subcategory_analysis["Profit"].idxmax()

# Find least profitable sub-category
least_profitable = subcategory_analysis["Profit"].idxmin()

print("\nHighest Selling Sub-Category:", top_subcategory)
print("Most Profitable Sub-Category:", most_profitable)
print("Least Profitable Sub-Category:", least_profitable)





















# Step 14: Customer Segment Analysis

# Calculate sales and profit by segment
segment_analysis = df_clean.groupby(
    "Segment"
)[["Sales", "Profit"]].sum()

# Sort by highest sales
segment_analysis = segment_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\n===== CUSTOMER SEGMENT ANALYSIS =====")
print(segment_analysis)

# Find highest sales segment
top_sales_segment = segment_analysis["Sales"].idxmax()

# Find most profitable segment
top_profit_segment = segment_analysis["Profit"].idxmax()

print("\nHighest Sales Segment:", top_sales_segment)
print("Most Profitable Segment:", top_profit_segment)





















# Step 15: Shipping Mode Analysis

# Count orders by shipping mode
shipping_count = df_clean.groupby(
    "Ship Mode"
)["Order ID"].nunique()

print("\n===== SHIPPING MODE ORDER COUNT =====")
print(shipping_count)

# Calculate sales and profit by shipping mode
shipping_analysis = df_clean.groupby(
    "Ship Mode"
)[["Sales", "Profit"]].sum()

shipping_analysis = shipping_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\n===== SHIPPING MODE SALES & PROFIT =====")
print(shipping_analysis)

# Find most preferred shipping mode
most_preferred = shipping_count.idxmax()

print("\nMost Preferred Shipping Mode:", most_preferred)

















# Step 16: Regional Sales & Profit Analysis

# Calculate sales and profit by region
regional_analysis = df_clean.groupby(
    "Region"
)[["Sales", "Profit"]].sum()

# Sort by highest sales
regional_analysis = regional_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\n===== REGIONAL SALES & PROFIT =====")
print(regional_analysis.round(2))

# Find highest sales region
top_sales_region = regional_analysis["Sales"].idxmax()

# Find most profitable region
top_profit_region = regional_analysis["Profit"].idxmax()

# Find least profitable region
lowest_profit_region = regional_analysis["Profit"].idxmin()

print("\nHighest Sales Region:", top_sales_region)
print("Most Profitable Region:", top_profit_region)
print("Least Profitable Region:", lowest_profit_region)





























# Step 17: Monthly Sales Trend Analysis

# Extract year and month from Order Date
df_clean["Year-Month"] = df_clean[
    "Order Date"
].dt.to_period("M")

# Calculate monthly sales
monthly_sales = df_clean.groupby(
    "Year-Month"
)["Sales"].sum()

# Sort by date
monthly_sales = monthly_sales.sort_index()

print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales.round(2))

# Find highest sales month
highest_sales_month = monthly_sales.idxmax()

# Find lowest sales month
lowest_sales_month = monthly_sales.idxmin()

print("\nHighest Sales Month:", highest_sales_month)
print("Lowest Sales Month:", lowest_sales_month)

print(
    "Highest Monthly Sales:",
    round(monthly_sales.max(), 2)
)






















# Step 18: Monthly Profit Trend Analysis

# Calculate monthly profit
monthly_profit = df_clean.groupby(
    "Year-Month"
)["Profit"].sum()

# Sort by date
monthly_profit = monthly_profit.sort_index()

print("\n===== MONTHLY PROFIT TREND =====")
print(monthly_profit.round(2))

# Find highest profit month
highest_profit_month = monthly_profit.idxmax()

# Find lowest profit month
lowest_profit_month = monthly_profit.idxmin()

print("\nHighest Profit Month:", highest_profit_month)
print("Lowest Profit Month:", lowest_profit_month)

print(
    "Highest Monthly Profit:",
    round(monthly_profit.max(), 2)
)

print(
    "Lowest Monthly Profit:",
    round(monthly_profit.min(), 2)
)

# Find months with negative profit
loss_months = monthly_profit[monthly_profit < 0]

print("\n===== LOSS-MAKING MONTHS =====")
print(loss_months.round(2))




















# Step 19: Category-wise Profit Analysis

# Calculate total profit by category
category_profit = df_clean.groupby(
    "Category"
)["Profit"].sum()

# Sort by highest profit
category_profit = category_profit.sort_values(
    ascending=False
)

print("\n===== CATEGORY-WISE PROFIT =====")
print(category_profit.round(2))

# Find most profitable category
top_profit_category = category_profit.idxmax()

# Find least profitable category
lowest_profit_category = category_profit.idxmin()

print("\nMost Profitable Category:", top_profit_category)
print("Least Profitable Category:", lowest_profit_category)

# Find loss-making categories
loss_categories = category_profit[category_profit < 0]

print("\n===== LOSS-MAKING CATEGORIES =====")
if loss_categories.empty:
    print("No loss-making categories found.")
else:
    print(loss_categories.round(2))
















# Step 20: Discount Analysis

# Calculate average discount by category
category_discount = df_clean.groupby(
    "Category"
)["Discount"].mean() * 100

# Sort by highest discount
category_discount = category_discount.sort_values(
    ascending=False
)

print("\n===== CATEGORY-WISE AVERAGE DISCOUNT =====")
print(category_discount.round(2))

# Find highest discount category
highest_discount_category = category_discount.idxmax()

print("\nHighest Discount Category:",
      highest_discount_category)

# Calculate overall average discount
average_discount = df_clean["Discount"].mean() * 100

print(f"\nOverall Average Discount: {average_discount:.2f}%")

# Calculate correlation between discount and profit
discount_profit_corr = df_clean[
    ["Discount", "Profit"]
].corr()

print("\n===== DISCOUNT VS PROFIT CORRELATION =====")
print(discount_profit_corr.round(3))


























# Step 21: Top 10 Customers by Sales

# Calculate total sales for each customer
customer_sales = df_clean.groupby(
    ["Customer ID", "Customer Name"]
)["Sales"].sum()

# Sort customers by highest sales
customer_sales = customer_sales.sort_values(
    ascending=False
)

# Select top 10 customers
top_10_customers = customer_sales.head(10)

print("\n===== TOP 10 CUSTOMERS BY SALES =====")
print(top_10_customers.round(2))

# Find highest spending customer
top_customer = customer_sales.idxmax()

print("\nHighest Spending Customer:", top_customer)
print(f"Total Spending: ${customer_sales.max():,.2f}")


















# Step 22: Top 10 Best-Selling Products

# Calculate quantity, sales and profit by product
product_analysis = df_clean.groupby(
    ["Product ID", "Product Name"]
)[["Quantity", "Sales", "Profit"]].sum()

# Sort by highest quantity sold
product_analysis = product_analysis.sort_values(
    by="Quantity",
    ascending=False
)

# Select top 10 products
top_10_products = product_analysis.head(10)

print("\n===== TOP 10 BEST-SELLING PRODUCTS =====")
print(top_10_products.round(2).to_string())

# Find best-selling product
best_selling_product = product_analysis.index[0]

print("\nBest-Selling Product:", best_selling_product)
print(
    "Total Units Sold:",
    product_analysis.iloc[0]["Quantity"]
)












# Step 23: Least Profitable Products Analysis

# Calculate sales and profit for each product
product_profit = df_clean.groupby(
    ["Product ID", "Product Name"]
)[["Sales", "Profit"]].sum()

# Sort by lowest profit
product_profit = product_profit.sort_values(
    by="Profit",
    ascending=True
)

# Select bottom 10 products
bottom_10_products = product_profit.head(10)

print("\n===== 10 LEAST PROFITABLE PRODUCTS =====")
print(bottom_10_products.round(2).to_string())

# Find product with highest loss
worst_product = product_profit.index[0]

print("\nLeast Profitable Product:", worst_product)

print(
    "Total Profit/Loss:",
    round(product_profit.iloc[0]["Profit"], 2)
)

# Count loss-making products
loss_products = product_profit[
    product_profit["Profit"] < 0
]

print("\nTotal Loss-Making Products:", len(loss_products))


















# Step 24: State-wise Sales & Profit Analysis

# Calculate sales and profit by state
state_analysis = df_clean.groupby(
    "State"
)[["Sales", "Profit"]].sum()

# Sort by highest sales
state_analysis = state_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\n===== STATE-WISE SALES & PROFIT =====")
print(state_analysis.round(2).to_string())

# Find highest sales state
top_sales_state = state_analysis["Sales"].idxmax()

# Find most profitable state
top_profit_state = state_analysis["Profit"].idxmax()

# Find least profitable state
lowest_profit_state = state_analysis["Profit"].idxmin()

print("\nHighest Sales State:", top_sales_state)
print("Most Profitable State:", top_profit_state)
print("Least Profitable State:", lowest_profit_state)

# Find loss-making states
loss_states = state_analysis[
    state_analysis["Profit"] < 0
]

print("\n===== LOSS-MAKING STATES =====")
print(loss_states.round(2).to_string())

print("\nTotal Loss-Making States:", len(loss_states))















# Step 25: Year-wise Sales & Profit Growth Analysis

# Extract year from Order Date
df_clean["Year"] = df_clean["Order Date"].dt.year

# Calculate yearly sales and profit
yearly_analysis = df_clean.groupby(
    "Year"
)[["Sales", "Profit"]].sum()

# Calculate year-over-year growth percentage
yearly_analysis["Sales Growth %"] = (
    yearly_analysis["Sales"].pct_change() * 100
)

yearly_analysis["Profit Growth %"] = (
    yearly_analysis["Profit"].pct_change() * 100
)

# Display results
print("\n===== YEAR-WISE SALES & PROFIT =====")
print(yearly_analysis.round(2).to_string())

# Find highest sales year
highest_sales_year = yearly_analysis["Sales"].idxmax()

# Find highest profit year
highest_profit_year = yearly_analysis["Profit"].idxmax()

print("\nHighest Sales Year:", highest_sales_year)
print("Highest Profit Year:", highest_profit_year)











# Step 26: Profit Margin Analysis

# Category-wise profit margin
category_margin = df_clean.groupby(
    "Category"
)[["Sales", "Profit"]].sum()

category_margin["Profit Margin %"] = (
    category_margin["Profit"] /
    category_margin["Sales"]
) * 100

print("\n===== CATEGORY-WISE PROFIT MARGIN =====")
print(category_margin.round(2).to_string())

# Sub-category-wise profit margin
subcategory_margin = df_clean.groupby(
    "Sub-Category"
)[["Sales", "Profit"]].sum()

subcategory_margin["Profit Margin %"] = (
    subcategory_margin["Profit"] /
    subcategory_margin["Sales"]
) * 100

# Sort by profit margin
subcategory_margin = subcategory_margin.sort_values(
    by="Profit Margin %",
    ascending=False
)

print("\n===== SUB-CATEGORY PROFIT MARGIN =====")
print(subcategory_margin.round(2).to_string())

# Best and worst profit margin
print(
    "\nHighest Profit Margin Sub-Category:",
    subcategory_margin["Profit Margin %"].idxmax()
)

print(
    "Lowest Profit Margin Sub-Category:",
    subcategory_margin["Profit Margin %"].idxmin()
)

















# Step 27: Final Business Insights

print("\n" + "=" * 55)
print("SUPERSTORE SALES & PROFIT - BUSINESS INSIGHTS")
print("=" * 55)

# Overall performance
total_sales = df_clean["Sales"].sum()
total_profit = df_clean["Profit"].sum()
total_orders = df_clean["Order ID"].nunique()

profit_margin = (total_profit / total_sales) * 100

print(f"\nTotal Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")

# Category insights
category_summary = df_clean.groupby(
    "Category"
)[["Sales", "Profit"]].sum()

print(
    "\nBest Sales Category:",
    category_summary["Sales"].idxmax()
)

print(
    "Most Profitable Category:",
    category_summary["Profit"].idxmax()
)

# Regional insights
region_summary = df_clean.groupby(
    "Region"
)[["Sales", "Profit"]].sum()

print(
    "\nTop Sales Region:",
    region_summary["Sales"].idxmax()
)

print(
    "Top Profit Region:",
    region_summary["Profit"].idxmax()
)

# Product insights
product_summary = df_clean.groupby(
    ["Product ID", "Product Name"]
)["Profit"].sum()

print(
    "\nLeast Profitable Product:",
    product_summary.idxmin()
)

# Customer insights
customer_summary = df_clean.groupby(
    ["Customer ID", "Customer Name"]
)["Sales"].sum()

print(
    "\nHighest Spending Customer:",
    customer_summary.idxmax()
)

# Discount insights
print(
    f"\nAverage Discount: "
    f"{df_clean['Discount'].mean() * 100:.2f}%"
)

print("\n===== BUSINESS RECOMMENDATIONS =====")
print("1. Review loss-making products and pricing.")
print("2. Investigate discounts on low-profit sales.")
print("3. Focus on high-performing categories.")
print("4. Improve performance in weak regions.")
print("5. Reward high-value customers.")

print("\nPYTHON EDA ANALYSIS COMPLETED!")
print("=" * 55)
