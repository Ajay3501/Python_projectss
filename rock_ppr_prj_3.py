                    #=======================================================================
                                      # Rock  Paper Scissors game #
                    #=======================================================================


import random

user_wins = 0                                   # to calculate score
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type rock/paper/scissors or q to quit. ").lower().strip()      # getting input from user
    if user_input == "q":
        print("Ookh ! we will play later .")
        break
    if user_input not in options :
        print("Oops ! pls enter valid text")
        continue

    random_number = random.randint(0,2)                                                #  computer random number
                                              # rock : 0 ,   paper : 1   scissor :2
    computer_pick = options[random_number]

    print("Computer picked",computer_pick,".")

    if user_input == "rock" and computer_pick == "scissors":                           # condition for win
        print("Hurray ! You Won.")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Hurray ! You Won.")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Hurray ! You Won.")
        user_wins += 1

    elif user_input == computer_pick:                                                  # tie handling
        print("Aww Its a tie !!")
        continue

    else:
        print("Oops ! You lost.")
        computer_wins += 1

print("You Won",user_wins,"times")
print("computer Won",computer_wins,"times")
print("Thank you !!")
print("Have a nice day. ")