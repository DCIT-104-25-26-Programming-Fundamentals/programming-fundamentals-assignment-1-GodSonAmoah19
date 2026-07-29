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


def display_menu():
    """
    Displays the main menu options.
    """
    print("\n" + "=" * 30)
    print("     TO-DO LIST MENU")
    print("=" * 30)
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    print("=" * 30)


def add_task(tasks):
    """
    Adds a new task to the to-do list.
    
    Parameters:
        tasks (list): The current list of tasks
    
    Returns:
        list: Updated list of tasks
    """
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Error: Task cannot be empty.")
    return tasks


def view_tasks(tasks):
    """
    Displays all tasks in the to-do list.
    
    Parameters:
        tasks (list): The current list of tasks
    """
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def delete_task(tasks):
    """
    Deletes a task from the to-do list.
    
    Parameters:
        tasks (list): The current list of tasks
    
    Returns:
        list: Updated list of tasks
    """
    if not tasks:
        print("Your task list is empty. Nothing to delete.")
        return tasks
    
    view_tasks(tasks)
    
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")
    
    return tasks


def main():
    """
    Main program - runs the to-do list application.
    """
    tasks = []
    
    print("Welcome to the To-Do List Application!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            tasks = add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            tasks = delete_task(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


# Program entry point
if __name__ == "__main__":
    main()
