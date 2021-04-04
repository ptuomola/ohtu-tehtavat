class TennisGame:
    SCORE_WORDS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.players = [player1_name, player2_name]
        self.scores = [0,0]

    def won_point(self, player_name):
        self.scores[self.players.index(player_name)] += 1
    
    def get_score(self):
        if self.scores[0] == self.scores[1]:
            return TennisGame.get_draw_score(self.scores[0])

        if self.scores[0] >= 4 or self.scores[1] >= 4:
            return TennisGame.get_winning_score(self.scores[0], self.scores[1])

        return TennisGame.get_score_word(self.scores[0]) + "-" + self.get_score_word(self.scores[1])

    @staticmethod
    def get_score_word(score):
        return TennisGame.SCORE_WORDS[score]

    @staticmethod
    def get_draw_score(score):
        if(score >= 4): 
            return "Deuce"

        return TennisGame.get_score_word(score) + "-All"
    
    @staticmethod
    def get_winning_score(score1, score2):
        if score1 > score2 + 1:
            return "Win for player1"

        if score1 > score2:
            return "Advantage player1"

        if score2 > score1 + 1:
            return "Win for player2"

        return "Advantage player2"

