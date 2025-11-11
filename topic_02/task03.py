def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed!"
    return a / b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

match op:
    case "+":
        print("Result:", add(a, b))
    case "-":
        print("Result:", subtract(a, b))
    case "*":
        print("Result:", multiply(a, b))
    case "/":
        print("Result:", divide(a, b))
    case _:
        print("Unknown operation!")
