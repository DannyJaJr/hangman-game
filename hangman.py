import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


# Global variable
name_x = input("What is your name ? ")


def intro():
    name_x
    print_pause(f"{name_x} Are you ready hangman?")
    print_pause("Guess the right letter, then press Enter.")
    print_pause(f"{name_x} let's start.")


word = ["bye", "love", "rain", "new york",
        "alabama", "arizona", "arkansas", "california",
        "colorado", "connecticut", "delaware", "florida",
        "georgia", "idaho", "illinois", "indiana"]


def valid_input():
    secret = random.choice(word)
    guessWord = ""
    totalCount = 5
    while totalCount > 0:
        data = input(" Enter a letter: ")
        if data == "":
            wrongInput += 1
        else:
            guess = str(data.lower())
        if guess in secret:
            print_pause("Now add new letter(s)")
            print_pause(f"Corect! there's '{guess}' in the secret word")
        else:
            totalCount -= 1
            print_pause(f"No '{guess}' in in the secret word")
            print_pause(f"your total count is: {totalCount} left")
        guessWord = guessWord + guess
        wrongInput = 0
        for letter in secret:
            if letter in guessWord:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                wrongInput += 1
        if wrongInput == 0:
            print_pause(f" Congratulation! {name_x} with hangman")
            print_pause(f"the word is: {secret}! You won")
            play_again()
            break
    else:
        print_pause(f" Sorry {name_x} you lost")
        print_pause("Game Over! try again")
        play_again()


def play_again():
    new = input("Do you want to plain again Yes or No? ")
    if new.lower() == "yes":
        print_pause("Okay let's play")
        play_game()
    else:
        print_pause("That's a NO")
        print_pause(f"Good Bye {name_x}")


def play_game():
    intro()
    valid_input()


play_game()
