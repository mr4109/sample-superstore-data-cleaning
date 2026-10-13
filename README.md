# Day 13 – Duplicate Record Check

## Results
- Original data rows: 9994
- Exact full-row duplicate occurrences removed: 0
- Cleaned rows: 9994
- Rows flagged for repeated Order ID + Product ID combinations: 16

## Files
- `duplicate_check_summary.csv`: counts and results.
- `full_row_duplicate_records.csv`: rows from exact duplicate groups.
- `order_product_key_duplicate_records.csv`: repeated key combinations for review.
- `cleaned_superstore_deduplicated.csv`: copy with exact full-row duplicates removed.
- `AUDIT_NOTE.md`: audit note.

## Method
The original source file is preserved. Only exact full-row duplicates are removed from the cleaned copy. Repeated Order ID + Product ID combinations are reported separately and not automatically deleted because they may require business-context review.
