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

1. "Iğdır için kamyon fiyatı nedir?"
   - Gebze ve İzmir çıkışlı kamyon fiyatları tam TL olarak döner.
2. "Gebze çıkışlı Adana kamyon, kırkayak ve tır fiyatları nedir?"
   - Desteklenen üç araç tipi için kurumsal ve doğrudan yanıt döner.
3. "Adana kamyonet fiyatı nedir?"
   - Kaynak yapısına değinmeden fiyatlandırmanın kamyon, kırkayak ve tır için sunulduğu belirtilir.
4. "Tuzla deposunun fiyatlarını ve teklif şartlarını özetle."
   - Yalnızca Tuzla için fiyatlar ve ticari şartlar özetlenir.
5. "Parsiyel taşıma fiyatı nedir?"
   - Mevcut fiyatlandırmanın yalnızca FTL/komple kapsamda olduğu belirtilir.

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
