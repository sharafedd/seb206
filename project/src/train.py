import numpy as np
from model_lstm import build_lstm
import os
import tensorflow as tf

def train_for_dyad(folder):
    X_train = np.load(os.path.join(folder, "X_train.npy"))
    y_train = np.load(os.path.join(folder, "y_train.npy"))

    model = build_lstm()

    history = model.fit(
        X_train, y_train,
        epochs=40,
        batch_size=16,
        validation_split=0.1,
        verbose=1
    )

    model.save(os.path.join(folder, "lstm_model.h5"))
    print(f"Model saved for {folder}")

if __name__ == "__main__":
    base = "../data/processed/train_test_splits/"
    for dyad in os.listdir(base):
        folder = os.path.join(base, dyad)
        if os.path.isdir(folder):
            train_for_dyad(folder)
