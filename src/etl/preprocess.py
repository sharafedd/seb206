import pandas as pd
import numpy as np
import os

def clean_and_aggregate(path_in, path_out):
    # Load raw dyad data
    df = pd.read_csv(path_in)

    # Remove invalid Goldstein rows
    df = df.dropna(subset=["GoldsteinScale"])
    df = df[df["GoldsteinScale"].between(-10, 10)]

    # Convert SQLDATE to proper timestamp
    df["date"] = pd.to_datetime(df["SQLDATE"], format="%Y%m%d")
    df = df.sort_values("date")

    # Weekly mean Goldstein score
    weekly = (
        df.groupby(pd.Grouper(key="date", freq="W"))["GoldsteinScale"]
        .mean()
        .reset_index()
        .rename(columns={"GoldsteinScale": "goldstein"})
    )

    # Create continuous weekly index
    full_range = pd.date_range(weekly["date"].min(),
                               weekly["date"].max(),
                               freq="W")

    weekly = (
        weekly.set_index("date")
        .reindex(full_range)
    )
    weekly.index.name = "week"

    # Fill missing weeks (forward then backward)
    weekly["goldstein"] = weekly["goldstein"].ffill().bfill()

    # Save
    os.makedirs(os.path.dirname(path_out), exist_ok=True)
    weekly.to_csv(path_out)

    print(f"[OK] Processed {path_out} ({len(weekly)} weeks)")


if __name__ == "__main__":
    raw_folder = "../data/raw/dyads/"
    out_folder = "../data/processed/weekly_series/"

    os.makedirs(out_folder, exist_ok=True)

    for file in os.listdir(raw_folder):
        if file.endswith(".csv"):
            input_path = os.path.join(raw_folder, file)

            # Remove "_raw" and force lowercase + .csv
            base_name = file.replace("_raw", "").lower()
            if not base_name.endswith(".csv"):
                base_name += ".csv"

            output_path = os.path.join(out_folder, base_name)

            clean_and_aggregate(input_path, output_path)
