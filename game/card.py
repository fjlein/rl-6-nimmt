class Card:
    def __init__(self, value, bullheads):
        self.value = value
        self.bullheads = bullheads

    def __str__(self):
        return f"{self.value} with {self.bullheads} bullhead{'s' if self.bullheads != 1 else ''}"
