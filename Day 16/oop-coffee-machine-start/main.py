#imports appropriate classes from the modules below
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creates objects of the machine, menu and the money machine from the imported Classes
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


should_operate = True #created a should_operate statement for the while loop. Machine runs until its turned off with command "off"
selection = menu.get_items() 

while should_operate is True:
    user_input = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    drink = menu.find_drink(user_input) #Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None
    if user_input == "report": #Prints a report of all resources and current profit
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off": #Turns off the machine for maintenance
        should_operate = False
        print("Machine is under maintenance.")
    elif user_input in ("espresso", "latte", "cappuccino"): # checks if user input is a valid drink choice
        if coffee_maker.is_resource_sufficient(drink) == True: #if there are enough resources, procceeds to ask for payment
            if money_machine.make_payment(drink.cost) == True: #if payment process is valid, procceeds to make the drink
                coffee_maker.make_coffee(drink)