import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("evaluation_results.csv")

# Remove rows with no model
df = df.dropna()

# Compute accuracy %
df["accuracy"] = 1 - (df["rmse"] / df["rmse"].max())
df["accuracy"] = df["accuracy"] * 100

plt.figure(figsize=(12, 6))
plt.bar(df["dyad"], df["accuracy"])
plt.xticks(rotation=90)
plt.ylabel("Accuracy (%)")
plt.title("Baseline LSTM Accuracy per Dyad (higher is better)")

plt.tight_layout()
plt.savefig("evaluation_plot.png")
plt.show()
