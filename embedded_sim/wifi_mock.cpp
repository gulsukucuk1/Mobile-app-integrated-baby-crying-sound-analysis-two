#include "wifi_mock.h"
#include <iostream>

void send_result_wifi_mock(const std::string& result) {
    std::cout << "[Wi-Fi MOCK] Sonuç gönderildi: "
              << result << std::endl;
}
