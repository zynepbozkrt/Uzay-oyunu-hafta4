
def gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler):
    satirlar = [f"[{oncelik.upper()}] {baslik}"]

    for numara, adim in enumerate(adimlar, start=1):
        satirlar.append(f"{numara}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f"{anahtar}: {deger}")

    return "\n".join(satirlar)


if __name__ == "__main__":
    adim_listesi = [
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al"
    ]

    ek_bilgiler = {
        "sorumlu": "Ayşe"
    }

    # 1. çağrı: listeyi * ile aç, sözlüğü ** ile aç
    sonuc1 = gorev_kaydi(
        "Kara deliğe atla",
        *adim_listesi,
        oncelik="YÜKSEK",
        **ek_bilgiler
    )
    print(sonuc1)

    print()

    # 2. çağrı: adımları tek tek ver, ek bilgileri ** ile aç
    sonuc2 = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="YÜKSEK",
        **ek_bilgiler
    )
    print(sonuc2)
