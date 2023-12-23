from card import Card
from ichimlik import Ichimlik
from Vending_machine import VendingMachine
machine = VendingMachine
class Sell:
    def sell(self, input_card_id, ichimlik_nomi):
        if machine.get_credit(machine, input_card_id) != -1.0:
            return "ok"
        


