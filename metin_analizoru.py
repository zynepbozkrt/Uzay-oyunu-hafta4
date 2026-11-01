
print("=== METİN ANALİZÖRÜ ===")

# GİRDİ
cumle = input("Bir cümle girin: ")

# Sayaçları başlat
harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0

# Kelime saymak için bayrak
kelime_icinde = False

# Palindrom kontrolü için metin
temiz_metin = ""

sesliler = "aeıioöuü"

# TEK FOR DÖNGÜSÜ
for karakter in cumle:

    kucuk = karakter.lower()

    # Harf kontrolü
    if karakter.isalpha():
        harf_sayisi += 1
        temiz_metin += kucuk

        if kucuk in sesliler:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1

    # Rakam kontrolü
    elif karakter.isdigit():
        rakam_sayisi += 1

    # Kelime kontrolü: Boşluktan kelimeye geçiş
    if karakter.isspace():
        kelime_icinde = False

    elif not kelime_icinde:
        kelime_sayisi += 1
        kelime_icinde = True

# Cümleyi ters çevir
ters = cumle[::-1]

# Palindrom kontrolü
if temiz_metin == temiz_metin[::-1]:
    sonuc = "Palindrom"
else:
    sonuc = "Palindrom değil"

# ÇIKTI
print("\n=== ANALİZ SONUCU ===")
print(f"Harf: {harf_sayisi}")
print(f"Sesli: {sesli_sayisi}")
print(f"Sessiz: {sessiz_sayisi}")
print(f"Rakam: {rakam_sayisi}")
print(f"Kelime: {kelime_sayisi}")
print(f"Ters: {ters}")
print(sonuc)
