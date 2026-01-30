"""
SmartCry - Backend API
Bebek ağlaması analiz sistemi
Flask API - AI modüllerini entegre eder
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import numpy as np
from werkzeug.utils import secure_filename
import librosa

# AI modüllerini import et
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'AI'))
from feature_extractor import extract_mfcc_cnn
from mel_extractor import extract_mel_cnn

# Flask uygulamasını başlat
app = Flask(__name__)
CORS(app)  # Cross-Origin Resource Sharing etkinleştir

# Ayarlar
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg', 'm4a'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Dosya uzantısı kontrol et
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Kategoriler ve açıklamalar
CATEGORIES = {
    'hungry': '🍽️ Açlık',
    'burping': '🤢 Gaz çıkarma',
    'discomfort': '😖 Rahatsızlık',
    'belly_pain': '🤕 Karın ağrısı',
    'tired': '😴 Yorgunluk'
}

@app.route('/api/health', methods=['GET'])
def health_check():
    """Sistem sağlık kontrolü"""
    return jsonify({
        'status': 'healthy',
        'message': 'SmartCry Backend aktif',
        'version': '1.0.0'
    }), 200

@app.route('/api/analyze/mel', methods=['POST'])
def analyze_mel():
    """
    Mel-Spektrogram ile analiz
    POST /api/analyze/mel
    Body: form-data with 'audio' file
    """
    try:
        # Dosya kontrolü
        if 'audio' not in request.files:
            return jsonify({'error': 'Ses dosyası yüklenmedi'}), 400
        
        file = request.files['audio']
        
        if file.filename == '':
            return jsonify({'error': 'Dosya seçilmedi'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'error': f'İzin verilen dosya türleri: {", ".join(ALLOWED_EXTENSIONS)}'
            }), 400
        
        # Dosyayı kaydet
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Mel-Spektrogram özellikleri çıkar
        mel_features = extract_mel_cnn(filepath)
        
        # Sonuç
        result = {
            'success': True,
            'features': {
                'shape': list(mel_features.shape),
                'dtype': str(mel_features.dtype),
                'min': float(np.min(mel_features)),
                'max': float(np.max(mel_features)),
                'mean': float(np.mean(mel_features)),
                'std': float(np.std(mel_features))
            },
            'filename': filename,
            'message': 'Mel-Spektrogram başarıyla çıkarıldı'
        }
        
        # Geçici dosyayı sil
        os.remove(filepath)
        
        return jsonify(result), 200
    
    except FileNotFoundError as e:
        return jsonify({'error': f'Dosya hatası: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Veri hatası: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Beklenmeyen hata: {str(e)}'}), 500

@app.route('/api/analyze/mfcc', methods=['POST'])
def analyze_mfcc():
    """
    MFCC (Mel-Frequency Cepstral Coefficients) ile analiz
    POST /api/analyze/mfcc
    Body: form-data with 'audio' file
    """
    try:
        # Dosya kontrolü
        if 'audio' not in request.files:
            return jsonify({'error': 'Ses dosyası yüklenmedi'}), 400
        
        file = request.files['audio']
        
        if file.filename == '':
            return jsonify({'error': 'Dosya seçilmedi'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'error': f'İzin verilen dosya türleri: {", ".join(ALLOWED_EXTENSIONS)}'
            }), 400
        
        # Dosyayı kaydet
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # MFCC özellikleri çıkar
        mfcc_features = extract_mfcc_cnn(filepath)
        
        # Sonuç
        result = {
            'success': True,
            'features': {
                'shape': list(mfcc_features.shape),
                'dtype': str(mfcc_features.dtype),
                'min': float(np.min(mfcc_features)),
                'max': float(np.max(mfcc_features)),
                'mean': float(np.mean(mfcc_features)),
                'std': float(np.std(mfcc_features))
            },
            'filename': filename,
            'message': 'MFCC başarıyla çıkarıldı'
        }
        
        # Geçici dosyayı sil
        os.remove(filepath)
        
        return jsonify(result), 200
    
    except FileNotFoundError as e:
        return jsonify({'error': f'Dosya hatası: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Veri hatası: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Beklenmeyen hata: {str(e)}'}), 500

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Bebek ağlaması kategorilerini listele"""
    return jsonify({
        'categories': CATEGORIES,
        'total': len(CATEGORIES)
    }), 200

@app.route('/api/info', methods=['GET'])
def get_info():
    """Sistem bilgileri"""
    return jsonify({
        'name': 'SmartCry AI Backend',
        'version': '1.0.0',
        'description': 'Bebek ağlaması analiz sistemi',
        'endpoints': {
            'health': 'GET /api/health',
            'analyze_mel': 'POST /api/analyze/mel',
            'analyze_mfcc': 'POST /api/analyze/mfcc',
            'categories': 'GET /api/categories',
            'info': 'GET /api/info'
        },
        'supported_formats': list(ALLOWED_EXTENSIONS),
        'max_file_size': f'{MAX_FILE_SIZE // (1024*1024)} MB'
    }), 200

@app.errorhandler(413)
def request_entity_too_large(error):
    """Dosya boyutu limiti aşıldı"""
    return jsonify({
        'error': f'Dosya çok büyük. Maksimum: {MAX_FILE_SIZE // (1024*1024)} MB'
    }), 413

@app.errorhandler(404)
def not_found(error):
    """Sayfa bulunamadı"""
    return jsonify({'error': 'Endpoint bulunamadı'}), 404

@app.errorhandler(500)
def internal_error(error):
    """İç server hatası"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("\n" + "*"*50)
    print("*" + " "*48 + "*")
    print("*  SmartCry Backend API - Başlatılıyor...       *")
    print("*" + " "*48 + "*")
    print("*"*50)
    print("[INFO] Flask Server: http://localhost:5000")
    print("[INFO] CORS: Etkinleştirildi (Flutter entegrasyonu)")
    print("[INFO] Modüller: Feature Extractor, Mel Extractor")
    print("-"*50)
    app.run(debug=True, host='0.0.0.0', port=5000)
