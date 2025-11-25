# Data preprocessing module for ETL pipeline:
# 1. Rank top 10 countries by event count
# 2. Filter events for these countries
# 3. Create dyad column
# 4. Convert SQLDATE to datetime
# 5. Resample to weekly frequency with mean GSS and QC distribution
# 6. Save to data/processed/<dyad_name>.csv

import os
import pandas as pd

RAW_PATH = "../data/raw/gdelt_events.csv"
PROCESSED_PATH = "../data/processed/"

def preprocess():
    print()
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    # Load raw data
    df = pd.read_csv(RAW_PATH)
    df["date"] = pd.to_datetime(df["SQLDATE"], format="%Y%m%d")
    print(f"[INFO] Loaded {len(df)} events from {RAW_PATH}")

    # Rank countries by event count
    counts = (
        pd.concat([df["Actor1"], df["Actor2"]])
        .value_counts()
        .head(10)
    )
    top10 = counts.index.tolist()
    print("[INFO] Top 10 countries by event count:", top10)

    # Filter only top 10 countries events
    df = df[
        df["Actor1"].isin(top10) &
        df["Actor2"].isin(top10)
    ]
    print(f"[INFO] Filtered to {len(df)} events involving top 10 countries")

    # Create dyad column
    df["dyad"] = df.apply(
        lambda row: "-".join(sorted([row["Actor1"], row["Actor2"]])),
        axis=1
    )
    print(f"[INFO] Created dyad column with {df['dyad'].nunique()} unique dyads")

    # Group by dyad and resample weekly
    for dyad, d in df.groupby("dyad"):
        d = d.sort_values("date").set_index("date")

        # Weekly mean Goldstein score
        gss_weekly = d["GoldsteinScale"].resample("W-SUN").mean()

        # QUADCLASS DISTRIBUTION
        weekly_groups = d["QuadClass"].resample("W-SUN")

        qc_list = []
        week_list = []

        for week, series in weekly_groups:
            counts = series.value_counts(normalize=True)
            counts = counts.reindex([1, 2, 3, 4], fill_value=0)  # ensure all 4 classes
            qc_list.append(counts)
            week_list.append(week)

        qc_distribution = pd.DataFrame(qc_list, index=week_list)
        qc_distribution.index.name = "week"
        qc_distribution.columns = ["QuadClass_1", "QuadClass_2", "QuadClass_3", "QuadClass_4"]

        out = pd.concat(
            [
                gss_weekly.rename("GoldsteinScale"),
                qc_distribution
            ],
            axis=1
        )

        out.index.name = "week"
        out.reset_index(inplace=True)

        # Save to CSV
        out_path = os.path.join(PROCESSED_PATH, f"{dyad.lower()}.csv")
        out.to_csv(out_path, index=False)
        print(f"[OK] Saved processed dyad {dyad} to {out_path}")

if __name__ == "__main__":
    preprocess()
