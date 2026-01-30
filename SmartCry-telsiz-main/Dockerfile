FROM python:3.10-slim

# Çalışma dizini
WORKDIR /app

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    libsndfile1-dev \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıkları
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı kopyala
COPY . .

# Port 5000'i expose et
EXPOSE 5000

# Uploads dizinini oluştur
RUN mkdir -p uploads

# SmartCry Logo
RUN echo "\n" && \
    echo "**************************************************" && \
    echo "*" && \
    echo "*  SmartCry AI Backend - Docker Image" && \
    echo "*" && \
    echo "**************************************************" && \
    echo ""

# Uygulamayı başlat
CMD ["python", "app.py"]
