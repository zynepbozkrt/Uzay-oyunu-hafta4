
print("=== ADAM ASMACA ===")

gizli_kelime = "KOŞUL"
tahminler = ""
hata = 0
maksimum_hata = 6

while hata < maksimum_hata:
    gorunen = ""

    for harf in gizli_kelime:
        if harf in tahminler:
            gorunen += harf + " "
        else:
            gorunen += "_ "

    print(f"\n{gorunen} (hata: {hata}/{maksimum_hata})")

    if "_" not in gorunen:
        print("Kazandınız!")
        break

    harf = input("Harf: ").strip()

    if len(harf) != 1 or not harf.isalpha():
        print("Lütfen tek bir harf girin.")
        continue

    harf = harf.upper()

    if harf in tahminler:
        print("Bu harfi zaten denediniz.")
        continue

    tahminler += harf

    if harf not in gizli_kelime:
        hata += 1

else:
    print(f"\nKaybettiniz! Gizli kelime: {gizli_kelime}")
