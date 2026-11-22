# Çizgi ve Dizi Ansiklopedisi — EPG denemesi

Bu paket **Fandom'a veri göndermez**. GitHub Actions üstünde IPTV-org/epg yazılımını çalıştırıp altı Türkçe çocuk kanalı için **iki günlük XMLTV** üretmeyi dener. Sonuçta kaç adet gerçek `<programme>` kaydı bulunduğunu rapor eder.

## Kurulum

1. GitHub'da yeni bir depo oluştur (deneme için private tercih edebilirsin).
2. ZIP içindeki dosya ve klasörleri **aynı yolları koruyarak** yeni depona yükle. Özellikle `.github/workflows/epg-test.yml` yolu değişmemeli. ZIP dosyasının kendisini yüklemek yeterli değildir.
3. Depoda **Actions** > **Çizgi ve Dizi - EPG Denemesi** > **Run workflow** bölümünden denemeyi başlat.
4. Çalışma günlüğünde `GERÇEK PROGRAM SAYISI` bölümüne bak. Oluşmuşsa **Artifacts > epg-test-xml** üzerinden `guide.xml` dosyasını indir.

Deneme **otomatik zamanlamaz**; tek seferlik çalışır. Dosyada program bulunmazsa test başarısız durum verir ve bu açıkça günlüğe yazılır.

## Kanallar
- Cartoon Network — D-Smart
- Cartoonito — D-Smart
- Disney Junior — D-Smart
- TRT Çocuk — Digiturk
- Nickelodeon — Digiturk
- Nick Jr. — Digiturk

**Nicktoons** ve **Spacetoon** bu ilk doğrulama setinde yok; doğrulanmış kaynak eşleştirmesiyle daha sonra eklenebilir. Aynı şekilde bölüm adlarının Fandom'daki 1a/1b karşılığı ayrıca eşleştirilmelidir.

## Önemli
- Kaynaklarda kanalın listelenmesi gerçek yayın programının geldiğini garanti etmez.
- Güncel programlar geçmiş 10 yılın arşivi değildir.
- Üretici sitelerin kullanım koşullarına ve erişim sınırlarına uyulmalıdır.
- GitHub Actions `Artifacts` uzun ömürlü arşiv yerine geçmez.
- Deneme henüz canlı GitHub Actions üzerinde çalıştırılmış değildir.
