import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_top_scorers_one(self):
      topscorer = self.statistics.top_scorers(0)
      self.assertEqual(len(topscorer), 1)
      self.assertEqual(topscorer[0].name, "Gretzky")

    def test_team_players(self):
      teamplayers = self.statistics.team("PIT")
      self.assertEqual(len(teamplayers), 1)
      self.assertEqual(teamplayers[0].name, "Lemieux")

    def test_search(self):
      result = self.statistics.search("Kurri")
      self.assertEqual(result.name, "Kurri")
      self.assertEqual(result.team, "EDM")

    def test_search_notfound(self):
      result = self.statistics.search("Nobody")
      self.assertIsNone(result)