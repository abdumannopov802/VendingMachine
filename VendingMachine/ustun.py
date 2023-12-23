from ichimlik import Ichimlik

class Ustun:
    def __init__(self, machine_id) -> None:
        self.machine_id = machine_id
        self.ustunlar = {1:[], 2:[], 3:[], 4:[]}
    
    def refillColumn(self, ustun_id, ichimlik_soni, ichimlik:Ichimlik):
        if ustun_id in self.ustunlar:
            if ichimlik_soni + len(self.ustunlar[ustun_id]) <= 20:
                for x in range(ichimlik_soni):
                    self.ustunlar[ustun_id].append(ichimlik)
                return f"{ichimlik_soni} ta ichimlik qo'shildi."
            elif len(self.ustunlar[ustun_id]) == 20:
                return "ustun to'lgan ichimlik qo'shib bo'lmaydi"
            else:
                return f"{20 - len(self.ustunlar[ustun_id])} ta ichimlik qo'shish mumkin"
    
    def availableCans(self, ichimlik_nomi):
        count = 0
        for ustun_id in self.ustunlar:
            for ichimlik in self.ustunlar[ustun_id]:
                if ichimlik.ichimlik_nomi == ichimlik_nomi:
                    count += 1
        if count > 0:
            return f"VendingMachine da --> {count} ta <{ichimlik_nomi}> mavjud"
        else:
            return f"""VendingMachine da "{ichimlik_nomi}" yo'q"""