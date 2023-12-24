from ichimlik import Ichimlik
from card import Card
from Vending_machine import VendingMachine
class Ustun:
    def __init__(self) -> None:
        self.ustunlar = {1:[], 2:[], 3:[], 4:[]}

    def getPrice(self, search_name): #ready
        for ustun in  self.ustunlar:
            for ichimlik in self.ustunlar[ustun]:
                if ichimlik.ichimlik_nomi == search_name:
                    return ichimlik
        return -1.0         
        
    def refillColumn(self, ustun_id, ichimlik_soni, ichimlik:Ichimlik): #ready
        if ustun_id in self.ustunlar:
            if ichimlik_soni + len(self.ustunlar[ustun_id]) <= 20:
                for x in range(ichimlik_soni):
                    self.ustunlar[ustun_id].append(ichimlik)
                return f"{ichimlik_soni} ta ichimlik qo'shildi."
            elif len(self.ustunlar[ustun_id]) == 20:
                return "ustun to'lgan ichimlik qo'shib bo'lmaydi"
            else:
                return f"{20 - len(self.ustunlar[ustun_id])} ta ichimlik qo'shish mumkin"
        
    
    def availableCans(self, ichimlik_nomi): #ready
        count = 0
        for ustun_id in self.ustunlar:
            for ichimlik in self.ustunlar[ustun_id]:
                if ichimlik.ichimlik_nomi == ichimlik_nomi:
                    count += 1
        if count > 0:
            return f"VendingMachine da --> {count} ta <{ichimlik_nomi}> mavjud"
        else:
            return f"""VendingMachine da "{ichimlik_nomi}" yo'q"""
        
    def sell(self, input_card_id, ichimlik_nomi):
        for ustun_id in self.ustunlar:
            for ichimlik in self.ustunlar[ustun_id]:
                if ichimlik.ichimlik_nomi == ichimlik_nomi:
                    if input_card_id in self.cards.keys():
                        if input_card_id.credit >= ichimlik.ichimlik_narxi:
                            del self.ustunlar[ustun_id][0]
                            Card.cards[input_card_id] -= ichimlik.ichimlik_narxi
                            return f"ichimlik {ustun_id}-ustundan harid qilindi"
                        return -1.0
                    return -1.0
                return -1.0