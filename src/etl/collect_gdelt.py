from google.cloud import bigquery
import pandas as pd
import os

client = bigquery.Client()

dyads = [
    ("USA", "RUS"), ("USA", "CHN"), ("USA", "IND"), ("USA", "PAK"),
    ("USA", "GBR"), ("USA", "TUR"), ("USA", "SAU"), ("USA", "IRN"), ("USA", "ISR"),

    ("RUS", "CHN"), ("RUS", "IND"), ("RUS", "PAK"),
    ("RUS", "GBR"), ("RUS", "TUR"), ("RUS", "SAU"),
    ("RUS", "IRN"), ("RUS", "ISR"),

    ("CHN", "IND"), ("CHN", "PAK"), ("CHN", "GBR"),
    ("CHN", "TUR"), ("CHN", "SAU"),
    ("CHN", "IRN"), ("CHN", "ISR"),

    ("IND", "PAK"), ("IND", "GBR"), ("IND", "TUR"),
    ("IND", "SAU"), ("IND", "IRN"), ("IND", "ISR"),

    ("PAK", "GBR"), ("PAK", "TUR"),
    ("PAK", "SAU"), ("PAK", "IRN"), ("PAK", "ISR"),

    ("GBR", "TUR"), ("GBR", "SAU"),
    ("GBR", "IRN"), ("GBR", "ISR"),

    ("TUR", "SAU"), ("TUR", "IRN"), ("TUR", "ISR"),

    ("SAU", "IRN"), ("SAU", "ISR"),

    ("IRN", "ISR")
]

# ----------------------------------------------------------------------
# Fetch dyad data with parameterized BigQuery query
# ----------------------------------------------------------------------
def fetch_dyad(a1, a2, save_path):
    query = """
    SELECT
      SQLDATE,
      Actor1CountryCode AS a1,
      Actor2CountryCode AS a2,
      GoldsteinScale
    FROM
      `gdelt-bq.full.events`
    WHERE
      (
        (Actor1CountryCode = @a1 AND Actor2CountryCode = @a2)
        OR
        (Actor1CountryCode = @a2 AND Actor2CountryCode = @a1)
      )
      AND SQLDATE >= 20000101
      AND SQLDATE <= 20051231
    ORDER BY SQLDATE ASC
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("a1", "STRING", a1),
            bigquery.ScalarQueryParameter("a2", "STRING", a2),
        ]
    )

    df = client.query(query, job_config=job_config).to_dataframe()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)

    print(f"[OK] Saved {save_path}  ({len(df)} rows)")


# ----------------------------------------------------------------------
# Main script: fetch all dyads
# ----------------------------------------------------------------------
if __name__ == "__main__":
    BASE = "../data/raw/dyads"

    for a1, a2 in dyads:
        fname = f"{a1}_{a2}_raw.csv"
        save_path = os.path.join(BASE, fname)
        fetch_dyad(a1, a2, save_path)
