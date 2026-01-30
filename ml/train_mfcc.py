print("train_mfcc.py CALISIYOR")

import os
import sys
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

sys.path.append(os.path.abspath("../AI"))
from feature_extractor import extract_mfcc_cnn

DATASET_PATH = "../AI/data"
MODEL_OUT = "models/mfcc_cnn.h5"

X, y = [], []

for label in os.listdir(DATASET_PATH):
    label_path = os.path.join(DATASET_PATH, label)
    if not os.path.isdir(label_path):
        continue

    for file in os.listdir(label_path):
        if file.endswith(".wav"):
            file_path = os.path.join(label_path, file)
            features = extract_mfcc_cnn(file_path)
            X.append(features)
            y.append(label)

X = np.array(X)

le = LabelEncoder()
y = to_categorical(le.fit_transform(y))

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=X.shape[1:]),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(y.shape[1], activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()
model.fit(X, y, epochs=20, batch_size=8, validation_split=0.2)
model.save(MODEL_OUT)

print("MFCC modeli kaydedildi:", MODEL_OUT)
