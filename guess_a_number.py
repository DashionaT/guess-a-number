import random
import math

# config
low = 1
high = 100

# helper functions
def show_start_screen():
    
    print("  ________                                        _______               ___.                ._.")
    print(" /  _____/ __ __   ____   ______ ______ _____     \      \  __ __  _____\_ |__   ___________| |")
    print("/   \  ___|  |  \_/ __ \ /  ___//  ___/ \__  \    /   |   \|  |  \/     \| __ \_/ __ \_  __ \ |")
    print("\    \_\  \  |  /\  ___/ \___ \ \___ \   / __ \_ /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\|")
    print(" \______  /____/  \___  >____  >____  > (____  / \____|__  /____/|__|_|  /___  /\___  >__|   __")
    print("        \/            \/     \/     \/       \/          \/            \/    \/     \/       \/")

def show_credits():
    print("This awesome game was created by Dai.")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")
        print()
        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +". You will get a total of 7 tries.")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
        
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You're so stupid....take your L.....The number I was thinking of was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision= decision.lower()
        
        print("")
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    limit = math.ceil(math.log(high - low + 1, 2))
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
