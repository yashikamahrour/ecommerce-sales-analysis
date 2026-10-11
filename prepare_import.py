
import pandas as pd
import os

folder = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(
    folder, "output", "cleaned_ecommerce_v2.csv"
)

output_path = os.path.join(
    folder, "output", "cleaned_ecommerce_import.csv"
)

df = pd.read_csv(input_path)

# Replace missing CustomerID values with an empty field
df["CustomerID"] = df["CustomerID"].astype("Int64").astype("string")
df["CustomerID"] = df["CustomerID"].fillna("")

df.to_csv(output_path, index=False)

print("Import-ready CSV created.")
print("Rows:", len(df))
print("File:", output_path)
print("Missing CustomerIDs:", df["CustomerID"].eq("").sum())
