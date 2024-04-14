from art import logo


# Addition
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)
    should_continue = True

    while should_continue == True:
        operator = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operator]
        answer = (calculation_function(num1, num2))

        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ") == "y":
            num1 = answer
            should_continue = True
        else:
            should_continue = False
            calculator()


calculator()