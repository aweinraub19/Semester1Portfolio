#Name
#Date
#Rock Paper Scissors

#init
import random

#function
def rps():
    print("Welcome to rock paper scissors!")
    print("Your goal is to beat the computer!")
    cwin = 0
    pwin = 0
    tie = 0
    while True:
        player = input("Rock (R), Paper (P), or Scissors (S)?")
        computer = random.randint(1,3)
        if computer == 1:
            computer = "R"
            print("The computer's move is Rock!")
        if computer == 2:
            computer = "P"
            print("The computer's move is Paper!")
        if computer == 3:
            computer = "S"
            print("The computer's move is Scissors!")
        if player == "R" and computer == "R":
            print("You tied with the computer")
            win = "Tie"
        if player == "R" and computer == "P":
            print("You lost to the computer :(")
            win = "No"
        if player == "R" and computer == "S":
            print("You beat the computer!")
            win = "Yes"
        if player == "P" and computer == "P":
            print("You tied with the computer")
            win = "Tie"
        if player == "P" and computer == "S":
            print("You lost to the computer :(")
            win = "No"
        if player == "P" and computer == "R":
            print("You beat the computer!")
            win = "Yes"
        if player == "S" and computer == "S":
            print("You tied with the computer")
            win = "Tie"
        if player == "S" and computer == "R":
            print("You lost to the computer :(")
            win = "No"
        if player == "S" and computer == "P":
            print("You beat the computer!")
            win = "Yes"
        if win == "Yes":
            pwin = 1 + pwin
        if win == "No":
            cwin = cwin + 1
        if win == "Tie":
            tie = tie + 1
        print("Your wins: "+str(pwin)+" / Computer wins: "+str(cwin)+" / Ties: "+str(tie))
        game = input("Would you like to keep playing? Yes (Y) or No (N)?")
        if game == "Y":
            print("Time for a new round!")
        if game == "N":
            print ("Thank you for playing!")
            break

#main
rps()





