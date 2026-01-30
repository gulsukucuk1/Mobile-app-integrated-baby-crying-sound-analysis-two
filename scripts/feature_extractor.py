import os
import numpy as np
import librosa

def extract_mfcc_cnn(
    file_path,
    sr=16000,
    duration=3.0,
    n_mfcc=40,
    n_fft=2048,
    hop_length=512,
    pre_emphasis=0.97
):
    # Dosya var mı kontrol et
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Ses dosyası bulunamadı: {file_path}")

    # Beklenen örnek sayısı
    expected_samples = int(sr * duration)

    # Ses dosyasını yükle (mono, sabit örnekleme hızı)
    y, _ = librosa.load(file_path, sr=sr, mono=True, duration=duration)

    # Ses boşsa hata ver
    if y is None or y.size == 0:
        raise ValueError("Ses sinyali boş veya okunamadı.")

    # Ses kısa ise sıfırlarla doldur
    if len(y) < expected_samples:
        y = np.pad(y, (0, expected_samples - len(y)), mode='constant')

    # Pre-emphasis filtresi (yüksek frekansları vurgular)
    if pre_emphasis is not None and pre_emphasis != 0:
        y = np.append(y[0], y[1:] - pre_emphasis * y[:-1])

    # MFCC hesapla
    mfcc = librosa.feature.mfcc(
        y=y,
        sr=sr,
        n_mfcc=n_mfcc,
        n_fft=n_fft,
        hop_length=hop_length
    )

    # Delta ve Delta-Delta hesapla
    delta = librosa.feature.delta(mfcc)
    delta2 = librosa.feature.delta(mfcc, order=2)

    # Özellikleri birleştir
    features = np.vstack([mfcc, delta, delta2])

    # Zaman boyutunu sabitle
    target_frames = int(np.ceil(expected_samples / hop_length))
    if features.shape[1] < target_frames:
        features = np.pad(
            features,
            ((0, 0), (0, target_frames - features.shape[1])),
            mode='constant'
        )
    else:
        features = features[:, :target_frames]

    # Normalizasyon (Z-score)
    features = (features - np.mean(features)) / (np.std(features) + 1e-8)

    # float32 ve CNN için kanal ekle
    return features.astype(np.float32)[..., np.newaxis]