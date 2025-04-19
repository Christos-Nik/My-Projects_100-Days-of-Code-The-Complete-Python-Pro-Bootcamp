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
        print(f"Water: {resources['water']} ml.")
        print(f"Milk: {resources['milk']} ml.")
        print(f"Coffee: {resources['coffee']} g.")
    elif user_input in MENU: #checks if input is a valid option
        user_choice = MENU[user_input]
        ingredients = user_choice["ingredients"]

        can_make = True
        for ingredient, amount in ingredients.items():
            if resources.get(ingredient, 0) < amount:
                print(f"Sorry, not enough {ingredient}.")
                can_make = False
                break 

        if can_make is True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?:\n")) * 0.25
            dimes = int(input("How many dimes?:\n")) * 0.10
            nickels = int(input("How many nickels?:\n")) * 0.05
            pennies = int(input("How many pennies?:\n")) * 0.01
            total_paid = quarters + dimes + nickels + pennies
            cost = user_choice['cost']
            if total_paid >= cost:
                change = round(total_paid - cost, 2)
                if change > 0:
                    print(f"Here is your change: ${change}")
                
                print(f"Here is your {user_input}. Enjoy!")
                for ingredient, amount in ingredients.items():
                    resources[ingredient] -= amount
            else:
                print("Not enough money. Money refunded.")
    else:
        print("Wrong input, try again.")