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

def check_guess(guess, answer, lower, upper):
    if guess > answer:
        print("Your guess was higher than the correct number")
        return True
    if guess < answer:
        print("Your guess was lower than the correct number")
        return True
    if guess == answer: 
        return False

def game():
    active = True
    while active == True:
        lower = int(input("Enter your lower bounds:"))
        upper = int(input("Enter your upper bounds:"))
        random_number = random.randint(lower,upper)
        print(f"The random number has been selected, we will be playing within {lower} and {upper}")
        playing = True
        while playing == True:
            guess = input("Enter your guess here:")
            if guess.isdigit():
                guess = int(guess)
                if guess >= lower and guess <= upper:
                    playing = check_guess(guess, random_number, lower, upper)
                else:
                    print("invalid number, try again")
            else:
                print("invalid entry, try again")
        print(f"Congratz you guessed {guess}, that was the correct number")
        repeat = input("Would you like to play again? (enter y or n)").lower()
        if repeat == 'y':
            pass
        else:
            print("Thanks for playing, see you!")
            active = False

    

game()

