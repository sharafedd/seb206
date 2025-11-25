# Queries GDELT 1.0 for events and saves raw CSV files in data/raw/

import os
from google.cloud import bigquery

DATA_OUT = "data/raw/gdelt_events.csv"

def fetch_gdelt_events():
    print()
    os.makedirs(os.path.dirname(DATA_OUT), exist_ok=True)
    client = bigquery.Client()

    print("[INFO] Fetching GDELT events...")

    query = """
    SELECT
        SQLDATE,
        Actor1CountryCode AS Actor1,
        Actor2CountryCode AS Actor2,
        GoldsteinScale,
        QuadClass
    FROM
        `gdelt-bq.full.events`
    WHERE
        SQLDATE >= 19790101
        AND SQLDATE <= 20130331
        AND Actor1CountryCode IS NOT NULL
        AND Actor2CountryCode IS NOT NULL
        AND GoldsteinScale IS NOT NULL
    ORDER BY SQLDATE ASC
    """

    df = client.query(query).to_dataframe()
    if df.empty:
        print("[WARN] No data fetched from GDELT.")
        return
    df.to_csv(DATA_OUT, index=False)

    print (f"[OK] Fetched GDELT events to {DATA_OUT} ({len(df)} rows)")

if __name__ == "__main__":
    fetch_gdelt_events()

