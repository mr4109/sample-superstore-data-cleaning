import pandas as pd

# Load the dataset

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")
# Show basic information
print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")
print(df.head())



print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)


# Convert date columns to proper datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

print("\nDate Columns After Cleaning:")
print(df[["Order Date", "Ship Date"]].dtypes)

# Clean text columns
text_columns = [
    "Ship Mode",
    "Segment",
    "Country",
    "City",
    "State",
    "Region",
    "Category",
    "Sub-Category",
    "Product Name"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

print("\nText columns cleaned successfully.")


# Final validation
print("\nFinal Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_csv("data/cleaned_superstore.csv", index=False)

print("\nCleaned dataset saved successfully!")