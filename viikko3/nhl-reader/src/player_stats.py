from player import Player

class PlayerStats:

    def __init__(self, player_reader):
      self.reader = player_reader

    def top_scorers_by_nationality(self, nationality):
      players = self.reader.get_players()
      return sorted((p for p in players if p.nationality == nationality), key = lambda x: x.points(), reverse=True)