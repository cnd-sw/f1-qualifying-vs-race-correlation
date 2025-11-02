import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import os

os.makedirs("data", exist_ok=True)

def fetch_race_data(season):
    url = f"https://ergast.com/api/f1/{season}/results.json?limit=1000"
    res = requests.get(url)
    if res.status_code != 200:
        return None
    return res.json()

def fetch_qualifying_data(season):
    url = f"https://ergast.com/api/f1/{season}/qualifying.json?limit=1000"
    res = requests.get(url)
    if res.status_code != 200:
        return None
    return res.json()

def parse_race_results(data):
    results = []
    for race in data["MRData"]["RaceTable"]["Races"]:
        race_name = race["raceName"]
        round_no = race["round"]
        for r in race["Results"]:
            driver = r["Driver"]["driverId"]
            pos = int(r["position"])
            results.append({
                "season": data["MRData"]["RaceTable"]["season"],
                "round": round_no,
                "race": race_name,
                "driver": driver,
                "race_pos": pos
            })
    return pd.DataFrame(results)

def parse_qualifying_results(data):
    results = []
    for race in data["MRData"]["RaceTable"]["Races"]:
        race_name = race["raceName"]
        round_no = race["round"]
        for q in race["QualifyingResults"]:
            driver = q["Driver"]["driverId"]
            pos = int(q["position"])
            results.append({
                "season": data["MRData"]["RaceTable"]["season"],
                "round": round_no,
                "race": race_name,
                "driver": driver,
                "qual_pos": pos
            })
    return pd.DataFrame(results)

def build_correlation(season):
    race_json = fetch_race_data(season)
    qual_json = fetch_qualifying_data(season)
    if not race_json or not qual_json:
        print(f"Data fetch failed for {season}")
        return None

    race_df = parse_race_results(race_json)
    qual_df = parse_qualifying_results(qual_json)

    merged = pd.merge(race_df, qual_df, on=["season", "round", "race", "driver"], how="inner")

    corr_values = merged.groupby("race").apply(
        lambda x: spearmanr(x["qual_pos"], x["race_pos"]).correlation
    ).reset_index(name="spearman_corr")

    corr_values["season"] = season
    return corr_values

def main():
    seasons = list(range(2015, 2024))
    all_corr = []

    for season in tqdm(seasons, desc="Processing seasons"):
        df = build_correlation(season)
        if df is not None:
            all_corr.append(df)

    full_corr = pd.concat(all_corr, ignore_index=True)
    full_corr.to_csv("data/qualifying_vs_race_correlation.csv", index=False)

    plt.figure(figsize=(12,6))
    sns.boxplot(data=full_corr, x="season", y="spearman_corr", palette="coolwarm")
    plt.title("Spearman Correlation between Qualifying and Race Results by Season")
    plt.xlabel("Season")
    plt.ylabel("Correlation (Qualifying vs Race)")
    plt.tight_layout()
    plt.savefig("data/qual_vs_race_correlation.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()