# SmartCry - Entegre Sistem Başlama Rehberi

## 📋 İçerik

1. [Genel Bakış](#genel-bakış)
2. [Sistem Gereksinimler](#sistem-gereksinimler)
3. [Adım Adım Kurulum](#adım-adım-kurulum)
4. [Hızlı Başlama](#hızlı-başlama)
5. [Yapılandırma](#yapılandırma)
6. [Test Etme](#test-etme)
7. [Sorun Giderme](#sorun-giderme)

---

## Genel Bakış

SmartCry, üç ana katmandan oluşur:

```
┌─────────────────────────────────────────┐
│   📱 Flutter Mobil Uygulaması (Dart)   │
│   - Dashboard                           │
│   - Analiz Ekranı                       │
│   - Canlı Görüntü                       │
└─────────────────────────────────────────┘
                    ↕ HTTP/REST
┌─────────────────────────────────────────┐
│   🔵 Flask Backend API (Python)         │
│   - Mel-Spektrogram Analizi             │
│   - MFCC Özellik Çıkarma                │
│   - Kategori Yönetimi                   │
└─────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────┐
│   🟢 AI Modülleri (Python/NumPy)       │
│   - Feature Extractor                   │
│   - Mel Extractor                       │
│   - Kategorilendirme                    │
└─────────────────────────────────────────┘
```

---

## Sistem Gereksinimler

### Yazılım Gereksinimleri

**Backend:**
- Python 3.8+
- pip (Python paket yöneticisi)
- Virtual Environment

**Flutter:**
- Flutter SDK 3.10+
- Dart 3.0+
- Android SDK (Android) veya Xcode (iOS/macOS)

**İsteğe Bağlı:**
- Docker & Docker Compose
- Git
- VS Code veya Android Studio

### Donanım Gereksinimleri

- **Bilgisayar:** Windows, macOS, veya Linux
- **RAM:** En az 4 GB
- **Disk:** En az 5 GB boş alan
- **İnternet:** Wi-Fi bağlantısı (Mobil test için)

---

## Adım Adım Kurulum

### A. Backend Kurulumu

#### 1. Virtual Environment Oluştur

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

**Beklenen çıktı:**
```
Successfully installed Flask-2.3.3 numpy-1.24.3 librosa-0.10.0 ...
```

#### 3. Uploads Klasörü Oluştur

```bash
mkdir uploads
```

#### 4. API Sunucusunu Başlat

```bash
python app.py
```

**Beklenen çıktı:**
```
**************************************************
*  SmartCry Backend API - Başlatılıyor...     *
**************************************************
[INFO] Flask Server: http://localhost:5000
[INFO] CORS: Etkinleştirildi (Flutter entegrasyonu)
[INFO] Modüller: Feature Extractor, Mel Extractor
-------------------------------------------------
```

### B. Flutter Kurulumu

#### 1. Flutter SDK Kontrol Et

```bash
flutter --version
flutter doctor
```

#### 2. Proje Dizinine Git

```bash
cd flutter-app/babycry
```

#### 3. Bağımlılıkları Yükle

```bash
flutter pub get
```

#### 4. Emülatör veya Cihaz Hazırla

**Emülatör (Android):**
```bash
flutter emulators --launch Pixel_5_API_31
```

**Fiziksel Cihaz:**
- USB Debugging'i aç
- Kabloyla bilgisayara bağla
- Sorulara Yes yanıtı ver

#### 5. Uygulamayı Çalıştır

```bash
flutter run
```

---

## Hızlı Başlama

### Seçenek 1: Otomatik Kurulum (Önerilen)

**Windows:**
```batch
setup.bat
```

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Seçenek 2: Manuel Kurulum

**Terminal 1 - Backend:**
```bash
cd SmartCry-telsiz-main
python -m venv venv
venv\Scripts\activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Terminal 2 - Flutter:**
```bash
cd flutter-app/babycry
flutter pub get
flutter run
```

---

## Yapılandırma

### Backend Yapılandırması

**Dosya:** `app.py`

```python
# Port değiştir (varsayılan 5000)
app.run(host='0.0.0.0', port=5001)

# DEBUG modunu kapat (production)
app.run(debug=False)

# Dosya boyutu limitini değiştir
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 MB
```

### Flutter Yapılandırması

**Dosya:** `lib/data/services/cry_analysis_service.dart`

```dart
// Emülatör (Android)
static const String baseUrl = 'http://10.0.2.2:5000/api';

// Fiziksel cihaz (Wi-Fi)
static const String baseUrl = 'http://192.168.1.100:5000/api';

// Cloud server
static const String baseUrl = 'https://api.smartcry.com/api';
```

### Dosya İzinleri (Android)

**Dosya:** `android/app/src/main/AndroidManifest.xml`

```xml
<!-- İnternet -->
<uses-permission android:name="android.permission.INTERNET" />

<!-- Mikrofon -->
<uses-permission android:name="android.permission.RECORD_AUDIO" />

<!-- Depolama -->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

---

## Test Etme

### 1. API Sağlık Kontrolü

```bash
python test_api.py
```

### 2. Spesifik Endpoint Test

**cURL ile:**
```bash
# Sağlık kontrolü
curl http://localhost:5000/api/health

# Kategoriler
curl http://localhost:5000/api/categories
```

**PowerShell ile:**
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/health"
```

### 3. Postman ile

1. `SmartCry_API.postman_collection.json` indir
2. Postman'i aç
3. Collections > Import > JSON dosyasını seç
4. Tüm endpoint'leri test et

### 4. AI Modülleri Test

```bash
python test_modules.py
```

---

## Sorun Giderme

### Backend Sorunları

#### "ModuleNotFoundError: No module named 'flask'"

```bash
# Çözüm:
pip install -r requirements.txt
```

#### "Address already in use"

Port 5000 zaten kullanımdadır.

```bash
# Port değiştir:
# app.py'de port parametresini değiştir
app.run(port=5001)
```

Veya mevcut işlemi sonlandır:

**Windows:**
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
lsof -i :5000
kill -9 <PID>
```

#### "ConnectionRefusedError"

Backend sunucusu çalışmıyor.

```bash
# Çözüm: Backend'i başlat
python app.py
```

### Flutter Sorunları

#### "Emulator not found"

```bash
flutter emulators --launch emulator_id
```

#### "Connection timeout"

```dart
// baseUrl'i kontrol et
// Emülatör: http://10.0.2.2:5000/api
// Fiziksel: http://[LOCAL_IP]:5000/api
```

#### "Pub get failed"

```bash
flutter clean
flutter pub get
```

### Network Sorunları

#### Emülatör Backend'e Bağlanamıyor

```dart
// YANLIŞ:
static const String baseUrl = 'http://localhost:5000/api';

// DOĞRU (Emülatör):
static const String baseUrl = 'http://10.0.2.2:5000/api';

// DOĞRU (Fiziksel cihaz):
static const String baseUrl = 'http://192.168.1.100:5000/api';
```

#### Bilgisayar IP Adresini Bul

**Windows:**
```powershell
ipconfig
# IPv4 Address'i ara: 192.168.x.x
```

**macOS/Linux:**
```bash
ifconfig
# inet 192.168.x.x ara
```

---

## Docker ile Çalıştırma

### Backend Docker'da

```bash
# İmage oluştur
docker build -t smartcry-backend .

# Konteyner başlat
docker run -p 5000:5000 smartcry-backend
```

### Docker Compose ile

```bash
# Tüm servisleri başlat
docker-compose up

# Background'da çalıştır
docker-compose up -d

# Logları görüntüle
docker-compose logs -f

# Durdur
docker-compose down
```

---

## Başarılı Kurulumun İşaretleri

✅ **Backend:**
```
[INFO] Flask Server: http://localhost:5000
[DURUM] Kütüphaneler: Hazır
```

✅ **Flutter:**
```
Launching lib/main.dart on Android
```

✅ **Bağlantı:**
```
✓ Backend Bağlı
```

---

## Sonraki Adımlar

1. **ML Modeli Eğit:**
   - TensorFlow/Keras ile CNN modeli oluştur
   - Eğitim verilerini kullan
   - Model'i `.tflite` formatına dönüştür

2. **Veritabanı Kur:**
   - PostgreSQL/MySQL kurulum
   - `models.py` oluştur
   - SQLAlchemy entegrasyon

3. **Bildirim Sistemi:**
   - Firebase Cloud Messaging
   - Local push notifications
   - Backend entegrasyon

4. **ESP32 Entegrasyonu:**
   - Firmware yazılımı geliştir
   - I2S mikrofon kurulumu
   - Wi-Fi bağlantısı

5. **Production Hazırlıkları:**
   - HTTPS/SSL sertifikaları
   - Kimlik doğrulama (JWT)
   - API rate limiting
   - Logging ve monitoring

---

## Yardım ve Destek

**GitHub Issues:** Sorunları bildir
**Email:** proje@smartcry.com
**Discord:** SmartCry Community Server

---

**SmartCry © 2024** | Versiyon 1.0.0 | Son Güncelleme: Ocak 2026
