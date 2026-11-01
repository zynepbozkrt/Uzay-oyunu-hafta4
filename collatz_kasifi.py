
print("=== COLLATZ KAŞİFİ ===")

# GİRDİ VE DOĞRULAMA
while True:
    try:
        n = int(input("Başlangıç sayısı (n): "))

        if n > 0:
            break
        else:
            print("Lütfen pozitif bir tam sayı girin.")

    except ValueError:
        print("Hatalı giriş! Tam sayı girmelisiniz.")

# (A) COLLATZ ZİNCİRİ
gecici = n
adim = 0
en_yuksek = n

print(f"\nCollatz zinciri: {n}", end="")

while gecici != 1:

    # Tek satırlık koşullu ifade
    gecici = gecici // 2 if gecici % 2 == 0 else 3 * gecici + 1

    adim += 1

    if gecici > en_yuksek:
        en_yuksek = gecici

print(" → 1")
print(f"{n} → 1: {adim} adım, en yüksek değer {en_yuksek}")


# (B) EN UZUN COLLATZ ZİNCİRİNİ BUL
while True:
    try:
        ust_sinir = int(input("\nÜst sınır: "))

        if ust_sinir >= 1:
            break
        else:
            print("Üst sınır en az 1 olmalıdır.")

    except ValueError:
        print("Hatalı giriş! Tam sayı girmelisiniz.")


en_uzun_baslangic = 1
en_uzun_adim = 0

# Dış döngü: 1'den üst sınıra kadar sayılar
for baslangic in range(1, ust_sinir + 1):

    gecici = baslangic
    adim = 0

    # İç döngü: Her sayının Collatz zincirini hesapla
    while gecici != 1:

        gecici = gecici // 2 if gecici % 2 == 0 else 3 * gecici + 1

        adim += 1

    if adim > en_uzun_adim:
        en_uzun_adim = adim
        en_uzun_baslangic = baslangic


# ÇIKTI
print(
    f"1–{ust_sinir} arasında en uzun zincir: "
    f"{en_uzun_baslangic} ({en_uzun_adim} adım)"
)
