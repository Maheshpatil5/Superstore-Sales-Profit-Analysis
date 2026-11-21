
# Step 40: Sales Distribution Histogram

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/superstore_cleaned.csv")

# Set chart theme
sns.set_theme(style="whitegrid")

# Create histogram
plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Sales",
    bins=50,
    color="steelblue"
)

plt.title("Superstore Sales Distribution", fontsize=16)
plt.xlabel("Sales ($)")
plt.ylabel("Frequency")

plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/sales_distribution.png",
    dpi=300
)

plt.close()

print("Sales Distribution Chart Saved Successfully!")





# Step 41: Profit Distribution Histogram

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Profit",
    bins=50,
    color="seagreen"
)

# Zero profit reference line
plt.axvline(
    x=0,
    color="red",
    linestyle="--",
    label="Zero Profit"
)

plt.title("Superstore Profit Distribution", fontsize=16)
plt.xlabel("Profit ($)")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/profit_distribution.png",
    dpi=300
)

plt.close()

print("Profit Distribution Chart Saved Successfully!")










# Step 42: Category-wise Sales Bar Chart

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    category_sales.index,
    category_sales.values,
    color=["steelblue", "seagreen", "orange"]
)

plt.title("Category-wise Total Sales", fontsize=16)
plt.xlabel("Product Category")
plt.ylabel("Total Sales ($)")

# Display sales values above bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"${height:,.0f}",
        ha="center",
        va="bottom"
    )

plt.ylim(0, category_sales.max() * 1.15)
plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/category_sales.png",
    dpi=300
)

plt.close()

print("Category Sales Chart Saved Successfully!")












# Step 43: Region-wise Sales Bar Chart

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    region_sales.index,
    region_sales.values,
    color=["steelblue", "seagreen", "orange", "mediumpurple"]
)

plt.title("Region-wise Total Sales", fontsize=16)
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")

# Show sales values above bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"${height:,.0f}",
        ha="center",
        va="bottom"
    )

plt.ylim(0, region_sales.max() * 1.15)
plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/region_sales.png",
    dpi=300
)

plt.close()

print("Region Sales Chart Saved Successfully!")












# Step 44: Shipping Mode Count Plot

shipping_counts = (
    df["Ship Mode"]
    .value_counts()
)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    shipping_counts.index,
    shipping_counts.values,
    color=["steelblue", "seagreen", "orange", "mediumpurple"]
)

plt.title("Shipping Mode Distribution", fontsize=16)
plt.xlabel("Shipping Mode")
plt.ylabel("Number of Order Items")

# Display count above bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height):,}",
        ha="center",
        va="bottom"
    )

plt.ylim(0, shipping_counts.max() * 1.15)
plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/shipping_mode_count.png",
    dpi=300
)

plt.close()

print("Shipping Mode Count Chart Saved Successfully!")










# Step 45: Customer Segment Pie Chart

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 7))

plt.pie(
    segment_sales.values,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["steelblue", "seagreen", "orange"],
    wedgeprops={"edgecolor": "white"}
)

plt.title("Sales Distribution by Customer Segment", fontsize=16)

plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/customer_segment_pie.png",
    dpi=300
)

plt.close()

print("Customer Segment Pie Chart Saved Successfully!")











# Step 46: Monthly Sales Trend Line Chart

# Convert Order Date into datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%Y-%m-%d"
)

# Calculate monthly sales
monthly_sales = (
    df.groupby(
        df["Order Date"].dt.to_period("M")
    )["Sales"]
    .sum()
    .sort_index()
)

# Convert months to timestamps for plotting
monthly_sales.index = monthly_sales.index.to_timestamp()

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    color="steelblue",
    marker="o",
    markersize=3,
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/monthly_sales_trend.png",
    dpi=300
)

plt.close()

print("Monthly Sales Trend Chart Saved Successfully!")





# Step 47: Profit Box Plot

plt.figure(figsize=(10, 6))

sns.boxplot(
    y=df["Profit"],
    color="seagreen"
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--",
    label="Zero Profit"
)

plt.title("Superstore Profit Box Plot", fontsize=16)
plt.ylabel("Profit ($)")
plt.legend()

plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/profit_boxplot.png",
    dpi=300
)

plt.close()

print("Profit Box Plot Saved Successfully!")




# Step 48: Correlation Heatmap

# Select numerical columns
numeric_data = df[
    ["Sales", "Profit", "Quantity", "Discount"]
]

# Calculate correlation
correlation_matrix = numeric_data.corr()

print("\n===== CORRELATION MATRIX =====")
print(correlation_matrix.round(2))

# Create heatmap
plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title("Superstore Correlation Heatmap", fontsize=16)

plt.tight_layout()

# Save chart
plt.savefig(
    "visualizations/correlation_heatmap.png",
    dpi=300
)

plt.close()

print("Correlation Heatmap Saved Successfully!")










# Step 49: Pair Plot

# Select numerical columns
pair_data = df[
    ["Sales", "Profit", "Quantity", "Discount"]
]

# Take a sample for faster plotting
pair_sample = pair_data.sample(
    n=min(1000, len(pair_data)),
    random_state=42
)

# Create pair plot
pair_plot = sns.pairplot(
    pair_sample,
    diag_kind="hist",
    plot_kws={
        "alpha": 0.5,
        "s": 15,
        "color": "steelblue"
    }
)

pair_plot.fig.suptitle(
    "Superstore Numerical Features Pair Plot",
    fontsize=16,
    y=1.02
)

# Save chart
pair_plot.savefig(
    "visualizations/pair_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(pair_plot.fig)

print("Pair Plot Saved Successfully!")
print("ALL 10 VISUALIZATIONS COMPLETED!")