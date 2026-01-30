import os
import numpy as np
import librosa

def extract_mel_cnn(
    file_path,
    sr=16000,
    duration=3.0,
    n_mels=128,
    n_fft=2048,
    hop_length=512,
    fmax=8000
):
    """
    SmartCry - Ses Ön İşleme Modülü
    Sesi Mel-Spektrogram formatına çevirerek CNN modeline hazırlar.
    """
    # 1. Dosya var mı kontrol et
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Ses dosyası bulunamadı: {file_path}")

    # 2. Beklenen örnek sayısı
    expected_samples = int(sr * duration)

    # 3. Ses dosyasını yükle
    y, _ = librosa.load(file_path, sr=sr, mono=True, duration=duration)

    # 4. Ses boşsa hata ver
    if y is None or y.size == 0:
        raise ValueError("Ses sinyali boş veya okunamadı.")

    # 5. Ses kısa ise sıfırlarla doldur (Padding)
    if len(y) < expected_samples:
        y = np.pad(y, (0, expected_samples - len(y)), mode='constant')

    # 6. Mel-Spektrogram hesapla
    mel = librosa.feature.melspectrogram(
        y=y,
        sr=sr,
        n_mels=n_mels,
        n_fft=n_fft,
        hop_length=hop_length,
        fmax=fmax
    )

    # 7. Desibel (dB) dönüşümü
    mel_db = librosa.power_to_db(mel, ref=np.max)

    # 8. Zaman boyutunu sabitle (CNN için 128x94 boyutunu korur)
    target_frames = int(np.ceil(expected_samples / hop_length))
    if mel_db.shape[1] < target_frames:
        mel_db = np.pad(
            mel_db,
            ((0, 0), (0, target_frames - mel_db.shape[1])),
            mode='constant'
        )
    else:
        mel_db = mel_db[:, :target_frames]

    # 9. Normalizasyon (Z-Score)
    mel_db = (mel_db - np.mean(mel_db)) / (np.std(mel_db) + 1e-8)

    # 10. CNN Kanal Boyutu Ekleme (Input Shape: 128, 94, 1)
    return mel_db.astype(np.float32)[..., np.newaxis]

# --- TEST VE SMARTCRY LOGO BLOĞU ---
if __name__ == "__main__":
    print("\n" + "*"*44)
    print("* *")
    print("* SMARTCRY YAPAY ZEKA MODÜLÜ AKTİF      *")
    print("* *")
    print("*"*44)
    print(f"[DURUM] Kütüphaneler: Hazır (Librosa {librosa.__version__})")
    print("[DURUM] Fonksiyon: extract_mel_cnn aktif.")
    print("-" * 44)
    print("Sıradaki Adım: Bebek ağlaması verisi bekleniyor...")
    print("*"*44 + "\n")