# Data Cleaning Change Log

## Dataset
Sample Superstore Dataset

## Data Quality Checks

| Issue Checked | Result | Action |
|---|---:|---|
| Missing Values | 0 | No missing values found |
| Duplicate Rows | 0 | No duplicate rows found |
| Date Format | Inconsistent datatype | Converted Order Date and Ship Date to datetime |
| Text Formatting | Extra whitespace possible | Removed leading/trailing whitespace |
| Data Types | Required validation | Checked and standardized relevant columns |

## Cleaning Actions

### 1. Date Conversion
- Converted `Order Date` into datetime format.
- Converted `Ship Date` into datetime format.
- Used `errors="coerce"` to safely handle invalid dates.

### 2. Text Cleaning
- Removed leading and trailing whitespace from text columns.
- Cleaned columns such as Category, Sub-Category, Product Name, City, State and Region.

### 3. Missing Values
- No missing values were found in the dataset.
- Therefore, no imputation or deletion was required.

### 4. Duplicate Records
- No duplicate rows were found.
- Therefore, no duplicate records were removed.

## Output

The cleaned dataset was saved as:

`data/cleaned_superstore.csv`