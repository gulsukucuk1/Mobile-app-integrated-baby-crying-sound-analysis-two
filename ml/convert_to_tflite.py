import tensorflow as tf
import numpy as np
import os

MODEL_PATH = "models/mfcc_cnn.h5"
OUT_PATH = "models/mfcc_cnn_int8.tflite"

print("Model yükleniyor...")
model = tf.keras.models.load_model(MODEL_PATH)

def representative_dataset():
    for _ in range(100):
        dummy = np.random.rand(1, 120, 94, 1).astype(np.float32)
        yield [dummy]

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

tflite_model = converter.convert()

with open(OUT_PATH, "wb") as f:
    f.write(tflite_model)

print("TFLite INT8 model oluşturuldu:")
print(OUT_PATH)
print("Model boyutu (KB):", len(tflite_model) / 1024)
