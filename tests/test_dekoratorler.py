
from uzay_oyunu.dekoratorler import sure_olc, say


def test_sure_olc_sonucu_degistirmez():
    @sure_olc
    def topla(a, b):
        return a + b

    assert topla(5, 3) == 8


def test_sure_olc_adli_argumanlarla_calisir():
    @sure_olc
    def selamla(isim, mesaj="Merhaba"):
        return f"{mesaj} {isim}"

    assert selamla(isim="Ayşe", mesaj="Selam") == "Selam Ayşe"


def test_sure_olc_fonksiyon_bilgilerini_korur():
    @sure_olc
    def ornek_fonksiyon():
        """Örnek fonksiyon açıklaması."""
        return True

    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Örnek fonksiyon açıklaması."


def test_say_cagri_sayisini_artirir():
    @say
    def carp(a, b):
        return a * b

    assert carp(2, 3) == 6
    assert carp(4, 5) == 20
    assert carp.cagri == 2


def test_say_fonksiyon_bilgilerini_korur():
    @say
    def ornek():
        """Say dekoratörü test fonksiyonu."""
        return 10

    assert ornek.__name__ == "ornek"
    assert ornek.__doc__ == "Say dekoratörü test fonksiyonu."
