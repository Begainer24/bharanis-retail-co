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

## Phase 5 — Merge Conflicts (Aug 29, 2026)

**Goal:** Deliberately create and resolve a merge conflict — the #1 real-world Git headache, and a core certification topic.

### What I learned
- A **merge conflict** happens when two branches change the *same line* of the *same file* differently since they diverged — Git can't auto-decide, so it stops and asks
- Created it on purpose:
  - Branch `conflict-demo-a`: edited the README's Status line one way, committed
  - Switched to `main`: edited the *same line* a different way, committed
  - Ran `git merge conflict-demo-a` → conflict triggered
- Learned to read Git's conflict markers inside the file:
```
  <<<<<<< HEAD (Current Change)
  version from the branch I'm currently on
  =======
  version coming in from the other branch
  >>>>>>> conflict-demo-a (Incoming Change)
```
- Resolved it manually — wrote a new combined line, deleted all the conflict markers
- `git add <file>` during a conflict has a second meaning: it tells Git "I've resolved this, this is final" (not just "stage for commit")
- Ran `git commit` (no `-m`) to finish the merge — this opens a pre-filled commit message in **Vim**, a terminal text editor
- Learned to survive Vim: press `Esc`, type `:wq`, press `Enter` to save and quit (or `:q!` to quit without saving)
- This created a **merge commit** — unlike normal commits (one parent), a merge commit has **two parents**, since it stitches two diverged histories back together
- Cleaned up: deleted the now-merged branch locally, pushed the resolved `main` to GitHub

### New terms
| Term | Meaning |
|---|---|
| Merge conflict | Same line changed differently on two branches — Git needs a human decision |
| Conflict markers | `<<<<<<<`, `=======`, `>>>>>>>` — show both competing versions inline |
| Merge commit | A commit with two parents, created when reconciling diverged branches |
| Vim | Terminal-based text editor Git opens for commit messages when no `-m` is given |

### Certification relevance
Merge conflicts are one of the most commonly tested GitHub Foundations topics — and the hardest to understand without actually living through one. Today was hands-on, safe practice in a throwaway branch.

### Still to cover for GitHub Foundations
- GitHub Issues (task/bug tracking)
- README / Markdown formatting basics
- `.gitignore` — what it's for and why

### Addendum — GitHub Issues (closing out Foundations prep)

**What I learned**
- **Issues** = a task/bug tracker built into GitHub, using the same Markdown as READMEs
- Filed a real bug as Issue #2: the notebook reproducibility problem flagged back in Phase 3
- Wrote it in standard bug-report format: description, Steps to reproduce, Expected behavior, Fix idea
- Fixed the actual bug: added `np.random.seed(42)` right after imports in the notebook
- **Verified the fix with `md5`** — ran the notebook twice, compared file hashes, got an identical match both times, proving the output is now reproducible
- Created a branch `fix/notebook-random-seed`, committed with a special phrase in the message:
```
  Fix notebook reproducibility with fixed random seed

  Closes #2
```
- Learned that `Closes #2` / `Fixes #2` / `Resolves #2` in a commit or PR description is a **magic keyword** GitHub watches for — merging it into the default branch **automatically closes that Issue**
- Opened and merged the PR — confirmed Issue #2 closed automatically, no manual clicking needed

**Real-world troubleshooting**
- Got stuck in a `dquote>` terminal prompt from an unclosed multi-line string — learned to recover with a closing `"` or `Ctrl+C`, and to prefer `-m "..." -m "..."` (multiple `-m` flags) over multi-line strings typed directly into the terminal

**New terms**
| Term | Meaning |
|---|---|
| Issue | A tracked task/bug/request, using Markdown, discussable and closeable |
| Closing keyword | `Closes #N` / `Fixes #N` / `Resolves #N` in a commit/PR — auto-closes that Issue on merge |
| `md5` | Command that fingerprints a file's exact content — identical hashes mean identical content |

### GitHub Foundations prep — status: core topics covered
- [x] Repositories, commits, push/pull
- [x] Branching
- [x] Pull Requests & merging
- [x] Merge conflicts
- [x] GitHub Actions (CI)
- [x] Markdown & .gitignore
- [x] Issues (with auto-close via commit keywords)