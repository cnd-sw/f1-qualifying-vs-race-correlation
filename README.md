# Qualifying vs Race Correlation Model

## Overview
This project analyzes how closely **Formula 1 qualifying positions** correlate with **final race results** over multiple seasons using public data from the **Ergast API**.  
It measures the **Spearman correlation** between qualifying ranks and race finishing positions for each Grand Prix, revealing which circuits and seasons reward raw pace versus strategic execution.

---

## How It Works

### 1. Data Retrieval
The script connects to the public **Ergast Developer API**, which provides structured Formula 1 data in JSON format.  
Two types of data are fetched for each season:
- **Qualifying results:** Driver starting positions.
- **Race results:** Final finishing positions.

Functions `fetch_race_data()` and `fetch_qualifying_data()` handle API calls and return JSON datasets for every round in a season.

### 2. Data Parsing
Each race’s data is normalized into Pandas DataFrames:
- `parse_race_results()` extracts driver IDs and race finish positions.
- `parse_qualifying_results()` extracts driver IDs and qualifying positions.
Both DataFrames are merged by season, race, and driver.

### 3. Correlation Calculation
For each race:
- The **Spearman correlation** between qualifying and race positions is calculated.  
  - A high positive correlation → Qualifying order largely determines race results.  
  - A lower correlation → Race dynamics (strategy, incidents, overtakes) had stronger influence.

### 4. Aggregation and Visualization
All race-level correlations are combined across multiple seasons (2015–2023).  
The project outputs:
- `data/qualifying_vs_race_correlation.csv` — Correlation data for all races.
- `data/qual_vs_race_correlation.png` — A boxplot visualization showing how correlations vary by season.

---

## Installation

Clone or download the repository, then create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main analysis script:

```bash
python qualifying_vs_race_correlation.py
```

The script will:

* Fetch F1 data from the Ergast API (2015–2023)
* Compute per-race Spearman correlations
* Save results and plots in the `data/` directory

---

## Output Files

| File                                      | Description                                   |
| ----------------------------------------- | --------------------------------------------- |
| `data/qualifying_vs_race_correlation.csv` | Contains race-wise correlation results        |
| `data/qual_vs_race_correlation.png`       | Boxplot of correlation distribution by season |

---

## Dependencies

All required libraries are listed in `requirements.txt`:

* pandas
* numpy
* matplotlib
* seaborn
* requests
* beautifulsoup4
* scipy
* tqdm

---

## Notes

* The Ergast API must be online for the script to function.
* Results depend on public data accuracy from the Ergast database.
* The project is designed for analytical and educational purposes only.

---