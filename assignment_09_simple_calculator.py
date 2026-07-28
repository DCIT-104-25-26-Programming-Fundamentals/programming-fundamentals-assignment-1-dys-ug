# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_numbers(first_number, second_number):

    addition_result = first_number + second_number

    return addition_result


def subtract_numbers(first_number, second_number):

    subtraction_result = first_number - second_number

    return subtraction_result


def multiply_numbers(first_number, second_number):

    multiplication_result = first_number * second_number

    return multiplication_result


def divide_numbers(first_number, second_number):

    if second_number == 0:
        return None

    division_result = first_number / second_number

    return round(division_result, 2)


def find_modulus(first_number, second_number):

    if second_number == 0:
        return None

    modulus_result = first_number % second_number

    return modulus_result


def calculate_power(first_number, second_number):

    exponent_result = first_number ** second_number

    return exponent_result


def display_menu():

    print()
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():

    calculator_running = True

    while calculator_running == True:

        display_menu()

        selected_operation = input(
            "Select an operation (1-7): "
        )

        if selected_operation == "7":
            print("Goodbye!")
            calculator_running = False
            continue

        if selected_operation not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Please choose a number from 1 to 7.")
            continue

        first_number = float(
            input("Enter first number : ")
        )

        second_number = float(
            input("Enter second number: ")
        )

        if selected_operation == "1":

            calculation_result = add_numbers(
                first_number,
                second_number
            )

            print(
                "Result:",
                first_number,
                "+",
                second_number,
                "=",
                calculation_result
            )

        elif selected_operation == "2":

            calculation_result = subtract_numbers(
                first_number,
                second_number
            )

            print(
                "Result:",
                first_number,
                "-",
                second_number,
                "=",
                calculation_result
            )

        elif selected_operation == "3":

            calculation_result = multiply_numbers(
                first_number,
                second_number
            )

            print(
                "Result:",
                first_number,
                "*",
                second_number,
                "=",
                calculation_result
            )

        elif selected_operation == "4":

            calculation_result = divide_numbers(
                first_number,
                second_number
            )

            if calculation_result == None:
                print("Error: Cannot divide by zero.")

            else:
                print(
                    "Result:",
                    first_number,
                    "/",
                    second_number,
                    "=",
                    calculation_result
                )

        elif selected_operation == "5":

            calculation_result = find_modulus(
                first_number,
                second_number
            )

            if calculation_result == None:
                print("Error: Cannot calculate modulus by zero.")

            else:
                print(
                    "Result:",
                    first_number,
                    "%",
                    second_number,
                    "=",
                    calculation_result
                )

        elif selected_operation == "6":

            calculation_result = calculate_power(
                first_number,
                second_number
            )

            print(
                "Result:",
                first_number,
                "**",
                second_number,
                "=",
                calculation_result
            )


main()