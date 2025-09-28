while True:
    expr = input("Enter expression (or type 'exit' to quit): ")
    if expr.lower() == "exit":
        print("Program finished.")
        break
    try:
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
