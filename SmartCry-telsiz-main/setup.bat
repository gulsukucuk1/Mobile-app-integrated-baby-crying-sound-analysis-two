@echo off
REM SmartCry - Hızlı Başlama Scripti (Windows)
REM Bu script hem Backend'i hem Flutter uygulamasını kurabilir

cls
echo.
echo **********************************************************
echo *                                                        *
echo *  SmartCry - Entegre Kurulum Asistanı                  *
echo *  Baby Cry Analysis System                              *
echo *                                                        *
echo **********************************************************
echo.

set /p choice="Yapılacak işlem seçin (1=Backend, 2=Flutter, 3=Her İkisi): "

if %choice%==1 goto backend
if %choice%==2 goto flutter
if %choice%==3 goto both
echo Geçersiz seçim!
goto end

:backend
echo.
echo [1] Backend Kurulumu Başlatılıyor...
echo.

REM Virtual environment kontrolü
if not exist venv (
    echo [*] Virtual environment oluşturuluyor...
    python -m venv venv
) else (
    echo [*] Virtual environment zaten var
)

REM Virtual environment'ı etkinleştir
call venv\Scripts\activate.bat

REM Bağımlılıkları yükle
echo [*] Bağımlılıklar yükleniyor...
pip install -r requirements.txt

REM API sunucusunu başlat
echo.
echo [✓] Backend başlatılıyor...
echo.
python app.py

goto end

:flutter
echo.
echo [2] Flutter Kurulumu Başlatılıyor...
echo.

REM Flutter proje dizinine git
cd flutter-app\babycry

REM Bağımlılıkları yükle
echo [*] Flutter bağımlılıkları yükleniyor...
flutter pub get

REM Emülatörü başlat veya cihaza yükle
echo.
echo [?] Emülatör mü fiziksel cihaz mı kullanacaksın?
set /p device="(e/fiziksel): "

if "%device%"=="e" (
    echo [*] Emülatör tespit ediliyor...
    flutter emulators --launch
    timeout /t 5
    flutter run
) else (
    echo [*] Fiziksel cihaza yükleniyor...
    flutter run
)

goto end

:both
echo.
echo [3] Tam Kurulum Başlatılıyor...
echo.

REM Backend
echo [ADIM 1/2] Backend Kurulumu...
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -r requirements.txt

REM Backend'i background'da başlat
echo [*] Backend başlatılıyor (arka planda)...
start cmd /k "python app.py"

REM Biraz bekle
timeout /t 5

REM Flutter
echo [ADIM 2/2] Flutter Kurulumu...
cd flutter-app\babycry
flutter pub get

echo.
echo [✓] Kurulum tamamlandı!
echo.
echo Adımlar:
echo 1. Backend penceresi açık kalmalı (http://localhost:5000)
echo 2. Flutter uygulaması yükleniyor...
echo.

flutter run

goto end

:end
echo.
echo **********************************************************
echo.
pause
