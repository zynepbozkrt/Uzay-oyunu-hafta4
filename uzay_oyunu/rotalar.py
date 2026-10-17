from functools import lru_cache


def rota_sayaci(baglantilar: dict[str, list[str]]):
    """Belirli sayıda adımda ulaşılabilecek rota sayısını hesaplayan fonksiyon döndürür."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Bir gezegenden tam adim yolculukta oluşan rota sayısını hesaplar."""
        if adim == 0:
            return 1

        hedefler = baglantilar.get(gezegen, [])

        return sum(
            rota_sayisi(hedef, adim - 1)
            for hedef in hedefler
        )

    return rota_sayisi


if __name__ == "__main__":
    import json
    from pathlib import Path
    from time import perf_counter

    yol = Path(__file__).with_name("galaksi.json")

    with open(yol, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)

    baglantilar = veri["baglantilar"]

    def rota_sayisi_onbelleksiz(gezegen: str, adim: int) -> int:
        """Rota sayısını önbellek kullanmadan hesaplar."""
        if adim == 0:
            return 1

        return sum(
            rota_sayisi_onbelleksiz(hedef, adim - 1)
            for hedef in baglantilar.get(gezegen, [])
        )

    baslangic = veri["baslangic"]
    adim = 20

    basla = perf_counter()
    sonuc1 = rota_sayisi_onbelleksiz(baslangic, adim)
    sure1 = perf_counter() - basla

    say = rota_sayaci(baglantilar)

    basla = perf_counter()
    sonuc2 = say(baslangic, adim)
    sure2 = perf_counter() - basla

    print("Önbelleksiz sonuç:", sonuc1)
    print(f"Önbelleksiz süre: {sure1:.6f} saniye")
    print("Önbellekli sonuç:", sonuc2)
    print(f"Önbellekli süre: {sure2:.6f} saniye")
    print("Önbellek bilgisi:", say.cache_info())
