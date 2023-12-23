from ichimlik import Ichimlik
from card import Card

class VendingMachine:
    def __init__(self) -> None:
        self.ichimliklar: list[Ichimlik] = []
        self.cards = {}
    
    def addBeverage(self, ichimlik:Ichimlik):
        self.ichimliklar.append(ichimlik)
        print("Yangi ichimlik qo'shildi:", ichimlik)

    def getPrice(self, nomi):
        for ichimlik_nomi in self.ichimliklar:
            if ichimlik_nomi == nomi:
                return ichimlik_nomi.narxi
            else:
                return -1.0
            
    def get_credit(self, card_id):
            if card_id in self.cards.keys():
                return card_id[card_id]
            else:
                return -1.0
            
    def recharge_card(self, card_id, credit):
        if card_id in self.cards.keys():
            self.cards[card_id] += credit
            return self.cards[card_id], self.cards, 'old'
        else:
            self.cards[card_id] = credit
            return self.cards[card_id], self.cards, 'new'
        
    