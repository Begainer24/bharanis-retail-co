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

## Phase 3 — Branching & Pull Requests (Aug 25, 2026)

**Goal:** Learn the core Git/GitHub collaboration workflow — branching and pull requests.

### What I learned
- A **branch** is just a movable pointer to a commit, not a copy of files — cheap and instant to create
- Created a feature branch: `feature/add-turnover-summary`
- Added a new turnover rate calculation to the cleaning/EDA notebook:
  - `turnover_rate = units_sold_last_month / stock_quantity`
  - Grouped by category to compare turnover across product categories
- Learned to read `git diff` output before committing, to tell real changes from noise (e.g. Jupyter notebook execution counts/outputs changing just from re-running cells)
- Staged and committed with a clear message: `git add` → `git commit -m "..."`
- Pushed the new branch to GitHub: `git push -u origin <branch>`
- Opened my first **Pull Request** — wrote a title and description explaining what changed and why
- Reviewed the PR diff on GitHub before merging
- **Merged** the PR into `main`, then deleted the branch (both on GitHub and locally)
- Synced local `main` with `git pull` after the merge

### Commands used
```bash
git branch feature/add-turnover-summary
git checkout feature/add-turnover-summary
git diff <file>
git restore <file>
git add <file>
git commit -m "message"
git push -u origin <branch>
git checkout main
git pull origin main
git branch -d <branch>
```

### Side quests / troubleshooting
- Fixed a broken Jupyter kernel connection — VS Code wasn't detecting the project's `venv`; registered it manually as a Jupyter kernel using `ipykernel install`
- Noticed the processed CSV changes slightly every time the notebook re-runs — likely unseeded randomness somewhere in the cleaning step. **Flagged for a future phase**, not fixed yet.

### Certification relevance
Branching, PRs, and merging are core **GitHub Foundations** exam topics. Today was hands-on practice of the full lifecycle, not just theory.

### Next up: Phase 4
Options considered: README/documentation polish, GitHub Actions (CI/CD), or fixing the reproducibility bug.