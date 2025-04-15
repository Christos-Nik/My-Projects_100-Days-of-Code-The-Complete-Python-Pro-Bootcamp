#Hangman game
#imports random module, and from 2 modules import specifically word list, stages and game's logo
import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list) #from the imported list picks a random word.
print(chosen_word)

print(logo)
lives = 6
placeholder = ""
word_length = len(chosen_word) #stores length of the word 
for letter in range(word_length): #loops according to length and makes a blank placeholder for the game
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = [] #makes a blank list with the correct guesses of user

while not game_over: #checks whether the game has finished and runs the loop.
    print(f"You have {lives} / 6 left")
    guess = input("Please guess a letter:\n").lower() 

    if guess in correct_letters: #Checks if the user already guessed this letter.
        print(f"You have already guessed this letter: {guess}. Try another.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) #if the above is true, appends the correct letter to the list
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
        
    print("Word to guess: " + display)

    if guess not in chosen_word: #uses not in to check if the guess of the player is not in the chosen word and deduct a life
        lives -= 1
        print("Wrong guess. You lose a life.")
        
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win!")
    
    print(stages[lives])