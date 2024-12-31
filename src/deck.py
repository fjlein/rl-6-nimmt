import random

import config as conf
from src.card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        for value in range(1, conf.TOTAL_CARD_COUNT + 1):
            bullheads = next(
                b
                for divisor, b in [(55, 7), (11, 5), (10, 3), (5, 2), (1, 1)]
                if value % divisor == 0
            )
            self.cards.append(Card(value=value, bullheads=bullheads))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card_from_deck(self):
        return self.cards.pop()
