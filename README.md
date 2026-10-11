# E-commerce Sales Analytics

## Project Overview
This project analyzes e-commerce transaction data using Python, MySQL, and data visualization. The goal is to explore sales trends over time and identify the countries contributing the highest sales amounts.

## Objectives
- Clean and prepare raw transaction data.
- Import the cleaned dataset into MySQL.
- Analyze monthly sales performance using SQL.
- Identify the top 10 countries by sales amount.
- Visualize key findings using Python and Matplotlib.
- Validate sales totals for consistency.

## Tools and Technologies
- **Python** — data cleaning, importing, and analysis
- **Pandas** — data manipulation and preprocessing
- **MySQL** — data storage and SQL analysis
- **MySQL Workbench** — database management and query execution
- **Matplotlib** — data visualization

## Dataset
The original dataset contains 541,909 transaction rows and 8 columns.

After removing duplicate records and rows with non-positive unit prices, the analysis dataset contains 534,129 rows and 9 columns.

The prepared dataset includes transaction details such as invoice number, product code, product description, quantity, invoice date, unit price, customer ID, country, and sales amount.

**Note:** Customer IDs may be missing for some transactions. These records are retained because they can still contribute to sales analysis.

## Data Cleaning
The preprocessing workflow includes:
- Removing duplicate records.
- Handling missing product descriptions.
- Preserving missing customer IDs as null values.
- Converting invoice dates into datetime format.
- Removing rows with non-positive unit prices.
- Retaining negative-quantity transactions in the cleaned dataset for transparency.
- Calculating `SalesAmount` as `Quantity × UnitPrice`.

## SQL Analysis
SQL queries were used to:
- Calculate total sales amounts.
- Analyze monthly sales and order counts.
- Rank countries by sales amount.
- Examine negative quantities and cancellation invoices.
- Validate that country-level sales totals reconcile with the overall total.

For the main sales charts, the analysis excludes cancellation invoices and includes only transactions with positive quantities.

## Key Findings
- The analyzed dataset contains **534,129 rows**.
- Sales across all countries total **10,642,110.80** in the dataset's currency units.
- **November 2011** has the highest monthly sales amount in the analyzed period, at **1,503,866.78**.
- The **United Kingdom** has the highest country-level sales amount, at **9,001,744.09**.
- Country-level totals reconcile with the overall sales total.

*These figures represent sales amounts, not profit. The currency symbol has not been specified in this report.*

## Visualizations
The project generates two charts:

1. `output/monthly_revenue.png` — monthly sales trends.
2. `output/top_countries_revenue.png` — top 10 countries by sales amount.

## Project Structure
```text
Ecommerce_Sales_Analytics/
├── ecommerce.csv
├── clean_data.py
├── prepare_import.py
├── import_to_mysql.py
├── audit_cleaning.py
├── sales_analysis.sql
├── visualise_sales.py
└── output/
    ├── cleaned_ecommerce_v2.csv
    ├── cleaned_ecommerce_import.csv
    ├── monthly_revenue.png
    └── top_countries_revenue.png
```

## How to Run
1. Install the required Python packages:
   ```bash
   python -m pip install pandas matplotlib sqlalchemy mysql-connector-python
   ```
2. Configure your local MySQL connection.
3. Run the data-cleaning script:
   ```bash
   python clean_data.py
   ```
4. Prepare the import-ready CSV:
   ```bash
   python prepare_import.py
   ```
5. Import the prepared dataset into MySQL:
   ```bash
   python import_to_mysql.py
   ```
6. Run the visualization script:
   ```bash
   python visualise_sales.py
   ```

Ensure the MySQL database and `ecommerce_sales_v2` table exist before running the visualization script. Review the scripts for any local configuration requirements before executing them.

## Skills Demonstrated
- Data cleaning and preprocessing
- SQL aggregation, filtering, and grouping
- Sales trend analysis
- Data validation and reconciliation
- Python–MySQL connectivity
- Data visualization
- Project documentation

## Future Improvements
- Build an interactive Power BI dashboard.
- Add product-level and customer-level analysis.
- Investigate missing customer information.
- Add automated data-quality checks.
- Improve the handling and reporting of returns and cancellations.