from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
pc_number = random.choice(range(1,101))
print(f"For testing purposes PC number is {pc_number}.")
game_difficulty = input("Please pick a difficulty level. Type 'easy' (10 tries) or 'hard' (5 tries).").lower()
attempts = 0
is_game_over = False
if game_difficulty == 'easy':
    attempts = 10
elif game_difficulty == 'hard':
    attempts = 5
else:
    print("Wrong Input")

while is_game_over is False:
    guess = int(input(f"You have {attempts} attempts to guess the number.\nMake a guess:"))
    if guess == pc_number:
        is_game_over = True
        print(f"Congrats! The answer was {pc_number}")
    elif guess > pc_number:
        print("Too high.")
        attempts -= 1
        if attempts == 0:
            is_game_over = True
            print(f"You lose. My number was {pc_number}.")
    elif guess < pc_number:
        print("Too low.")
        attempts -= 1
        if attempts == 0:
            is_game_over = True
            print(f"You lose. My number was {pc_number}.")