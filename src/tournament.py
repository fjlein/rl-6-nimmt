import config as conf
from src.game import Game


class Tournament:
    def __init__(self, players, iterations):
        self.players = players
        self.iterations = iterations
        self.winners = []

    def play(self):
        for i in range(self.iterations):
            if conf.PRINT:
                print(f"{"-"*20}\nStarting game {i+1}\n{"-"*20}")
            game = Game(self.players)
            winner = game.play()
            self.winners.append(winner)

    def evaluate(self):
        for player_name, player_class in self.players:
            wins = self.winners.count(player_name)
            print(
                f"{player_name} ({player_class.__name__}): {wins} / {self.iterations} {format(wins/self.iterations, ".2%")}"
            )
        draws = self.winners.count(None)
        print(
            f"draw: {draws} / {self.iterations} {format(draws/self.iterations, ".2%")}"
        )
