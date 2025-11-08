# here we are going to built a small model which asks some question from user and then display result of correct answer.

print("Welcome to my Computer Quiz ! ");

playing = input("Do you Want to Play ? ")

#asking user if he/she wants to play or not.
if playing != "yes":
    print("Thank you for your attention ! ")
    print("no worries we will play later !")
    quit()
    
print("Ok let's play the quiz game now :)")
# setting score counter which count each correct answer and store it in variable "score"
score = 0

#here it is the 1st question >>>>>
ques1 = input("What does CPU Stand for ? ")
if ques1.lower().strip() == "central processing unit":
    print(" Absolutely Correct answer :)")
    score += 1
else:
    print( "Oops Incorrect answer")
    
    
#here it is the 2nd question >>>>>
ques1 = input("What does GPU Stand for ? ")
if ques1.lower().strip() == "graphical processing unit":
    print(" Absolutely Correct answer :)")
    score += 1
else:
    print( "Oops Incorrect answer")
    
    
#here it is the 3rd question >>>>>
ques1 = input("What does ALU Stand for ? ")
if ques1.lower().strip() == "arithmatic logical unit":
    print(" Absolutely Correct answer :)")
    score += 1
else:
    print( "Oops Incorrect answer")
    
    
 #here it is the 4th question >>>>>
ques1 = input("What does IC Stand for ? ")
if ques1.lower().strip() == "interagated circuit":
    print(" Absolutely Correct answer :)")
    score += 1
else:
    print( "Oops Incorrect answer")


#here it is the 5th question >>>>>
ques1 = input("What does RAM Stand for ? ")
if ques1.lower().strip() == "random access memory":
    print(" Absolutely Correct answer :)")
    score += 1
else:
    print( "Oops Incorrect answer")


#here it is the 6th question >>>>>
ques1 = input("What does ROM Stand for ? ")
if ques1.lower().strip() == "read only memory":
    print(" Absolutely Correct answer :)")
    score += 1
else:
    print( "Oops Incorrect answer")


#here it is the 7th question  >>>>>
ques1 = input("What does ISRO Stand for ? ")
if ques1.lower().strip() == "indian space research organisation":
    print(" Absolutely Correct answer :)")
    score += 1
else:
    print( "Oops Incorrect answer")
    
    # here report of user is present >>>>>
print("your number of correct answer is " + str(score))
print("your correct attempt percentage is "+str(round((score/7)*100,2)) + " %")

print("Thankyou! :)")




