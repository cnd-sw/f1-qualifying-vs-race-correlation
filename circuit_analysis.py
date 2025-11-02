import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from qualifying_vs_race_correlation import load_data

# Load correlation data
df = load_data()

# Ensure expected columns exist
required_columns = {"season", "round", "race_name", "correlation"}
if not required_columns.issubset(df.columns):
    raise ValueError(f"Missing required columns in data: {required_columns - set(df.columns)}")

# Compute per-circuit statistics
circuit_summary = (
    df.groupby("race_name")["correlation"]
    .agg(["mean", "std", "count"])
    .sort_values(by="mean", ascending=False)
    .reset_index()
)

# Save results
Path("data").mkdir(exist_ok=True)
circuit_summary.to_csv("data/circuit_correlation_summary.csv", index=False)

# Visualization — average correlation per circuit
plt.figure(figsize=(10, 12))
sns.barplot(
    y="race_name",
    x="mean",
    data=circuit_summary,
    palette="viridis"
)
plt.xlabel("Average Spearman Correlation (Qualifying vs Race)")
plt.ylabel("Circuit")
plt.title("Average Qualifying–Race Correlation by Circuit (2015–2023)")
plt.tight_layout()
plt.savefig("data/circuit_correlation_summary.png", dpi=300)
plt.close()

print("Circuit analysis complete.")
print("→ data/circuit_correlation_summary.csv")
print("→ data/circuit_correlation_summary.png")
