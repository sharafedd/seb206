# Analyze data module
# Generates:
#   - Weekly GSS plots
#   - Weekly QuadClass distribution plots
#   - Summary statistics
#
# Reads from:   ../data/processed/
# Writes to:    ../reports/data_analysis/

import os
import pandas as pd
import matplotlib.pyplot as plt

# FIX: paths must be relative to the notebook, which lives in /notebooks/
DATA_DIR = "../data/processed"
OUTPUT_DIR = "../reports/data_analysis"

def analysis():
    print()
    print("[INFO] Starting analysis...")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Check data directory exists
    if not os.path.exists(DATA_DIR):
        raise FileNotFoundError(f"[ERROR] Data directory not found: {DATA_DIR}")

    all_stats = []

    # Loop through all processed CSV files
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            file_path = os.path.join(DATA_DIR, file)
            dyad_name = file.replace(".csv", "")
            df = pd.read_csv(file_path)

            # Convert week to datetime
            df["week"] = pd.to_datetime(df["week"])

            # ---------- SUMMARY STATISTICS ----------
            stats = {
                "dyad": dyad_name,
                "num_weeks": len(df),
                "mean_gss": df["GoldsteinScale"].mean(),
                "std_gss": df["GoldsteinScale"].std(),
                "min_gss": df["GoldsteinScale"].min(),
                "max_gss": df["GoldsteinScale"].max(),
            }
            all_stats.append(stats)

            # ---------- PLOT GSS ----------
            plt.figure(figsize=(10, 6))
            plt.plot(df["week"], df["GoldsteinScale"], marker="o", linestyle="-", label="GSS Weekly Mean")
            plt.title(f"GSS Over Time for {dyad_name}")
            plt.xlabel("Week")
            plt.ylabel("Goldstein Scale")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_DIR, f"{dyad_name}_gss_over_time.png"))
            plt.close()

            # ---------- PLOT QUADCLASS DISTRIBUTION ----------
            qc_cols = [col for col in df.columns if col.startswith("QuadClass_")]

            plt.figure(figsize=(10, 6))
            for col in qc_cols:
                plt.plot(df["week"], df[col], marker="o", linestyle="-", label=col)

            plt.title(f"QuadClass Distribution Over Time for {dyad_name}")
            plt.xlabel("Week")
            plt.ylabel("Proportion")
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_DIR, f"{dyad_name}_quadclass_distribution.png"))
            plt.close()

            print(f"[OK] Processed dyad: {dyad_name}")

    # ---------- SAVE SUMMARY ----------
    stats_df = pd.DataFrame(all_stats)
    stats_df.to_csv(os.path.join(OUTPUT_DIR, "summary_statistics.csv"), index=False)

    print("[OK] Data analysis complete. Summary saved to summary_statistics.csv")
    print(f"[OK] All plots stored in: {OUTPUT_DIR}")


if __name__ == "__main__":
    analysis()
