from art import logo, vs
from game_data import data
import random

player_score = 0
is_game_over = False
compare_a = {}
compare_b = {}
player_choice = {}
pc_choice = {}

def higher_lower():
    """This function initiates the game"""
    global player_choice, pc_choice, compare_b, compare_a
    compare_a = random.choice(data) #picks a random choice from dictionary and inserts it in a variable A
    compare_b = random.choice(data) #picsk a random choice from dictionary and inserts it in a variable B
    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}\n")
    guess = input("Who has more followers, 'A' or 'B'?:\n").lower()
    if guess == 'a':
        player_choice = compare_a
        pc_choice = compare_b
    else:
        player_choice = compare_b
        pc_choice = compare_a


while is_game_over is False:
    print(logo)
    higher_lower()
    if player_choice['follower_count'] > pc_choice['follower_count']:
        player_score += 1
        print(f"You are right! Current score: {player_score}")
    elif player_choice['follower_count'] < pc_choice['follower_count']:
        print(f"Wrong choice! Final score: {player_score}")
        is_game_over = True
