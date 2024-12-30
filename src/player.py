import random
from abc import ABC, abstractmethod
import config as conf


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.hand_cards = []
        self.penalty_cards = []
        self.selected_card = None

    def draw(self, deck):
        self.hand_cards.append(deck.draw_from_deck())
        self.hand_cards.sort(key=lambda card: card.value)

    @abstractmethod
    def select_card(self, rows):
        pass

    @abstractmethod
    def select_row_index(self, rows):
        pass

    def play_card(self, rows):
        row_index = rows.get_append_index(card=self.selected_card)

        if row_index is None:
            index = self.select_row_index(rows)
            self.penalty_cards.extend(rows.take_row(index))
            rows.add_to_row(index=index, card=self.selected_card)

        elif rows.check_row_full(row_index):
            self.penalty_cards.extend(rows.take_row(row_index))
            rows.add_to_row(index=row_index, card=self.selected_card)

        else:
            rows.add_to_row(index=row_index, card=self.selected_card)

    def get_score(self):
        return sum([card.bullheads for card in self.penalty_cards])

    def show_hand_cards(self):
        if conf.PRINT:
            print(
                f"{self.name} hand: {", ".join([str(card) for card in self.hand_cards])}"
            )

    def show_penalty_cards(self):
        if conf.PRINT:
            print(
                f"{self.name} penalty cards: {", ".join([str(card) for card in self.penalty_cards])}"
            )

    def show_selected_card(self):
        if conf.PRINT:
            print(f"{self.name} selected card: {str(self.selected_card)}")


class RandomPlayer(Player):
    def select_card(self, rows):
        card = random.choice(self.hand_cards)
        self.selected_card = card
        self.hand_cards.remove(card)

    def select_row_index(self, rows):
        return random.choice(range(conf.ROW_COUNT))


class SmartPlayer1(RandomPlayer):

    def select_row_index(self, rows):
        return min(
            range(conf.ROW_COUNT),
            key=lambda i: sum(card.bullheads for card in rows.get_rows()[i]),
        )


class SmartPlayer2(SmartPlayer1):

    @staticmethod
    def card_score(c, rows):
        index = rows.get_append_index(c)
        if index is None:
            return 6
        return len(rows.get_rows()[rows.get_append_index(c)])

    def select_card(self, rows):

        self.hand_cards.sort(key=lambda c: self.card_score(c, rows))

        card = self.hand_cards[0]
        self.selected_card = card
        self.hand_cards.remove(card)


class SmartPlayer3(SmartPlayer2):
    @staticmethod
    def card_score(c, rows):
        index = rows.get_append_index(c)
        if index is None:
            return 6
        return len(rows.get_rows()[rows.get_append_index(c)])
