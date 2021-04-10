from pelitehdas import Pelitehdas

# Tässä luokassa toteutetaan käyttöliittymä

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        if vastaus.endswith("a"):
            peli = Pelitehdas.kps_pelaaja_vs_pelaaja()
        elif vastaus.endswith("b"):
            peli = Pelitehdas.kps_tekoaly()
        elif vastaus.endswith("c"):
            peli = Pelitehdas.kps_parempi_tekoaly()
        else:
            break

        peli.pelaa()


if __name__ == "__main__":
    main()
