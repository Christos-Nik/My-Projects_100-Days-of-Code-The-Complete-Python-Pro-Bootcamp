from art import logo, vs
from game_data import data
import random

# Initialize game
player_score = 0
is_game_over = False
compare_a = random.choice(data)
compare_b = random.choice(data)

# Ensure A and B are different initially
while compare_b == compare_a:
    compare_b = random.choice(data)

def higher_lower():
    """Displays the comparison and gets user's guess."""
    global compare_a, compare_b, player_choice, pc_choice
    
    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}\n")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == 'a':
        player_choice = compare_a
        pc_choice = compare_b
    else:
        player_choice = compare_b
        pc_choice = compare_a

# Game loop
while not is_game_over:
    print(logo)
    higher_lower()
    
    if player_choice['follower_count'] > pc_choice['follower_count']:
        player_score += 1
        print(f"✅ Correct! Current score: {player_score}")
        
        # Update compare_a (correct answer) and pick a new compare_b
        compare_a = player_choice
        compare_b = random.choice(data)
        
        # Ensure compare_b is not the same as compare_a
        while compare_b == compare_a:
            compare_b = random.choice(data)
    else:
        print(f"❌ Game Over! Final score: {player_score}")
        is_game_over = True