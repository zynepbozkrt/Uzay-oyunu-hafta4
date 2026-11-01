import json
from functools import reduce, partial
from pathlib import Path
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler
from uzay_oyunu.akis import yakit_gostergesi
from uzay_oyunu.dekoratorler import log_cagri
from uzay_oyunu.komutlar import KOMUTLAR 
from uzay_oyunu.dekoratorler import sinirla


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    esyalar = []

    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return "Sende: " + ", ".join(esyalar)


@log_cagri
def hedef_menusu(hedefler: list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]

    for numara, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{numara}] {hedef}")

    return "\n".join(satirlar)


@log_cagri
def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs
) -> dict:
    """Galaksi haritasını ve başlangıç durumunu oluşturur."""
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni listede bulunamadı.")

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": kwargs.get("yakit", 50),
    }


def galaksi_yukle() -> dict:
    """Galaksi verilerini JSON dosyasından yükler."""
    dosya_yolu = Path(__file__).with_name("galaksi.json")

    with dosya_yolu.open("r", encoding="utf-8") as dosya:
        veri = json.load(dosya)

    return galaksi_kur(**veri)



def travel(hiz: int = 1) -> None:
    envanter = envanter_metni(True, False, True)

    if envanter:
        print(envanter)

    galaksi = galaksi_yukle()
    planet = galaksi["konum"]
    yakit = galaksi["yakit"]
    yakit_akisi = yakit_gostergesi(yakit, 10)

    sayac = hamle_sayaci()
    toplam_hamle = 0

    
    credits = True
    engines = False
    copilot = True

    while True:
        destinations = galaksi["baglantilar"].get(planet, [])

        if not destinations:
            print("Kara deliğe ulaştın veya yol bitti!")
            break

        print(f"\nŞu anki konum: {planet}")
        print(hedef_menusu(destinations))

        secim = input("Seçiminiz (Çıkış için q): ")

        if secim.lower() == "q":
            break

        
        if secim in KOMUTLAR:
            durum = {
                "konum": planet,
                "baglantilar": galaksi["baglantilar"],
                "credits": credits,
                "engines": engines,
                "copilot": copilot,
            }

            fonksiyon, aciklama = KOMUTLAR[secim]
            sonuc = fonksiyon(durum)

            if sonuc is not None:
                print(sonuc)

            continue

        
        try:
            index = int(secim) - 1

            if 0 <= index < len(destinations):
                try:
                    yakit = next(yakit_akisi)
                except StopIteration:
                    print("Yakıtın bitti, uzayda sürükleniyorsun...")
                    break

                sayac()
                toplam_hamle += 1
                planet = destinations[index]

                print(f"Kalan yakıt: {yakit}")

                if yakit == 0:
                    print("Yakıtın bitti, uzayda sürükleniyorsun...")
                    break
            else:
                print("Geçersiz seçim!")

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    print(f"Oyunu {toplam_hamle} hamlede bitirdin!")

hizli_yolculuk = partial(travel, hiz=3)


@sinirla(0, 100)
def yakit_harca(miktar):
    """100 birimlik yakıttan belirtilen miktarı harcar."""
    return 100 - miktar

if __name__ == "__main__":
    travel()