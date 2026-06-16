import pandas as pd
import matplotlib.pyplot as plt
# LOAD CLEANED DATASET
df = pd.read_csv(
    r"C:\Users\malla\Desktop\ApexPlanet\Task1\cleaned_dataset.csv"
)

print("="*60)
print("TASK 2: EXPLORATORY DATA ANALYSIS & BUSINESS INTELLIGENCE")
print("="*60)

# DESCRIPTIVE STATISTICS
print("\nDESCRIPTIVE STATISTICS")
print(df.describe(include='all'))

# BUSINESS INSIGHTS
total_revenue = df['Total_Sales'].sum()
avg_sales = df['Total_Sales'].mean()
total_orders = len(df)

print("\nTOTAL REVENUE :", round(total_revenue, 2))
print("AVERAGE SALES :", round(avg_sales, 2))
print("TOTAL ORDERS :", total_orders)

# TOP 5 CUSTOMERS
top_customers = (
    df.groupby('Customer_Name')['Total_Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTOP 5 CUSTOMERS")
print(top_customers)

# SALES BY CATEGORY
sales_category = (
    df.groupby('Category')['Total_Sales']
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY CATEGORY")
print(sales_category)

# SALES BY CITY
sales_city = (
    df.groupby('City')['Total_Sales']
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY CITY")
print(sales_city)

# MOST SOLD PRODUCTS
most_sold = (
    df.groupby('Product')['Quantity']
    .sum()
    .sort_values(ascending=False)
)

print("\nMOST SOLD PRODUCTS")
print(most_sold)

# GENDER DISTRIBUTION
print("\nGENDER DISTRIBUTION")
print(df['Gender'].value_counts())

# VISUALIZATION 1
# SALES BY CATEGORY

plt.figure(figsize=(8,6))
sales_category.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# VISUALIZATION 2
# TOP CUSTOMERS
plt.figure(figsize=(8,5))
top_customers.plot(kind='bar')
plt.title("Top 5 Customers")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_customers.png")
plt.show()

# VISUALIZATION 3
# SALES DISTRIBUTION

plt.figure(figsize=(8,5))
plt.hist(df['Total_Sales'], bins=20)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

# VISUALIZATION 4
# QUANTITY VS SALES

plt.figure(figsize=(8,5))
plt.scatter(df['Quantity'], df['Total_Sales'])
plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("quantity_vs_sales.png")
plt.show()

# VISUALIZATION 5
# AGE VS SALES

plt.figure(figsize=(8,5))
plt.scatter(df['Age'], df['Total_Sales'])
plt.title("Age vs Sales")
plt.xlabel("Age")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("age_vs_sales.png")
plt.show()

# CORRELATION ANALYSIS

print("\nCORRELATION MATRIX")

corr = df[['Age','Quantity','Unit_Price','Total_Sales']].corr()

print(corr)

plt.figure(figsize=(10,8))
plt.imshow(corr)
plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=90
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.show()

# EDA REPORT

with open("EDA_Report.txt", "w") as report:

    report.write("TASK 2 - EDA & BUSINESS INTELLIGENCE\n")
    report.write("="*50 + "\n\n")

    report.write(f"Total Orders : {total_orders}\n")
    report.write(f"Total Revenue : {total_revenue:.2f}\n")
    report.write(f"Average Sales : {avg_sales:.2f}\n\n")

    report.write("Top 5 Customers:\n")
    report.write(str(top_customers))
    report.write("\n\n")

    report.write("Sales by Category:\n")
    report.write(str(sales_category))
    report.write("\n\n")

    report.write("Sales by City:\n")
    report.write(str(sales_city))
    report.write("\n\n")

print("\nEDA COMPLETED SUCCESSFULLY")

print("\nFILES GENERATED")
print("1. sales_by_category.png")
print("2. top_customers.png")
print("3. sales_distribution.png")
print("4. quantity_vs_sales.png")
print("5. age_vs_sales.png")
print("6. correlation_matrix.png")
print("7. EDA_Report.txt")