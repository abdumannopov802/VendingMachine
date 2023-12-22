from ichimlik import Ichimlik
from Vending_machine import VendingMachine

ichimlik1 = Ichimlik('Pepsi', 15000)
# print(ichimlik1)

vendingmachine = VendingMachine()
# vendingmachine.addBeverage(ichimlik1)
# print(vendingmachine.ichimliklar)

vendingmachine.getPrice("Pepsi")