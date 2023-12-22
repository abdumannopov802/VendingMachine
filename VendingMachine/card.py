class Card:
    def __init__(self, card_id, credit) -> None:
        self._card_id = card_id
        self._credit = credit

    @property
    def card_id(self):
        return self._card_id
    @property
    def credit(self):
        return self._credit
    
    def __str__(self) -> str:
        return f"{self.card_id} --> {self.credit}"