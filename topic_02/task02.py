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

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", subtract(a, b))
elif op == "*":
    print("Result:", multiply(a, b))
elif op == "/":
    print("Result:", divide(a, b))
else:
    print("Unknown operation!")
