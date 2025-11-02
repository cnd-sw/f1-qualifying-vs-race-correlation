````markdown
# Qualifying vs Race Correlation Model

## Overview
This project analyzes how closely **Formula 1 qualifying positions** correlate with **final race results** across multiple seasons using public data from the **Ergast API**.  
It measures the **Spearman correlation** between qualifying ranks and race finishing positions for each Grand Prix, revealing which circuits and seasons reward raw pace versus race-day execution.

---

## How It Works

### 1. Data Retrieval  
The main script **`qualifying_vs_race_correlation.py`** connects to the **Ergast Developer API** to fetch structured Formula 1 data (qualifying and race results) from multiple seasons (2015–2023).  
It calculates the **Spearman correlation** between qualifying position and race finish position for each Grand Prix and stores the results locally.

### 2. Data Analysis  
The second script **`circuit_analysis.py`** loads the generated correlation data from CSV (no API calls required) and aggregates results by circuit to determine which tracks show stronger qualifying–race consistency.  
It outputs both tabular and visual summaries of circuit-level trends.

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

### Step 1 – Generate Base Correlation Data

Run the main script (requires Ergast API availability):

```bash
python qualifying_vs_race_correlation.py
```

This will:

* Fetch F1 data from the Ergast API (2015–2023)
* Compute per-race Spearman correlations
* Save results and plots in the `data/` directory

**Outputs:**

* `data/qualifying_vs_race_correlation.csv`
* `data/qual_vs_race_correlation.png`

---

### Step 2 – Analyze Circuits (Offline)

Once the CSV exists, run:

```bash
python circuit_analysis.py
```

This script:

* Loads correlation results from local storage
* Aggregates and ranks circuits by average qualifying–race correlation
* Generates both CSV and PNG outputs for circuit-level analysis

**Outputs:**

* `data/circuit_correlation_summary.csv`
* `data/circuit_correlation_summary.png`

---

## Output Files

| File                                      | Description                                   |
| ----------------------------------------- | --------------------------------------------- |
| `data/qualifying_vs_race_correlation.csv` | Race-wise correlation results (from API)      |
| `data/qual_vs_race_correlation.png`       | Boxplot of correlation distribution by season |
| `data/circuit_correlation_summary.csv`    | Circuit-level aggregated results (offline)    |
| `data/circuit_correlation_summary.png`    | Barplot of average correlation by circuit     |

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

* The **Ergast API** must be online for Step 1; Step 2 runs fully offline using local CSVs.
* Running Step 1 again updates the dataset automatically.
* The project is intended for analytical and educational purposes.
* All generated figures and tables are stored in the `data/` directory.

```
```
