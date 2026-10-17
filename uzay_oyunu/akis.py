import time
from collections.abc import Iterator
from pathlib import Path

def fibonacci() -> Iterator[int]:
    """Sonsuz Fibonacci dizisini bir üreteç olarak üretir."""
    onceki = 0
    simdiki = 1

    while True:
        yield onceki
        onceki, simdiki = simdiki, onceki + simdiki


def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Her çağrıda kalan yakıtı tüketim miktarı kadar azaltarak üretir."""
    while yakit > 0:
        yakit = max(0, yakit - tuketim)
        yield yakit


def satirlari_oku(yol: str | Path) -> Iterator[str]:
    """Dosyayı satır satır okur; boş ve yorum satırlarını atlar."""
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.strip()

            if satir and not satir.startswith("#"):
                yield satir


def ayristir(satirlar: Iterator[str]) -> Iterator[tuple[str, str, int]]:
    """Yolculuk satırlarını kaynak, hedef ve yakıt demetlerine dönüştürür."""
    for satir in satirlar:
        kaynak_hedef, yakit_metni = satir.rsplit(maxsplit=1)
        kaynak, hedef = kaynak_hedef.split("->")
        yield kaynak.strip(), hedef.strip(), int(yakit_metni)


def uzun_yolculuklar(
    kayitlar: Iterator[tuple[str, str, int]],
    esik: int,
) -> Iterator[tuple[str, str, int]]:
    """Yakıt tüketimi eşikten büyük olan yolculukları üretir."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield kaynak, hedef, yakit


def zamanlayici(aralik: int) -> Iterator[int]:
    """Belirtilen süre boyunca tik ve tak mesajları üretir."""
    baslangic = time.perf_counter()
    sonraki_tik = 2
    sonraki_tak = 5

    while True:
        gecen = time.perf_counter() - baslangic

        if gecen >= aralik:
            return

        if gecen >= sonraki_tik:
            print("tik")
            sonraki_tik += 2

        if gecen >= sonraki_tak:
            print("tak")
            sonraki_tak += 5

        yield int(gecen)

