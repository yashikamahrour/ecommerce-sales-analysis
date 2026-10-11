
import pandas as pd
import os

# Get project folder
folder = os.path.dirname(os.path.abspath(__file__))

# Load original dataset
file_path = os.path.join(folder, "ecommerce.csv")
df = pd.read_csv(file_path, encoding="latin1")

print("Original dataset shape:", df.shape)

# 1. Remove exact duplicate rows
df = df.drop_duplicates().copy()
print("After removing duplicates:", df.shape)

# 2. Clean product descriptions
df["Description"] = (
    df["Description"].fillna("Unknown Product").astype(str).str.strip()
)

# 3. Clean customer IDs without deleting unknown customers
df["CustomerID"] = pd.to_numeric(
    df["CustomerID"], errors="coerce"
).astype("Int64")

# 4. Parse dates using the dataset's day-month-year format
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    format="mixed",
    errors="coerce"
)

invalid_dates = df["InvoiceDate"].isna().sum()
print("Invalid dates:", invalid_dates)

# 5. Remove only rows with invalid dates
df = df.dropna(subset=["InvoiceDate"]).copy()

# 6. Remove non-positive prices
invalid_prices = (df["UnitPrice"] <= 0).sum()
df = df[df["UnitPrice"] > 0].copy()
print("Rows removed for non-positive prices:", invalid_prices)

# 7. Keep negative quantities because they may represent returns
print("Negative quantity rows retained:", (df["Quantity"] < 0).sum())

# 8. Calculate sales amount
df["SalesAmount"] = df["Quantity"] * df["UnitPrice"]

# 9. Save as a NEW file to preserve the old cleaned dataset
output_folder = os.path.join(folder, "output")
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(
    output_folder, "cleaned_ecommerce_v2.csv"
)
df.to_csv(output_path, index=False)

# 10. Display results
print("\n--- CLEANING RESULTS ---")
print("Final dataset shape:", df.shape)
print("Missing values:")
print(df.isnull().sum())
print("\nNew cleaned dataset saved at:")
print(output_path)