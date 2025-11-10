                          # Here we are gonna create Game called Number Guesser
            # ==============================================================================#
import random

top_of_range = input("Type a Number upto a max limit : ")   # asking user to set top limit.

if top_of_range.lstrip('-').isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Oops ! Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time. ")
    quit()

random_number = random.randint(0,top_of_range)          # generating random number

Guessess = 0                                            # guess counter

while True:                                             # creating loop to ask multiple time
    Guessess += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("Congratulations ! You got it.")
        print("Thank you for your time.")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

print("You got it in",Guessess, "Guessess.")
