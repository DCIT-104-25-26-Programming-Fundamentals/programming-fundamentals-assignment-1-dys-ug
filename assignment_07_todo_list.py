# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_task(task_list):

    task_description = input("Enter task: ")

    task_list.append(task_description)

    print('Task added: "' + task_description + '"')


def view_tasks(task_list):

    if len(task_list) == 0:
        print("Your to-do list is empty.")

    else:
        print("Your Tasks:")

        task_number = 1

        for current_task in task_list:
            print(str(task_number) + ".", current_task)

            task_number = task_number + 1


def delete_task(task_list):

    if len(task_list) == 0:
        print("There are no tasks to delete.")
        return

    view_tasks(task_list)

    task_number = int(
        input("Enter task number to delete: ")
    )

    if task_number < 1 or task_number > len(task_list):
        print("Error: Invalid task number.")

    else:
        task_position = task_number - 1

        deleted_task = task_list.pop(task_position)

        print(
            'Task "' + deleted_task + '" has been removed.'
        )


def display_menu():

    print()
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():

    task_list = []

    program_running = True

    while program_running == True:

        display_menu()

        selected_option = input(
            "Enter your choice (1-4): "
        )

        if selected_option == "1":
            add_task(task_list)

        elif selected_option == "2":
            view_tasks(task_list)

        elif selected_option == "3":
            delete_task(task_list)

        elif selected_option == "4":
            print("Goodbye!")

            program_running = False

        else:
            print("Error: Please choose a number from 1 to 4.")


main()