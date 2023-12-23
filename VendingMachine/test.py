from ichimlik import Ichimlik
from Vending_machine import VendingMachine
from ustun import Ustun
from sell import Sell
ichimlik1 = Ichimlik('Pepsi', 15000)
print(ichimlik1)

vendingmachine = VendingMachine()
vendingmachine.addBeverage(ichimlik1)
print(vendingmachine.ichimliklar)

print(vendingmachine.getPrice("Pepsi"))
print(vendingmachine.get_card(2))
# print(vendingmachine.recharge_card(2, 12000))
a = Ustun(1)
print(a.refillColumn(2, 20, ichimlik1))
print(a.refillColumn(2, 1, ichimlik1))
print(a.refillColumn(2, 0, ichimlik1))
print(a.availableCans("Pepsi"))
a = Sell()
print(a.sell(1, "pepsi"))