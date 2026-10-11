
import os
import pandas as pd
import mysql.connector
from getpass import getpass

folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    folder, "output", "cleaned_ecommerce_v2.csv"
)

password = getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="ecommerce_analytics"
)

cursor = connection.cursor()

# The destination table must already exist and be empty.
cursor.execute("SELECT COUNT(*) FROM ecommerce_sales_v2")
existing_rows = cursor.fetchone()[0]

if existing_rows != 0:
    raise RuntimeError(
        f"Destination table is not empty: {existing_rows} rows."
    )

insert_sql = """
INSERT INTO ecommerce_sales_v2
(InvoiceNo, StockCode, Description, Quantity, InvoiceDate,
 UnitPrice, CustomerID, Country, SalesAmount)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

total_imported = 0

try:
    for chunk in pd.read_csv(
        csv_path,
        encoding="utf-8",
        chunksize=5000,
        dtype={"CustomerID": "Int64"},
        parse_dates=["InvoiceDate"]
    ):
        chunk = chunk.astype(object).where(
            pd.notna(chunk), None
        )

        rows = []
        for row in chunk.itertuples(index=False, name=None):
            rows.append(tuple(
                value.to_pydatetime()
                if isinstance(value, pd.Timestamp)
                else value
                for value in row
            ))

        cursor.executemany(insert_sql, rows)
        connection.commit()

        total_imported += len(rows)
        print(f"Imported {total_imported} rows...")

    print("\nImport finished.")

except Exception:
    connection.rollback()
    raise

finally:
    cursor.close()
    connection.close()

print("Total rows processed:", total_imported)
