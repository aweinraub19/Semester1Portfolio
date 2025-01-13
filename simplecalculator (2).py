#11/18/24

#init
#functions
def add(num1, num2):
    ans = num1 + num2
    print("The answer is " + str(ans))
def subtract(num1, num2):
    ans = num1 - num2
    print("The answer is " + str(ans))
def multiply(num1, num2):
    ans = num1 * num2
    print("The answer is " + str(ans))
def divide(num1, num2):
    ans = num1 / num2
    print("The answer is " + str(ans))
def simplecalc():
    print("Welcome to Simple Calculator!")
    while True:
        print("Please choose an operation")
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit""")
        option = int(input("1-5: "))
        if option == 1:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            add(num1, num2)
        if option == 2:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            subtract(num1, num2)
        if option == 3:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            multiply(num1, num2)
        if option == 4:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            divide(num1, num2)
        if option == 5:
            print("Thanks for using this calculator!")
            break
#main
simplecalc()
