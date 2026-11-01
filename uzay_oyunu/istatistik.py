import json
from functools import reduce, partial
from pathlib import Path
from uzay_oyunu.oyun import travel

def galaksi_yukle() -> dict:
    """Galaksi verilerini JSON dosyasından yükler."""
    yol = Path(__file__).with_name("galaksi.json")

    with open(yol, "r", encoding="utf-8") as dosya:
        return json.load(dosya)


def istatistikleri_hesapla(galaksi: dict) -> None:
    """Galaksi verilerini iki farklı yöntemle analiz eder."""
    gezegenler = galaksi["gezegenler"]
    baglantilar = galaksi["baglantilar"]

    # 1. Gezegen isimlerini büyük harfe dönüştürme
    buyuk_harf_map = list(map(str.upper, gezegenler))
    buyuk_harf_liste = [gezegen.upper() for gezegen in gezegenler]

    # 2. En az iki bağlantısı olan gezegenleri bulma
    cok_baglantili_filter = list(
        filter(lambda gezegen: len(baglantilar[gezegen]) >= 2, gezegenler)
    )
    cok_baglantili_liste = [
        gezegen for gezegen in gezegenler
        if len(baglantilar[gezegen]) >= 2
    ]

    # 3. Toplam bağlantı sayısını hesaplama
    toplam_reduce = reduce(
        lambda toplam, gezegen: toplam + len(baglantilar[gezegen]),
        gezegenler,
        0,
    )
    toplam_sum = sum(len(baglantilar[gezegen]) for gezegen in gezegenler)

    print("Büyük harf (map):", buyuk_harf_map)
    print("Büyük harf (liste):", buyuk_harf_liste)
    print("En az 2 bağlantı (filter):", cok_baglantili_filter)
    print("En az 2 bağlantı (liste):", cok_baglantili_liste)
    print("Toplam bağlantı (reduce):", toplam_reduce)
    print("Toplam bağlantı (sum):", toplam_sum)

hizli_yolculuk = partial (travel, hiz=3)

if __name__ == "__main__":
    istatistikleri_hesapla(galaksi_yukle())
