
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_bazi_esyalar():
    assert envanter_metni(True, False, True) == (
        "Sende: bol kredi, yetenekli bir pilot"
    )


def test_envanter_bos():
    assert envanter_metni(False, False, False) == ""


def test_hedef_menusu():
    assert hedef_menusu(["centauri", "sirius"]) == (
        "Nereye gitmek istersin?\n"
        "[1] centauri\n"
        "[2] sirius"
    )


def test_hedef_menusu_bos():
    assert hedef_menusu([]) == "Nereye gitmek istersin?"