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

while True:
    print("\nSimple Calculator")
    print("Enter 'exit' to quit.")
    
    a = input("Enter the first number: ")
    if a.lower() == "exit":
        break
    b = input("Enter the second number: ")
    if b.lower() == "exit":
        break
    op = input("Enter operation (+, -, *, /): ")
    if op.lower() == "exit":
        break

    a = float(a)
    b = float(b)

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
