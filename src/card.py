class Card:
    def __init__(self, value, bullheads):
        self.value = value
        self.bullheads = bullheads

    def __str__(self):
        return f"[{str(self.value).rjust(3)}, {self.bullheads}]"
