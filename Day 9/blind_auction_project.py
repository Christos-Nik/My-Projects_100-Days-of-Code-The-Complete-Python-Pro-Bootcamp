def find_highest_bidder(bidding_dictionary):
    """This function compares the bid amount of each bidder and picks the winner"""
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of $ {highest_bid}")

from art import logo
print(logo)

bid_list = {} #makes an empty dictionary of the bidders' list

continue_bid = True
while continue_bid: #as long as statement is true, runs the while loop
    name = input("Please enter your name:\n")
    bid = int(input("What is your bid:\n$"))

    bid_list[name] = bid #appends to each bidder in dictionary their bid amount
    check = input("Are there are more bidders? Type 'yes' or 'no':\n").lower()

    if check == "no": #ends the while loop and finds the highest bidder
        continue_bid = False 
        find_highest_bidder(bid_list)
    elif check == "yes":
        print("\n" * 2)  # clears the output so bidders don't "cheat"





