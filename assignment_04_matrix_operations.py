# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def enter_matrix(number_of_rows, number_of_columns):

    matrix_values = []

    for row_number in range(number_of_rows):

        current_row = input(
            "Enter row " + str(row_number + 1) + ": "
        ).split()

        while len(current_row) != number_of_columns:
            print("Please enter exactly", number_of_columns, "numbers.")

            current_row = input(
                "Enter row " + str(row_number + 1) + " again: "
            ).split()

        converted_row = []

        for current_value in current_row:
            converted_row.append(int(current_value))

        matrix_values.append(converted_row)

    return matrix_values


def display_matrix(matrix_values):

    for current_row in matrix_values:

        for current_value in current_row:
            print(f"{current_value:6}", end="")

        print()


def transpose_matrix(original_matrix):

    number_of_rows = len(original_matrix)
    number_of_columns = len(original_matrix[0])

    transposed_matrix = []

    for column_position in range(number_of_columns):

        new_row = []

        for row_position in range(number_of_rows):
            new_row.append(
                original_matrix[row_position][column_position]
            )

        transposed_matrix.append(new_row)

    return transposed_matrix


def add_matrices(first_matrix, second_matrix):

    number_of_rows = len(first_matrix)
    number_of_columns = len(first_matrix[0])

    added_matrix = []

    for row_position in range(number_of_rows):

        new_row = []

        for column_position in range(number_of_columns):

            added_value = (
                first_matrix[row_position][column_position]
                + second_matrix[row_position][column_position]
            )

            new_row.append(added_value)

        added_matrix.append(new_row)

    return added_matrix


def multiply_matrices(first_matrix, second_matrix):

    first_matrix_rows = len(first_matrix)
    first_matrix_columns = len(first_matrix[0])
    second_matrix_columns = len(second_matrix[0])

    multiplied_matrix = []

    for row_position in range(first_matrix_rows):

        new_row = []

        for column_position in range(second_matrix_columns):

            total_value = 0

            for common_position in range(first_matrix_columns):

                total_value = total_value + (
                    first_matrix[row_position][common_position]
                    * second_matrix[common_position][column_position]
                )

            new_row.append(total_value)

        multiplied_matrix.append(new_row)

    return multiplied_matrix


def main():

    print("MATRIX OPERATIONS")
    print("1. Transpose a matrix")
    print("2. Add two matrices")
    print("3. Multiply two matrices")

    selected_option = int(input("Choose an option: "))

    if selected_option == 1:

        number_of_rows = int(input("Enter number of rows: "))
        number_of_columns = int(input("Enter number of columns: "))

        original_matrix = enter_matrix(
            number_of_rows,
            number_of_columns
        )

        transposed_result = transpose_matrix(original_matrix)

        print("\nOriginal Matrix:")
        display_matrix(original_matrix)

        print("\nTransposed Matrix:")
        display_matrix(transposed_result)

    elif selected_option == 2:

        number_of_rows = int(input("Enter number of rows: "))
        number_of_columns = int(input("Enter number of columns: "))

        print("\nEnter Matrix A")
        first_matrix = enter_matrix(
            number_of_rows,
            number_of_columns
        )

        print("\nEnter Matrix B")
        second_matrix = enter_matrix(
            number_of_rows,
            number_of_columns
        )

        added_result = add_matrices(
            first_matrix,
            second_matrix
        )

        print("\nMatrix A:")
        display_matrix(first_matrix)

        print("\nMatrix B:")
        display_matrix(second_matrix)

        print("\nAdded Matrix:")
        display_matrix(added_result)

    elif selected_option == 3:

        first_matrix_rows = int(
            input("Enter rows for Matrix A: ")
        )

        first_matrix_columns = int(
            input("Enter columns for Matrix A: ")
        )

        second_matrix_rows = int(
            input("Enter rows for Matrix B: ")
        )

        second_matrix_columns = int(
            input("Enter columns for Matrix B: ")
        )

        if first_matrix_columns != second_matrix_rows:
            print(
                "Error: Columns of Matrix A must equal rows of Matrix B."
            )
            return

        print("\nEnter Matrix A")
        first_matrix = enter_matrix(
            first_matrix_rows,
            first_matrix_columns
        )

        print("\nEnter Matrix B")
        second_matrix = enter_matrix(
            second_matrix_rows,
            second_matrix_columns
        )

        multiplied_result = multiply_matrices(
            first_matrix,
            second_matrix
        )

        print("\nMatrix A:")
        display_matrix(first_matrix)

        print("\nMatrix B:")
        display_matrix(second_matrix)

        print("\nMultiplied Matrix:")
        display_matrix(multiplied_result)

    else:
        print("Error: Please choose 1, 2, or 3.")


main()