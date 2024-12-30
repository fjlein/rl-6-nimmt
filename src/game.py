import config as conf
from src.deck import Deck
from src.rows import Rows


class Game:
    def __init__(self, players):
        self.players = [player_class(name) for name, player_class in players]

        self.deck = Deck()

        self.rows = Rows(deck=self.deck)

        for i in range(conf.CARDS_PER_PERSON):
            for player in self.players:
                player.draw(self.deck)

    def play(self):

        for i in range(conf.CARDS_PER_PERSON):
            if conf.PRINT:
                print(f"Before round {i + 1}")
                print(str(self.rows))

            self.play_round()

            if conf.PRINT:
                print(f"After round {i + 1}")
                print(str(self.rows))

        if self.players[0].get_score() == self.players[1].get_score():
            return None

        self.players.sort(
            key=lambda player: sum([c.bullheads for c in player.penalty_cards])
        )

        return self.players[0].name

    def play_round(self):

        for player in self.players:
            player.show_hand_cards()
            player.select_card(self.rows)
            player.show_selected_card()

        self.players.sort(key=lambda p: p.selected_card.value)

        for player in self.players:
            player.play_card(self.rows)

        if conf.PRINT:
            print("Cards played")
            print("New penalty Cards:")

        for player in self.players:
            player.show_penalty_cards()
