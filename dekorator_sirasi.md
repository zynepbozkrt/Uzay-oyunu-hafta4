# Dekoratör Sırası ve Fibonacci Çağrı Sayıları

Fibonacci fonksiyonu fib(20) için üç farklı dekoratör kullanımıyla çalıştırılmıştır.

## Elde edilen sonuçlar

| Kullanım şekli | Çağrı sayısı |
|---|---:|
| Yalnızca @say | 21891 |
| @say üstte, @lru_cache altta | 39 |
| @lru_cache üstte, @say altta | 21 |

## Sonuçların açıklaması

**1. Yalnızca @say**

Fibonacci fonksiyonu özyinelemeli olarak çalışır. Aynı değerler tekrar tekrar hesaplanır. Bu nedenle fonksiyonun çağrı sayısı 21891 olur.

**2. @say üstte, @lru_cache altta**

Bu kullanımda say dekoratörü, önbellek dekoratörünü sarar. Her çağrı sayaç tarafından görülür. Ancak önbellek sayesinde Fibonacci hesaplamaları tekrar yapılmaz. Çağrı sayısı 39 olur.

**3. @lru_cache üstte, @say altta**

Bu kullanımda önbellek dekoratörü, say dekoratörünü sarar. Önbellekte bulunan sonuçlar doğrudan döndürülür ve sayaç her çağrıda çalışmaz. Sayaç değerine fib.__wrapped__.cagri üzerinden ulaşılır. Çağrı sayısı 21 olur.

## Genel değerlendirme

Dekoratörlerin sırası fonksiyonun çalışma şeklini ve çağrı sayısını etkiler. Önbellekleme, aynı hesaplamaların tekrar yapılmasını önleyerek performansı artırır. Sayacın önbelleğe göre hangi konumda olduğu ise hangi çağrıların sayılacağını belirler.