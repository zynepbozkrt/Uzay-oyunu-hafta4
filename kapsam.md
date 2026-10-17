
# Python'da Değişken Kapsamı

## Örnek 1: Yerel değişken

### Tahminim
Fonksiyonun Merhaba! yazdıracağını tahmin ettim.

### Gerçek sonuç
Merhaba!

### Nedeni
mesaj değişkeni fonksiyonun içinde tanımlanmıştır
ve aynı fonksiyon içinde kullanılmıştır.

## Örnek 2: Global değişken

### Tahminim
Ekrana iki kez 100 yazdırılacağını tahmin ettim.

### Gerçek sonuç
100
100

### Nedeni
puan değişkeni fonksiyon dışında tanımlanmıştır.
Fonksiyon içinden okunabilir ve fonksiyon dışında
da kullanılabilir.

## Örnek 3: UnboundLocalError

### Tahminim
Kodun UnboundLocalError hatası vereceğini tahmin ettim.

### Gerçek sonuç
UnboundLocalError oluştu.

### Nedeni
Fonksiyon içinde puan değişkenine atama yapıldığı
için Python onu yerel değişken kabul eder.
puan = puan + 10 satırında değişkenin değeri
atanmadan önce okunmaya çalışılır.

### Düzeltme
Global değişkeni değiştirmek için global puan
kullanılabilir. Alternatif olarak fonksiyona
parametre verilip sonuç döndürülebilir.
