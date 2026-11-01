
import math

print("=== ÜÇGEN ANALİZÖRÜ ===")

# GİRDİ: Üç kenarı kullanıcıdan al
sayac = 0

while sayac < 3:
    try:
        if sayac == 0:
            a = float(input("Birinci kenarı girin: "))
        elif sayac == 1:
            b = float(input("İkinci kenarı girin: "))
        else:
            c = float(input("Üçüncü kenarı girin: "))

        sayac += 1

    except ValueError:
        print("Hatalı giriş! Lütfen sayısal bir değer girin.")
        continue


# DOĞRULA: Kenarların pozitif olup olmadığını kontrol et
pozitif = True

for kenar in (a, b, c):
    if kenar <= 0:
        print("Hata: Üçgenin kenarları pozitif olmalıdır.")
        pozitif = False
        break
    else:
        continue


if pozitif:

    # Üçgen eşitsizliğini kontrol et
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Hata: Bu kenarlarla üçgen oluşturulamaz.")

    else:
        # İŞLE: En uzun kenarı belirle
        if a >= b and a >= c:
            en_uzun = a
            diger1 = b
            diger2 = c

        elif b >= a and b >= c:
            en_uzun = b
            diger1 = a
            diger2 = c

        else:
            en_uzun = c
            diger1 = a
            diger2 = b

        # Üçgeni kenarlarına göre sınıflandır
        if math.isclose(a, b) and math.isclose(b, c):
            kenar_turu = "Eşkenar"

        elif (math.isclose(a, b) or
              math.isclose(a, c) or
              math.isclose(b, c)):
            kenar_turu = "İkizkenar"

        else:
            kenar_turu = "Çeşitkenar"

        # Çevre ve yarı çevre
        cevre = a + b + c
        u = cevre / 2

        # Heron formülü ile alan
        alan = math.sqrt(
            u * (u - a) * (u - b) * (u - c)
        )

        # En büyük açıyı kosinüs teoremi ile bul
        kosinus = (
            diger1 ** 2 + diger2 ** 2 - en_uzun ** 2
        ) / (2 * diger1 * diger2)

        # Yuvarlama kaynaklı küçük taşmaları engelle
        kosinus = max(-1, min(1, kosinus))

        aci = math.degrees(math.acos(kosinus))

        # En büyük açıya göre sınıflandır
        if math.isclose(aci, 90, abs_tol=1e-9):
            aci_turu = "Dik açılı"

        elif aci > 90:
            aci_turu = "Geniş açılı"

        else:
            aci_turu = "Dar açılı"

        # ÇIKTI
        print("\n=== ÜÇGEN ANALİZ SONUCU ===")
        print(f"Tür: {kenar_turu}, {aci_turu}")
        print(f"Çevre: {cevre:.2f}")
        print(f"Alan: {alan:.2f}")
        print(f"En büyük açı: {aci:.2f}°")
