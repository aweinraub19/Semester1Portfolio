#1/9/25
#Multiplication Quiz

#init
import random
#func
def quiz():
    print("Welcome to the multiplication quiz!")
    challenge = str(input("What difficulty do you want to play? Easy, medium, or hard?")) #This variable records what difficulty the user wants to play so the range of numbers can be adjusted accordingly
    challenge = challenge.lower()
    print("You will answer 5 "+challenge+" questions! Get ready... \n.........................................")
    right = 0 #Variable that is used later in the code to calculate how many problems the user has gotten right
    if challenge == "easy":
        level = 5 #Level controls the right side of the range of numbers in the problems and gets bigger based on the user's selected difficulty
    elif challenge == "medium":
        level = 10
    elif challenge == "hard":
        level = 15
    for i in range (5):
        y = random.randint(1,level) #First number in the multiplication problem
        z = random.randint(1,level) #Second number in the multiplication problem
        x = int(input("What is "+str(y)+" X "+str(z)+"?")) #This variable stores the user's answer so it can be compared to the correct answer
        print("Your answer: "+str(x))
        if (y*z) == x:
            print("That is the correct answer!")
            right = right+1
        elif y*z != x:
            print("That is not the correct answer :(")
    print("You got "+str(right)+" out of 5 correct!")
#main
quiz()
