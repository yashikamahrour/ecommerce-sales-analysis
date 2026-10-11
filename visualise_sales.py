
import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from getpass import getpass

# Project folders
folder = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(folder, "output")
os.makedirs(output_folder, exist_ok=True)

# MySQL connection
username = "root"
password = quote_plus(getpass("Enter your MySQL password: "))
database = "ecommerce_analytics"

connection_string = (
    f"mysql+mysqlconnector://{username}:{password}"
    f"@localhost:3306/{database}"
)

engine = create_engine(connection_string)

try:
    # 1. Monthly sales analysis
    monthly_query = """
        SELECT
            DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
            ROUND(SUM(SalesAmount), 2) AS sales_amount,
            COUNT(DISTINCT InvoiceNo) AS total_orders
        FROM ecommerce_sales_v2
        WHERE InvoiceNo NOT LIKE 'C%'
          AND Quantity > 0
        GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
        ORDER BY sales_month;
    """

    monthly_df = pd.read_sql(monthly_query, engine)

    print("\nMONTHLY SALES")
    print(monthly_df.to_string(index=False))

    plt.figure(figsize=(12, 6))
    plt.plot(
        monthly_df["sales_month"],
        monthly_df["sales_amount"],
        marker="o"
    )
    plt.title("Monthly E-commerce Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    monthly_path = os.path.join(
        output_folder, "monthly_revenue.png"
    )
    plt.savefig(monthly_path, dpi=300)
    plt.close()
    print("\nChart saved:", monthly_path)

    # 2. Top 10 countries by sales amount
    country_query = """
        SELECT
            Country,
            ROUND(SUM(SalesAmount), 2) AS sales_amount
        FROM ecommerce_sales_v2
        WHERE InvoiceNo NOT LIKE 'C%'
          AND Quantity > 0
        GROUP BY Country
        ORDER BY sales_amount DESC
        LIMIT 10;
    """

    country_df = pd.read_sql(country_query, engine)

    print("\nTOP 10 COUNTRIES BY SALES")
    print(country_df.to_string(index=False))

    plt.figure(figsize=(12, 6))
    plt.bar(
        country_df["Country"],
        country_df["sales_amount"]
    )
    plt.title("Top 10 Countries by E-commerce Sales")
    plt.xlabel("Country")
    plt.ylabel("Sales Amount")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    country_path = os.path.join(
        output_folder, "top_countries_revenue.png"
    )
    plt.savefig(country_path, dpi=300)
    plt.close()
    print("Chart saved:", country_path)

finally:
    engine.dispose()

print("\nBoth charts have been generated successfully!")
