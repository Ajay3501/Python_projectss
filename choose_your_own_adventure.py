                               # ====================================================
                                       # Choose you path wisely Adventure game #
                               # ====================================================


ask = input("Hey buddy would you like to play a adventure game ? type (yes/no) : ").lower().strip()
if ask == "yes":
    print("Thank you lets start the game now .")
else:
    print("Oops ! okh we will play later. ")
    quit()

name = input("Type your first name here : ")
print("Welcome", name,"to this adventure.")

answer = input("Ajay you are on a dirt road, it has come to an end from here you can only go left or right which way would you like to go ?(left/right) ").lower().strip()

if answer == "left":
    answer = input("Now you come to a river, you can walk around it or swim across it what do you prefer ? (walk/swim) ").lower().strip()

    if answer == "walk":
        print("You walk many miles, ran out of water, you lost the game. ")
    elif answer == "swim":
        print("You swam across but eventually eaten by predator. ")
    else:
        print("Not a valid option you lose.")

elif answer == "right":
    answer = input("You come to a bridge, and it looks woobly, do you want to cross it or head back ? (cross/back) ").lower().strip()

    if answer == "cross":
        answer = input("Yeah ! you cross the bridge now you meet with a strangers, do you talk to them ? (yes/no). ").lower().strip()

        if answer == "yes":
            print("Hurray !!! You talked to the stranger and they give you a Gold plate, You Won. ")
        elif answer == "no":
            print("You ignored the stranger you lose.")
        else:
            print("Not a valid option you lose.")

    elif answer == "back":
        print("Oops you choose to go head back, unfortunately you lose.")
    else:
        print("Not a valid option,You lose. ")
else:
    print("Not a valid option,you lose. ")

print("Thank you for trying",name)