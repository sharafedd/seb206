import numpy as np
import pandas as pd
import os

def make_windows(series, window=10):
    X, y = [], []
    for i in range(len(series) - window):
        X.append(series[i:i+window])
        y.append(series[i+window])
    return np.array(X), np.array(y)

def build_for_dyad(path_in, save_folder, window=10):
    df = pd.read_csv(path_in)
    series = df["goldstein"].values

    X, y = make_windows(series, window)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    split = int(len(X) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    os.makedirs(save_folder, exist_ok=True)

    np.save(os.path.join(save_folder, "X_train.npy"), X_train)
    np.save(os.path.join(save_folder, "X_test.npy"), X_test)
    np.save(os.path.join(save_folder, "y_train.npy"), y_train)
    np.save(os.path.join(save_folder, "y_test.npy"), y_test)

    print("Saved train-test windows.")

if __name__ == "__main__":
    in_folder = "../data/processed/weekly_series/"
    out_folder = "../data/processed/train_test_splits/"

    for file in os.listdir(in_folder):
        if file.endswith(".csv"):
            name = file.replace(".csv", "")
            build_for_dyad(
                os.path.join(in_folder, file),
                os.path.join(out_folder, name)
            )
