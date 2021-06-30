# start loop
    # Take input for upper bound
    # Take input for lower bound
    # Select a random number between the u/l bounds
    # start loop 
        # ask for guess
            # evaulate guess
            # if incorrect
                # higher or lower output
            # if correct
                # break loop
                # show victory
        # ask if they want to play again
        # break loop

import random

# little function to check our guesses so we dont have to croud our main function for the game
def check_guess(guess, answer):
    if guess > answer:
        print("Your guess was higher than the correct number")
        return True
    if guess < answer:
        print("Your guess was lower than the correct number")
        return True
    if guess == answer: 
        return False

def game():
    # starting our game loop with a flag variable, so we can exit this loop from anywhere within the 
    # loop by changing the active variable to false
    active = True
    while active == True:
        lower = int(input("Enter your lower bounds:"))
        upper = int(input("Enter your upper bounds:"))
        # using the random library to quickly select an interger to work with
        random_number = random.randint(lower,upper)
        # formatted strings for the win
        print(f"The random number has been selected, we will be playing within {lower} and {upper}")
        # another loop with a flag variable to allow for 'infinite' guesses and checking for their 
        # validity
        playing = True
        while playing == True:
            guess = input("Enter your guess here:")
            # checking to make sure the input string has only digit like characters
            if guess.isdigit():
                # changing the data type from str to int
                guess = int(guess)
                # checking to make sure the guess is within the bounds
                if guess >= lower and guess <= upper:
                    # refers to the function we made earlier to check the guess against the answer
                    # if the answer is wrong, the flag will remain True, if it is correct the flag 
                    # will change to False, thus ending this loop
                    playing = check_guess(guess, random_number)
                else:
                    # send back wrong numbers to the start of this loop
                    print("invalid number, try again")
            else:
                # send back non numbers to the start of this loop
                print("invalid entry, try again")
        # winner winner chicken dinner
        print(f"Congratz you guessed {guess}, that was the correct number")
        # wanna play again?
        repeat = input("Would you like to play again? (enter y or n)").lower()
        if repeat == 'y':
            pass
        else:
            print("Thanks for playing, see you!")
            active = False

    
# running our function!
game()

