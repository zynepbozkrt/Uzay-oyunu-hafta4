
from itertools import islice, takewhile

from uzay_oyunu.akis import fibonacci, yakit_gostergesi, satirlari_oku, ayristir, uzun_yolculuklar


def test_fibonacci_ilk_uc_deger():
    """next() ile ilk üç Fibonacci değerini kontrol eder."""
    g = fibonacci()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1


def test_fibonacci_ilk_on_iki_deger():
    """islice ile ilk 12 değeri kontrol eder."""
    sonuc = list(islice(fibonacci(), 12))

    assert sonuc == [
        0, 1, 1, 2, 3, 5,
        8, 13, 21, 34, 55, 89
    ]


def test_fibonacci_yuzden_kucuk_degerler():
    """takewhile ile 100'den küçük değerleri alır."""
    sonuc = list(takewhile(lambda sayi: sayi < 100, fibonacci()))

    assert sonuc == [
        0, 1, 1, 2, 3, 5,
        8, 13, 21, 34, 55, 89
    ]


def test_uretec_kaldigi_yerden_devam_eder():
    """Aynı üretecin sonraki çağrıda yeni değerler verdiğini kontrol eder."""
    g = fibonacci()

    ilk_bes = list(islice(g, 5))
    sonraki_bes = list(islice(g, 5))

    assert ilk_bes == [0, 1, 1, 2, 3]
    assert sonraki_bes == [5, 8, 13, 21, 34]

def test_yakit_gostergesi():
    """Yakıtın her adımda azaldığını ve sıfırda bittiğini kontrol eder."""
    from uzay_oyunu.akis import yakit_gostergesi

    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]

from pathlib import Path

def test_satirlari_oku():
    """Boş satırların ve yorum satırlarının atlandığını kontrol eder."""
    yol = Path("veri/seyir.txt")
    satirlar = list(satirlari_oku(yol))

    assert len(satirlar) == 6
    assert "# bakım molası" not in satirlar
    assert satirlar[0] == "dünya -> sirius 12"


def test_ayristir():
    """Yolculuk satırlarının doğru demetlere ayrıldığını kontrol eder."""
    sonuc = list(ayristir(["dünya -> sirius 12", "sirius -> orion 8"]))

    assert sonuc == [
        ("dünya", "sirius", 12),
        ("sirius", "orion", 8),
    ]


def test_uzun_yolculuklar():
    """Eşikten fazla yakıt tüketen yolculukları seçer."""
    kayitlar = [
        ("dünya", "sirius", 12),
        ("sirius", "orion", 8),
        ("orion", "centauri", 15),
    ]

    sonuc = list(uzun_yolculuklar(iter(kayitlar), 10))

    assert sonuc == [
        ("dünya", "sirius", 12),
        ("orion", "centauri", 15),
    ]


def test_seyir_dosyasi_uzun_yolculuklar():
    """Dosyayı okuyup uzun yolculukları ve toplam yakıtı kontrol eder."""
    from pathlib import Path

    yol = Path("veri/seyir.txt")
    satirlar = satirlari_oku(yol)
    kayitlar = ayristir(satirlar)

    sonuc = list(uzun_yolculuklar(kayitlar, 10))

    assert [kayit[1] for kayit in sonuc] == [
        "sirius",
        "centauri",
        "orion",
        "kara_delik",
    ]
    assert sum(kayit[2] for kayit in sonuc) == 72
