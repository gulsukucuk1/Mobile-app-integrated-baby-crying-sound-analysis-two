👶 SmartCry: Yapay Zekâ Tabanlı Akıllı Bebek Analiz Sistemi

SmartCry, bebeklerin ağlama seslerini gerçek zamanlı analiz ederek nedenini (açlık, ağrı, uykusuzluk vb.) belirleyen ve ebeveynlere mobil uygulama üzerinden bildirim sunan IoT tabanlı bir araştırma projesidir. Bu çalışma, TÜBİTAK 2209-A programı kapsamında desteklenmektedir.

## 🔧 Entegrasyon Durumu (Integration Status)

✅ **Backend API** - Flask REST API (Çalışıyor / Working)
- ✅ Mel-Spektrogram Analizi
- ✅ MFCC Özellik Çıkarma
- ✅ CORS Desteği
- ✅ Docker Desteği

✅ **Flutter Entegrasyonu** (Tamamlandı / Completed)
- ✅ API İstemcisi (`CryAnalysisService`)
- ✅ Analiz Ekranı (`AnalysisScreen`)
- ✅ Dashboard Entegrasyonu
- ✅ Model Güncellemesi

✅ **AI Modülleri**
- ✅ Feature Extractor (MFCC)
- ✅ Mel Extractor (Mel-Spektrogram)
- ✅ Kategori Sınıflandırması

---

## 🚀 Hızlı Başlama (Quick Start)

### Seçenek 1: Otomatik Kurulum (Windows)
```bash
cd SmartCry-telsiz-main
setup.bat
```

### Seçenek 2: Otomatik Kurulum (macOS/Linux)
```bash
cd SmartCry-telsiz-main
chmod +x setup.sh
./setup.sh
```

### Seçenek 3: Manuel Kurulum

**Backend:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
python app.py
```

**Flutter:**
```bash
cd flutter-app/babycry
flutter pub get
flutter run
```

---

## � Dosya Yapısı ve Görevleri

```
SmartCry-telsiz-main/
├── app.py                         # 🔵 Flask Backend API (Çalışıyor)
├── requirements.txt               # Python bağımlılıkları
├── Dockerfile                     # Docker konteyner yapısı
├── docker-compose.yml             # Docker Compose orchestration
├── test_api.py                    # API test suite
├── INTEGRATION_GUIDE.md           # Detaylı entegrasyon kılavuzu
├── .env.example                   # Konfigürasyon örneği
│
├── AI/                            # 🟢 Python AI Modülleri
│   ├── feature_extractor.py       # MFCC özellik çıkarma
│   ├── mel_extractor.py           # Mel-Spektrogram çıkarma
│   └── data/                      # Eğitim veri setleri
│       ├── belly_pain/
│       ├── burping/
│       ├── discomfort/
│       ├── hungry/
│       └── tired/
│
├── flutter-app/babycry/           # 🔴 Flutter Mobil Uygulaması
│   ├── lib/
│   │   ├── main.dart              # Ana uygulama (Güncellenmiş)
│   │   ├── core/
│   │   │   └── theme/
│   │   │       └── app_theme.dart # Tema sistemi (Güncellenmiş)
│   │   ├── data/
│   │   │   ├── models/
│   │   │   │   └── cry_analysis_model.dart  # Veri modeli (Güncellenmiş)
│   │   │   └── services/
│   │   │       └── cry_analysis_service.dart # API İstemcisi (YENİ)
│   │   └── ui/
│   │       └── screens/
│   │           ├── analysis_screen.dart      # AI Analiz Ekranı (YENİ)
│   │           ├── dashboard_view.dart       # Dashboard (Güncellenmiş)
│   │           └── live_stream_view.dart
│   └── pubspec.yaml               # Flutter bağımlılıkları (Güncellenmiş)
│
├── uploads/                       # 📁 Geçici ses dosyaları
├── setup.bat                      # 🪟 Windows kurulum scripti (YENİ)
└── setup.sh                       # 🐧 Linux/macOS kurulum scripti (YENİ)
```

---

## 🔌 API Endpoints (REST)

### Sağlık Kontrolü
```
GET /api/health
```
**Yanıt:**
```json
{
  "status": "healthy",
  "message": "SmartCry Backend aktif",
  "version": "1.0.0"
}
```

### Mel-Spektrogram Analizi
```
POST /api/analyze/mel
Content-Type: multipart/form-data
Body: { "audio": file }
```
**Yanıt:**
```json
{
  "success": true,
  "features": {
    "shape": [128, 94, 1],
    "dtype": "float32",
    "min": -2.5,
    "max": 2.5,
    "mean": 0.0,
    "std": 1.0
  },
  "filename": "audio.wav",
  "message": "Mel-Spektrogram başarıyla çıkarıldı"
}
```

### MFCC Analizi
```
POST /api/analyze/mfcc
Content-Type: multipart/form-data
Body: { "audio": file }
```

### Kategorileri Al
```
GET /api/categories
```
**Yanıt:**
```json
{
  "categories": {
    "hungry": "🍽️ Açlık",
    "burping": "🤢 Gaz çıkarma",
    "discomfort": "😖 Rahatsızlık",
    "belly_pain": "🤕 Karın ağrısı",
    "tired": "😴 Yorgunluk"
  },
  "total": 5
}
```

---

## 📱 Flutter Uygulaması

### Ana Özellikler
- ✅ Dashboard - Gerçek zamanlı durum takibi
- ✅ Canlı Görüntü - ESP32-CAM entegrasyonu
- ✅ AI Analiz - Backend API ile ses analizi
- ✅ Kategorilendirme - 5 bebek ağlaması kategorisi
- ✅ Tema Desteği - Açık/Koyu tema

### Kurulum
```bash
cd flutter-app/babycry
flutter pub get
flutter run
```

### Backend Bağlantı Ayarı
`lib/data/services/cry_analysis_service.dart` dosyasında:
- **Emülatör:** `http://10.0.2.2:5000/api`
- **Fiziksel Cihaz:** `http://[IP]:5000/api`

---

## 🧪 API Test Etme

```bash
# Tüm testleri çalıştır
python test_api.py

# Ses dosyası ile test
python test_api.py C:\path\to\audio.wav
```

---

## 🛠️ Gereksinimler
pip install librosa tensorflow numpy matplotlib scikit-learn


Paylaşılan preprocess.py dosyasını açıp çalıştırarak öznitelik çıkarımını test edin.

C. Mobil Uygulama (Flutter Katmanı)
VS Code'da flutter-app klasörünü açın.

Terminalden paketleri çekin:
flutter pub get

Android Studio Emulator veya fiziksel cihaz bağlayarak projeyi başlatın:
flutter run

D. Donanım (ESP32 Katmanı)
Arduino IDE'de "AI Thinker ESP32-CAM" kartını seçin.

esp32_firmware içindeki kodu açın, Wi-Fi ve Firebase bilgilerinizi güncelleyin.

"Upload" diyerek kodu cihaza yükleyin.

---

## 🛠️ Gereksinimler

### Backend (Python)
- Python 3.8+
- Flask 2.3.3
- librosa 0.10.0
- numpy 1.24.3
- scipy 1.11.2
- scikit-learn 1.3.1

### Flutter
- Flutter SDK 3.10+
- Android SDK / Xcode
- Dart 3.0+

### İsteğe Bağlı
- Docker & Docker Compose
- Git

---

## 📊 Mimari

```
┌─────────────────────────────────────────────────────────┐
│                    Flutter Uygulaması                    │
│  (Dashboard, Analiz Ekranı, Canlı Görüntü)              │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/REST
                     │
┌────────────────────▼────────────────────────────────────┐
│          Flask Backend API (app.py)                     │
│   - Health Check                                        │
│   - Mel-Spektrogram Analizi                            │
│   - MFCC Özellik Çıkarma                               │
│   - Kategori Bilgisi                                    │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
┌───────▼──────────┐    ┌────────▼────────┐
│  AI Modülleri    │    │   Uploading    │
│  (Python)        │    │  (Temp Files)   │
│                  │    │                 │
│ • feature_       │    │ uploads/        │
│   extractor.py   │    │                 │
│ • mel_extractor  │    └─────────────────┘
│   .py            │
└──────────────────┘
```

---

## 💡 Başlıca Özellikleri

### 1. **Ses Analizi** 🎙️
- MFCC özellik çıkarma
- Mel-Spektrogram analizi
- Doğruluk oranı raporlama

### 2. **Kategorilendirme** 🏷️
- Açlık (Hungry)
- Gaz çıkarma (Burping)
- Rahatsızlık (Discomfort)
- Karın ağrısı (Belly Pain)
- Yorgunluk (Tired)

### 3. **Gerçek Zamanlı** ⚡
- HTTP REST API
- Düşük gecikmeli (low latency)
- Skalabilir mimari

### 4. **Güvenlik** 🔒
- CORS desteği
- Dosya boyutu limiti
- Input validasyonu

---

## 🚀 Gelecek Planları

- [ ] ML Model Entegrasyonu (TensorFlow/PyTorch)
- [ ] Veritabanı Entegrasyonu (PostgreSQL)
- [ ] Firebase Realtime Database
- [ ] Bildirim Sistemi (Push Notifications)
- [ ] Kullanıcı Kimlik Doğrulama (JWT)
- [ ] Web Dashboard
- [ ] ESP32 Firmware Entegrasyonu
- [ ] Edge Computing (TinyML)
- [ ] Analitik Panel
- [ ] Multi-dil Desteği

---

## 🐛 Sorun Giderme

### Backend bağlanamıyor
```bash
# Backend çalıştığını kontrol et
python app.py

# Port 5000 kullanımdaysa başka port kullan
# app.py'de: app.run(port=5001)
```

### Flutter bağlantı hatası
```dart
// cry_analysis_service.dart'da IP adresi değiştir
static const String baseUrl = 'http://192.168.1.X:5000/api';
```

### ModuleNotFoundError
```bash
pip install -r requirements.txt
```

---

## 📞 İletişim ve Destek

**Danışman:** Hüseyin YANIK (Mersin Üniversitesi)
**Yürütücü:** Gülsu KÜÇÜK
**Araştırmacılar:** Hilal Şuheda ESER, Meysem BAKİR, Bilge BEKTAŞ, Çağla KUŞ

---

## 📄 Lisans

Bu proje TÜBİTAK 2209-A programı kapsamında geliştirilmektedir.

---

**SmartCry © 2024** - Akıllı Bebek Analiz Sistemi
Versiyon: 1.0.0 | Son Güncelleme: Ocak 2026










