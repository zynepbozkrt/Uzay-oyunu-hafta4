
import time
from functools import wraps, lru_cache


def sure_olc(fonksiyon):
    @wraps(fonksiyon)
    def wrapper(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()

        gecen_sure = bitis - baslangic
        print(f"{fonksiyon.__name__}: {gecen_sure:.4f} sn")

        return sonuc

    return wrapper


def say(fonksiyon):
    @wraps(fonksiyon)
    def wrapper(*args, **kwargs):
        wrapper.cagri += 1
        return fonksiyon(*args, **kwargs)

    wrapper.cagri = 0
    return wrapper


def log_cagri(fonksiyon):
    @wraps(fonksiyon)
    def wrapper(*args, **kwargs):
        argumanlar = [repr(arg) for arg in args]
        argumanlar.extend(
            f"{anahtar}={deger!r}"
            for anahtar, deger in kwargs.items()
        )

        print(f"-> {fonksiyon.__name__}({', '.join(argumanlar)})")

        sonuc = fonksiyon(*args, **kwargs)

        print(f"<- {fonksiyon.__name__} = {sonuc!r}")

        return sonuc

    return wrapper


# 1. Yalnızca say dekoratörü
@say
def fib_say(n):
    """Özyinelemeli Fibonacci."""
    if n < 2:
        return n
    return fib_say(n - 1) + fib_say(n - 2)


# 2. say üstte, lru_cache altta
@say
@lru_cache(maxsize=None)
def fib_say_cache(n):
    """Say dekoratörü dışta, önbellek içte."""
    if n < 2:
        return n
    return fib_say_cache(n - 1) + fib_say_cache(n - 2)


# 3. lru_cache üstte, say altta
@lru_cache(maxsize=None)
@say
def fib_cache_say(n):
    """Önbellek dışta, say dekoratörü içte."""
    if n < 2:
        return n
    return fib_cache_say(n - 1) + fib_cache_say(n - 2)


def fibonacci_cagri_sonuclari():
    print("Yalnızca @say:")
    print("fib(20) =", fib_say(20))
    print("Çağrı sayısı:", fib_say.cagri)

    print("\n@say üstte, @lru_cache altta:")
    print("fib(20) =", fib_say_cache(20))
    print("Çağrı sayısı:", fib_say_cache.cagri)

    print("\n@lru_cache üstte, @say altta:")
    print("fib(20) =", fib_cache_say(20))
    print("Çağrı sayısı:", fib_cache_say.__wrapped__.cagri)


if __name__ == "__main__":
    fibonacci_cagri_sonuclari()


def sinirla(alt, ust):
    """Fonksiyonun ilk argümanını belirtilen aralıkta tutar."""

    def dekorator(fonksiyon):
        @wraps(fonksiyon)
        def wrapper(*args, **kwargs):
            if not args:
                raise ValueError(
                    f"{fonksiyon.__name__}: İlk argüman verilmedi."
                )

            miktar = args[0]

            if not alt <= miktar <= ust:
                raise ValueError(
                    f"{fonksiyon.__name__}: {miktar} değeri "
                    f"{alt}-{ust} aralığında değil"
                )

            return fonksiyon(*args, **kwargs)

        return wrapper

    return dekorator


def hafiza(maxsize=None):
    """Sonuçları closure içindeki sözlükte saklar."""

    if maxsize is not None and maxsize < 0:
        raise ValueError("maxsize negatif olamaz.")

    def dekorator(fonksiyon):
        cache = {}

        @wraps(fonksiyon)
        def wrapper(*args, **kwargs):
            anahtar = (args, tuple(sorted(kwargs.items())))

            if anahtar in cache:
                return cache[anahtar]

            sonuc = fonksiyon(*args, **kwargs)

            if maxsize != 0:
                if maxsize is not None and len(cache) >= maxsize:
                    en_eski = next(iter(cache))
                    del cache[en_eski]

                cache[anahtar] = sonuc

            return sonuc

        wrapper.cache = cache
        return wrapper

    return dekorator
