# Import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path
file_path = "./data/customer_shoping_data.csv"

# Load dataset
df = pd.read_csv(file_path)

# Preview dataset
print("Dataset Preview:")
print(df.head())

# Convert 'invoice_date' to datetime
df['invoice_date'] = pd.to_datetime(df['invoice_date'], format='%d/%m/%Y')

# Add a new column for total sales (quantity * price)
df['total_sales'] = df['quantity'] * df['price']

# Clean Data
print("\nChecking for missing values:")
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Analyze: Top-Selling Categories
top_categories = df.groupby("category")['quantity'].sum().sort_values(ascending=False)
print("\nTop-Selling Categories:")
print(top_categories)

# Analyze: Monthly Sales Trend
df['month'] = df['invoice_date'].dt.month
monthly_sales = df.groupby("month")['total_sales'].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

# Analyze: Total Revenue by Shopping Mall
mall_revenue = df.groupby("shopping_mall")['total_sales'].sum().sort_values(ascending=False)
print("\nRevenue by Shopping Mall:")
print(mall_revenue)

# Visualization: Top-Selling Categories
plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.index, y=top_categories.values, palette="Blues_d")
plt.title("Top-Selling Categories")
plt.xlabel("Category")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization: Monthly Sales Trend
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.grid()
plt.tight_layout()
plt.show()

# Visualization: Revenue by Shopping Mall
plt.figure(figsize=(10, 6))
sns.barplot(x=mall_revenue.index, y=mall_revenue.values, palette="Greens_d")
plt.title("Revenue by Shopping Mall")
plt.xlabel("Shopping Mall")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
