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

## Phase 4 — GitHub Actions / CI-CD (Aug 29, 2026)

**Goal:** Learn GitHub Actions — automatically checking that my code still works every time I push.

### What I learned
- **GitHub Actions** = an automated "robot inspector" that runs checks on your code every time you push or open a PR — no manual work needed
- Workflow files live in a specific folder: `.github/workflows/`
- Workflows are written in **YAML** — a simple `key: value` format that uses indentation (not brackets/commas) to show structure
- A workflow file needs:
  - `name:` — label for the workflow
  - `on:` — the trigger (what event starts it, e.g. `push` or `pull_request` to `main`)
  - `jobs:` — one or more tasks to run
  - `runs-on:` — a fresh, temporary virtual machine GitHub spins up just for this job
  - `steps:` — the actual sequence of actions (checkout code, set up Python, install dependencies, run checks)
- Built my first real workflow: **notebook-check.yml**
  - Triggers on every push/PR to `main`
  - Checks out the repo, sets up Python 3.13, installs `requirements.txt`, then runs `notebooks/02_cleaning_eda.ipynb` end-to-end using `nbconvert`
  - If any cell in the notebook errors out, the whole check fails — this is CI (Continuous Integration) doing its job
- Pushed straight to `main` this time (not every change needs a branch/PR — fine for small, safe, solo changes)
- **First run succeeded on the first try** ✅ — all steps passed in 42 seconds
- Got a **deprecation warning** (Node.js 20 → 24) — learned to read warnings even when the run passes; not urgent, just a note for later (bump action versions: `checkout@v5`, `setup-python@v6` when available)

### New terms
| Term | Meaning |
|---|---|
| GitHub Actions | Automated workflows that run on events like push/PR |
| Workflow | A YAML file defining what to automatically check/run |
| YAML | Simple `key: value` config format using indentation |
| CI (Continuous Integration) | Automatically testing code every time it changes, to catch breakage early |
| Job / Step | A job is a task; steps are the ordered actions inside it |
| Runner | The temporary virtual machine GitHub uses to execute a job |

### Certification relevance
GitHub Actions is its own certification track. Workflow syntax, triggers, jobs/steps, and runners are core exam topics — today was hands-on, not just theory.

### Next up: Phase 5
Options to consider: README/documentation polish, fixing the notebook reproducibility bug (random seed), or expanding CI (e.g. adding a linter, or running checks on every PR before merge is even allowed).