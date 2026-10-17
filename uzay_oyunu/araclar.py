# uzay_oyunu/araclar.py
import time
from functools import wraps

def hamle_sayaci():
    """
    Her çağrıldığında 1 artan bir sayaç closure fonksiyonu döndürür.
    nonlocal kullanarak dış fonksiyonun değişkenini günceller.
    """
    sayac = 0
    def say():
        nonlocal sayac
        sayac += 1
        return sayac
    return say

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """
    Gezegenleri bağlantı sayısına göre azalan (-len), 
    eşitlik durumunda ise alfabetik sıraya göre sıralar.
    """
    baglantilar = galaksi.get("baglantilar", {})
    
    sirali = sorted(
        baglantilar.keys(),
        key=lambda gezegen: (-len(baglantilar[gezegen]), gezegen)
    )
    return sirali

def sure_olc(fonksiyon):
    """
    Bonus (+10): Verilen fonksiyonun çalışma süresini ölçen sarmalayıcı (wrapper).
    """
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc
    return sarmalayici

