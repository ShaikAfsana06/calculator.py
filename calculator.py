import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    print("=== Simple Command-line Calculator ===")
    print("Supports: +, -, *, /")
    print("Example: 5+3 or 12.5 * 2")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter expression: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Use regex to extract operands and operator
        match = re.match(r'\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$', user_input)
        if not match:
            print("Invalid input! Please enter in format like 5+3 or 8 * 2\n")
            continue

        a = float(match.group(1))
        op = match.group(2)
        b = float(match.group(3))

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)

        print(f"Result: {result}\n")

if __name__ == "__main__":
    calculator()
