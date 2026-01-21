tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    while True:
        print("\nSimpleTodoApp Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting SimpleTodoApp.")
            break
        else:
            print("Invalid choice. Try again.")

main()