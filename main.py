
import random

def generateRandomNumber():
    return random.randint(1, 10)

def getUserInput():
    return int(input("Guess a number between 1 and 10"))

def check_user_input(user_input, random_number):
    if user_input == random_number:
        return True
    else:
        return False

def print_result(bool):
    if bool:
        print("You won!")
    else:
        print("You lost")

def playGame():
    randomNum = generateRandomNumber()
    user_input = getUserInput()
    if user_input > 10:
        print("Pick a number less than 10!")
        return
    elif user_input < 1:
        print("Pick a number greater than 1!")
        return
    print_result(check_user_input(user_input, randomNum))

playGame()

def play_game_repeat():
    while True:
        user_input = input("Do you want to play again? (y/n)")
        if user_input == 'n':
            break
        elif user_input == 'y':
            playGame()
        else:
            print("Invalid Input. Try again")
            print()

play_game_repeat()
