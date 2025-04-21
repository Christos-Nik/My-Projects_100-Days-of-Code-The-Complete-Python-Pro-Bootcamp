from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide}
def calculator():
    print(logo)
    print("Welcome to this Python Calculator.")
    n1 = float(input("Please type the first number: \n"))
    operator = input("Please type what operator you would like to use. Valid options are +, -, *, /:\n")
    n2 = float(input("Please type the second number: \n"))

    new_calc = True
    while new_calc:
        if operator == "+":
            calculation = operation["+"](n1, n2)
            print(calculation)
        elif operator == "-":
            calculation = operation["-"](n1, n2)
            print(calculation)
        elif operator == "*":
            calculation = operation["*"](n1, n2)
            print(calculation)
        elif operator == "/":
            calculation = operation["/"](n1, n2)
            print(calculation)
        else:
            print("Wrong input.")
            new_calc = False

        continue_calc = input("Do you want to continue? Type 'yes' to continue or 'no' to start over.").lower()
        if continue_calc == "yes":
            new_calc = True
            n1 = calculation #assigns to variable 'n1' the value of the previous calculation(s)
            n2 = n2 = float(input("Please type the second number: \n"))
            operator = input("Please type what operator you would like to use. Valid options are +, -, *, /:\n")
            print(calculation)
        elif continue_calc == "no":
            new_calc = True
            n1 = float(input("Please type the first number: \n"))
            operator = input("Please type what operator you would like to use. Valid options are +, -, *, /:\n")
            n2 = float(input("Please type the second number: \n"))
        else:
            new_calc = False
            print("Goodbye.")

calculator()
