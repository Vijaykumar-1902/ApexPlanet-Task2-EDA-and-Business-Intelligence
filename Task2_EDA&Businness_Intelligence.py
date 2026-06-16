import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(
    r"C:\Users\malla\Desktop\ApexPlanet\Task1\cleaned_customer_dataset.csv"
)

print("="*50)
print("TASK 2 - EDA & BUSINESS INTELLIGENCE")
print("="*50)

# Dataset Overview
print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
df.info()

print("\nDESCRIPTIVE STATISTICS")
print(df.describe())

# Business Questions

print("\nTOP 10 CUSTOMERS BY PURCHASES")
top_customers = df.nlargest(10, 'purchases')
print(top_customers[['cust_id', 'purchases']])

print("\nAVERAGE CREDIT LIMIT")
print(df['credit_limit'].mean())

print("\nAVERAGE BALANCE")
print(df['balance'].mean())

print("\nTOTAL PURCHASES")
print(df['purchases'].sum())

print("\nAVERAGE PAYMENTS")
print(df['payments'].mean())

print("\nTOP 10 CUSTOMERS BY BALANCE")
print(df.nlargest(10, 'balance')[['cust_id', 'balance']])

# Histograms
plt.figure(figsize=(8,5))
plt.hist(df['balance'], bins=30)
plt.title("Balance Distribution")
plt.xlabel("Balance")
plt.ylabel("Frequency")
plt.savefig("balance_distribution.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df['purchases'], bins=30)
plt.title("Purchases Distribution")
plt.xlabel("Purchases")
plt.ylabel("Frequency")
plt.savefig("purchases_distribution.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df['credit_limit'], bins=30)
plt.title("Credit Limit Distribution")
plt.xlabel("Credit Limit")
plt.ylabel("Frequency")
plt.savefig("credit_limit_distribution.png")
plt.show()

# Scatter Plot

plt.figure(figsize=(8,5))
plt.scatter(df['balance'], df['credit_limit'])
plt.title("Balance vs Credit Limit")
plt.xlabel("Balance")
plt.ylabel("Credit Limit")
plt.savefig("balance_vs_credit_limit.png")
plt.show()

# Correlation Analysis
corr = df.corr(numeric_only=True)

print("\nCORRELATION MATRIX")
print(corr)

plt.figure(figsize=(12,8))
plt.imshow(corr, aspect='auto')
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# High Credit Utilization

if 'credit_utilization' in df.columns:
    high_util = df[df['credit_utilization'] > 0.8]

    print("\nCUSTOMERS WITH CREDIT UTILIZATION > 80%")
    print(len(high_util))

# Payment Ratio Analysis

if 'payment_ratio' in df.columns:
    print("\nAVERAGE PAYMENT RATIO")
    print(df['payment_ratio'].mean())

# Save EDA Summary

with open("EDA_Report.txt", "w") as f:
    f.write("TASK 2 - EDA & BUSINESS INTELLIGENCE\n")
    f.write("="*50 + "\n\n")
    f.write(f"Total Customers: {len(df)}\n")
    f.write(f"Average Balance: {df['balance'].mean()}\n")
    f.write(f"Average Credit Limit: {df['credit_limit'].mean()}\n")
    f.write(f"Total Purchases: {df['purchases'].sum()}\n")
    f.write(f"Average Payments: {df['payments'].mean()}\n")

print("\nEDA REPORT GENERATED SUCCESSFULLY")
print("Charts Saved:")
print("- balance_distribution.png")
print("- purchases_distribution.png")
print("- credit_limit_distribution.png")
print("- balance_vs_credit_limit.png")
print("- correlation_heatmap.png")
print("- EDA_Report.txt")