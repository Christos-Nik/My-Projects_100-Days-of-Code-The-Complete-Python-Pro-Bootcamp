from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()

should_operate = True
while should_operate is True:
    user_input = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if user_input == "report":
        print(coffee_maker.report)
    elif user_input == "off":
        should_operate = False
        print("Machine is under maintenance.")