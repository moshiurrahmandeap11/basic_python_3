# Simple Calculator (OOP)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus ( a, b):
    return a % b


def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = input("Enter choice (1/2/3/4/5): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == "5":
        print(f"{num1} % {num2} = {modulus(num1, num2)}")
    else:
        print("Invalid input")


# Example usage
calculator()