import random

# config
low = 1
high = 100
limit = 5
rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")

guess = -1
tries = 0

while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1

# tell player out come
if guess == rand:
    print ("You Win!")
else:
    print ("You suck.... Take your L... The number I was thinking of was " + str(rand) + ".")
    
