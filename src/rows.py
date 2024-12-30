import config as conf


class Rows:
    def __init__(self, deck):
        self.rows = [[deck.draw_from_deck()] for _ in range(conf.ROW_COUNT)]

    def __str__(self):
        row_strings = []
        for i, row in enumerate(self.rows):
            row_strings.append(f"Row {i+1}: {", ".join([str(card) for card in row])}")
        return "\n".join(row_strings)

    def get_append_index(self, card):
        min_delta = conf.TOTAL_CARD_COUNT
        best_index = None

        for i, row in enumerate(self.rows):
            last_card = row[-1]
            if card.value > last_card.value:
                delta = card.value - last_card.value
                if delta < min_delta:
                    min_delta = delta
                    best_index = i

        return best_index

    def take_row(self, index):
        row = self.rows[index]
        cards = []
        while row:
            cards.append(row.pop())
        return cards

    def add_to_row(self, index, card):
        self.rows[index].append(card)

    def check_row_full(self, index):
        return len(self.rows[index]) == 5

    def get_rows(self):
        return self.rows
