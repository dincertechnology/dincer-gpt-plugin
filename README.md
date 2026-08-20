# Dincer Logistics ChatGPT Plugin

ChatGPT ve Codex için Dincer Logistics'in yetkili iki Excel veri kaynağında
salt okunur arama yapan, OAuth korumalı MCP eklentisi.

## Yapı

```text
.agents/plugins/marketplace.json
plugins/s3-knowledge-assistant/
├── .codex-plugin/plugin.json
├── .mcp.json
├── assets/
├── config/
└── skills/
infra/
├── template.yaml
└── backend/
    ├── app.py
    ├── excel_reader.py
    ├── oauth_dcr.py
```

## Güvenlik

- Lambda rolü yalnızca deployment sırasında belirtilen iki S3 nesnesini okur.
- Erişim anahtarı, secret key veya kullanıcı parolası repoda tutulmaz.
- MCP araçları `readOnlyHint: true` olarak işaretlidir.
- Kullanıcılar Cognito'nun yönetilen kayıt ekranında kendi hesaplarını açar.
- API Gateway geçerli Cognito JWT'si ve `dincer-data/read` scope'u olmadan
  MCP araçlarına erişim vermez.

## ChatGPT bağlantısı

1. ChatGPT web'de **Settings → Security and login → Developer mode** açılır.
2. Plugins sayfasında `+` seçilir ve MCP endpoint'i `/mcp` yolu ile eklenir.
3. ChatGPT'nin gösterdiği `https://chatgpt.com/connector/oauth/{callback_id}`
   callback URL'si kopyalanır.
4. [infra/README.md](infra/README.md) izlenerek stack bu callback URL ile deploy edilir.
5. Deployment çıktısındaki `McpUrl`,
   `plugins/s3-knowledge-assistant/.mcp.json` içindeki URL ile değiştirilir.
6. ChatGPT'de **Scan Tools** çalıştırılır ve Cognito kayıt/giriş akışı tamamlanır.

Beklenen araçlar:

- `sources_status`
- `query_data`

## Yerel marketplace testi

```powershell
codex plugin marketplace add "C:\Dincer GPT Plugin"
```

ChatGPT masaüstü uygulaması yeniden başlatıldıktan sonra Plugins Directory
içindeki **Dincer Logistics** kaynağından eklenti kurulabilir.

Manifest doğrulaması:

```powershell
python "C:\Users\<user>\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" `
  "C:\Dincer GPT Plugin\plugins\s3-knowledge-assistant"
```

## Public Plugin Directory başvurusu

Kod ve MCP hazırlandıktan sonra
[OpenAI Plugin Submission Portal](https://platform.openai.com/apps-manage)
üzerinden başvuru yapılır. Başvuru için:

- doğrulanmış Dincer Logistics kuruluş kimliği,
- Apps Management `Write` yetkisi,
- çalışan public HTTPS MCP endpoint'i,
- yayınlanmış gizlilik ve kullanım koşulları URL'leri,
- beş olumlu ve üç olumsuz test senaryosu

gereklidir. Nihai yayın OpenAI inceleme onayına bağlıdır.

## Örnekler

- "Güncel hizmet fiyatını paylaş."
- "Belirttiğim lokasyon için teklif şartlarını özetle."
- "Uygun seçenekleri karşılaştır."

## Gizlilik ve destek

- [Dincer Logistics Gizlilik ve Çerez Politikası](https://dincerlogistics.com/gizlilik-ve-cerez-politikasi/)
- [Connector veri işleme bildirimi](docs/privacy-policy.md)
- [Kullanım koşulları](docs/terms-of-use.md)
- [dincerlogistics.com](https://dincerlogistics.com/)
- [info@dincerlojistik.com](mailto:info@dincerlojistik.com)
