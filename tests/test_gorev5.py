
import pytest
from functools import lru_cache

from uzay_oyunu.oyun import yakit_harca
from uzay_oyunu.dekoratorler import hafiza


# YAKIT TESTLERİ

def test_yakit_harca_normal_deger():
    assert yakit_harca(30) == 70


def test_yakit_harca_alt_sinir():
    assert yakit_harca(0) == 100


def test_yakit_harca_ust_sinir():
    assert yakit_harca(100) == 0


def test_yakit_harca_ust_sinir_asimi():
    with pytest.raises(ValueError, match="150 değeri 0-100 aralığında değil"):
        yakit_harca(150)


def test_yakit_harca_alt_sinir_asimi():
    with pytest.raises(ValueError, match="-1 değeri 0-100 aralığında değil"):
        yakit_harca(-1)


# HAFIZA DEKORATÖRÜ TESTLERİ

def test_hafiza_sonucu_onbellekte_saklar():
    sayac = {"deger": 0}

    @hafiza()
    def kare(x):
        sayac["deger"] += 1
        return x * x

    assert kare(5) == 25
    assert kare(5) == 25
    assert sayac["deger"] == 1


def test_hafiza_maxsize_eski_kaydi_siler():
    @hafiza(maxsize=2)
    def kare(x):
        return x * x

    kare(2)
    kare(3)

    assert len(kare.cache) == 2

    kare(4)

    assert len(kare.cache) == 2

    # En eski kayıt olan 2 silinmiş olmalı.
    assert ((2,), ()) not in kare.cache
    assert ((3,), ()) in kare.cache
    assert ((4,), ()) in kare.cache


def test_hafiza_lru_cache_ile_ayni_sonucu_verir():

    @hafiza()
    def kendi_fibonacci(n):
        if n < 2:
            return n
        return kendi_fibonacci(n - 1) + kendi_fibonacci(n - 2)

    @lru_cache(maxsize=None)
    def lru_fibonacci(n):
        if n < 2:
            return n
        return lru_fibonacci(n - 1) + lru_fibonacci(n - 2)

    for n in range(21):
        assert kendi_fibonacci(n) == lru_fibonacci(n)


def test_hafiza_anahtar_kelime_argumanlariyla_calisir():
    @hafiza()
    def topla(a, b=0):
        return a + b

    assert topla(5, b=3) == 8
    assert topla(5, b=3) == 8
    assert topla(5, b=4) == 9
