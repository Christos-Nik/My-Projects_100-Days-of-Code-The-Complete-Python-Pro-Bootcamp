from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

should_operate = True
selection = menu.get_items()

while should_operate is True:
    user_input = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    drink = menu.find_drink(user_input)
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        should_operate = False
        print("Machine is under maintenance.")
    elif user_input in ("espresso", "latte", "cappuccino"):
        if coffee_maker.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)