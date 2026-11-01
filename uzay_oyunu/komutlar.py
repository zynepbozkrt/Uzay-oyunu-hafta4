
KOMUTLAR = {}


def komut(ad, aciklama=""):
    """Fonksiyonu komut olarak kaydeder."""

    def dekorator(fonksiyon):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten tanımlanmış.")

        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon

    return dekorator


@komut("envanter", "eşyalarını gösterir")
def envanter(durum):
    """Oyuncunun envanterini gösterir."""

    esyalar = []

    if durum["credits"]:
        esyalar.append("bol kredi")

    if durum["engines"]:
        esyalar.append("güçlü motor")

    if durum["copilot"]:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return "Sende: " + ", ".join(esyalar)


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum):
    """Bulunulan konumdan gidilebilecek gezegenleri gösterir."""

    konum = durum["konum"]
    baglantilar = durum["baglantilar"]

    hedefler = baglantilar.get(konum, [])

    return ", ".join(hedefler)


@komut("yardim", "komutları listeler")
def yardim(durum):
    """Kullanılabilir komutları ve açıklamalarını gösterir."""

    satirlar = []

    for ad, (fonksiyon, aciklama) in KOMUTLAR.items():
        satirlar.append(f"{ad}  {aciklama}")

    return "\n".join(satirlar)
