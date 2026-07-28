# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_total(number_list):

    total_value = 0

    for current_number in number_list:
        total_value = total_value + current_number

    return total_value


def calculate_average(number_list):

    total_value = calculate_total(number_list)
    average_value = total_value / len(number_list)

    return average_value


def find_maximum(number_list):

    maximum_value = number_list[0]

    for current_number in number_list:
        if current_number > maximum_value:
            maximum_value = current_number

    return maximum_value


def find_minimum(number_list):

    minimum_value = number_list[0]

    for current_number in number_list:
        if current_number < minimum_value:
            minimum_value = current_number

    return minimum_value


def main():

    number_count = int(input("How many numbers? "))

    if number_count <= 0:
        print("Error: The number must be a positive integer.")
        return

    entered_numbers = []

    for number_position in range(1, number_count + 1):
        user_number = float(input("Enter number " + str(number_position) + ": "))
        entered_numbers.append(user_number)

    total_result = calculate_total(entered_numbers)
    average_result = calculate_average(entered_numbers)
    maximum_result = find_maximum(entered_numbers)
    minimum_result = find_minimum(entered_numbers)

    print()
    print("Results:")
    print("Sum:    ", total_result)
    print("Average:", average_result)
    print("Maximum:", maximum_result)
    print("Minimum:", minimum_result)


main()