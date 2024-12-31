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
    def select_row_to_take(self, rows):
        pass

    @staticmethod
    def get_row_to_append_to(rows, card):
        min_delta = conf.TOTAL_CARD_COUNT
        best_row = None

        for row in rows:
            last_card = row[-1]
            if card.value > last_card.value:
                delta = card.value - last_card.value
                if delta < min_delta:
                    min_delta = delta
                    best_row = row

        return best_row

    def play_card(self, rows):
        row = self.get_row_to_append_to(rows, card=self.selected_card)

        if row is None or len(row) == 5:
            row = row or self.select_row_to_take(rows)
            self.penalty_cards.extend(row)
            row.clear()

        row.append(self.selected_card)

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

    def select_row_to_take(self, rows):
        return random.choice(rows)


class SmartPlayer1(RandomPlayer):

    def select_row_to_take(self, rows):
        return min(
            rows,
            key=lambda row: sum(card.bullheads for card in row),
        )


class SmartPlayer2(SmartPlayer1):

    @staticmethod
    def card_score(self, c, rows):
        row = self.get_row_to_append_to(rows, c)
        if row is None:
            return 6
        return len(self.get_row_to_append_to(rows, c))

    def select_card(self, rows):

        self.hand_cards.sort(key=lambda c: self.card_score(self, c, rows))

        card = self.hand_cards[0]
        self.selected_card = card
        self.hand_cards.remove(card)
