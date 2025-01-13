#12/9/24
#Mad Libs

#input
#functions
def madlibs():
    print("Hi! Welcome to Mad Libs! In this game you will fill in the blanks to create a funny story")
    print("You will have to input specific types of words like nouns, verbs, and adjectives.")
    print("Let's get started!")
    name = input("Please input a name")
    person = input("Please input a type of person (grandpa, cousin, friend, etc.)")
    location = input("Please input a location")
    food = input("Please input a food")
    animal = input("Please input an animal")
    adjective = input("Please input an adjective")
    print("Once upon a time there was a little girl named "+name+" who was going to visit her "+person+".")
    print("She walked through the "+location+ " while holding a basket filled with "+food+", and she heard a startling sound!")
    print("A huge "+animal+" popped out of the trees and noticed where she was going.")
    print("By the time she got to her "+person+"'s house, she noticed something strange.")
    print("What "+adjective+" eyes it had! What "+adjective+" ears it had! What a "+adjective+" mouth it had!")
    print("Her "+person+" hopped out of the bed and started chasing her through the "+location+", but she escaped just in time and found her real "+person+"!")
#main
madlibs()

