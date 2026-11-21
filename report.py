
# Step 50: Create Automated PDF Report

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image, PageBreak
import os
# Load cleaned dataset
df = pd.read_csv("data/superstore_cleaned.csv")

# Create PDF
pdf = SimpleDocTemplate(
    "reports/Superstore_Business_Report.pdf",
    pagesize=A4
)

styles = getSampleStyleSheet()
elements = []

# Report Title
elements.append(
    Paragraph(
        "SUPERSTORE SALES & PROFIT ANALYSIS",
        styles["Title"]
    )
)

elements.append(Spacer(1, 20))

# Introduction
elements.append(
    Paragraph(
        "Automated Business Analysis Report",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        "This report analyzes Superstore sales, "
        "profit, customers, products and regional performance.",
        styles["Normal"]
    )
)

# Step 51: Executive Summary and KPI Metrics

# Calculate KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
average_discount = df["Discount"].mean() * 100

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

# Add Executive Summary
elements.append(Spacer(1, 20))

elements.append(
    Paragraph(
        "EXECUTIVE SUMMARY",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        "This report provides an overview of Superstore "
        "business performance using sales, profit, "
        "customer and order data.",
        styles["Normal"]
    )
)

elements.append(Spacer(1, 15))

# Add KPI Section
elements.append(
    Paragraph(
        "KEY PERFORMANCE INDICATORS",
        styles["Heading2"]
    )
)

kpis = [
    f"Total Sales: ${total_sales:,.2f}",
    f"Total Profit: ${total_profit:,.2f}",
    f"Total Orders: {total_orders:,}",
    f"Total Customers: {total_customers:,}",
    f"Average Discount: {average_discount:.2f}%",
    f"Profit Margin: {profit_margin:.2f}%"
]

for kpi in kpis:
    elements.append(
        Paragraph(kpi, styles["Normal"])
    )
    elements.append(Spacer(1, 8))

print("Executive Summary and KPIs Added!")





# Step 52: Business Insights

# Calculate category-wise sales
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Calculate region-wise sales
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Calculate product-wise profit
product_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

# Add Business Insights heading
elements.append(Spacer(1, 20))

elements.append(
    Paragraph(
        "BUSINESS INSIGHTS",
        styles["Heading2"]
    )
)

# Category Insight
elements.append(
    Paragraph(
        "1. CATEGORY PERFORMANCE",
        styles["Heading3"]
    )
)

for category, sales in category_sales.items():
    elements.append(
        Paragraph(
            f"{category}: ${sales:,.2f}",
            styles["Normal"]
        )
    )

elements.append(Spacer(1, 12))

# Regional Insight
elements.append(
    Paragraph(
        "2. REGIONAL PERFORMANCE",
        styles["Heading3"]
    )
)

for region, sales in region_sales.items():
    elements.append(
        Paragraph(
            f"{region}: ${sales:,.2f}",
            styles["Normal"]
        )
    )

elements.append(Spacer(1, 12))

# Product Profitability Insight
elements.append(
    Paragraph(
        "3. PRODUCT PROFITABILITY",
        styles["Heading3"]
    )
)

top_product = product_profit.index[0]
least_product = product_profit.index[-1]

elements.append(
    Paragraph(
        f"Most Profitable Product: {top_product}",
        styles["Normal"]
    )
)

elements.append(
    Paragraph(
        f"Least Profitable Product: {least_product}",
        styles["Normal"]
    )
)

elements.append(Spacer(1, 12))

print("Business Insights Added Successfully!")




# Step 53: Add Visualization Charts to PDF

elements.append(PageBreak())

elements.append(
    Paragraph(
        "DATA VISUALIZATIONS",
        styles["Heading2"]
    )
)

chart_files = [
    ("Sales Distribution", "sales_distribution.png"),
    ("Profit Distribution", "profit_distribution.png"),
    ("Category-wise Sales", "category_sales.png"),
    ("Region-wise Sales", "region_sales.png"),
    ("Shipping Mode Distribution", "shipping_mode_count.png"),
    ("Customer Segment Sales", "customer_segment_pie.png"),
    ("Monthly Sales Trend", "monthly_sales_trend.png"),
    ("Profit Box Plot", "profit_boxplot.png"),
    ("Correlation Heatmap", "correlation_heatmap.png"),
    ("Pair Plot", "pair_plot.png")
]

for chart_title, chart_filename in chart_files:

    chart_path = os.path.join(
        "visualizations",
        chart_filename
    )

    if os.path.exists(chart_path):

        elements.append(
            Paragraph(
                chart_title,
                styles["Heading3"]
            )
        )

        # Read image dimensions and maintain aspect ratio
        chart = Image(chart_path)

        max_width = 450
        max_height = 550

        scale = min(
            max_width / chart.imageWidth,
            max_height / chart.imageHeight,
            1
        )

        chart.drawWidth = chart.imageWidth * scale
        chart.drawHeight = chart.imageHeight * scale

        elements.append(chart)
        elements.append(Spacer(1, 20))

        print(f"Added: {chart_filename}")

    else:
        print(f"Chart Not Found: {chart_filename}")

print("Visualization Charts Added Successfully!")





# Step 54: Final Business Recommendations

elements.append(PageBreak())

elements.append(
    Paragraph(
        "BUSINESS RECOMMENDATIONS",
        styles["Heading2"]
    )
)

# Identify best region
best_region = region_sales.idxmax()

# Identify category with lowest profit
category_profit = df.groupby("Category")["Profit"].sum()
lowest_profit_category = category_profit.idxmin()

# Calculate loss-making transactions
loss_transactions = (df["Profit"] < 0).sum()

recommendations = [
    (
        f"1. Focus on the {best_region} region, "
        "which generates the highest sales. "
        "Study successful strategies used in this region."
    ),
    (
        f"2. Review the {lowest_profit_category} category, "
        "which has the lowest total profit. "
        "Identify opportunities to improve profitability."
    ),
    (
        f"3. Investigate {loss_transactions:,} loss-making "
        "order items and identify the main causes of losses."
    ),
    (
        "4. Review discount policies and measure their "
        "impact on profit before offering large discounts."
    ),
    (
        "5. Monitor monthly sales trends to improve "
        "inventory planning and marketing decisions."
    )
]

for recommendation in recommendations:
    elements.append(
        Paragraph(
            recommendation,
            styles["Normal"]
        )
    )
    elements.append(Spacer(1, 15))

elements.append(
    Paragraph(
        "CONCLUSION",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        "This analysis provides insights into Superstore "
        "sales, profitability, customer segments and "
        "regional performance. These findings can help "
        "support data-driven business decisions.",
        styles["Normal"]
    )
)

print("Business Recommendations Added Successfully!")


# Generate PDF
pdf.build(elements)

print("PDF Report Created Successfully!")