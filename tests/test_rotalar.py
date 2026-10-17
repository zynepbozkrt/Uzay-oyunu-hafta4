from uzay_oyunu.rotalar import rota_sayaci


def test_rota_sayisi():
    """Rota sayacının küçük bir galakside doğru çalıştığını kontrol eder."""
    baglantilar = {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "sirius"],
        "sirius": ["dünya"],
    }

    say = rota_sayaci(baglantilar)

    assert say("dünya", 0) == 1
    assert say("dünya", 1) == 2
    assert say("dünya", 2) == 3
