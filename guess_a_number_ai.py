#Guess A Number A.I
#Dashiona T
import random
import math

# config



# helper functions
def show_start_screen():
    print("  ___  __  __  ____  ___  ___      __      _  _  __  __  __  __  ____  ____  ____      __      ____ /\ ")
    print(" / __)(  )(  )( ___)/ __)/ __)    /__\    ( \( )(  )(  )(  \/  )(  _ \( ___)(  _ \    /__\    (_  _))( ")
    print("( (_-. )(__)(  )__) \__ \\__ \    /(__)\    )  (  )(__)(  )    (  ) _ < )__)  )   /   /(__)\    _)(_ \/ ")
    print(" \___/(______)(____)(___/(___/  (__)(__)  (_)\_)(______)(_/\/\_)(____/(____)(_)\_)  (__)(__)()(____)() ")                                                                                                                                        

def show_credits():
    print("  /$$$$$$$$ /$$       /$$                                                                                                          ")
    print(" |__  $$__/| $$      |__/                                                                                                          ")
    print("    | $$   | $$$$$$$  /$$  /$$$$$$$        /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$  /$$  /$$  /$$$$$$   /$$$$$$$      ")
    print("    | $$   | $$__  $$| $$ /$$_____/       /$$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$ | $$ | $$ |____  $$ /$$_____/      ")
    print("    | $$   | $$  \ $$| $$|  $$$$$$       | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$ | $$ | $$  /$$$$$$$|  $$$$$$       ")
    print("    | $$   | $$  | $$| $$ \____  $$      | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$ | $$ | $$ /$$__  $$ \____  $$      ")
    print("    | $$   | $$  | $$| $$ /$$$$$$$/      |  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$/$$$$/|  $$$$$$$ /$$$$$$$/      ")
    print("   |__/   |__/  |__/|__/|_______/        \____  $$ \_______/|__/ |__/ |__/ \_______/       \_____/\___/  \_______/|_______/        ")
    print("                                         /$$  \ $$                                                                                 ")
    print("                                        |  $$$$$$/                                                                                 ")
    print("                                         \______/                                                                                  ")
    print("                                           /$$                     /$$       /$$                       /$$$$$$$            /$$     ")
    print("                                          | $$                    | $$      | $$                      | $$__  $$          |__/     ")
    print("  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$      | $$$$$$$  /$$   /$$      | $$  \ $$  /$$$$$$  /$$     ")
    print(" /$$_____/ /$$__  $$ /$$__  $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$      | $$__  $$| $$  | $$      | $$  | $$ |____  $$| $$     ")
    print("| $$      | $$  \__/| $$$$$$$$  /$$$$$$$  | $$    | $$$$$$$$| $$  | $$      | $$  \ $$| $$  | $$      | $$  | $$  /$$$$$$$| $$     ")
    print("| $$      | $$      | $$_____/ /$$__  $$  | $$ /$$| $$_____/| $$  | $$      | $$  | $$| $$  | $$      | $$  | $$ /$$__  $$| $$     ")
    print("|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$$      | $$$$$$$/|  $$$$$$$      | $$$$$$$/|  $$$$$$$| $$     ")
    print("\_______/|__/       \_______/ \_______/   \___/   \_______/ \_______/       |_______/  \____  $$      |_______/  \_______/|__/     ") 
    print("                                                                                       /$$  | $$                                   ")
    print("                                                                                      |  $$$$$$/                                   ")
    print("                                                                                      \______/                                     ")
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    guess = (current_low + current_high) // 2
    return guess

def pick_number(low, high,limit):
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print("Think of a number from " + str(low) + " to " +
    str(high) +" and I will try to guess it and I will get a total of " + limit + " tries. Press Enter when you are ready.")
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
    answer= answer.lower()
    
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
        decision= decision.lower()
        
        if decision == 'yes' or decision == 'y':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    print("Enter the lowest number you want me to be able to guess.")
    current_low = input()
    current_low = int(current_low)
    
    print("Enter the highest number you want me to be able to guess.")
    current_high = input()
    current_high = int(current_high)
    
    check = -1
    limit = math.ceil(math.log(current_high - current_low + 1, 2))

    pick_number(current_low, current_high)
    
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



