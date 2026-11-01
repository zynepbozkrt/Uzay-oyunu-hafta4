
print("=== LUHN KONTROL HANESİ ===")

numara = "453914880343646"

for kontrol in range(10):
    tam_numara = numara + str(kontrol)
    ters_numara = tam_numara[::-1]

    toplam = 0

    for indeks in range(len(ters_numara)):
        rakam = int(ters_numara[indeks])

        if indeks % 2 == 1:
            rakam *= 2

            if rakam > 9:
                rakam -= 9

        toplam += rakam

    if toplam % 10 == 0:
        print(f"Kontrol hanesi: {kontrol}")
        print(f"Geçerli numara: {tam_numara}")
        break
