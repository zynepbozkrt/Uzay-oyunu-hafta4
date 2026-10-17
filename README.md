# Hafta 4 Lab Ödevi

**Ad Soyad:** ZEYNEP BOZKURT
**Öğrenci Numarası:** 20253004020 
**Bölüm:** BİLİŞİM SİSTEMLERİ VE TEKNOLOJİLERİ

## Ödev Hakkında

Bu proje, Python programlama dersi kapsamında hazırlanan Hafta 4 Lab Ödevi çalışmalarını içerir.
# Hafta 4 Python Ödevi

## Görev 1 — Fibonacci üreteci

Fibonacci dizisini üreten bir generator yazıldı.
`next()`, `itertools.islice` ve `itertools.takewhile` ile test edildi.

## Görev 2 — Yakıt göstergesi

Kalan yakıtı her yolculukta azaltan bir generator yazıldı.
Yakıt bittiğinde oyunun sona ermesi sağlandı.

## Görev 3 — Seyir kayıtları

`satirlari_oku()`, `ayristir()` ve `uzun_yolculuklar()` fonksiyonları yazıldı.
Testler başarılı oldu.


## Görev 4 — Rota sayacı ve önbellek

- Adım sayısı: 20
- Önbelleksiz sonuç: 835841
- Önbelleksiz süre: 0.247921 saniye
- Önbellekli sonuç: 835841
- Önbellekli süre: 0.000093 saniye
- Önbellek bilgisi: `CacheInfo(hits=73, misses=97, maxsize=None, currsize=97)`

**Değerlendirme:** Önbellekli ve önbelleksiz hesaplamalar aynı sonucu verdi. Önbellekli hesaplama bu çalıştırmada yaklaşık 2.666 kat daha hızlıydı. `lru_cache`, daha önce hesaplanan alt problemlerin sonuçlarını saklayarak tekrar hesaplanmalarını önler.
