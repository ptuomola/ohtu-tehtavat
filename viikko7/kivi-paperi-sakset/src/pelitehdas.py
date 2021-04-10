from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Pelitehdas:
  @staticmethod
  def kps_pelaaja_vs_pelaaja():
    return KPSPelaajaVsPelaaja()

  @staticmethod
  def kps_tekoaly():
    return KPSTekoaly()

  @staticmethod
  def kps_parempi_tekoaly():
    return KPSParempiTekoaly()