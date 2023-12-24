from ichimlik import Ichimlik
from Vending_machine import VendingMachine
from ustun import Ustun
# from sell import Sell

# print(ichimlik1)
# print(vendingmachine.ichimliklar)
# print(vendingmachine.getPrice("Pepsi"))
# print(vendingmachine.get_card(2))
# print(vendingmachine.recharge_card(2, 12000))
# vendingmachine.addBeverage(ichimlik1)


vendingmachine = VendingMachine()
ustun = Ustun()

ichimlik1 = Ichimlik('Pepsi', 15000)
ichimlik2 = Ichimlik('Coca Cola', 12000)
ichimlik3 = Ichimlik('Fanta', 9000)
ichimlik4 = Ichimlik('Suv', 5000)

# recharge_card
print(vendingmachine.recharge_card(1, 12000))
print(vendingmachine.recharge_card(1, 12000))
print(vendingmachine.recharge_card(2, 15000))
print(vendingmachine.recharge_card(2, 20000))
print(vendingmachine.recharge_card(3, 1000))

# get_credit
print(vendingmachine.get_credit(1))
print(vendingmachine.get_credit(2))
print(vendingmachine.get_credit(3))
print(vendingmachine.get_credit(4))

# refillColumn
print(ustun.refillColumn(1, 20, ichimlik1))
print(ustun.refillColumn(2, 15, ichimlik2))
print(ustun.refillColumn(3, 10, ichimlik3))
print(ustun.refillColumn(4, 20, ichimlik4))

# getPrice
print(ustun.getPrice("Pepsi"))
print(ustun.getPrice("Fanta"))
print(ustun.getPrice("Coca Cola"))
print(ustun.getPrice("Suv"))
print(ustun.getPrice(""))

# availableCans
print(ustun.availableCans("Pepsi"))
print(ustun.availableCans("Fanta"))
print(ustun.availableCans("Coca Cola"))
print(ustun.availableCans("Suv"))
print(ustun.availableCans("Sprite"))

# sell
print(ustun.sell(1, "Pepsi"))
