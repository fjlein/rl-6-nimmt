import logging

import config as conf
from src.deck import Deck


class Game:
    def __init__(self, players):
        self.players = [player_class(name) for name, player_class in players]

        self.deck = Deck()

        self.rows = [[self.deck.draw_card_from_deck()] for _ in range(conf.ROW_COUNT)]

        for i in range(conf.CARDS_PER_PERSON):
            for player in self.players:
                player.draw_card(self.deck)

    def play(self):
        logging.info(f"Rows at start")
        [logging.info(", ".join(map(str, row))) for row in self.rows]

        for i in range(conf.CARDS_PER_PERSON):
            self.play_round()

            logging.info(f"Rows after round {i + 1}")
            [logging.info(", ".join(map(str, row))) for row in self.rows]

        self.players.sort(key=lambda player: player.get_score())

        if self.players[0].get_score() == self.players[1].get_score():
            return None

        return self.players[0].name

    def play_round(self):

        for player in self.players:
            logging.info(
                f"{player.name} hand: {", ".join([str(card) for card in player.hand_cards])}"
            )
            player.select_card(self.rows)
            logging.info(f"{player.name} selected card: {str(player.selected_card)}")

        sorted_indices = sorted(
            range(len(self.players)), key=lambda i: self.players[i].selected_card.value
        )

        for i in sorted_indices:
            self.players[i].play_card(self.rows)

        logging.info("All cards played, new penalty Cards:")

        for player in self.players:
            logging.info(
                f"{player.name} penalty cards: {", ".join(str(card) for card in player.penalty_cards)}"
            )
