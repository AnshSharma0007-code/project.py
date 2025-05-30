# Simple To Do List Application with user interaction feedback

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.\n")
    else:
        print("\nTo Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{index}. [{status}] {task['content']}")
        print()

def add_task(tasks):
    task_content = input("Enter the new task description: ").strip()
    if task_content:
        tasks.append({'content': task_content, 'done': False})
        print(f"\nTask '{task_content}' has been added.\n")
    else:
        print("\nTask description cannot be empty.\n")

def mark_task_done(tasks):
    if not tasks:
        print("\nThere are no tasks to mark as done.\n")
        return
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['done'] = True
            print(f"\nTask '{tasks[task_number - 1]['content']}' marked as done.\n")
        else:
            print("\nInvalid task number. Please try again.\n")
    except ValueError:
        print("\nPlease enter a valid number.\n")

def delete_task(tasks):
    if not tasks:
        print("\nThere are no tasks to delete.\n")
        return
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"\nTask '{removed['content']}' has been deleted.\n")
        else:
            print("\nInvalid task number. Please try again.\n")
    except ValueError:
        print("\nPlease enter a valid number.\n")

def main():
    tasks = []
    while True:
        print("To Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            display_tasks(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '2':
            add_task(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '3':
            mark_task_done(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '4':
            delete_task(tasks)
            input("Press Enter to return to the menu...")
        elif choice == '5':
            print("\nExiting the To Do List application. Goodbye!")
            break
        else:
            print("\nInvalid option! Please select a number between 1 and 5.\n")
            input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
