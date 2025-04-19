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
while should_operate is True:
    user_input = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if user_input == "off": #checks for the secret word for maintainers to turn off the coffee machine
        should_operate = False
    elif user_input == "report":
        print(resources)
    elif user_input == "espresso":
        user_choice = MENU[user_input]
        if user_choice[ingredients['water']] < resources['water']:
            print("Sorry not enough water")
        elif user_choice['milk'] < resources['milk']:
            print("Sorry not enough milk.")
        elif user_choice['coffee'] < resources['coffee']:
            print("Sorry not enough coffee.")
    elif user_input == "latte":
        user_choice = MENU[user_input]
        if user_choice['water'] < resources['water']:
            print("Sorry not enough water")
        elif user_choice['milk'] < resources['milk']:
            print("Sorry not enough milk.")
        elif user_choice['coffee'] < resources['coffee']:
            print("Sorry not enough coffee.")
    elif user_input == "cappuccino":
        user_choice = MENU[user_input]
        if user_choice['water'] < resources['water']:
            print("Sorry not enough water")
        elif user_choice['milk'] < resources['milk']:
            print("Sorry not enough milk.")
        elif user_choice['coffee'] < resources['coffee']:
            print("Sorry not enough coffee.")
    else:
        print("Wrong input, try again.")    
#TODO: 5. Process coins

#TODO: 6. Check transaction successful? 

#TODO: 7. Make coffee.