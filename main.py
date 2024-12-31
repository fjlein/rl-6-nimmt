import config as conf
from src.player import RandomPlayer, SmartPlayer1, SmartPlayer2
from src.tournament import Tournament
from itertools import combinations_with_replacement
from multiprocessing import Pool

import logging

logging.basicConfig(level=logging.DEBUG if conf.LOGGING else logging.CRITICAL)


def all_combinations_tournament(players):
    p = Pool()
    all_combinations = []
    for r in range(2, len(players) + 1):
        all_combinations.extend(list(combinations_with_replacement(players, r)))

    p.map(host_tournament, all_combinations)


def host_tournament(players):
    tournament = Tournament(
        [(f"player{i+1}", player_class) for i, player_class in enumerate(players)],
        conf.ITERATIONS,
    )
    tournament.play()
    tournament.evaluate()


def main():
    players = [RandomPlayer, SmartPlayer1, SmartPlayer2]

    # all_combinations_tournament(players)
    host_tournament(players)


if __name__ == "__main__":
    main()
