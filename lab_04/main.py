class RPNCalculator:
    def __init__(self):
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def infix_to_rpn(self, expression):
        output = []
        stack = []
        i = 0
        while i < len(expression):
            token = expression[i]
            if token.isdigit() or token == '.':
                num = token
                while i + 1 < len(expression) and (expression[i+1].isdigit() or expression[i+1] == '.'):
                    i += 1
                    num += expression[i]
                output.append(num)
            elif token in self.operators:
                while (stack and stack[-1] in self.operators and
                       ((self.operators[token] <= self.operators[stack[-1]] and token != '^') or
                        (self.operators[token] < self.operators[stack[-1]] and token == '^'))):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")
            elif token == ' ':
                pass
            else:
                raise ValueError(f"Unknown token: {token}")
            i += 1
        while stack:
            if stack[-1] in '()':
                raise ValueError("Mismatched parentheses")
            output.append(stack.pop())
        return output

    def evaluate_rpn(self, rpn_tokens):
        stack = []
        for token in rpn_tokens:
            if token not in self.operators:
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)
        if len(stack) != 1:
            raise ValueError("Error in RPN evaluation")
        return stack[0]


def main():
    calc = RPNCalculator()
    expr = input("Enter infix expression: ")
    try:
        rpn = calc.infix_to_rpn(expr)
        print("RPN:", ' '.join(rpn))
        result = calc.evaluate_rpn(rpn)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
