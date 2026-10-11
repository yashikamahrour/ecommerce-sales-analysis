
import pandas as pd

df = pd.read_csv("ecommerce.csv", encoding="latin1")

print("Original rows:", len(df))

# Remove exact duplicate rows
df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df))

# Parse dates correctly
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce",
    format="mixed"
)

print("Invalid dates:", df["InvoiceDate"].isna().sum())

# Check the filters separately
valid_dates = df["InvoiceDate"].notna()
valid_prices = df["UnitPrice"] > 0
valid_quantities = df["Quantity"] != 0

print("Rows with valid dates:", valid_dates.sum())
print("Rows with positive prices:", valid_prices.sum())
print("Rows with non-zero quantities:", valid_quantities.sum())

clean_mask = valid_dates & valid_prices & valid_quantities

print("Rows remaining after all filters:", clean_mask.sum())
print("Rows removed by all filters:", (~clean_mask).sum())

print("\nRows removed by each individual condition:")
print("Invalid dates:", (~valid_dates).sum())
print("Non-positive prices:", (~valid_prices).sum())
print("Zero quantities:", (df["Quantity"] == 0).sum())