#!/bin/bash
# SmartCry - Hızlı Başlama Scripti (macOS/Linux)

clear

echo ""
echo "**********************************************************"
echo "*                                                        *"
echo "*  SmartCry - Entegre Kurulum Asistanı                  *"
echo "*  Baby Cry Analysis System                              *"
echo "*                                                        *"
echo "**********************************************************"
echo ""

read -p "Yapılacak işlem seçin (1=Backend, 2=Flutter, 3=Her İkisi): " choice

case $choice in
    1)
        setup_backend
        ;;
    2)
        setup_flutter
        ;;
    3)
        setup_all
        ;;
    *)
        echo "Geçersiz seçim!"
        exit 1
        ;;
esac

setup_backend() {
    echo ""
    echo "[1] Backend Kurulumu Başlatılıyor..."
    echo ""

    # Virtual environment kontrolü
    if [ ! -d "venv" ]; then
        echo "[*] Virtual environment oluşturuluyor..."
        python3 -m venv venv
    else
        echo "[*] Virtual environment zaten var"
    fi

    # Virtual environment'ı etkinleştir
    source venv/bin/activate

    # Bağımlılıkları yükle
    echo "[*] Bağımlılıklar yükleniyor..."
    pip install -r requirements.txt

    # API sunucusunu başlat
    echo ""
    echo "[✓] Backend başlatılıyor..."
    echo ""
    python app.py
}

setup_flutter() {
    echo ""
    echo "[2] Flutter Kurulumu Başlatılıyor..."
    echo ""

    # Flutter proje dizinine git
    cd flutter-app/babycry

    # Bağımlılıkları yükle
    echo "[*] Flutter bağımlılıkları yükleniyor..."
    flutter pub get

    # Emülatörü başlat veya cihaza yükle
    echo ""
    read -p "[?] Emülatör mü (e) fiziksel cihaz mı (f) kullanacaksın? " device

    if [ "$device" == "e" ]; then
        echo "[*] Emülatör tespit ediliyor..."
        flutter emulators --launch
        sleep 5
        flutter run
    else
        echo "[*] Fiziksel cihaza yükleniyor..."
        flutter run
    fi
}

setup_all() {
    echo ""
    echo "[3] Tam Kurulum Başlatılıyor..."
    echo ""

    # Backend
    echo "[ADIM 1/2] Backend Kurulumu..."
    if [ ! -d "venv" ]; then
        python3 -m venv venv
    fi
    source venv/bin/activate
    pip install -r requirements.txt

    # Backend'i background'da başlat
    echo "[*] Backend başlatılıyor (arka planda)..."
    nohup python app.py > backend.log 2>&1 &
    BACKEND_PID=$!

    # Biraz bekle
    sleep 5

    # Flutter
    echo "[ADIM 2/2] Flutter Kurulumu..."
    cd flutter-app/babycry
    flutter pub get

    echo ""
    echo "[✓] Kurulum tamamlandı!"
    echo ""
    echo "Adımlar:"
    echo "1. Backend çalışıyor (PID: $BACKEND_PID)"
    echo "2. Backend log: ../backend.log"
    echo "3. Flutter uygulaması yükleniyor..."
    echo ""

    flutter run
}

# Setup'u çalıştır
if [ "$choice" == "1" ]; then
    setup_backend
elif [ "$choice" == "2" ]; then
    setup_flutter
elif [ "$choice" == "3" ]; then
    setup_all
fi
