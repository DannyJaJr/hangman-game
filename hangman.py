import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    name = input("What is your name ? ")
    print_pause(f"{name} Are you ready hangman?")
    print_pause("Guess the right letter, then press Enter.") 
    print_pause(f"{name} let's start.")
   

word = ["bye", "love", "rain", "new york", 
        "alabama", "arizona", "arkansas", "california", 
        "colorado", "connecticut", "delaware", "florida", 
        "georgia", "idaho", "illinois", "indiana"]


def valid_input():
    secret = random.choice(word)
    guessWord = ""
    totalCount = 5
    wrongInput = 0

    while totalCount > 0:
        data = input(" Enter a letter: ")
        if data == "":
            wrongInput += 1
        else:
            guess = str(data.lower())
        if guess in secret:
            print_pause(f"Corect! there is on more {guess} in the secret word")
        else:
            totalCount -= 1
            print_pause(f"No {guess} in XXXX word. Remains {totalCount} left")
        guessWord = guessWord + guess

        for letter in secret:
            if letter in guessWord:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                wrongInput += 1
        if wrongInput == 0:
            print_pause(f" Congrstulation! the word was : {secret} you won")
            secret = random.choice(word)
            break
    else:
        print_pause("Sorry you lost")
        secret = random.choice(word)
        print_pause("Game Over! try again")
        

def play_game():
    intro()
    n = 1
    while n == 1:
        valid_input()

    
play_game()
