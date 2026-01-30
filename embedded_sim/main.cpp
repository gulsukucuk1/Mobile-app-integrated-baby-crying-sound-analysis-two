#include <iostream>
#include <thread>
#include <chrono>

#include "audio_input_mock.h"
#include "tinyml_inference.h"
#include "wifi_mock.h"

int main() {

    std::cout << "=== SmartCry ESP32 MOCK BAŞLADI ===" << std::endl;

    while (true) {

        auto audio = read_audio_mock("sample.wav");
        std::string result = run_tinyml_inference(audio);
        send_result_wifi_mock(result);

        std::this_thread::sleep_for(
            std::chrono::seconds(3)
        );
    }

    return 0;
}
