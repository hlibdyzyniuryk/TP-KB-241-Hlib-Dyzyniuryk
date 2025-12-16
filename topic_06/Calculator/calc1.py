import functions1
import operations1
import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("=== Simple Calculator ===")

while True:
    op = operations1.choose_operation()

    if op not in ['1', '2', '3', '4']:
        print("Invalid operation. Please try again.")
        logging.warning("Invalid operation selected")
        continue

    a, b = operations1.get_numbers()
    logging.info(f"Input numbers: a={a}, b={b}")

    if op == '1':
        result = functions1.add(a, b)
        operation_name = "Addition"
    elif op == '2':
        result = functions1.subtract(a, b)
        operation_name = "Subtraction"
    elif op == '3':
        result = functions1.multiply(a, b)
        operation_name = "Multiplication"
    elif op == '4':
        result = functions1.divide(a, b)
        operation_name = "Division"

    print("Result:", result)
    logging.info(f"Operation: {operation_name}, Result: {result}")

    next_action = input("\nDo you want to perform another operation? (y/n): ").lower()
    if next_action != 'y':
        logging.info("Calculator closed by user")
        print("Exiting the calculator. Goodbye!")
        break
