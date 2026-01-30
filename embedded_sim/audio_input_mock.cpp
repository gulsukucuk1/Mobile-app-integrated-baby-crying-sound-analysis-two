#include "audio_input_mock.h"
#include <iostream>

std::vector<float> read_audio_mock(const char* wav_path) {
    std::cout << "[MOCK] WAV dosyasından ses okunuyor: "
              << wav_path << std::endl;

    std::vector<float> audio(16000, 0.01f);
    return audio;
}
