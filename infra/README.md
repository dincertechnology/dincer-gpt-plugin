# Güvenli AWS kurulumu

Bu stack şu kaynakları oluşturur:

- Cognito self-service kullanıcı kaydı,
- OAuth authorization code + PKCE,
- Cognito JWT ve `dincer-data/read` scope'u ile korunan HTTP API,
- iki Excel'i salt okunur kullanan stateless MCP Lambda,
- yalnızca deployment sırasında verilen iki tam S3 nesnesine `s3:GetObject`
  veren otomatik oluşturulmuş Lambda rolü.

## Yönetici kurulumu

Ön koşullar: AWS SAM CLI ve şirket yöneticisinin oluşturduğu bir CloudFormation
yürütme rolü. Bu rol yalnızca bu stack'in Lambda, API Gateway, log ve Lambda
  yürütme rolü ve Cognito kaynaklarını yönetebilmelidir. Kişisel kullanıcınıza geniş
yetki vermek yerine yalnızca:

- bu stack için gerekli CloudFormation işlemleri,
- yalnızca bu yürütme rolü için `iam:PassRole`

verilmesi önerilir. Rol ARN'ini deployment sırasında kullanın:

```powershell
cd infra
sam build
sam deploy --guided --role-arn <CLOUDFORMATION_EXECUTION_ROLE_ARN>
```

Yürütme rolünün güven ilişkisinde yalnızca `cloudformation.amazonaws.com`
servisi bulunmalıdır.

`CognitoDomainPrefix` aynı AWS region içinde benzersiz, küçük harfli bir ad
olmalıdır.

`sam deploy --guided` sırasında `DataBucketName`, `DepotObjectKey`,
`TransportObjectKey` ve ChatGPT'nin verdiği `ChatGptCallbackUrl` değerlerini
girin. Gerçek S3 değerlerini tracked
dosyalara, deployment komutlarına veya shell geçmişine yazmayın.

Deployment çıktılarındaki şu değerleri kaydedin:

- `McpUrl`
- `CognitoClientId`
- `CognitoMetadataUrl`
- `CognitoUserPoolId`

Bunların hiçbiri secret değildir; Cognito client public PKCE client'ıdır.

## Kullanıcı kaydı

Kullanıcı ilk bağlantıda Cognito'nun yönetilen ekranında e-posta adresiyle kayıt
olur ve doğrulama kodunu girer. Kullanıcıya IAM user, access key, AWS console
erişimi veya S3 yetkisi verilmez.

Kayıt belirli bir e-posta alan adıyla sınırlandırılmaz; doğrulayabildiği bir
e-posta adresi olan kullanıcı kayıt olabilir. Her kullanıcı gerçek veri arama
aracını UTC günü başına en fazla 20 kez çağırabilir. Kaynak ve güncellik bilgisi
sorguları bu kotaya dahil değildir.

## ChatGPT plugin bağlantısı

Canlı endpoint, ChatGPT Developer mode içinde özel MCP bağlantısı olarak eklenir.
OAuth client kimliği public client'tır ve PKCE kullanır. ChatGPT'nin ürettiği
callback URL Cognito app client allowlist'inde bulunmalıdır.

İlk kurulum için kişisel kullanıcıya verilen bootstrap policy deployment
tamamlandıktan sonra kaldırılabilir. Çalışma anında bu kullanıcı kullanılmaz.

## KMS notu

İki nesne müşteri yönetimli KMS anahtarıyla şifreliyse Lambda yürütme rolüne
yalnızca ilgili key ARN'i için `kms:Decrypt` ekleyin. SSE-S3 veya AWS-managed
S3 anahtarında bu ek izin gerekmez.
