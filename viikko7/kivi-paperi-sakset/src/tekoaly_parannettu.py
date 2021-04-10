from collections import deque

# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = deque([], muistin_koko)

    def aseta_siirto(self, siirto):
        self._muisti.append(siirto)

    def anna_siirto(self):
        if(self._muisti.__len__() <= 1):
            return "k"

        k = self._muisti.count("k")
        p = self._muisti.count("p")
        s = self._muisti.count("s")

        print(self._muisti)
        print(f"k {k} p {p} s {s}")

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p and k > s:
            return "p"
        elif p > k and p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
