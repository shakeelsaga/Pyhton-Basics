import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a % b

def calculate(expression):
    # Match valid expressions like: number operator number (e.g., 10+40)
    match = re.fullmatch(r'\s*(-?\d+(?:\.\d*)?)\s*([\+\-\*/%])\s*(-?\d+(?:\.\d*)?)\s*', expression)
    if not match:
        raise ValueError("Invalid expression format.")

    operand1, operator, operand2 = match.groups()
    num1 = float(operand1)
    num2 = float(operand2)

    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '%':
        return modulus(num1, num2)
if __name__ == "__main__":
    print("Welcome to the Simple Calculator!\n")
    print("Operations allowed are: +, -, *, /, %")
    print("Enter expressions in the format: number operator number (e.g., 10 + 20)\n")

    while True:
        try:
            user_input = input("Enter an expression: ")
            result = calculate(user_input)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

        while True:
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont in ['yes', 'no']:
                break
            print("Please answer with 'yes' or 'no'.\n")
        if cont == 'no':
            print("\nThank you for using the calculator!")
            break
        print()