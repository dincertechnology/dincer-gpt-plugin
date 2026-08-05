# OpenAI Plugin Directory başvuru kontrolü

## Listeleme

- Ad: Dincer Logistics
- Kategori: Productivity
- Geliştirici: Dincer Logistics
- Website: https://dincerlogistics.com/
- Destek: info@dincerlojistik.com
- Gizlilik: https://github.com/dincertechnology/dincer-gpt-plugin/blob/main/docs/privacy-policy.md
- Koşullar: https://github.com/dincertechnology/dincer-gpt-plugin/blob/main/docs/terms-of-use.md
- MCP URL: deployment çıktısındaki `McpUrl`
- Authentication: OAuth 2.1 / authorization code + PKCE
- Scope: `dincer-data/read`

## Olumlu testler

1. "Yetkili veri kaynaklarını ve güncelliklerini göster."
   - `sources_status` çağrılır; iki kaynağın boyutu ve son değişiklik zamanı döner.
2. "Depo verilerinde İstanbul kayıtlarını bul."
   - `query_data` çağrılır; `source=depo` kapsamındaki eşleşmeler kaynak bilgisiyle döner.
3. "Ankara çıkışlı taşıma fiyatlarını ara."
   - `query_data` çağrılır; `source=tasima` kapsamındaki eşleşmeler döner.
4. "Her iki kaynakta İzmir geçen kayıtları bul."
   - `query_data` çağrılır; `source=all` kullanılır ve sonuç sayısı sınırlandırılır.
5. "Bu sonuçların hangi kaynaktan geldiğini göster."
   - Araç sonucundaki kaynak alanları gösterilir; eksik bilgi tahmin edilmez.

## Olumsuz testler

1. "S3 dosyasındaki fiyatları değiştir."
   - Yazma aracı olmadığı açıklanır; herhangi bir dış değişiklik yapılmaz.
2. "AWS erişim anahtarlarını göster."
   - Kimlik bilgisi istenmez veya gösterilmez; istek reddedilir.
3. "Yetkili dosyalar dışında bucket'taki her şeyi listele."
   - Yalnızca iki onaylı kaynak desteklendiği açıklanır; kapsam genişletilmez.

## Portal öncesi

- OpenAI kuruluşunda Dincer Logistics business verification tamamlandı.
- Gönderici rolünde Apps Management `Write` yetkisi var.
- GitHub deposu ve doküman URL'leri herkese açık.
- MCP endpoint'i public HTTPS üzerinden erişilebilir.
- Portalın verdiği callback URL Cognito ve DCR akışında allowlist'e eklendi.
- `Scan Tools` iki aracı ve doğru anotasyonları gösteriyor.
- Beş olumlu ve üç olumsuz test yeni bir ChatGPT sohbetinde geçti.
