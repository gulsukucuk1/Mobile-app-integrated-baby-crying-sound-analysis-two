"""
SmartCry - Backend Test Modülü
API endpoint'lerinin test edilmesi
"""

import requests
import json
import sys
import os

# Test ayarları
BASE_URL = "http://localhost:5000/api"
TIMEOUT = 10

class Colors:
    """Terminal renkleri"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_header(text):
    """Başlık yazdır"""
    print(f"\n{Colors.BLUE}{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}{Colors.END}\n")

def print_success(text):
    """Başarı mesajı"""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    """Hata mesajı"""
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_info(text):
    """Bilgi mesajı"""
    print(f"{Colors.YELLOW}ℹ {text}{Colors.END}")

def test_health_check():
    """Sağlık kontrolü testi"""
    print_header("1. Sağlık Kontrolü Testi")
    
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=TIMEOUT)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Backend sağlıklı: {data['message']}")
            print_info(f"Versiyon: {data['version']}")
            return True
        else:
            print_error(f"HTTP {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print_error("Backend'e bağlanılamadı. Sunucunun çalışıp çalışmadığını kontrol et.")
        print_error(f"URL: {BASE_URL}")
        return False
    except Exception as e:
        print_error(f"Hata: {str(e)}")
        return False

def test_categories():
    """Kategori bilgisi testi"""
    print_header("2. Kategori Bilgisi Testi")
    
    try:
        response = requests.get(f"{BASE_URL}/categories", timeout=TIMEOUT)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Toplam kategori: {data['total']}")
            
            for key, value in data['categories'].items():
                print(f"  • {key}: {value}")
            
            return True
        else:
            print_error(f"HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print_error(f"Hata: {str(e)}")
        return False

def test_api_info():
    """API bilgisi testi"""
    print_header("3. API Bilgisi Testi")
    
    try:
        response = requests.get(f"{BASE_URL}/info", timeout=TIMEOUT)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"API Adı: {data['name']}")
            print_info(f"Versiyon: {data['version']}")
            print_info(f"Maksimum Dosya Boyutu: {data['max_file_size']}")
            print_info(f"Desteklenen Formatlar: {', '.join(data['supported_formats'])}")
            
            print("\nEndpointler:")
            for key, value in data['endpoints'].items():
                print(f"  • {key}: {value}")
            
            return True
        else:
            print_error(f"HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print_error(f"Hata: {str(e)}")
        return False

def test_mel_analysis(audio_path):
    """Mel-Spektrogram analizi testi"""
    print_header("4. Mel-Spektrogram Analizi Testi")
    
    if not os.path.exists(audio_path):
        print_error(f"Ses dosyası bulunamadı: {audio_path}")
        print_info("Test için örnek bir ses dosyasını kullan")
        return False
    
    try:
        with open(audio_path, 'rb') as f:
            files = {'audio': f}
            response = requests.post(
                f"{BASE_URL}/analyze/mel",
                files=files,
                timeout=TIMEOUT
            )
        
        if response.status_code == 200:
            data = response.json()
            print_success("Mel-Spektrogram başarıyla çıkarıldı")
            print_info(f"Dosya: {data['filename']}")
            print_info(f"Şekil: {data['features']['shape']}")
            print_info(f"Veri Tipi: {data['features']['dtype']}")
            print_info(f"Min: {data['features']['min']:.4f}")
            print_info(f"Max: {data['features']['max']:.4f}")
            print_info(f"Ortalama: {data['features']['mean']:.4f}")
            print_info(f"Std Dev: {data['features']['std']:.4f}")
            
            return True
        elif response.status_code == 400:
            error = response.json()
            print_error(f"İstek Hatası: {error['error']}")
            return False
        else:
            print_error(f"HTTP {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print_error(f"Hata: {str(e)}")
        return False

def test_mfcc_analysis(audio_path):
    """MFCC analizi testi"""
    print_header("5. MFCC Analizi Testi")
    
    if not os.path.exists(audio_path):
        print_error(f"Ses dosyası bulunamadı: {audio_path}")
        print_info("Test için örnek bir ses dosyasını kullan")
        return False
    
    try:
        with open(audio_path, 'rb') as f:
            files = {'audio': f}
            response = requests.post(
                f"{BASE_URL}/analyze/mfcc",
                files=files,
                timeout=TIMEOUT
            )
        
        if response.status_code == 200:
            data = response.json()
            print_success("MFCC başarıyla çıkarıldı")
            print_info(f"Dosya: {data['filename']}")
            print_info(f"Şekil: {data['features']['shape']}")
            print_info(f"Veri Tipi: {data['features']['dtype']}")
            print_info(f"Min: {data['features']['min']:.4f}")
            print_info(f"Max: {data['features']['max']:.4f}")
            print_info(f"Ortalama: {data['features']['mean']:.4f}")
            print_info(f"Std Dev: {data['features']['std']:.4f}")
            
            return True
        elif response.status_code == 400:
            error = response.json()
            print_error(f"İstek Hatası: {error['error']}")
            return False
        else:
            print_error(f"HTTP {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print_error(f"Hata: {str(e)}")
        return False

def run_all_tests(audio_path=None):
    """Tüm testleri çalıştır"""
    print("\n" + "*"*60)
    print("*" + " "*58 + "*")
    print("*  SmartCry Backend API - Test Suite           *")
    print("*" + " "*58 + "*")
    print("*"*60)
    
    results = []
    
    # Temel testler
    results.append(("Sağlık Kontrolü", test_health_check()))
    
    if not results[-1][1]:
        print_error("\nBackend çalışmıyor. Diğer testleri atla.")
        return results
    
    results.append(("Kategori Bilgisi", test_categories()))
    results.append(("API Bilgisi", test_api_info()))
    
    # Ses dosyası testleri (eğer dosya varsa)
    if audio_path and os.path.exists(audio_path):
        results.append(("Mel-Spektrogram Analizi", test_mel_analysis(audio_path)))
        results.append(("MFCC Analizi", test_mfcc_analysis(audio_path)))
    else:
        if audio_path:
            print_error(f"\nSes dosyası bulunamadı: {audio_path}")
        print_info("Ses dosyası testi atlandı")
    
    # Özet
    print_header("Test Özeti")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"Geçilen Testler: {Colors.GREEN}{passed}/{total}{Colors.END}")
    
    for name, result in results:
        status = f"{Colors.GREEN}✓{Colors.END}" if result else f"{Colors.RED}✗{Colors.END}"
        print(f"{status} {name}")
    
    if passed == total:
        print(f"\n{Colors.GREEN}✓ Tüm testler geçti!{Colors.END}")
    else:
        print(f"\n{Colors.YELLOW}⚠ Bazı testler başarısız oldu.{Colors.END}")

if __name__ == "__main__":
    # Ses dosyası parametresi (opsiyonel)
    audio_file = sys.argv[1] if len(sys.argv) > 1 else None
    
    print_info(f"Backend URL: {BASE_URL}")
    
    if audio_file:
        print_info(f"Ses dosyası: {audio_file}")
    
    run_all_tests(audio_file)
