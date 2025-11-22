import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm(window=10):
    model = Sequential([
        LSTM(32, input_shape=(window, 1)),
        Dense(1)
    ])

    model.compile(optimizer="adam", loss="mse")
    return model
