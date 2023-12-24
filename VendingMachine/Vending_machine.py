from ichimlik import Ichimlik
from card import Card
from ustun import Ustun

class VendingMachine:
    def __init__(self) -> None:
        self.ichimliklar: list[Ichimlik] = []
        self.cards = {}
    
    def addBeverage(self, ichimlik:Ichimlik):
        self.ichimliklar.append(ichimlik)
        return f"Yangi ichimlik qo'shildi: {ichimlik}"

    def getPrice(self, search_name):
        return Ustun.getPrice(Ustun, search_name)
            
    def get_credit(self, card_id): #ready
            if card_id in self.cards.keys():
                return f"ID-{card_id} kartasida {self.cards[card_id]}so'm mablag' mavjud"
            else:
                return -1.0
            
    def recharge_card(self, recharge_card_id, payment): #ready
        if recharge_card_id in self.cards.keys():
            self.cards[recharge_card_id] += payment
            return f"Successfuly Payment! --> ID-{recharge_card_id} : {self.cards[recharge_card_id]}so'm"
        else:
            self.cards.update({recharge_card_id : payment})
            return f"Successfuly New card and Payment --> ID-{recharge_card_id} : {self.cards[recharge_card_id]}so'm"
        
    