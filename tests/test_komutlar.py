
import pytest

from uzay_oyunu.komutlar import (
    KOMUTLAR,
    komut,
    yardim,
    envanter,
    harita,
)


def test_envanter_komutu():
    durum = {
        "konum": "dünya",
        "baglantilar": {},
        "credits": True,
        "engines": False,
        "copilot": True,
    }

    sonuc = envanter(durum)

    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"


def test_harita_komutu():
    durum = {
        "konum": "dünya",
        "baglantilar": {
            "dünya": ["orion", "sirius"]
        },
        "credits": False,
        "engines": False,
        "copilot": False,
    }

    assert harita(durum) == "orion, sirius"


def test_yardim_komutu():
    durum = {
        "konum": "dünya",
        "baglantilar": {},
        "credits": False,
        "engines": False,
        "copilot": False,
    }

    sonuc = yardim(durum)

    assert "envanter" in sonuc
    assert "harita" in sonuc
    assert "yardim" in sonuc


def test_ayni_komut_iki_kez_tanimlanamaz():
    @komut("test_tekil_komut", "test açıklaması")
    def ilk_komut(durum):
        return "ilk"

    with pytest.raises(ValueError):

        @komut("test_tekil_komut", "ikinci açıklama")
        def ikinci_komut(durum):
            return "ikinci"
