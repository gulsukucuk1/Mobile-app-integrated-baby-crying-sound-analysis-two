import pathlib

tflite_path = "models/mfcc_cnn_int8.tflite"
output_path = "model_data.cc"

data = pathlib.Path(tflite_path).read_bytes()

with open(output_path, "w") as f:
    f.write("unsigned char mfcc_cnn_int8_tflite[] = {\n")

    for i, byte in enumerate(data):
        if i % 12 == 0:
            f.write("  ")
        f.write(f"0x{byte:02x}, ")
        if i % 12 == 11:
            f.write("\n")

    f.write("\n};\n")
    f.write(f"unsigned int mfcc_cnn_int8_tflite_len = {len(data)};\n")

print("model_data.cc oluşturuldu")
print("Boyut:", len(data), "byte")
