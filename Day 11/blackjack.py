import random
from art import logo




def deal():
    """Returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates hands score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21: #checks if user's hand contain an ACE and depending if user is over 21 to count as 1
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, pc_score):
    """Compares player's score with dealer's score and pick a winner (or a draw)"""
    if user_score == pc_score:
        return "It's a draw!"
    elif pc_score == 0:
        return "You lose. Dealer has a blackjack."
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over! You lose."
    elif pc_score > 21:
        return "Dealer drew over! Player wins!"
    elif user_score > pc_score:
        return "You win!"
    else:
        return "You lose."

def blackjack_game():
    print(logo)
    user_score = -1
    pc_score = -1
    user_hand = []
    pc_hand = []
    game_over = False
    for i in range(2):
        user_hand.append(deal())
        pc_hand.append(deal())


    while game_over is False:
        user_score = calculate_score(user_hand)
        pc_score = calculate_score(pc_hand)
        print(f"Your hand is: {user_hand}, current score: {user_score}")

        if user_score == 0 or pc_score == 0 or user_score > 21:
            game_over = True
        else:
            shall_draw = input("Do you wish to draw another card? type 'y' for yes or 'n' for to pass.").lower()
            if shall_draw == "y":
                user_hand.append(deal())
            else:
                game_over = True

    while pc_score != 0 and pc_score < 17:
        pc_hand.append(deal())
        pc_score = calculate_score(pc_hand)

    print(f"Your hand is: {user_hand} with a score of {user_score}")
    print(f"Dealer hand is: {pc_hand} with a score of {pc_score}")
    print(compare(user_score, pc_score))


while input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no.").lower() == "y":
    print("\n" * 20) #clears the line to initiate a new game
    blackjack_game()
