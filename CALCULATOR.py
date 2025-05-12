#Task-2 --> Calculator

def add(a,b):
    print(f"\nAddition of {a} and {b} is {a+b}.")

def sub(a,b):
    print(f"\nSubtraction of {a} and {b} is {a-b}.")

def mul(a,b):
    print(f"\nMultiplication of {a} and {b} is {a*b}.")

def div(a,b):
    if b==0:
        print("Division by 0 is not possible..")
    else:
        print(f"\nDivision of {a} and {b} is {a/b}.")


while True:
    print("--CALCULATOR--")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    operation = int(input("What do you want to do:"))

    while operation < 1 or operation > 5:

        operation = int(input("Enter a valid input:"))

    if operation == 5:
        print("Closing calculator...")
        print("Goodbye")
        break

    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if operation == 1:
            add(num1,num2)

        elif operation == 2:
            sub(num1,num2)

        elif operation == 3:
            mul(num1,num2)

        elif operation == 4:
            div(num1,num2) 
    
    except ValueError:
        print("Error: Please enter valid numeric inputs.")