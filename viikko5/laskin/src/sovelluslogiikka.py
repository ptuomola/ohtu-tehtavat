class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def tallenna_komento(self, komento):
        self._viimeinen_komento = komento

class Summa:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        self._edellinen_arvo = self._sovellus.tulos
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass        

        self._sovellus.plus(arvo)
    
    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen_arvo)

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        self._edellinen_arvo = self._sovellus.tulos
        arvo = 0

        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass        

        self._sovellus.miinus(arvo)

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen_arvo)

class Nollaus:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        self._edellinen_arvo = self._sovellus.tulos
        self._sovellus.nollaa()

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen_arvo)


class Kumoa:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote

    def suorita(self):
        self._sovellus._viimeinen_komento.kumoa()
