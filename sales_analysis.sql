show databases;
create database ecommerce_analytics;
use ecommerce_analytics;

CREATE TABLE IF NOT EXISTS ecommerce_sales (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(30),
    Description VARCHAR(255),
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID INT NULL,
    Country VARCHAR(100),
    SalesAmount DECIMAL(12,2)
);
DESCRIBE ecommerce_sales;


SELECT COUNT(*) AS total_records
FROM ecommerce_sales;

SELECT *
FROM ecommerce_sales
LIMIT 10;


SELECT COUNT(*) AS total_records
FROM ecommerce_sales;
SELECT
    ROUND(SUM(SalesAmount), 2) AS total_revenue
FROM ecommerce_sales;


SELECT
    StockCode,
    Description,
    SUM(Quantity) AS total_quantity_sold,
    ROUND(SUM(SalesAmount), 2) AS total_revenue
FROM ecommerce_sales
WHERE Quantity > 0
  AND InvoiceNo NOT LIKE 'C%'
GROUP BY StockCode, Description
ORDER BY total_revenue DESC
LIMIT 10;


-- 2. Monthly Sales Analysis

SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
    ROUND(SUM(SalesAmount), 2) AS monthly_revenue,
    COUNT(DISTINCT InvoiceNo) AS total_orders
FROM ecommerce_sales
WHERE InvoiceNo NOT LIKE 'C%'
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY sales_month;


-- 3. Country-wise Sales Analysis

SELECT
    Country,
    ROUND(SUM(SalesAmount), 2) AS total_revenue,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    COUNT(DISTINCT CustomerID) AS total_customers
FROM ecommerce_sales
WHERE InvoiceNo NOT LIKE 'C%'
GROUP BY Country
ORDER BY total_revenue DESC;


-- 4. Top 10 Customers by Revenue

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    ROUND(SUM(SalesAmount), 2) AS total_revenue
FROM ecommerce_sales
WHERE CustomerID IS NOT NULL
  AND InvoiceNo NOT LIKE 'C%'
GROUP BY CustomerID
ORDER BY total_revenue DESC
LIMIT 10;