class IntJoukko:
    def __init__(self, kapasiteetti = 0, oletuskasvatus = 0):
        # ei tarvettaa varata tilaa etukäteen - Pythonin listan toteutus on lähes yhtä nopea kuin ennaltavaraava versio
        self.ljono = []

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        self.ljono.append(n)
        return True

    def poista(self, n):
        try: 
            self.ljono.remove(n) 
        except ValueError:
            return False

        return True

    def mahtavuus(self):
        return len(self.ljono)

    def to_int_list(self):
        return self.ljono

    @staticmethod
    def yhdiste(a, b):
        yhdisteJoukko = IntJoukko()
        yhdisteJoukko.ljono = a.ljono + b.ljono
        return yhdisteJoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausJoukko = IntJoukko()
        leikkausJoukko.ljono = [aArvo for aArvo in a.ljono if aArvo in b.ljono]
        return leikkausJoukko

    @staticmethod
    def erotus(a, b):
        erotusJoukko = IntJoukko()
        erotusJoukko.ljono = [aArvo for aArvo in a.ljono if aArvo not in b.ljono]
        return erotusJoukko

    def __str__(self):
        if len(self.ljono)  == 0:
            return "{}"
        elif len(self.ljono) == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in self.ljono[:-1]:
                tuotos = tuotos + str(i)
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[-1])
            tuotos = tuotos + "}"
            return tuotos
