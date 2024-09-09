import tensorflow as tf
from tensorflow.keras import layers # type: ignore

def create_decision_model(input_shape, action_size):
    # Neural network model for decision-making
    model = tf.keras.Sequential([
        layers.Dense(64, input_dim=input_shape, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(action_size, activation='linear')
    ])
    return model
