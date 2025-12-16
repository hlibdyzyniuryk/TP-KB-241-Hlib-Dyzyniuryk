from operations2 import Operations

class Calculator:
    def __init__(self):
        self.operations = Operations()

    def calculate(self, choice, a, b):
        if choice == '1':
            return self.operations.add(a, b)
        elif choice == '2':
            return self.operations.subtract(a, b)
        elif choice == '3':
            return self.operations.multiply(a, b)
        elif choice == '4':
            return self.operations.divide(a, b)
        else:
            return "Invalid operation"
