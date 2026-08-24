    # Learning Notes

## Phase 1: Project Setup & Synthetic Data Generation

**Date completed:** August 2026

### GitHub concepts learned
- Repository creation
- Commits (via browser and terminal)
- README / Markdown formatting
- Cloning a repository to a local machine
- The add → commit → push workflow
- Reading Git status indicators (e.g. `main*` = uncommitted changes)

### What was built
- Initial repository setup for Bharani's Retail & Co. (fictional company)
- `generate_data.py`: a Python script that generates a synthetic inventory
  dataset (50 fictional products across 5 categories, with pricing, stock,
  and sales figures)
- `inventory_data.csv`: the generated dataset, used as the foundation for
  upcoming analysis and AI-generated insights

### Next up (Phase 2)
Clean and analyze `inventory_data.csv` using Python — identify low-stock
items, best/worst sellers, and cost/price patterns.

## Phase 2: Data Cleaning & Exploratory Analysis (Python)

- Set up a Python virtual environment (`venv`) to isolate this project's
  packages from the rest of the system.
- Installed pandas, numpy, matplotlib, seaborn, jupyter — saved exact
  versions to `requirements.txt` for reproducibility.
- Built `notebooks/02_cleaning_eda.ipynb`:
  - Loaded `inventory_data.csv` (50 products, 8 columns) with pandas.
  - Verified data quality: 0 missing values, 0 duplicate rows, correct
    data types across all columns (confirmed with `df.info()`).
  - Ran summary statistics (`df.describe()`) on cost, price, stock, and
    sales columns.
  - Calculated `turnover_rate` (units sold vs. current stock) to identify
    fast- and slow-moving products.
  - Caught and documented a data-interpretation issue: very low
    `stock_quantity` on some rows inflates turnover_rate artificially
    (e.g. Running Shoes at stock=1 showed a 184.0 ratio) — noted as a
    caveat rather than silently excluded.
  - Saved the validated dataset to `data/processed/inventory_clean.csv`,
    keeping the raw file untouched.

### Next up (Phase 3)
Visualize the cleaned data — stock-by-category, cost distribution,
turnover comparisons — building toward the same insights as the Excel
dashboard, now reproducible in Python.