MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
should_operate = True
#TODO: 1. Prompt user by asking "What would you like? (espresso, latte, capuccino):"
while should_operate is True:
    user_input = input("What would you like? (espresso/latte/cappuccino):\n").lower()
#TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if user_input == "off": #checks for the secret word for maintainers to turn off the coffee machine
        should_operate = False
#TODO: 3. Print report
    elif user_input == "report":
        print(resources)
#TODO: 4. Check resources efficient?
    elif user_input == "espresso":
#TODO: 5. Process coins

#TODO: 6. Check transaction successful? 

#TODO: 7. Make coffee