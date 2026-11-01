
print("=== T.C. KİMLİK NUMARASI DOĞRULAMA ===")

# GİRDİ
numara = input("T.C. kimlik no: ")

# DOĞRULA: Biçim kontrolü
if len(numara) != 11 or not numara.isdigit() or numara[0] == "0":
    print("GEÇERSİZ: Numara biçimi hatalı.")

else:
    # Toplamları başlat
    tek = 0
    cift = 0

    # İlk 9 haneyi tek döngüyle incele
    for indeks in range(9):

        rakam = int(numara[indeks])

        if indeks % 2 == 0:
            tek += rakam
        else:
            cift += rakam

    # Kontrol hanelerini hesapla
    h10 = (7 * tek - cift) % 10
    h11 = (tek + cift + h10) % 10

    # Numaradaki son iki haneyle karşılaştır
    if h10 == int(numara[9]) and h11 == int(numara[10]):
        sonuc = "GEÇERLİ"
    else:
        sonuc = "GEÇERSİZ"

    # ÇIKTI
    print(f"Tek: {tek}")
    print(f"Çift: {cift}")
    print(f"10. hane: {h10}")
    print(f"11. hane: {h11}")
    print(f"→ {sonuc}")
