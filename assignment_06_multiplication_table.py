# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(selected_number):

    print("Multiplication Table for", selected_number)

    for multiplier_number in range(1, 13):

        multiplication_result = selected_number * multiplier_number

        print(
            selected_number,
            "x",
            multiplier_number,
            "=",
            multiplication_result
        )


def print_multiple_tables(last_table_number):

    for current_table_number in range(1, last_table_number + 1):

        print()
        print("Multiplication Table for", current_table_number)

        for multiplier_number in range(1, 13):

            multiplication_result = (
                current_table_number * multiplier_number
            )

            print(
                current_table_number,
                "x",
                multiplier_number,
                "=",
                multiplication_result
            )

        print("---------------------------")


def main():

    print("MULTIPLICATION TABLE GENERATOR")
    print("1. Print one multiplication table")
    print("2. Print multiplication tables from 1 to N")

    selected_option = int(input("Choose an option: "))

    if selected_option == 1:

        selected_number = int(
            input("Enter a number: ")
        )

        print_single_table(selected_number)

    elif selected_option == 2:

        last_table_number = int(
            input("Enter a positive number: ")
        )

        if last_table_number <= 0:
            print("Error: The number must be a positive integer.")
            return

        print_multiple_tables(last_table_number)

    else:
        print("Error: Please choose option 1 or 2.")


main()