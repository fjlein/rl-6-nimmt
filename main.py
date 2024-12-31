import config as conf
from src.player import RandomPlayer, SmartPlayer1, SmartPlayer2
from src.tournament import Tournament
from itertools import combinations

import logging

logging.basicConfig(level=logging.DEBUG if conf.PRINT else logging.CRITICAL)


def main():
    players = [
        ("player1", RandomPlayer),
        ("player2", SmartPlayer1),
        ("player3", SmartPlayer2),
    ]

    all_combinations = []
    for r in range(2, len(players) + 1):
        all_combinations.extend(list(combinations(players, r)))

    for i, players in enumerate(all_combinations):
        print(f"Tournament {i+1}")
        tournament = Tournament(
            players,
            conf.ITERATIONS,
        )
        tournament.play()
        tournament.evaluate()


if __name__ == "__main__":
    main()
