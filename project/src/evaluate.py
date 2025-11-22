import numpy as np
import tensorflow as tf
import os
import pandas as pd

def evaluate(folder):
    model_path = os.path.join(folder, "lstm_model.keras")

    dyad_name = folder.replace("data/processed/train_test_splits/", "").strip("/")

    if not os.path.exists(model_path):
        return dyad_name, None

    model = tf.keras.models.load_model(model_path)

    X_test = np.load(os.path.join(folder, "X_test.npy"))
    y_test = np.load(os.path.join(folder, "y_test.npy"))

    preds = model.predict(X_test).flatten()
    rmse = np.sqrt(np.mean((preds - y_test)**2))

    return dyad_name, rmse


if __name__ == "__main__":
    base = "data/processed/train_test_splits/"
    results = []

    for dyad in os.listdir(base):
        folder = os.path.join(base, dyad)
        if os.path.isdir(folder):
            dyad_name, rmse = evaluate(folder)
            results.append({"dyad": dyad_name, "rmse": rmse})

    df = pd.DataFrame(results)
    df.to_csv("evaluation_results.csv", index=False)
    print(df)
