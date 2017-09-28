#Guess A Number A.I
#Dashiona T
import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    print("This awesome game was created by Dai.")
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    guess = (current_low + current_high) // 2
    return guess

def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print("Think of a number from " + str(low) + " to " +
    str(high) +" and I will try to guess it and I will get a total of 7 tries. Press Enter when you are ready.")
    input()

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print(" Was " + str(guess) + " too high, too low, or correct?")
    answer = input()
    if answer == 'too low' or answer == 'to low':
        return -1
    if answer == 'too high' or answer == 'to high':
        return 1
    if answer == 'correct':
        return 0

def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    print("I win!!")
   


def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'yes' or decision == 'y':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
           current_low = guess
        elif check == 1:
            # adjust current_high
            current_high = guess

    show_result()


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



