import 'package:flutter_test/flutter_test.dart';
import 'package:babycry/main.dart'; // Proje adının babycry olduğundan emin ol

void main() {
  testWidgets('Uygulama baslatma ve arayuz dogrulama testi', (
    WidgetTester tester,
  ) async {
    // 1. Uygulamayi baslat (main.dart'taki BebekTelsiziApp sınıfını kullanır)
    await tester.pumpWidget(const BebekTelsiziApp());

    // 2. Dashboard ekraninin dogru baslikla acilip acilmadigini kontrol et
    // Arastirma onerisindeki "Bebek Analiz Paneli" basligini arar
    expect(find.text('Bebek Analiz Paneli'), findsOneWidget);

    // 3. TinyML analiz kategorilerinin ekranda olup olmadigini dogrula
    // Arastirma onerisi Hedef 2'de belirtilen kategoriler [cite: 84]
    expect(find.text('Açlık'), findsOneWidget);
    expect(find.text('Uykusuzluk'), findsOneWidget);
    expect(find.text('Rahatsızlık'), findsOneWidget);

    // 4. Sensor verilerinin (Hareketlilik Skoru) gorunurlugunu kontrol et [cite: 88]
    expect(find.text('Hareketlilik Skoru'), findsOneWidget);
    expect(find.text('Düşük'), findsOneWidget);
  });
}
