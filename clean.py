import pandas as pd

# Read Excel file
file = "sales_data.xlsx"

# Load Excel data
df = pd.read_excel(file)

# Display first rows
print("Original Data:")
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing City values
df["City"] = df["City"].fillna("Unknown")

# Fill missing Quantity values
df["Quantity"] = df["Quantity"].fillna(1)

# Fill missing PaymentMethod values
df["PaymentMethod"] = df["PaymentMethod"].fillna("Unknown")

# Standardize text formatting
df["Customer"] = df["Customer"].str.title()
df["City"] = df["City"].str.title()
df["Product"] = df["Product"].str.title()

# Create TotalSales column
df["TotalSales"] = df["Quantity"] * df["Price"]

# Save cleaned output
output = "Cleaned_Output.xlsx"
df.to_excel(output, index=False)

print("Data cleaning completed successfully!")
print("Cleaned file saved as:", output)