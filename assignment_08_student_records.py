# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_average(student_scores):

    total_score = 0

    for current_score in student_scores:
        total_score = total_score + current_score

    average_score = total_score / len(student_scores)

    return round(average_score, 2)


def add_student(student_records):

    student_name = input("Student name: ")
    student_id = int(input("Student ID: "))

    for current_student in student_records:

        if current_student["id"] == student_id:
            print("Error: This student ID already exists.")
            return

    number_of_scores = int(input("How many scores? "))

    if number_of_scores <= 0:
        print("Error: Number of scores must be positive.")
        return

    student_scores = []

    for score_number in range(1, number_of_scores + 1):

        current_score = float(
            input("Enter score " + str(score_number) + ": ")
        )

        student_scores.append(current_score)

    new_student = {
        "name": student_name,
        "id": student_id,
        "scores": student_scores
    }

    student_records.append(new_student)

    print(
        'Student "' + student_name + '" added successfully.'
    )


def display_all_students(student_records):

    if len(student_records) == 0:
        print("No student records have been added.")
        return

    print()
    print("-" * 70)
    print(
        f"{'Name':20}"
        f"{'ID':15}"
        f"{'Scores':25}"
        f"{'Average':10}"
    )
    print("-" * 70)

    for current_student in student_records:

        student_name = current_student["name"]
        student_id = current_student["id"]
        student_scores = current_student["scores"]

        scores_text = ""

        for score_position in range(len(student_scores)):

            scores_text = scores_text + str(
                student_scores[score_position]
            )

            if score_position < len(student_scores) - 1:
                scores_text = scores_text + ", "

        average_score = calculate_average(student_scores)

        print(
            f"{student_name:20}"
            f"{student_id:<15}"
            f"{scores_text:25}"
            f"{average_score:<10}"
        )

    print("-" * 70)


def find_student_average(student_records):

    student_id_to_find = int(
        input("Enter student ID: ")
    )

    student_found = False

    for current_student in student_records:

        if current_student["id"] == student_id_to_find:

            student_name = current_student["name"]
            student_scores = current_student["scores"]

            average_score = calculate_average(
                student_scores
            )

            print(
                student_name
                + "'s average score:",
                average_score
            )

            student_found = True
            break

    if student_found == False:
        print("Error: Student ID was not found.")


def display_menu():

    print()
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():

    student_records = []

    program_running = True

    while program_running == True:

        display_menu()

        selected_option = input(
            "Enter your choice (1-4): "
        )

        if selected_option == "1":
            add_student(student_records)

        elif selected_option == "2":
            display_all_students(student_records)

        elif selected_option == "3":
            find_student_average(student_records)

        elif selected_option == "4":
            print("Goodbye!")

            program_running = False

        else:
            print(
                "Error: Please choose a number from 1 to 4."
            )


main()