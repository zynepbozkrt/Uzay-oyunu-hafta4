# tests/test_tuzaklar.py

# Hatalı fonksiyon
def yakit_ekle(miktar, depo=None):
    if depo is None:
     depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_bagimsiz_cagrilarda_yeni_liste_donmeli():
    # İlk çağrı: [10] dönmesini bekleriz
    arac_1 = yakit_ekle(10)
    assert arac_1 == [10]

    # İkinci bağımsız çağrı: Sadece [20] dönmesini bekleriz
    arac_2 = yakit_ekle(20)
    # Hatalı kodda arac_2 -> [10, 20] dönecektir ve aşağıdaki assert BAŞARISIZ (FAILED) olacaktır:
    assert arac_2 == [20]
