# Sample Superstore - Data Cleaning and Preprocessing

## Project Overview

This project focuses on cleaning and preprocessing the Sample Superstore dataset to make it ready for reliable data analysis.

## Objective

The main objective is to identify common data quality issues and prepare a clean dataset for further analysis.

## Tools Used

- Python
- Pandas
- VS Code

## Dataset

The dataset contains 9,994 records and 21 columns related to orders, customers, products, sales, discounts and profit.

## Data Quality Checks

The following checks were performed:

- Missing value check
- Duplicate row check
- Data type validation
- Date format validation
- Text formatting and whitespace cleaning

## Cleaning Performed

### Date Columns
`Order Date` and `Ship Date` were converted into proper datetime format.

### Text Columns
Leading and trailing whitespace was removed from relevant text columns.

### Missing Values
No missing values were found, so no imputation or deletion was required.

### Duplicate Records
No duplicate rows were found.

## Output

The cleaned dataset is available at:

`data/cleaned_superstore.csv`

## Project Structure

```text
Sample-Superstore-Data-Cleaning/
│
├── data/
│   ├── Sample - Superstore.csv
│   └── cleaned_superstore.csv
│
├── data_cleaning.py
├── CHANGELOG.md
└── README.md